from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Annotated

from backend.app.schemas.users_schema import UserInfoSchema
from backend.app.schemas.auth_schemas import LogginingSchema
from backend.app.models.users_models import Users
from backend.app.database import get_session
from backend.app.services.auth_service import validate_password


router = APIRouter(prefix='/user', tags=['Users'])


@router.get('/me/', response_model=UserInfoSchema)
async def get_my_info(
    credentials: Annotated[LogginingSchema, Query()],
    session: AsyncSession = Depends(get_session)):
    try:
        response_db = select(Users).where(Users.username == credentials.username)
        result = await session.execute(response_db)
        user_data = result.scalars().first()
        if not validate_password(credentials.password, user_data.password.encode('utf-8')):
            raise HTTPException(status_code=404, detail="Неверный пароль")
        return UserInfoSchema(
            username=user_data.email,
            email=user_data.email,
            phone=user_data.phone,
            verify_email=user_data.verify_email,
            verify_phone=user_data.verify_email,
            created_at=user_data.created_at,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))