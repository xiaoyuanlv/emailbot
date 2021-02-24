import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info(info):
    return input(info + ": ")


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('myemail@gmail.com', 'mypassword')
    email = EmailMessage()
    email['From'] = 'xiaoyuanlv.31@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'yourfriend': 'yourfriend@gmail.com',
    'lisa': 'lisanobody@nobody.com'
}


def get_email_info():
    talk('Hey! Friend. To whom you want to send email')
    name = get_info('Name')
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of the email')
    subject = get_info('Subject')
    talk('Tell me the text in your email')
    message = get_info('Message')
    send_email(receiver, subject, message)
    talk('Hey Lazy. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info('More? yes or no')
    if 'yes' in send_more:
        get_email_info()




get_email_info()
