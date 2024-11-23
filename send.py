import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import random
import string

# Function to print hacker-style banner
def print_hacker_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Only clear at the start
    print("\033[1;31;40m")  # Red color for the banner
    print("""
  ____                  _               
 |  _ \                | |              
 | |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |_) | (_) | | | | | | |_) |  __/ |   
 |____/ \___/|_| |_| |_|_.__/ \___|_|   
                                        
    """)
    print("\033[0m")  # Reset the color after the banner

    # Box with multi-colored text below the banner
    print("\033[1;32;40m")  # Green color for the box
    print("╔═════════════════════════════════════════╗")
    print("\033[1;34;40m" + "║ " + "\033[1;33;40m" + "Author Name : Pak Anonymous" +           "\033[1;34;40m" +           " ║")
    print("\033[1;34;40m" + "║ " + "\033[1;33;40m" + "Whatsapp Number : +923000448415"           + "\033[1;34;40m" +           " ║")
    print("╚═════════════════════════════════════════╝")
    print("\033[0m")  # Reset the color after the box

    print("\033[1;33;40m")
    print("Welcome to the Hacker Tool")
    print("Choose an option:")
    print("1. Email Bomber")
    print("2. SMS Bomber (Dummy)")
    print("3. Exit")
    print("\033[0m")
    time.sleep(1)

# SMTP server details
SMTP_SERVER = 'mail.royalearninghub.click'
SMTP_PORT = 587
SENDER_EMAIL = 'noreply@royalearninghub.click'  # Apna email daalein
SENDER_PASSWORD = '+bUtR?g=)p+2'  # Apna password ya app-specific password

# Function to generate random OTP
def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))  # Random 6-digit OTP
    return otp

# Function to send email
def send_email(receiver_email, num_emails):
    # List of random companies
    companies = ["TechCorp", "FinSolve", "InnoSys", "XenoTech", "GlobalX", "SoftWare Solutions", "Alpha Inc."]
    
    # Start sending emails
    for _ in range(num_emails):
        # Select random company and generate OTP
        company = random.choice(companies)
        otp = generate_otp()
        
        # Generate random email content
        subject = f"Account Verification - {company}"
        body = f"Hello,\n\nPlease verify your account using the following OTP: {otp}\n\nThank you,\n{company} Support Team"

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to SMTP server and send email
            server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            text = msg.as_string()
            server.sendmail(SENDER_EMAIL, receiver_email, text)
            server.quit()
            print(f"Email sent to {receiver_email} from {company} with OTP {otp}")
        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")

# Example usage
if __name__ == "__main__":
    print_hacker_banner()
    receiver_email = input("Enter the receiver email address: ")
    num_emails = int(input("How many emails do you want to send? "))
    send_email(receiver_email, num_emails)
