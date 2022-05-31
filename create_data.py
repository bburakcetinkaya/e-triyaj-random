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
male_names =  pd.read_csv("tr_isim_erkek.csv")["[isim]"]
female_names = pd.read_csv("tr_isim_kadin.csv")["[isim]"]
surnames = pd.read_csv("tr_soyisimler.csv")["[soyisim]"]

i=0
while i < 1010:
    idn = np.random.randint(12345678901,98765432101,1,dtype=np.int64)
    passw = np.random.randint(100000,999999,1)
    age = np.random.randint(18,80,1)
    if idn not in male_id and idn not in female_id and i%2==0 and i<1000:
        male_id.append(idn)
        male_password.append(passw)
        male_gender.append("MALE")
        male_age.append(age)
        male_name.append(np.random.choice(male_names))
        male_surname.append(np.random.choice(surnames))
        

    if idn not in male_id and idn not in female_id and i%2==1 and i<1000:
        female_id.append(idn)
        female_password.append(passw)
        female_gender.append("FEMALE")
        female_age.append(age)
        female_name.append(np.random.choice(female_names))
        female_surname.append(np.random.choice(surnames))
    
    if i>=1000:
        doctor_id.append(idn)
        doctor_password.append(passw)
    i+=1   

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

data = np.vstack([male, female])
data = np.column_stack([male,female])
data = data.transpose()
df = pd.DataFrame(data,columns=["id","password","gender","age","name","surname"])
# df.columns([])
df.to_csv("data.csv")

