"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from .data_store import *


class Group(Base):
    __tablename__ = 'groups'

    g_id = Column('g_id', Integer, primary_key=True, autoincrement=True)
    g_name = Column('g_name', String)
    g_comments = Column('g_comments', String, nullable=True)
