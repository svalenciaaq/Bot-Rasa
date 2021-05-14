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
        
        Database.inititialize()


        slot = tracker.get_slot("dniuser")

        month =  slot[0]

        query ={
            "month" : month
        }
        result = Database.find_one("users", query)

      
        return []


class ActionReceiveHour(Action):
    def name(self) -> Text:
        return "action_ask_hour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        Database.inititialize()
     
        dispatcher.utter_message(text="El dia que elegiste:" )

        dispatcher.utter_message(text="Los horarios disponibles son:" + "12:00" + "13:00" + "15:00")
      
        return []



class ActionReceiveMonth(Action):
    def name(self) -> Text:
        return "action_ask_month"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot = tracker.get_slot("dniuser")

        dni= int(slot[0])

        print(type(dni))

        print(dni)   
        Database.inititialize()


        query ={
            "dni_user" : dni
        }
        result = Database.find_one("users", query)

        userName=  result['firstname']
        print(userName)
        dispatcher.utter_message(text="Tu nombre es " + userName)
        dispatcher.utter_message(text="Que mes quisiera la cita")
        return []


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def inititialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['Users']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)    
       