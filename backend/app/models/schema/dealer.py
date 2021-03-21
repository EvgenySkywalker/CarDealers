from typing import Optional

from app.models.schema.custom_base_model import CamelCaseBaseModel


class BaseDealer(CamelCaseBaseModel):
	name: str


class Dealer(BaseDealer):
	id: int

	class Config:
		orm_mode = True


class DealerCreateRequest(BaseDealer):
	pass


class DealerUpdateRequest(CamelCaseBaseModel):
	name: Optional[str]
