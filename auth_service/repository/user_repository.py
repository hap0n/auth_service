from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from auth_service.repository.models.user import User
from auth_service.utils.database import PostgresDB


class UserRepository:
    session: Session = Depends(PostgresDB.get_session_local())

    @classmethod
    def get_user(cls, user_id: int) -> Optional[User]:
        return cls.session.query(User).filter(User.id == user_id).first()

    @classmethod
    def get_user_by_nickname(cls, nickname: str) -> Optional[User]:
        return cls.session.query(User).filter(User.nickname == nickname).first()

    @classmethod
    def get_users(cls, skip: int = 0, limit: int = 100) -> List[User]:
        return cls.session.query(User).offset(skip).limit(limit).all()

    @classmethod
    def create_user(cls, user: User) -> User:
        cls.session.add(user)
        cls.session.commit()
        cls.session.refresh(user)
        return user

    @classmethod
    def update_password(cls, user: User):
        cls.session.query(User).filter(User.nickname == user.nickname).update({"hashed_password": user.hashed_password})
        cls.session.commit()
