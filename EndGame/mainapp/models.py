from django.db import models
import pymongo
# Create your models here.

class CustomerDatabase:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://jd254:pass123@cluster0-shard-00-00-yftzb.mongodb.net:27017,cluster0-shard-00-01-yftzb.mongodb.net:27017,cluster0-shard-00-02-yftzb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        self.mydb = self.client["customer"]


    def insert(self,name,phoneNumber,email,dateOfBirth,gender,password,location=None,policyNumber=None,cliendID=None):
        mycol = self.mydb["data"]
        #check if data already exists
        x = mycol.insert_one({"name":name,"phoneNumber":phoneNumber,"email":email,"dateOfBirth":dateOfBirth,"gender":gender,"password":password,"location":location,"policyNumber":policyNumber,"cliendID":cliendID})

