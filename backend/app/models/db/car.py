from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Car(Base):
	__tablename__ = 'car'

	id = Column(Integer, primary_key=True)
	brand = Column(String)
	model = Column(String)
	price = Column(Integer)

	dealer_id = Column(Integer, ForeignKey('dealer.id'))
	dealer = relationship('Dealer', back_populates='cars')
