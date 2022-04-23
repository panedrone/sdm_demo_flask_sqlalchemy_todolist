"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from .data_store import *


class GroupEx(Base):
    g_id = Column('g_id', autoincrement=True)
    g_name = Column('g_name')
    g_comments = Column('g_comments')
    tasks_count = Column('tasks_count')

    __abstract__ = True

    SQL = """select g.*,  
                (select count(*) from tasks where g_id=g.g_id) as tasks_count 
                from groups g 
                order by g.g_id"""
