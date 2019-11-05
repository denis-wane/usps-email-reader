'''
Created on Jul 28, 2017

@author: denis.r.wane
'''
import sys
import email
import os
import imaplib
import configparser
 
from_email = ""
from_pwd = ""
smtp_server = ""
detach_dir = ""

# -------------------------------------------------
#
#  This loads properties about the Gmail account from
#  a properties.ini file.  If not present, a
#  configparser.NoSectionError will be returned
#
# -------------------------------------------------
def getConfigs(from_email, from_pwd, smtp_server, detach_dir):
    config = configparser.ConfigParser()
    
    config.read('../properties.ini')
    
    from_email = config.get("SectionOne","GMAIL_USER")
    from_pwd = config.get("SectionOne","GMAIL_APP_PASS")
    smtp_server = config.get("SectionOne","GMAIL_SERVER")
    detach_dir = config.get("SectionOne","IMAGE_DIR_PATH")
    
    return from_email, from_pwd, smtp_server, detach_dir

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
try:
    
    from_email, from_pwd, smtp_server, detach_dir = getConfigs(from_email, from_pwd, smtp_server, detach_dir)
        
    m = imaplib.IMAP4_SSL(smtp_server)
    m.login(from_email,from_pwd)
    m.select('inbox')

    type, data = m.search(None, '(FROM "USPSInformedDelivery@usps.gov")')
    mail_ids = data[0]

    id_list = mail_ids.split()  
    
    for emailid in id_list:
        resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        
        email_body = data[0][1] # getting the mail content 
        mail = email.message_from_bytes(email_body) # parsing the mail content to get a mail object  
                   
        # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
        for part in mail.walk():

            # multipart are just containers, so we skip them
            if part.get_content_maintype() == 'multipart':
                continue
    
            # is this part an attachment ?
            if part.get('Content-Disposition') is None:
                continue
    
            filename = part.get_filename()

            att_path = os.path.join(detach_dir, filename)
    
            #Check if its already there
            if not os.path.isfile(att_path) :
                # finally write the stuff
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

except:
    e = sys.exc_info()[0]
    print( "<p>Error: %s</p>" % e )
    

    
    

