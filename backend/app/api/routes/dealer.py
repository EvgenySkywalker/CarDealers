from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import joinedload

from app.models.db import Dealer
from app.models.db.base import session_scope
from app.models.schema import car as car_schema, dealer as dealer_schema

router = APIRouter()


@router.post('/create')
def create(data: dealer_schema.DealerCreateRequest):
	"""
	Создание дилера
	"""

	with session_scope() as session:
		session.add(Dealer(**data.dict()))


@router.get('/all', response_model=List[dealer_schema.Dealer])
def get_all():
	"""
	Возвращает данные всех дилеров в JSON
	"""

	with session_scope() as session:
		dealers = session.query(Dealer).all()
		session.expunge_all()
		return dealers


@router.get('/{dealer_id}', response_model=dealer_schema.Dealer)
def get(dealer_id: int):
	"""
	Возвращает данные конкретного дилера в JSON
	"""

	with session_scope() as session:
		dealer = session.query(Dealer).get(dealer_id)
		if dealer is None:
			raise HTTPException(status.HTTP_404_NOT_FOUND, 'Dealer not found')
		session.expunge_all()
		return dealer


@router.post('/{dealer_id}/update')
def update(dealer_id: int, data: dealer_schema.DealerUpdateRequest):
	"""
	Изменение конкретного дилера
	"""

	with session_scope() as session:
		session.query(Dealer).where(Dealer.id == dealer_id).update(data.dict())


@router.post('/{dealer_id}/delete')
def delete(dealer_id: int):
	"""
	Удаление конкретного дилера
	"""

	with session_scope() as session:
		session.query(Dealer).where(Dealer.id == dealer_id).delete()


@router.get('/{dealer_id}/cars', response_model=List[car_schema.Car], tags=['cars'])
def cars(dealer_id: int):
	"""
	Возвращает данные всех машин конкретного дилера в JSON
	"""

	with session_scope() as session:
		dealer = session.query(Dealer).options(joinedload(Dealer.cars)).get(dealer_id)
		if dealer is None:
			raise HTTPException(status.HTTP_404_NOT_FOUND, 'Dealer not found')
		session.expunge_all()
		return dealer.cars
