# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import asyncio
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionHelloWorld(Action):

     def name(self) -> Text:
        return "action_my_query"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                         

         dispatcher.utter_message(text="Yes this action response")

         print('I am from action py file')

         return []



class ActionSearchResturant(Action):

     def name(self) -> Text:
         return "action_search_resturant"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'hotel':
                 name = e['value']

             if name == 'indian':
                 message = 'Indian1', 'Indian2', 'Indian3'

             if name == 'thai':
                 message = 'thai1', 'thai2', 'thai3'

             if name == 'italian':
                 message = 'italian1', 'italian1', 'italian1'
         dispatcher.utter_message(text=message)

         return []
