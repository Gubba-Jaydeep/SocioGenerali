from django.db import models
import pymongo
import base64
# Create your models here.

class CustomerDatabase:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://jd254:pass123@cluster0-shard-00-00-yftzb.mongodb.net:27017,cluster0-shard-00-01-yftzb.mongodb.net:27017,cluster0-shard-00-02-yftzb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
        self.mydb = self.client["customer"]

    def getData(self):
        mycol = self.mydb["data"]
        res = []
        for x in mycol.find({},{"_id": 0,"address":0}):
            res.append(x)
        return res

    def getDataFromPk(self,pk):
        mycol=self.mydb["data"]
        x=mycol.find_one({"pk":pk},{"_id": 0,"address":0})
        if x == None:
            return False
        else:
            return x

    def setImage(self,path,pk):
        mycol = self.mydb["data"]
        with open(path, "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
            mycol.update_one({"pk":pk},{"$set":{"image":str}})




    def getImage(self,pk):
        mycol = self.mydb["data"]
        res=mycol.find_one({"pk":pk})
        fh = open("mainapp/static/mainapp/cusImages/test.jpg", "wb")
        fh.write(base64.b64decode(res["image"]))
        fh.close()


    def insertData(self,name,phoneNumber,email,dateOfBirth,gender,password,location=None,policyNumber=None,cliendID=None):
        mycol = self.mydb["data"]
        if mycol.find_one({"email":email})==None:
            x = mycol.insert_one({"name":name,"phoneNumber":phoneNumber,"email":email,"dateOfBirth":dateOfBirth,"gender":gender,"password":password,"location":location,"policyNumber":policyNumber,"cliendID":cliendID})
            return True
        else:
            return False

    '''
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
    def getDataFromEmail(self,email):
        mycol=self.mydb["data"]
        x=mycol.find_one({"email":email},{"_id": 0})
        if x == None:
            return False
        else:
            return x


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






