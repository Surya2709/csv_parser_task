import pandas as pd
from datetime import date, datetime
import json

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

df = pd.read_csv('student.csv')

df = pd.DataFrame(df)

obj = df.to_dict('split')

res = []
for ob in obj['data']:
    
    if len(ob[1])>3 :
        f_name = ob[1][:4]
    else:
        f_name = ob[1]
    if len(ob[2])>3 :
        l_name = ob[2][:4]
    else:
        l_name = ob[2]
    
    username = f_name+l_name
    full_name = ob[1]+ob[2]

    age = calculate_age( datetime.strptime( ob[4],"%Y-%m-%d"))

    if age<18:
        age_criteria = 'minor'
    
    elif age>18 and age <40:
        age_criteria = 'middle_age'
    else:
        age_criteria = 'senior'

    res.append({'full_name' : full_name, 'username' : username , 'age_criteria' : age_criteria})


data = pd.read_json(json.dumps(res))
data.to_csv('results.csv')