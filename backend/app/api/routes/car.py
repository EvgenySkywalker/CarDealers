from typing import List

from fastapi import APIRouter, HTTPException, status

from app.models.db import Car, Dealer
from app.models.db.base import session_scope
from app.models.schema import car as car_schema

router = APIRouter()


@router.post('/create')
def create(data: car_schema.CarCreateRequest):
	"""
	Создание машины
	"""

	with session_scope() as session:
		dealer = session.query(Dealer).get(data.dealer_id)
		if dealer is None:
			raise HTTPException(status.HTTP_404_NOT_FOUND, 'Dealer not found')
		session.add(Car(**data.dict()))


@router.get('/all', response_model=List[car_schema.Car])
def get_all():
	"""
	Возвращает данные всех машин в JSON
	"""

	with session_scope() as session:
		cars = session.query(Car).all()
		session.expunge_all()
		return cars


@router.get('/{car_id}', response_model=car_schema.Car)
def get(car_id: int):
	"""
	Возвращает данные конкретной машины в JSON
	"""

	with session_scope() as session:
		car = session.query(Car).get(car_id)
		if car is None:
			raise HTTPException(status.HTTP_404_NOT_FOUND, 'Car not found')
		session.expunge_all()
		return car


@router.post('/{car_id}/update')
def update(car_id: int, data: car_schema.CarUpdateRequest):
	"""
	Изменение конкретной машины
	"""

	with session_scope() as session:
		session.query(Car).where(Car.id == car_id).update(data.dict())


@router.post('/{car_id}/delete')
def delete(car_id: int):
	"""
	Удаление конкретной машины
	"""

	with session_scope() as session:
		session.query(Car).where(Car.id == car_id).delete()
