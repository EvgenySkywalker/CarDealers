from typing import Optional

from pydantic import validator

from app.models.schema.custom_base_model import CamelCaseBaseModel


@validator('price', allow_reuse=True)
def validate_price(cls, price):
	if price < 0:
		raise ValueError('Цена не может быть отрицательной')
	return price


class BaseCar(CamelCaseBaseModel):
	brand: str
	model: str
	price: int

	validate_price = validate_price


class Car(BaseCar):
	id: int
	dealer_id: Optional[int] = None

	class Config:
		orm_mode = True


class CarCreateRequest(BaseCar):
	dealer_id: Optional[int]


class CarUpdateRequest(CamelCaseBaseModel):
	brand: Optional[str]
	model: Optional[str]
	price: Optional[int]

	validate_price = validate_price
