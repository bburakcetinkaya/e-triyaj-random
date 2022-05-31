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
male_names =  pd.read_csv("tr_isim_erkek.csv")["[isim]"]
female_names = pd.read_csv("tr_isim_kadin.csv")["[isim]"]
surnames = pd.read_csv("tr_soyisimler.csv")["[soyisim]"]
tc =  


for i in range(500):
    age = np.random.randint(18,80,1)
    gender = "MALE"
    name = np.random.choice(male_names)
    surname = np.random.choice(surnames)
    tc =

class Poster:
    
    def createDoctorData(name,password):
        postData = {
                          "id": 0,
                          "name": "string",
                          "password": "string"
                   }
        
    
    def postEntry(name,surname,age,gender,tc,sp02,heartRate,
                        temperature,systolicBP,diastolicBP):
        postData = {
                          "id": 0,
                          "name": "string",
                          "surname": "string",
                          "age": 0,
                          "gender": "MALE",
                          "tc": 0,
                          "password": 0,
                          "sp02": 0,
                          "heartRate": 0,
                          "temperature": 0,
                          "systolicBP": 0,
                          "diastolicBP": 0,
                          "role": "ROLE_PATIENT",
                          "doctorID": 0,
                          "date": "string",
                          "time": "string"
                        }
        # self.postData["id"] = id
        now = datetime.now()
        postData["name"] = name
        postData["surname"] = surname
        postData["age"] = int(age)
        postData["gender"] = gender
        postData["tc"] = int(tc)
        postData["password"] = int(password)
        postData["sp02"] = int(sp02)
        postData["heartRate"] = int(heartRate)
        postData["temperature"] = float(temperature)
        postData["systolicBP"] = int(systolicBP)
        postData["diastolicBP"] = int(diastolicBP)
        postData["date"] = now.strftime("%Y-%m-%d")
        postData["time"] = now.strftime("%H.%M.%S")
        jsonPostData = json.dumps(postData)
    
        try:
            x = rq.post(url + '/users/createUser', data = jsonPostData)
            
            # time.sleep(3)      
    
        except: 
            print()
    
        else:
            print()
    
        # finally:
            # stopFlag.clear()