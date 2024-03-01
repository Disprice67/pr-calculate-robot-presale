import os

from exchangelib import (DELEGATE, Account, Credentials, FileAttachment,
                         Mailbox, Message)

from config import *

# Settings
UPDATE_DB: dict = {     
    'ОБНОВЛЕНИЕ СТАТУСОВ': STATUS_DIR,
    'ОБНОВЛЕНИЕ ЗАКУПАЕТСЯ': PURCHASE_ONE_DIR,
    'ОБНОВЛЕНИЕ ХОТИМ': PURCHASE_TWO_DIR,
    'ОБНОВЛЕНИЕ КАТЕГОРИЙ': CATEGORIZER_ONE_DIR,
    'ОБНОВЛЕНИЕ ЦЕННИКОВ': CATEGORIZER_TWO_DIR,
    'ОБНОВЛЕНИЕ КОЛЛИЗИЙ': COLLISION_DIR,
    'ОБНОВЛЕНИЕ СВОДА': ARCH_DIR,
    'ОБНОВЛЕНИЕ АРХИВА': ARCHIVE_DIR,
    'ОБНОВЛЕНИЕ ШАССИ': SHASSI_DIR,
    'ОБНОВЛЕНИЕ ДОГОВОРОВ': AGREEMENT_DIR
}

#сделать classmethod в Email, для проверки по темам messageSubject, по словарю Update_DB, в Update_db сделать свои методы и алгоритмы по каждой тебе, (обновление database и тд)

class Email:

    UPDATE_INDEX_DB: int = None

    RECIPIENTS: list = CONST_MAIL.split(', ')

    MESSAGE_SUBJECT: str = None
    MESSAGE_SENDER: str = None
    MESSAGE_BODY: str = None


    def __init__(self, username: str, password: str):
        
        self.credentials = Credentials(
            username=username,
            password=password
        )        

        self.a = Account(
            primary_smtp_address=username,
            credentials=self.credentials,
            autodiscover=True,
            access_type=DELEGATE
        )


    def find_items_in_message(self, file: 'File'):
        """Return_item_in_message."""

        for item in self.a.inbox.all():

                self.FILE_LIST: list = []
                self.MESSAGE_SENDER = item.sender.email_address
                self.MESSAGE_SUBJECT = item.subject

                if item.attachments:
                    for attachment in item.attachments:

                        if 'xlsx' in attachment.name:
                            
                            if self.MESSAGE_SUBJECT in UPDATE_DB:

                                self.UPDATE_INDEX_DB = list(UPDATE_DB).index(self.MESSAGE_SUBJECT)
                                local_path = os.path.join(UPDATE_DB[self.MESSAGE_SUBJECT], attachment.name)

                            else:
                                local_path = os.path.join(INPUT_DIR, attachment.name)
                            
                            with open(local_path, 'wb') as f:
                                f.write(attachment.content)

                            self.FILE_LIST.append((local_path, attachment.name))

                item.delete()        
                return True
        return False


    def send_email(self, attachments=None):
            """
            Send an email.

            Parameters
            ----------
            account : Account object
            subject : str
            body : str
            recipients : list of str
                Each str is and email adress
            attachments : list of tuples or None
                (filename, binary contents)

            Examples
            --------
            >>> send_email(account, 'Subject line', 'Hello!', ['info@example.com'])
            """

            to_recipients = []
            for recipient in self.RECIPIENTS:

                to_recipients.append(Mailbox(email_address=recipient))

            # Create message
            m = Message(account=self.a,
                        folder=self.a.sent,
                        subject=self.MESSAGE_SUBJECT,
                        body=self.MESSAGE_BODY,
                        to_recipients=to_recipients)

            # attach files
            if attachments:

                with open(attachments[0], 'rb') as f:
                    attachment_content = f.read()

                file = FileAttachment(name=attachments[1], content=attachment_content)
                m.attach(file)

            m.send_and_save()

