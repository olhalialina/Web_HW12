from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr
    phone_number: str = Field(max_length=15)
    born_date: date


class ContactModel(ContactBase):
    description: str = Field(max_length=150)


class ContactUpdate(ContactModel):
    ...


class ContactResponse(ContactBase):
    id: int
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone_number: str | None
    born_date: date | None
    description: str | None

    class Config:
        from_attributes = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: EmailStr
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"