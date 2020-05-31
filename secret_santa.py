import smtplib
from email.mime.text import MIMEText
import random
import datetime
import sys
import csv

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()


# mail credentials 
email_address = 'example@gmail.com' # email address where the emails will be sent
email_pw = 'email_pw' # email password

mail.login(email_address, email_pw)

current_year = str(datetime.datetime.now().year)
value = '10' # maximum ammount of money for the present
data_limit = '25th of December' # limit date 
subject = 'Secret Santa ' + current_year +'!' # email subject

tuple_list = []
email_list = []

with open('path/to/file/file.txt', encoding='UTF-8') as inf:
    reader = csv.reader(inf, delimiter=";")
    for row in reader:
        tuple_list.append((row[0], row[1]))
        email_list.append(row[0])

random.shuffle(email_list)
random.shuffle(tuple_list)
pair_results_final = []

def create_pair_results():
    condition_met = True
    pair_results = []
    emails = [i for i in email_list]
    tuple = [i for i in tuple_list]
    iteration = len(emails)
    while(iteration > 0):
        iterator1 = random.randrange(0, len(emails))
        iterator2 = random.randrange(0, len(tuple))
        condition_met = True
        while(emails[iterator1] == tuple[iterator2][0]):
            if iteration == 1:
                condition_met = False
                emails = [i for i in email_list]
                tuple = [i for i in tuple_list]
                pair_results = []
                iteration = len(email_list)
                print('Failed.') 
            else:
                random.shuffle(emails)
                iterator1 = random.randrange(0, len(emails))
                iterator2 = random.randrange(0, len(tuple))

        if(condition_met):
            receiver = emails[iterator1]
            person = tuple[iterator2][1]
            del emails[iterator1]
            del tuple[iterator2]
            pair_results.append((receiver, person))
            iteration = iteration - 1

        

    return pair_results


def send_email(person, receiver, optional_message=''):    
    content = """\
        <!DOCTYPE html>
        <html>
            <head>
                <title>Secret Santa</title>
            </head>
            <body style="background-color: #f2f2f2; text-align: center; color: black; padding-top: 10px; padding-bottom: 20px; padding-left: 20px;  padding-right: 20px; font-family: Arial, Helvetica, sans-serif;">
                <div style="align='center'">
                    <h3 style="font-size: 20px; text-align: center;">
                        Your secret santa is:
                    </h3>
                    <h1 style="font-size: 50px;
                        word-spacing: 10px;
                        margin-left: 50px;
                        text-align: center; 
                        margin-right: 50px;
                        padding: 4px;">""" + person + """
                    </h1>

                    <h2 style="margin-left: 50px; text-align: center; margin-right: 50px;">
                        Now you know! Youu need to buy a present with a maximum value of """ + value + """€ until """ + data_limit + """ from """ + current_year + """!
                    </h2>

                    <h1 style="font-weight: bold; text-align: center;">
                        Happy Christmas!!
                    </h1>

                    <br/>
                    <br/>
                    <p style="font-weight: bold; text-align: center;">
                        Any error please contact the support!
                    </p>
                    <p style="font-size: 9px; text-align: center;">
                        """ + optional_message + """
                    </p>
                </div>
            </body>
            """
    
    msg = MIMEText(content, 'html')
    msg['From'] = email_address
    msg['To'] = receiver
    msg['Subject'] = subject
    mail.sendmail(email_address, receiver, msg.as_string()) 
    #print(receiver, " received: ", person)


pair_results_final = create_pair_results()
for p in pair_results_final:
    send_email(p[1], p[0])

mail.close()
sys.exit()
