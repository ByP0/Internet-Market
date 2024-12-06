from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.app.schemas.auth_schemas import RegisterSchema, LogginingSchema, TokenInfo
from backend.app.models.users_models import Users
from backend.app.database import get_session
from backend.app.services.auth_service import hash_password, validate_password, create_access_token


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/sing_up/')
async def register(
    credentials: RegisterSchema,
    session: AsyncSession = Depends(get_session),):
    try:
        response_db = select(Users).where(Users.username == credentials.username)
        result = await session.execute(response_db)
        user = result.scalars().first()
        try:
            if user:
                return HTTPException(status_code=400, detail="Такой пользователь уже зарегестрирован")
            if user.email == credentials.email:
                return HTTPException(status_code=400, detail="Почта уже используется")
        except AttributeError:
            pass 
        
        data_for_db = Users(
            username=credentials.username,
            password=hash_password(credentials.password).decode('utf-8'),
            email=credentials.email,
        )
        
        session.add(data_for_db)
        await session.commit()
        await session.refresh(data_for_db)
        second_response = select(Users.id).where(Users.username == credentials.username)
        second_result = await session.execute(second_response)
        user_data = second_result.scalars().first()

        payload = {
            "subject": user_data,
            "username": credentials.username,
            "email": credentials.email,
            "role": "customer",
        }
        access_token = create_access_token(payload)
        
        return TokenInfo(
            access_token=access_token, 
            token_type="Bearer",
        ) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.post('/login/', response_model=TokenInfo)
async def login(
    credentials: LogginingSchema,
    session: AsyncSession = Depends(get_session),) -> bool:
    try:
        response_db = select(Users).where(Users.username == credentials.username)
        result = await session.execute(response_db)
        user_data = result.scalars().first()
        if user_data is None:
            raise HTTPException(status_code=404, detail="Такой пользователь не найден")

        if not validate_password(credentials.password, user_data.password.encode('utf-8')):
            raise HTTPException(status_code=404, detail="Неверный пароль")
        
        payload = {
            "subject": user_data.id,
            'username': user_data.username,
            'email': user_data.email,
            'role': user_data.role,
        }
        access_token = create_access_token(payload)
        return TokenInfo(
            access_token=access_token, 
            token_type="Bearer",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))