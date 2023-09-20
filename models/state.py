#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel):
    """ State class """
    name = Column(String(128), nullable=False)
