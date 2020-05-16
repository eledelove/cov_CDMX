from peewee import *
import datetime
import os

#-----Run this script only if you want to create the data base -----------------

data_base = "covid_california"
host = "172.17.0.2"
#host = "localhost"
port = 3306
username = "covcalifornia"
password = "cov19"

#Creating data base ¡Uncomment only if you want to create local data base!-------
#os.system("echo \"create database "+data_base+";\" | mysql --user="+username+
                                                        #" --password="+password)

db= MySQLDatabase(data_base,host=host,port=port,user=username,password=password)

class BaseModel(Model):
    class Meta:
        database = db

class City(BaseModel):
    name = CharField(unique=True)
    latitude = CharField()
    longitude = CharField()

class Statistics_by_City(BaseModel):
    cases = CharField(default='0')
    deaths = CharField(default='0')
    date = DateField(default=datetime.datetime.now)
    city = ForeignKeyField(City, backref='statistics')

class Neighborhoods(BaseModel):
    name = CharField(unique=True)
    latitude = CharField()
    longitude = CharField()
    city = ForeignKeyField(City, backref='neighborhoods')

class Statistics_by_Neighborhood(BaseModel):
    cases = CharField(default='0')
    deaths = CharField(default='0')
    date = DateField(default=datetime.datetime.now)
    neighborhood = ForeignKeyField(Neighborhoods, backref='statistics')

db.connect()
db.create_tables([City, Statistics_by_City, Neighborhoods, 
                                                    Statistics_by_Neighborhood])
db.close()
