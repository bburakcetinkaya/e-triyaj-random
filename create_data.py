import pandas as pd
import numpy as np

male_id = []
male_password = []
female_id = []
female_password = []
female_age = []
doctor_id = []
doctor_password = []
male_gender = []
male_age = []
female_gender = []
male_name = []
female_name = []
male_surname = []
female_surname = []
male = []
female = []
doctor_name = []
doctor_surname = []
doctors_select = []
male_names =  pd.read_csv("tr_isim_erkek.csv")["[isim]"]
female_names = pd.read_csv("tr_isim_kadin.csv")["[isim]"]
surnames = pd.read_csv("tr_soyisimler.csv")["[soyisim]"]
doctors=[]
i=0
for i in range(0,20):
    index = np.random.randint(0,20,1)
    idn = np.random.randint(12345678901,98765432101,1,dtype=np.int64)
    passw = np.random.randint(100000,999999,1)
    doctor_id.append(idn)
    doctor_password.append(passw)  
     
    surname = np.random.choice(surnames)
    if i < 7:
        name = np.random.choice(male_names)
        doctor_name.append(name)
    else:
        name = np.random.choice(female_names)
        doctor_name.append(name)
    doctor_surname.append(surname)

    doctors_select.append(idn)
    doctors_select.append(name)
    doctors_select.append(surname)

doctors_select = np.array(doctors_select)
doctors_select = doctors_select.reshape(20,3)
# selection = a = pd.DataFrame(doctor_id)
i = 0
while i < 1000:
    idn = np.random.randint(12345678901,98765432101,1,dtype=np.int64)
    
    if idn not in male_id and idn not in female_id and i%2==0:
        passw = np.random.randint(100000,999999,1)
        age = np.random.randint(18,80,1)
        index = np.random.randint(0,20,1)
        male_id.append(idn)
        male_password.append(passw)
        male_gender.append("MALE")
        male_age.append(age)
        male_name.append(np.random.choice(male_names))
        male_surname.append(np.random.choice(surnames))
        doctors.append(doctors_select[int(index)])
        i+=1

    if idn not in male_id and idn not in female_id and i%2==1:
        passw = np.random.randint(100000,999999,1)
        age = np.random.randint(18,80,1)
        index = np.random.randint(0,20,1)
        female_id.append(idn)
        female_password.append(passw)
        female_gender.append("FEMALE")
        female_age.append(age)
        female_name.append(np.random.choice(female_names))
        female_surname.append(np.random.choice(surnames))
        doctors.append(doctors_select[int(index)])
        i+=1

    
doctor = []
doctor = np.hstack([doctors_select,doctor_password])
df = pd.DataFrame(doctor,columns=["id","name","surname","password"])
df.to_csv("doctor.csv")

male.append(male_id)
male.append(male_password)   
male.append(male_gender)
male.append(male_age)
male.append(male_name)
male.append(male_surname)

female.append(female_id)
female.append(female_password)
female.append(female_gender)
female.append(female_age)
female.append(female_name)
female.append(female_surname)

# data = np.vstack([male, female])

data = np.column_stack([male,female])
# data.append(doctors)

data = data.transpose()
data = np.hstack((data, np.array(doctors).reshape(1000,3)))


df = pd.DataFrame(data,columns=["id","password","gender","age","name","surname","doctortc","doctorname","doctorsurname"])
df.to_csv("data.csv")

