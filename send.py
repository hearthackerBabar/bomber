import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'  # Apna email daalein
SENDER_PASSWORD = 'your_email_password'  # Apna password ya app-specific password

# Function to send email
def send_email(receiver_email):
    # Generate random email content
    subjects = ["Welcome", "Notification", "Alert", "Update", "Important"]
    body_messages = [
        "This is a random email sent from a Python script.",
        "Your request has been processed successfully.",
        "Please check your inbox for further updates.",
        "Important: This is just a random email.",
        "Thank you for using our service!"
    ]
    
    # Select random subject and body message
    subject = random.choice(subjects)
    body = random.choice(body_messages)
    
    # Create the email message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_email
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
        server.quit()
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error: {e}")

# Main code to get user email and send the message
def main():
    print("Welcome to the Email Sending Tool")
    receiver_email = input("Please enter the recipient's email address: ")
    
    print("Sending email...")
    time.sleep(2)  # Simulate delay for 2 seconds (you can increase if needed)
    
    # Call the function to send the email
    send_email(receiver_email)

if __name__ == "__main__":
    main()
