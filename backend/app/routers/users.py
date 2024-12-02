from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.users_schema import RegisterSchema
from models.users_models import Users
from database import get_session
from config import pattern
from services.users_service import hash_password, password_check



router = APIRouter()


@router.post('/registration')
async def register(
    data: RegisterSchema,
    session: AsyncSession = Depends(get_session),) -> bool:
    try:
        response_db = select(Users).where(Users.username == data.username)
        result = await session.execute(response_db)
        user = result.scalars().first()
        if user:
            raise HTTPException(status_code=400, detail="Такой пользователь уже зарегестрирован")       
        
        data_for_db = Users(
            username=data.username, 
            password=hash_password(data.password).decode('utf-8'),)
        
        session.add(data_for_db)
        await session.commit()
        await session.refresh(data_for_db)
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))