from fastapi import FastAPI
from routs.user import user,suma


app = FastAPI()
app.include_router(user)

app.include_router(suma)


