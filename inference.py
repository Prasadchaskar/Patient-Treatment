import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('treatment.pkl', 'rb'))
sex_encod = pickle.load(open('sex_lbl.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
class_names = ['Out Care Patient','In Care Patient']

def predict(df):
    df = df[['HAEMATOCRIT','HAEMOGLOBINS','ERYTHROCYTE','LEUCOCYTE','THROMBOCYTE','MCH','MCHC','MCV','AGE','SEX']]
    df.SEX = sex_encod.transform(df.SEX)
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output
hm = 33.8
hb = 11.1
ery =4.18
leu = 4.6	
thr=150
mch = 26.6
mchc = 32.8
mcv = 80.9
age = 33
sex = 'F'
df = pd.DataFrame({ 
   'HAEMATOCRIT':[hm],
   'HAEMOGLOBINS':[hb], 
    'ERYTHROCYTE':[ery], 
    'LEUCOCYTE':[leu], 
    'THROMBOCYTE':[thr],
    'MCH':[mch],
    'MCHC':[mchc], 
    'MCV':[mcv],
    'AGE':[age],
    'SEX':[sex]
})
print(predict(df))  