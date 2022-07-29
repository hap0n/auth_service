import re

from pydantic import BaseModel, validator


class UserBase(BaseModel):
    username: str


class UserDTO(UserBase):
    password: str

    @validator("password")
    def password_length_validation(cls, password):  # noqa:N805
        match_pattern = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).{8,}$"  # noqa:W605
        if not re.match(match_pattern, password):
            raise ValueError
        return password


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
