# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#from typing_extensions import Required


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.types import DomainDict
import webbrowser
import requests
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

### Form Slot Action example
class ValidateResturantForm(Action):

    def name(self) -> Text:
        return "user_detail_form"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        
        required_slots = ['name', 'number']

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet('requested_slot', None)]


class ActionSubmit(Action):
    def name(self) ->Text:
        return 'action_submit'

    async def run(self, dispatcher, 
        tracker: Tracker, 
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(template="utter_detail_thanks", Name = tracker.get_slot("name"), Mobile_number=tracker.get_slot("number"))
        


# For playing video

class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        
        video_url = "https://www.youtube.com/watch?v=OUpL5nxKI4A&list=PLtFHvora00y80hvsNJ-6YkmfTMrxk5rOe&index=6"
        
        
        dispatcher.utter_message(text="wait...playing your video!")
        webbrowser.open(video_url)
        return []

#Corona Tracker

class Actioncoronastats(Action):

    def name(self) -> Text:
        return "actions_corona_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Covid report for:", entities)
        state = None

        for i in entities:
            if i["entity"] == "state":
                state = i["value"]

        message = "Please Enter Correct State Name !"

        if state == "india":
            state = "Total"
        
        for data in responses["statewise"]:
            if data["state"] == state.title():
                
                message = "Now Showing Cases For --> " + state.title() + " Since Last 24 Hours : "+ "\n" + "Active: " + data[
                    "active"] + " \n" + "Confirmed: " + data["confirmed"] + " \n" + "Recovered: " + data[
                              "recovered"] + " \n" + "Deaths: " + data["deaths"] + " \n" + "As Per Data On: " + data[
                              "lastupdatedtime"]

        print(message)
        dispatcher.utter_message(message)

        return []


