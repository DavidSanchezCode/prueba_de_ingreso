from sqlalchemy import create_engine,MetaData

engine=create_engine("mysql+pymysql://Xr3iuCv8SvKs:5zAJRuTKGjgGvK2CAKwkioaLr@rds-social-listener.c5nzakkef7oq.us-east-1.rds.amazonaws.com:3306/sociallistener_development")

meta =MetaData()

conn=engine.connect()


