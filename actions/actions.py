# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import pymongo
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import requests

url ="http://7gqvd.mocklab.io/"
rutepost = "json"
ruteget = ""

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
        

        slot = tracker.get_slot("dniuser")

        dispatcher.utter_message(text="Que dia quisiera la cita")
      
        return []


class ActionReceiveHour(Action):
    def name(self) -> Text:
        return "action_ask_hour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot =  tracker.get_slot("day")


        day  = slot[0]
     
        dispatcher.utter_message(text="El dia que elegiste:" + day )

        dispatcher.utter_message(text="Los horarios disponibles son:" + "12:00" + "13:00" + "15:00")

        dispatcher.utter_message(text="Que hora quisiera su cita")
      
        return []



class ActionReceiveMonth(Action):
    def name(self) -> Text:
        return "action_ask_month"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot = tracker.get_slot("dniuser")

        dni= int(slot[0])

        query ={
            "dni_user" : dni
        }

        response =  requests.post(url + rutepost , query)

        if response.status_code == 200:
            print("success")
        elif response.status_code == 404:
            print("Not found")

        username = "Santiago"
        dispatcher.utter_message(text="Tu nombre es" + " " + str(dni))
        dispatcher.utter_message(text="Que mes quisiera la cita")


        return []




class ActionInformForm(Action):

    def name(self) -> Text:
        return "action_inform_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



    
        slot =  tracker.get_slot("month")
        monthe =  slot.lower()

        slot2 = tracker.get_slot("day")

        day =  slot2

        slot3 =  tracker.get_slot("hour")
        
        month = None


        year = "2021"


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
 






        date = year +"-"+ month +"-"+ day

        print(date)


        data = {
            "date": date
        }

        x = json.dumps(data)


        # response = requests.post(url + rutepost, x)

     
        dispatcher.utter_message(text="xddd")

        return []

# class Database(object):
#     URI = "mongodb://127.0.0.1:27017"
#     DATABASE = None

#     @staticmethod
#     def inititialize():
#         client = pymongo.MongoClient(Database.URI)
#         Database.DATABASE = client['Users']

#     @staticmethod
#     def insert(collection, data):
#         Database.DATABASE[collection].insert(data)


#     @staticmethod
#     def find(collection, query):
#         return Database.DATABASE[collection].find(query)

#     @staticmethod
#     def find_one(collection, query):
#         return Database.DATABASE[collection].find_one(query)    
       