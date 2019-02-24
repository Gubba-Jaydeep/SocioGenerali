from django.db import models
import pymongo
# Create your models here.

class CustomerDatabase:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://jd254:pass123@cluster0-shard-00-00-yftzb.mongodb.net:27017,cluster0-shard-00-01-yftzb.mongodb.net:27017,cluster0-shard-00-02-yftzb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        self.mydb = self.client["customer"]

    def getData(self):
        mycol = self.mydb["data"]
        res = []
        for x in mycol.find({},{"_id": 0,"pk":1 , "first_name": 1, "email": 1, "phoneNumber": 1, "policyNumber": 1, "maturityDate": 1}):
            res.append(x)
        return res


    '''def insertData(self,name,phoneNumber,email,dateOfBirth,gender,password,location=None,policyNumber=None,cliendID=None):
        mycol = self.mydb["data"]
        if mycol.find_one({"email":email})==None:
            x = mycol.insert_one({"name":name,"phoneNumber":phoneNumber,"email":email,"dateOfBirth":dateOfBirth,"gender":gender,"password":password,"location":location,"policyNumber":policyNumber,"cliendID":cliendID})
            return True
        else:
            return False

    def insertHistory(self,email,time):
        mycol = self.mydb["history"]
        if mycol.find_one({"email":email})==None:
            x=mycol.insert_one({"email":email,"log":[]})
        log=mycol.find_one({"email": email})['log']
        log.insert(0,time)
        mycol.update_one({"email": email}, {"$set": {"log": log}})

    def deleteData(self,email):
        mycol = self.mydb["data"]
        if mycol.find_one({"email":email})!=None:
            x=mycol.delete_one({"email":email})

    def flushHistory(self,email):
        mycol = self.mydb["history"]
        if mycol.find_one({"email": email}) != None:
            mycol.update_one({"email": email}, {"$set": {"log": []}})

    def updateData(self,email,key,value):
        mycol = self.mydb["data"]
        if mycol.find_one({"email": email}) != None:
            mycol.update_one({"email": email}, {"$set": {key:value}})
    
    '''





class AdvisorDatabase:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://jd254:pass123@cluster0-shard-00-00-yftzb.mongodb.net:27017,cluster0-shard-00-01-yftzb.mongodb.net:27017,cluster0-shard-00-02-yftzb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        self.mydb = self.client["advisor"]

    #this gives a dicionary containing all advisors with key as email and password as value
    def getData(self):
        mycol = self.mydb["data"]
        res={}
        for x in mycol.find({},{"email":1,"password":1}):
            res[x["email"]]=x["password"]
        return res

    #returns a dict containing the details of the user whose email is passed as paramater
    def getCompleteInfo(self,email):
        mycol=self.mydb["data"]
        res=mycol.find_one({"email":email},{"_id":0,"password":0})
        if res is None:
            return False
        return res



    '''def insertData(self, name, phoneNumber, email, dateOfBirth,type, gender, password, location=None):
        mycol = self.mydb["data"]
        if mycol.find_one({"email": email}) == None:
            x = mycol.insert_one(
                {"name": name, "phoneNumber": phoneNumber, "email": email, "dateOfBirth": dateOfBirth,"type":type ,"gender": gender,
                 "password": password, "location": location})
            return True
        else:
            return False

    def insertHistory(self, email, time):
        mycol = self.mydb["history"]
        if mycol.find_one({"email": email}) == None:
            x = mycol.insert_one({"email": email, "log": []})
        log = mycol.find_one({"email": email})['log']
        log.insert(0, time)
        mycol.update_one({"email": email}, {"$set": {"log": log}})

    def deleteData(self, email):
        mycol = self.mydb["data"]
        if mycol.find_one({"email": email}) != None:
            x = mycol.delete_one({"email": email})

    def flushHistory(self, email):
        mycol = self.mydb["history"]
        if mycol.find_one({"email": email}) != None:
            mycol.update_one({"email": email}, {"$set": {"log": []}})

    def updateData(self,email,key,value):
        mycol = self.mydb["data"]
        if mycol.find_one({"email": email}) != None:
            mycol.update_one({"email": email}, {"$set": {key:value}})
    '''






