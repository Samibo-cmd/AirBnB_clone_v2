#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
	""" A place to stay """
	__tablename__ = "places"
	city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
	user_id = user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
	name = Column(String(128), nullable=False)
	description = Column(String(1024))
	number_rooms = Column(Integer, default=0)
	number_bathrooms = Column(Integer, default=0)
	max_guest = Column(Integer, default=0)
	price_by_night = Column(Integer, default=0)
	latitude = Column(Float)
	longitude = Column(Float)
	amenity_ids = []
