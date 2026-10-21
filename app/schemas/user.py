from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

# Shared properties
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to return to client
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    # This is required for Pydantic to read SQLAlchemy objects directly
    model_config = ConfigDict(from_attributes=True)        

# Properties to receive via API on login
class Token(BaseModel):
    access_token: str
    token_type: str