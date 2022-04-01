from pydantic import BaseModel
from typing import Optional

#aca establecimos la variables que vamos a usar en la tabla y los que se organizaran en e l diccionario.

class User(BaseModel):
   id:Optional[str]
   name:str
   email:str
   password:str 

class Sumar(BaseModel):
    id:Optional[str]
    numero1:int
    numero2:int
    resul:int