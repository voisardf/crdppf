# -*- coding: utf-8 -*-

from sqlalchemy import(
    Column, 
    Sequence, 
    Integer, 
    Text,
    String,
    Float)

from papyrus.geo_interface import GeoInterface

from geoalchemy2 import Geometry

from sqlalchemy.orm import relationship, backref, deferred
from zope.sqlalchemy import ZopeTransactionExtension
import sqlahelper

from crdppf import db_config
srid_ = db_config['srid']

Base = sqlahelper.get_base()

# Specific model definition here
class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': db_config['schema'], 'autoload': True}


class RoadBuildingLines(GeoInterface, Base):
    __tablename__ = 'r901_alignements'
    __table_args__ = {'schema': db_config['schema'], 'autoload': True}
    idobj = Column(Integer, primary_key=True)
    geom = Column(Geometry("MULTILINE", srid=srid_))
