from plyer import notification
import Drinking_WaterPopUp
import EatingFoodPopUp
import Meeting_Time
import Playing
import reading_time
import YoGa

# Define a list of notifications
notifications =[
    {"title":"Drinking Water", "Reminder":"Reminder 1","message": "Drinking water is essential to a healthy lifestyle", "delay": 10},
    {"title":"Eating Food","Reminder": "Reminder 2","message":"Part of the Secret of Success is to eat what you like and let the food fight it out inside ,Say By Mark Twain" , "delay": 20},
    {"title":" Meeting Time ","Reminder":"Reminder 3","message": "Don't forget our important meeting today at ZOOM!", "delay": 30},
    {"title":"Playing Cricket ","Reminder":"Reminder 4","message":"Calling all cricket enthusiasts! Join us for a thrilling game of cricket this weekend. Don't miss out on the excitement!", "delay": 40},
    {"title":"Reading Time","Reminder": "Reminder 5","message": "Books are windows to new worlds, where imagination takes flight and knowledge finds its voice.","delay": 50},
    {"title":"YoGa Time","Reminder":"Reminder 6","message": "Find balance, peace, and strength within. Embrace the art of yoga and unlock the harmony of mind, body, and soul", "delay": 60},
]

# Iterate through the list and schedule notifications
for notification_info in notifications:
    title = notification_info.get("title")
    Reminder = notification_info.get("Reminder")
    message = notification_info.get("message")
    delay = notification_info.get("delay")
    
    notification.notify(
        title=title,
        message=message,
        timeout=delay
    )

# Keep the script running
while True:
    pass