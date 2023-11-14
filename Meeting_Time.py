import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
        title =" Meeting Time ",
        message = """Don't forget our important meeting today at ZOOM!""",
        app_icon = "C:\\Users\\sneha\\Downloads\\ReminderApplicationWithNotification-main\\Meeting.ico.ico",
        timeout = 10
    )
    time.sleep(60*60)
    