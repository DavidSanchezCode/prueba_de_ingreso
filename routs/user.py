from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User   
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f=Fernet(key)
 
user= APIRouter()

#traemos la informacion a la base de datos gracias al conn.execute
@user.get("/users")
def get_user():
    return conn.execute(users.select()).fetchall()


#enviamos los datos y los vemos por ultimo en ser publicado
@user.post("/users")
def create_user(user: User):
    new_user = {"name":user.name,"email":user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result=conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first() 


#buscamos los datos desde su id
@user.get("/users/{id}")
def ids(id: str):
   return conn.execute(users.select().where(users.c.id == id)).first()
   

#eliminamos los datos desde su id
@user.delete("/users/{id}")
def delete_user(id: str):
   conn.execute(users.delete().where(users.c.id == id))
   return "se elimino correctamente" 


#actualizamos los datos de la base de datos
@user.put("/users/{id}")
def actualizar_users(id: str, user: User):
    conn.execute(users.update().values(name=user.name,
                                       email=user.email, 
                                        password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first() 
