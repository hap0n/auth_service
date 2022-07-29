from sqlalchemy import Boolean, Column, Integer, String

from auth_service.repository.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # TODO: add pwd_last_change field that means date where password was changed last time
    is_active = Column(Boolean, default=True)
