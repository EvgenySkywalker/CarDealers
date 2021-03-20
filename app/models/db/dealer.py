from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .car import Car


class Dealer(Base):
	__tablename__ = 'dealer'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	cars: List[Car] = relationship(
		Car,
		back_populates='dealer',
		cascade='all, delete',
	)
