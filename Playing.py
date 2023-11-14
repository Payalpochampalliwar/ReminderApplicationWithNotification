import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
        title =" Playing Cricket ",
        message = """Calling all cricket enthusiasts! 
        Join us for a thrilling game of cricket this weekend.
          Don't miss out on the excitement!""",
        app_icon = "C:\\Users\\sneha\\Downloads\\ReminderApplicationWithNotification-main\\Playing.ico",
        timeout = 10
    )
    time.sleep(60*60)