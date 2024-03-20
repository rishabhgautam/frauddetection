import requests

url = 'http://localhost:5000/predict_api'


request.get( {timeout: 1500})

r = requests.post(url,json={
'V22':-0.1,
'V3':-1.4,
'V8':-0.9,
'V11':-1.8,	
'V17':0.6,	
'V4':0.1,	
'V14':-2.6,
'V21':-0.1,
'V12':-1.4,
'V7':-0.9,
'V16':-1.8,	
'V10':0.6,	
'V13':0.1
})

print(r.json())
