import schedule
import time

# Define a function to send email
def send_email():
    print("Email sent at:", time.strftime("%H:%M:%S"))

# Schedule the task to run every day at 11:53 pm
schedule.every().day.at("23:53").do(send_email)

# Keep the program running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)

