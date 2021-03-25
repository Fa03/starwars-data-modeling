import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'userIds'
    id_user = Column(Integer, primary_key=True)
    user_Name = Column(String(250))
    password = Column(String(250))
    email = Column(String(250))
    b_day = Column(Integer, nullable=False)
    
class Personajes(Base):
    __tablename__ = 'personajes'
    id_person = Column(Integer, primary_key=True)
    name_person = Column(String(250))
    height = Column(Integer, nullable=False)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))

class Planetas(Base):
    __tablename__ = 'planetas'
    id_planet = Column(Integer, primary_key=True)
    name_planet = Column(String(250))
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))

class Favoritos(Base):
    __tablename__ = 'favoritos'
    favorite_id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('userIds.id_user'))
    usuario = relationship(Usuarios)
    id_personaje = Column(Integer, ForeignKey('personajes.id_person'))
    personaje = relationship(Personajes)
    id_planeta = Column(Integer, ForeignKey('planetas.id_planet'))
    planeta = relationship(Planetas)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')