from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine


sumas = Table("suma",meta,
        Column("id",Integer,primary_key=True),
        Column("numero1",Integer),
        Column("numero2",Integer),
        Column("resul",Integer))

meta.create_all(engine)

#aca creamos la tabla de la base de datos 

users = Table("users",meta,
Column("id",Integer,primary_key=True), 
    Column("name",String(255)),
    Column("email",String(255)),
    Column("password",String(255)))

meta.create_all(engine)

