#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None
    all_classes = {User, State, City, Review, Amenity, Place}

    def __init__(self):
        """Initialize a new DBStorage instance."""

        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                format(user, password, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)


    def all(self, cls=None):
        """ this is a comment """
        dic = {}
        if cls:
            sess = self.__session.query(eval(cls)).all()
            for val in sess:
                dic.update({"{}.{}".format(cls, val.id): val})
        else:
            for item in self.all_classes:
                sess = self.__session.query(item).all()
                for sta in sess:
                    dic.update(
                        {"{}.{}".format(type(sta).__name__, sta.id): sta})
        return dic

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
