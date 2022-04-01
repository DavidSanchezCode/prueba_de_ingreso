from sqlalchemy import create_engine,MetaData

#aca conectamos con tableplus que es tambien conectar con Mysql

engine=create_engine("mysql+pymysql://Xr3iuCv8SvKs:5zAJRuTKGjgGvK2CAKwkioaLr@rds-social-listener.c5nzakkef7oq.us-east-1.rds.amazonaws.com:3306/sociallistener_development")
                                    #usuario       #pass                     #host                                                        #port #name        

meta =MetaData()

conn=engine.connect()


