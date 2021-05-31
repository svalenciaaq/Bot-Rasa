import requests
import json


headers = {'content-type' : 'application/json'}

data = {
            "appointment_type": "Cita Medica",
            "appointment_with": "Carlos",
            "datetime": "2021-05-19T23:30:00.000Z",
            "hours": [{"client_name": "Santiago","available":False,  "time":"00:30:00"} ]
}
r  = requests.post('https://appointments-carvajal.herokuapp.com/appointments', headers=headers,data=json.dumps(data))


print(r.status_code)



