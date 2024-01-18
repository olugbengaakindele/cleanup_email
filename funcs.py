from email.message import EmailMessage
import smtplib as sml,ssl, os
import imaplib


# print(os.environ['SALES_DATA_EMAIL_SENDER'])
def deleteEmail():
    
    for em in os.environ["EMAILS_TO_CLEANUP"].split(","):
        em = em.strip()
        print(em)
        if "akin" in em.lower() :
            mypassword = os.environ['GMAILPASS2']
            folder_to_clean = 'Inbox'
        else:
            mypassword = os.environ['GMAILPASS']
            folder_to_clean = 'Inbox'

        
            # Login to your email account
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(em, mypassword)
           
            # Select the mailbox you want to delete emails from
            mail.select(f'"{folder_to_clean}"')

            for ems in os.environ["EMIALS_TO_DELETE"].split(","):
                ems = ems.strip()   
               
                # Search for emails from a specific sender
                typ, data = mail.search(None, 'FROM', f'"{ems}"')
                try:
                    # Iterate through the list of emails and delete them
                    for num in data[0].split():
                        mail.store(num, '+FLAGS', '\\Deleted')
                        print(f'{ems} from {em} deleted')

                    # Permanently remove the deleted emails from the mailbox
                        mail.expunge()
                except Exception as e:
                    print(f"{e} is the error")
            # Close the mailbox connection
            mail.close()
            mail.logout()


