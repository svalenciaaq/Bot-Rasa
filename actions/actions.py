# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker,  FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.types import DomainDict

import json
import requests
import datetime

url ="http://localhost:1337/"
rutepost = "json"
ruteget = "appointments"
rutegetuser = "usuarios"
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class Actionrecievedni(Action):
    def name(self) -> Text:
        return "action_ask_dniuser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Cual es tu numero de identificacion")
      
        return []



class ActionReceiveDay(Action):
    def name(self) -> Text:
        return "action_ask_day"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Que dia quisiera la cita")
      
        return []


class ActionReceiveHour(Action):
    def name(self) -> Text:
        return "action_ask_hour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        dispatcher.utter_message(text="Que hora quisiera su cita")
      
        return []



class ActionReceiveMonth(Action):
    def name(self) -> Text:
        return "action_ask_month"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
    
     
        dispatcher.utter_message(text="Que mes quisiera la cita")


        return []




class ActionInformForm(Action):

    def name(self) -> Text:
        return "action_inform_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



    
        slot =  tracker.get_slot("month")
        monthe =  slot[0].lower()

      

        slot2 = tracker.get_slot("day")

        day =  slot2[0]

        slot3 =  tracker.get_slot("hour")
        
        month = None

        if isinstance(slot3, str):
            hour = slot3.replace(' ','').split(":")
        else:
            hour =  slot3[0].replace(' ','')

        


        slot4 =  tracker.get_slot("dni_user")

        dni = slot4[0]

        year = "2021"

        entities =  tracker.latest_message['entities']

        for e in entities:
            if e['entity'] == 'timer':
                timer =  e['value']

        if isinstance(slot, str):
            monthe =  slot
           
        else:
            monthe =  slot[0].lower()
          
           

        print(monthe)
        if monthe  == "enero":
            month = "01"
        elif monthe == "febrero":
            month = "02"
        elif monthe == "marzo":
            month = "03"  
        elif monthe == "abril":
            month = "04"
        elif monthe == "mayo":
            month = "05"
        elif monthe == "junio":
            month = "06"
        elif monthe == "julio":
            month = "07"                  
        elif monthe == "agosto":
            month = "08"                  
        elif monthe == "septiembre":
            month = "09"                  
        elif monthe == "octubre":
            month = "10"                  
        elif monthe == "noviembre":
            month = "11"                  
        elif monthe == "diciembre":
            month = "12"                  
 
        if timer == "tarde":
            print("Hora que creo",hour)   



        year1 = int(year)
        month1 = int(month)
        day1 =  int(day)

        date = datetime.datetime(year1, month1, day1 , 1).isoformat()


        if isinstance(hour, str):
            hour1 = int(hour)
            time = datetime.time(hour1)
            time1 =  str(time)
        else:
            time = datetime.time(int(hour[0]), int(hour[1]))
            time1 =  str(time)
           
    


        r  = requests.get('https://appointments-carvajal.herokuapp.com/users')

        data =  r.json()
        username = ""


        if isinstance(slot4, str):
            dni = slot_value.replace(' ','')
        else:
            dni =  slot4[0].replace(' ','')
   

        for i in range(len(data)):
            x = data[i]
            if dni == x["dni"]:
                username = x["name"]

      
        data = {
            "appointment_type": "Cita Medica",
            "appoinment_with": "Carlos",
            "datetime": date,
            "hours": [{"client_name": username,"available":False,  "time":time1} ]
}

        send = json.dumps(data)

    
        headers = {'content-type' : 'application/json'}
        try:
            r = requests.post("https://appointments-carvajal.herokuapp.com/appointments",headers=headers ,data = send)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        dispatcher.utter_message(text="Cita creada con exito")

        return [AllSlotsReset()]


     


class ActionRequestCitaCercana(Action):

    def name(self) -> Text:
        return "action_citacercana"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      
        horarios = ["6:00:00.000", "7:00:00.000", "8:00:00.000", "9:00:00.000", "10:00:00.000", "11:00:00.000", "12:00:00.000", "13:00:00.000",
         "14:00:00.000", "15:00:00.000", "16:00:00.000", "17:00:00.000", "18:00:00.000","6:30:00.000", "7:30:00.000","8:30:00.000","9:30:00.000",
         "10:30:00.000","11:30:00.000","12:30:00.000","13:30:00.000","14:30:00.000","15:30:00.000","16:30:00.000","17:30:00.000", "18:30:00.000"]
        try:
            r  = requests.get('https://appointments-carvajal.herokuapp.com/appointments')
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        

        data =  r.json()
        date = data[0]
        l =  date["datetime"].split("-")
        m =  l[2]
        t = (m.split("T"))[0]
        

        for i in range(len(data)):
            x = data[i]
            y = x["hours"]
            z =  y[0]

            time =  z['time']
            p =  len(horarios)



            for j in range(p):
                if time == horarios[j]:
                    horarios.pop(j)
                    break
        


        # print(response.text)

        dispatcher.utter_message(text="Es estas")
        return []




class ActionRequestCitaEspecifica(Action):

    def name(self) -> Text:
        return "action_cita_especifica"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:





        # day =  tracker.get_slot("day_request")
        # month =  tracker.get_slot("month_request")


        entities =  tracker.latest_message['entities']
        monthe= ""
        for e in entities:
            if e['entity'] == 'day_request':
                day =  e['value']
            

            if e['entity'] == 'month_request':
                monthe = e['value']    
               

        month = ""
        if monthe  == "enero":
            month = "01"
        elif monthe == "febrero":
            month = "02"
        elif monthe == "marzo":
            month = "03"  
        elif monthe == "abril":
            month = "04"
        elif monthe == "mayo":
            month = "05"
        elif monthe == "junio":
            month = "06"
        elif monthe == "julio":
            month = "07"                  
        elif monthe == "agosto":
            month = "08"                  
        elif monthe == "septiembre":
            month = "09"                  
        elif monthe == "octubre":
            month = "10"                  
        elif monthe == "noviembre":
            month = "11"                  
        elif monthe == "diciembre":
            month = "12" 


        horarios = ["6:00:00.000","6:30:00.000", "7:00:00.000", "7:30:00.000", "8:00:00.000", "8:30:00.000","9:00:00.000","9:30:00.000",
         "10:00:00.000","10:30:00.000", "11:00:00.000",  "11:30:00.000","12:00:00.000","12:30:00.000", "13:00:00.000","13:30:00.000",
         "14:00:00.000",  "14:30:00.000","15:00:00.000", "15:30:00.000", "16:00:00.000", "16:30:00.000", "17:00:00.000","17:30:00.000", "18:00:00.000",
         "18:30:00.000"]


        try:
            r  = requests.get('https://appointments-carvajal.herokuapp.com/appointments')
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        

        data =  r.json()
        # date = data[0]
        # l =  date["datetime"].split("-")
        # m =  l[2]
        # t = (m.split("T"))[0]
        # k = l[1]




 
        
        
        
        for i in range(len(data)):
            x = data[i]
            l =  x["datetime"].split("-")


            m =  l[2]


            # Day
            t = (m.split("T"))[0]

    
            # Month
            k = l[1]



            y = x["hours"]
            z =  y[0]

            time =  z['time']
            p =  len(horarios)

            if k ==  month and t  == day:
         
                for j in range(p):

                    if time == horarios[j]:
                        horarios.pop(j)
                        break
        
        textr=  ""
        for b in range(len(horarios)):
            if horarios[b] == "6:00:00.000":
                textr+= "6 de la mañana, "
            if horarios[b] == "6:30:00.000":
                textr+= "6 y 30 de la mañana, "
            if horarios[b] == "7:00:00.000":
                textr+= "7 de la mañana, "
            if horarios[b] == "7:30:00.000":
                textr+= "7 y 30 de la mañana, "    
            if horarios[b] == "8:00:00.000":
                textr+= "8 de la mañana, "
            if horarios[b] == "8:30:00.000":
                textr+= "8 y 30 de la mañana, "
            if horarios[b] == "9:00:00.000":
                textr+= "9 de la mañana, "
            if horarios[b] == "9:30:00.000":
                textr+= "9 y 30 de la mañana, "
            if horarios[b] == "10:00:00.000":
                textr+= "10 de la mañana, "
            if horarios[b] == "10:30:00.000":
                textr+= "10 y 30 de la mañana, "
            if horarios[b] == "11:00:00.000":
                textr+= "11 de la mañana, "
            if horarios[b] == "11:30:00.000":
                textr+= "11 y 30 de la mañana, "
            if horarios[b] == "12:00:00.000":
                textr+= "12 de la mañana, "
            if horarios[b] == "12:30:00.000":
                textr+= "12 y 30 de la mañana, "
            if horarios[b] == "13:00:00.000":
                textr+= "13 de la mañana, "
            if horarios[b] == "13:30:00.000":
                textr+= "13 y 30 de la mañana, "
            if horarios[b] == "14:00:00.000":
                textr+= "14 de la mañana, "
            if horarios[b] == "14:30:00.000":
                textr+= "14 y 30 de la mañana, "
            if horarios[b] == "15:00:00.000":
                textr+= "15 de la mañana, "
            if horarios[b] == "15:30:00.000":
                textr+= "15 y 30 de la mañana, "


            if horarios[b] == "16:00:00.000":
                textr+= "16 de la mañana, "
            if horarios[b] == "16:30:00.000":
                textr+= "16 y 30 de la mañana, "

            if horarios[b] == "17:00:00.000":
                textr+= "17 de la mañana, "
            if horarios[b] == "17:30:00.000":
                textr+= "17 y 30 de la mañana, " 

            if horarios[b] == "18:00:00.000":
                textr+= "18 de la mañana, "
            if horarios[b] == "18:30:00.000":
                textr+= "18 y 30 de la mañana, "     

            

     
        dispatcher.utter_message(text=textr)
        return []




def defaultconverter(o):
  if isinstance(o, datetime.datetime):
      return o.__str__()


class ValidateCitaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_cita_form"

    

    def validate_dni_user(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
    
        r  = requests.get('https://appointments-carvajal.herokuapp.com/users')

        data =  r.json()
        check = False
        dni = ""
        if isinstance(slot_value, str):
            dni = slot_value.replace(' ','')
        
        else:
            dni =  slot_value[0].replace(' ','')
          
    
        # print(dni)
        for i in range(len(data)):
            x = data[i]
            if dni == x["dni"]:
              
                check = True    

        if check == False:

            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"dni_user": None}
        else:
            return {"dni_user": slot_value}