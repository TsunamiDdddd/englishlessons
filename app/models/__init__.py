import datetime


import sqlalchemy
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("ID",Integer,primary_key=True),
    Column("Name",String, nullable=False),
    Column("permissions",JSON)
)
users = Table(
    "Users",
    metadata,
    Column("ID",Integer,primary_key=True),
    Column("email",String,nullable=False),
    Column("username",String,nullable=False),
    Column("password",String,nullable=False),
    Column("registered_at",TIMESTAMP,default=datetime.UTC),
    Column("role_ID",Integer,ForeignKey("roles.ID"))
)
