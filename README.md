# usps-email-reader
Pull Images from your USPS Informed Delivery Feed (Gmail Only)

This is a python script that looks for USPS Informed Delivery emails in a GMAIL inbox and writes the images found within them to a local directory you specify in the properties file.There is some setup to use this script, which includes:

If you're using Multi-Factor Authentication for your GMAIL Account, follow these steps:
	1.  Create an application username for your GMAIL account (can be done within GMAIL)
		1a. The steps to create a GMAIL application password can be found here:  https://support.google.com/accounts/answer/185833?hl=en 
	2. Update the properties.ini file - 
		GMAIL_USER: Set this to your gmail account username
		GMAIL_APP_PASS: Set this to your recently created app password (from step 1)
		GMAIL_SERVER, GMAIL_PORT: Leave as-is
		IMAGE_DIR_PATH: Set to the local path you would like the images to be loaded into
	3.  Once updated, run email_reader.py (or .exe if using executable) and verify images get populated into the directory you specified in properties.ini 
	
If you're not using Multi-Factor Authentication for your GMAIL Account, follow these steps:
	1. Change your settings in GMAIL to allow connections from less secure apps - https://support.google.com/accounts/answer/6010255?hl=en 
	2. Update the properties.ini file - 
		GMAIL_USER: Set this to your gmail account username
		GMAIL_APP_PASS: Set this to your gmail login password
		GMAIL_SERVER, GMAIL_PORT: Leave as-is
		IMAGE_DIR_PATH: Set to the local path you wouldd like the images to be loaded into
	3. Once updated, run email_reader.py (or .exe if using executable) and verify images get populated into the directory you specified in properties.ini 
=======
>>>>>>> branch 'email-features' of https://github.com/denis-wane/usps-email-reader.git
