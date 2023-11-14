import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
        title =" Eating Food ",
        message = """Part of the Secret of Success is to eat what you like 
        and let the food fight it out inside ,Say By Mark Twain""",
        app_icon = "C:\\Users\\sneha\\Downloads\\ReminderApplicationWithNotification-main\\Food.ico.ico",
        timeout = 10
    )
    time.sleep(60*60)
    


    