from peewee import *
import datetime
import os

"""
-------- Este script sólo se deberá ejecutar para crear la base de datos -------
"""

data_base = "covid_cdmx"
host = "localhost"
port = 3306
username = ""
password = ""

#--------------- Crea la base de datos en el servidor --------------------------
#os.system("echo \"create if not exists database "+data_base+";\" | mysql --user="
#                                            +username+" --password="+password)


#----------------------- Conexión a la base de datos ---------------------------
db = MySQLDatabase(
    data_base,
    host = host,
    port = port,
    user = username,
    password = password
    )

#------------------------- Creación de entidades -------------------------------

class BaseModel(Model):
    class Meta:
        database = db

class Estado(BaseModel):
    nombre = CharField(max_length = 50, unique = True)
    latitud = CharField(max_length = 20)
    longitud = CharField(max_length = 20)

class Estadisticas_Estado(BaseModel):
    casos = CharField(max_length = 8, default = '0')
    muertes = CharField(max_length = 8, default = '0', null = True)
    fecha = DateField(default = datetime.datetime.now)
    estado = ForeignKeyField(Estado, backref = 'estadisticas')

class Alcaldia(BaseModel):
    nombre = CharField(max_length = 100, unique = True)
    latitud = CharField(max_length = 20)
    longitud = CharField(max_length = 20)
    estado = ForeignKeyField(Estado, backref = 'alcaldia')

class Estadisticas_Alcaldia(BaseModel):
    casos = CharField(max_length = 8, default = '0')
    muertes = CharField(max_length = 8, default = '0', null = True)
    fecha = DateField(default = datetime.datetime.now)
    alcaldia = ForeignKeyField(Estado, backref = 'estadisticas')

class Colonia(BaseModel):
    nombre = CharField(max_length = 100, unique = True)
    latitud = CharField(max_length = 20)
    longitud = CharField(max_length = 20)
    alcaldia = ForeignKeyField(Estado, backref = 'colonia')

class Estadisticas_Colonia(BaseModel):
    casos = CharField(max_length = 8, default = '0')
    muertes = CharField(max_length = 8, default = '0', null = True)
    fecha = DateField(default = datetime.datetime.now)
    colonia = ForeignKeyField(Estado, backref = 'estadisticas')


#------------------- Crea las tablas en la base de datos -----------------------

db.connect()

db.create_tables([
    Estado, Estadisticas_Estado,
    Alcaldia, Estadisticas_Alcaldia,
    Colonia, Estadisticas_Colonia
    ])

db.close()