from passlib.handlers.bcrypt import bcrypt

from auth_service.router import schemas
from auth_service.repository.models.user import User
from auth_service.repository.user_repository import UserRepository


class UserService:
    @classmethod
    def update_user_password(cls, user: schemas.user.UserDTO):
        hashed_password = cls._generate_password_hash(user.password)
        # TODO: check if new password != current password
        db_user = User(username=user.username, hashed_password=hashed_password)
        UserRepository.update_password(db_user)

    @classmethod
    def create_user(cls, user: schemas.user.UserDTO) -> User:
        hashed_password = cls._generate_password_hash(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password)
        return UserRepository.create_user(db_user)

    @classmethod
    def _generate_password_hash(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def _verify_password(cls, password: str, password_hash: str):
        return bcrypt.verify(password, password_hash)
