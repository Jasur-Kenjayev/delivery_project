from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': "mohirdevs",
                'email': "mohirdev.praktiskum@gmail.com",
                'password': "password12345s",
                'is_staff': False,
                "is_active": True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key: str = 'de1272f2ec9caa2d9bea669cc8e838edc655cb4553e3df36129588f3460f6979'

class LoginModel(BaseModel):
    username_or_email: str
    password: str

class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_statuses: Optional[str] = "PENDING"
    user_id: Optional[int]
    product_id: int

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "quantity": 2,
            }
        }

class OrderStatusModel(BaseModel):
    order_statuses: Optional[str] = "PENDING"

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "order_srtatuses": "PENDING"
            }
        }

class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    price: int

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "name": "baliq",
                "price": 120000
            }
        }