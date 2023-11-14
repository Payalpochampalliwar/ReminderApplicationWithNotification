import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
        title =" YoGa Time ",
        message = """Find balance, peace, and strength within. 
        Embrace the art of yoga and unlock the harmony of mind, body, and soul.""",
        app_icon = "C:\\Users\\sneha\\Downloads\\ReminderApplicationWithNotification-main\\YoGA.ico.ico",
        timeout = 10
    )
    time.sleep(60*60)
    