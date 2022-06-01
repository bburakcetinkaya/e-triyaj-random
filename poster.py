# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:47:04 2022

@author: piton
"""
import requests as rq
import pandas as pd
from datetime import datetime
import numpy as np
import json
url = "http://localhost:8000"
data =  pd.read_csv("data.csv")
doctor =  pd.read_csv("doctor.csv")
def main():
    # Poster.enterDoctorInfo()
    # Poster.enterUserPasswordTC()
    Poster.postEntry()
class Poster:
    def enterUserPasswordTC():
        postData = {
                          "id": 0,
                          "tc": 0,
                          "name": "string",
                          "surname": "string",
                          "role": "ROLE_PATIENT",
                          "password": "string"
                   }
        for i in range(1000):
            patient = data.iloc[i]
            tc = patient["id"]
            tc = patient["id"].replace("[","")
            tc = tc.replace("]","")
            print(tc)
            postData["tc"] = int(tc)
            postData["name"] = patient["name"]
            postData["surname"] = patient["surname"]
            postData["password"] = str(patient["password"])
            print(postData)
            jsonPostData = json.dumps(postData)
            x = rq.post(url + '/users/newUser', data = jsonPostData)
            print(x.request)
            print(i,"  ",x.status_code)
    def enterDoctorInfo():
        postData = {
                          "id": 0,
                          "tc": 0,
                          "name": "string",
                          "surname": "string",
                          "role": "ROLE_DOCTOR",
                          "password": "string"
                   }
        for i in range(20):
            doc = doctor.iloc[i]
            tc = doc["id"]
            tc = doc["id"].replace("[","")
            tc = tc.replace("]","")
            print(tc)
            postData["tc"] = int(tc)
            postData["name"] = doc["name"]
            postData["surname"] = doc["surname"]
            postData["password"] = str(doc["password"])
            print(postData)
            jsonPostData = json.dumps(postData)
            x = rq.post(url + '/users/newUser', data = jsonPostData)
            print(x.request)
            print(i,"  ",x.status_code)
# http://localhost:8000/users/newUser
# {
#   "id": 2,
#   "tc": 0,
#   "name": "string",
#   "surname": "string",
#   "role": "ROLE_PATIENT",
#   "password": "string"
# }

    
    def postEntry():
        postData = {
                          "id": 0,
                          "name": "string",
                          "surname": "string",
                          "age": 0,
                          "gender": "MALE",
                          "tc": 0,
                          "sp02": 0,
                          "heartRate": 0,
                          "temperature": 0,
                          "systolicBP": 0,
                          "diastolicBP": 0,
                          "doctorID": 0,
                          "onlyMyDoctor": "TRUE",
                          "date": "string",
                          "time": "string"
                        }

        for i in range(0,10000):
            index = np.random.randint(0,1000,1)
            patient = data.iloc[int(index)]
            tc = patient["id"]
            tc = patient["id"].replace("[","")
            tc = tc.replace("]","")
            # print(tc)
            postData["tc"] = int(tc)
            postData["name"] = patient["name"]
            postData["gender"] = patient["gender"]
            postData["surname"] = patient["surname"]
            age = patient["age"]
            age = patient["age"].replace("[","")
            age = age.replace("]","")
            # print(tc)
            postData["age"] = int(age)
            
            postData["sp02"] = int(np.random.randint(93,101,1))
            postData["heartRate"] = int(np.random.randint(60,101,1))
            postData["temperature"] = float(np.round((np.random.uniform(35.7,38.3,1)),2))
            systolic = int(np.random.randint(80,160,1))
            postData["systolicBP"] = systolic
            diastolic = int(np.random.randint(55,101,1))
            
            while (systolic - diastolic) < 10 and (systolic - diastolic) > 45:
                print(systolic,"  ",diastolic)
                diastolic = int(np.random.randint(55,101,1))
                
            postData["diastolicBP"] = diastolic
            doctorID = patient["doctortc"]
            doctorID = patient["doctortc"].replace("[","")
            doctorID = doctorID.replace("]","")
            # print(tc)
            postData["doctorID"] = int(doctorID)
            
            if index%2 ==0:
                postData["onlyMyDoctor"] = "TRUE"
            else:
                postData["onlyMyDoctor"] = "FALSE"
                
            
            year = np.random.randint(2020,2023,1)
            if year>=2022:
                month = np.random.randint(1,6,1)
            else: 
                month = np.random.randint(1,13,1)
            
            year = str(year)
            year = year.replace("[","")
            year = year.replace("]","")
            if month == 4 or 6 or 9 or 10:
                day = np.random.randint(1,31,1)
            elif month == 2:
                day = np.random.randint(1,29,1)
            else:
                day = np.random.randint(1,32,1)
            month = str(month)
            month = month.replace("[","")
            month = month.replace("]","")
            if len(month)<2:
                month = '0'+str(month)
            day = str(day)
            day = day.replace("[","")
            day = day.replace("]","")
            if len(day)<2:
                day = '0'+str(day)
            date = str(year)+'-'+month+'-'+day
            minutes = str(np.random.randint(0,60,1))
            hours = str(np.random.randint(0,24,1))
            seconds = str(np.random.randint(0,60,1))
            minutes = str(minutes)
            minutes = minutes.replace("[","")
            minutes = minutes.replace("]","")
            hours = str(hours)
            hours = hours.replace("[","")
            hours = hours.replace("]","")
            seconds = str(seconds)
            seconds = seconds.replace("[","")
            seconds = seconds.replace("]","")
            if len(minutes)<2:
                minutes = '0'+minutes
            if len(hours)<2:
                hours = '0'+hours
            if len(seconds)<2:
                seconds = '0'+seconds
            time = str(hours+'.'+minutes+'.'+seconds)
            
            postData["date"] = date
            postData["time"] = time
            jsonPostData = json.dumps(postData)
            # print(jsonPostData)
            x = rq.post(url + '/users/createUser', data = jsonPostData)
            print(i,"  ", x.status_code)
        # try:
        #     
            
        #     # time.sleep(3)      
    
        # except: 
        #     print()
    
        # else:
        #     print()
    
        # finally:
            # stopFlag.clear()
main()