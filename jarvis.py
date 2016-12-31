import sys
import requests 
import json
import apis
import os
import random
import urllib2 
import pprint
import random
import imaplib
import getpass
import email
import email.header
import datetime
from datetime import datetime

passwd=getpass.getpass()

def speak_a(line):
	try:
		line=line.lower()
	except:
		pass

	line='google_speech -l en '+'\"'+line+'\"'
	os.system(line)

def speak_d(line):
	try:
		line=line.lower()
	except:
		pass
	line='pico2wave -w cook.wav '+'\"'+line+'\"'+' && aplay cook.wav'
	os.system(line)
	os.system("rm cook.wav")

def process_mailbox(M):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        speak_a( "No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            speak_a( "ERROR getting message"+str( num ))
            return

        msg = email.message_from_string(data[0][1])
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = unicode(decode[0])
	speak_a('Message From '+msg['From'])
	speak_a('Message '+str(num)+' '+subject)
        print 'Message %s: %s' % (num, subject)
        print 'Raw Date:', msg['Date']
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            print "Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S")
def mail():
	EMAIL_ACCOUNT = "compcode18@gmail.com"
	EMAIL_FOLDER = "INBOX"
	M = imaplib.IMAP4_SSL('imap.gmail.com')

	try:
	    rv, data = M.login(EMAIL_ACCOUNT,passwd )
	except imaplib.IMAP4.error:
	    speak_a( "LOGIN FAILED!!! ")
	    sys.exit(1)

	print rv, data

	rv, mailboxes = M.list()
	if rv == 'OK':
	    print "Mailboxes:"
	    print mailboxes

	rv, data = M.select(EMAIL_FOLDER)
	if rv == 'OK':
	    speak_a( "Processing mailbox...\n")
	    process_mailbox(M)
	    M.close()
	else:
	    speak_a( "ERROR: Unable to open mailbox "+str(rv))

	M.logout()





def weather():
	speak_d("Okay sir, Please tell me the city ")
    	city =raw_input()	
	pp = pprint.PrettyPrinter(indent=4)
	API_KEY = "9294d3ed0680074c429b6f1e653d8800"
	CITY_NAME = city
	try:
	    f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' \
		            + CITY_NAME + '&units=metric' + '&APPID=' +  API_KEY)
	    respond_raw = f.read()
	except:
		print 'Execption: URL is not correct!'
		raise
	weather_dict = json.loads(respond_raw)
	#pp.pprint(weather_dict)
	#", Lat "+str(weather_dict['coord']['lat']) + " Lon "+str(weather_dict['coord']['lon'])+
	line=('\n\n' +'here is the weather for '+ weather_dict['name']+" \n, , "+ weather_dict['weather'][0]['description'] +',minimum temperature: ' + str(weather_dict['main']['temp_min'])+',maximum temperature: ' + str(weather_dict['main']['temp_max'])+', humidity: ' + str(weather_dict['main']['humidity']) + '%.' )
	try:	
		speak_a(line)
	except:	
		print (line)


def get_greet(f):
    '''
    Input: Salutation type ('hello', 'goodbye', etc.)
    Output: Random relevent string
    '''

    polite_tolerance = 3
    humor_tolerance = 3
    hour = datetime.now().hour
    if hour < 12:
        lt = "Morning"
    elif hour > 17:
        lt = "Night"
    else:
        lt = "Afternoon"


    greetings = open("personality.txt").read().split("\n")
    file = open("output.txt").read().split("\n")
    polite = int(file[0].split("polite=")[1])
    humor = int(file[1].split("humor=")[1])
    phrase_array = []

    for greet in greetings:
        try:
            class_list = greet.split(':')[1].split(",")
            phrase = greet.split(":")[0]
            if class_list[0] == lt or class_list[0] == "Neutral":
                values_list = class_list[1].split(";")
                polite_val = int(values_list[0].split('polite=')[1])
                if polite in range(polite_val - polite_tolerance,
                                   polite_val + polite_tolerance):
                    humor_val = int(values_list[1].split("/")[0].split("humor=")[1])
                    if humor in range(humor_val - humor_tolerance,
                                      humor_val + humor_tolerance):
                        salutation = values_list[1].split("/")[1].split("f=")[1]
                        if salutation == f:
                            phrase_array.append(phrase)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except IndexError:
            pass
    finalout = random.choice(phrase_array)
    return finalout
def command():
	speak_d("Enter command")
	c=raw_input()
	os.system(c)


def start():


    speak_a("Summoning Nikki")
    speak_d(get_greet("hello"))
    while True:
	    speak_d("How can i Help u Sir, ")
	    choice=raw_input()
	    if choice =='mail':
		mail()
	    if choice =='weather':
	    	weather()
	    if choice=='command':
		command()


start()



