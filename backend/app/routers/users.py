from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Annotated

from schemas.users_schema import UserInfoSchema
from schemas.auth_schemas import LogginingSchema
from models.users_models import Users
from database import get_session


router = APIRouter(prefix='/user', tags=['Users'])


@router.get('/me/', response_model=UserInfoSchema)
async def get_my_info(
    credentials: Annotated[LogginingSchema, Query()],
    session: AsyncSession = Depends(get_session)):
    try:
        response_db = select(Users).where(Users.username == credentials.username)
        result = await session.execute(response_db)
        user_data = result.scalars().first()
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