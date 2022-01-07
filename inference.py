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
 
