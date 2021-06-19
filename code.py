import subprocess #Setup Email Notification
import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#from email import encoders
#from email.mime.base import MIMEBase
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import threading
#import RPi.GPIO as GPIO #Import
#import glob
#GPIO.setmode(GPIO.BCM) #Set for GPIO Number

import os

import datetime            #Desplay Time 
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
import time #Sleeptime

state=False
#temp sensor
# Initialize the GPIO Pins
#os.system('modprobe w1-gpio')  # Turns on the GPIO module
#os.system('modprobe w1-therm') # Turns on the Temperature module

# Finds the correct device file that holds the temperature data
#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

# A function that reads the sensors data
#def read_temp_raw():
#  f = open(device_file, 'r') # Opens the temperature device file
#  lines = f.readlines() # Returns the text
#  f.close()
#  return lines

# Convert the value of the sensor into a temperature
#def read_temp():
#  lines = read_temp_raw() # Read the temperature 'device file'
  #print(len(lines))

  # While the first line does not contain 'YES', wait for 0.2s
  # and then read the device file again.
#  stop=False
#  if len(lines)<1:
#      stop=True
#  while stop:
#    time.sleep(0.2)
#    lines = read_temp_raw()
#    if len(lines)>1:
#        if lines[0].strip()[-3:] == 'YES' :
#            stop=False
            
  #while lines[0].strip()[-3:] != 'YES' :
    #time.sleep(0.2)
    #lines = read_temp_raw()

  # Look for the position of the '=' in the second line of the
  # device file.
#  equals_pos = lines[1].find('t=')

  # If the '=' is found, convert the rest of the line after the
  # '=' into degrees Celsius, then degrees Fahrenheit
#  if equals_pos != -1:
#    temp_string = lines[1][equals_pos+2:]
#    temp_c = float(temp_string) / 1000.0
#    temp_f = temp_c * 9.0 / 5.0 + 32.0
#    return temp_f #add temp_c, before temp_f for celcus

# def photo():

#     print('Capturing Photo')
#     subprocess.call(["raspistill", "-o", "/home/pi/Desktop/Sump.jpg"])
#     time.sleep(0.5)
#     email_sender = 'sumptankalarm@gmail.com'
#     email_receiver = 'sumptankalarm@gmail.com'
#     subject = 'Sump Over Flow'
#    msg = MIMEMultipart()
#    msg['From'] = email_sender
#    msg['To'] = email_receiver
#    msg['Subject']= subject
#    body = 'High water Level has been detected in Sump'
#    msg.attach(MIMEText(body, 'plain'))
    #FILE PART
#    filename = 'Sump.jpg'
#    attachment = open(filename, 'rb')
    # part = MIMEBase('application', 'octet_stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', 'attachment; filename= '+filename)
    # msg.attach(part)
    # #########
    # text = msg.as_string()
    # connection = smtplib.SMTP('smtp.gmail.com', 587)
    # connection.starttls()
    # connection.login(email_sender, 'sumptank420')
    # connection.sendmail(email_sender, email_receiver, text )
    # connection.quit()
    # GPIO.output(26,GPIO.HIGH) # Turn off Emergency Lights
    # print ("Email Sent")

def reading():
    global closing
    global lightstate
    global state
    while closing:
        while closing:
            #print("reading")
            #buttonState = GPIO.input (18) # SensorState means GPIO 18
            #time.sleep(0.1)
            #temperaturebtnstate(temp)
            #temperaturebtnstate(read_temp())
            print("leyendo")
            time.sleep(1)
            if state == True:
            #if state == True:
                #plt.pause(0.1)
                print("overflow")
                
                overflowbtnstate(state)
                instructionshown(1) #case 1= Overflow
                
                time.sleep(1)
                
                #GPIO.output(6, False) #LED Green Light Off
                #GPIO.output(12, True) #lED Red Light ON
                #GPIO.output(26,GPIO.LOW)
               # thread2=threading.Thread(target=photo,daemon=True)
               # thread2.start()
                print('photo')
                
#                 #time.sleep(0.5)
#                 import subprocess #Setup Email Notification
#                 import smtplib
#                 from email.mime.text import MIMEText
#                 from email.mime.multipart import MIMEMultipart
#                 from email import encoders
#                 from email.mime.base import MIMEBase
#                 from email.mime.text import MIMEText
#                 from email.mime.multipart import MIMEMultipart
#                 print('Capturing Photo')
#                 subprocess.call(["raspistill", "-o", "/home/pi/Desktop/Sump.jpg"])
#                 time.sleep(0.5)
#                 email_sender = 'sumptankalarm@gmail.com'
#                 email_receiver = 'sumptankalarm@gmail.com'
#                 subject = 'Sump Over Flow'
#                 msg = MIMEMultipart()
#                 msg['From'] = email_sender
#                 msg['To'] = email_receiver
#                 msg['Subject']= subject
#                 body = 'High water Level has been detected in Sump'
#                 msg.attach(MIMEText(body, 'plain'))
#                 #FILE PART
#                 filename = 'Sump.jpg'
#                 attachment = open(filename, 'rb')
#                 part = MIMEBase('application', 'octet_stream')
#                 part.set_payload((attachment).read())
#                 encoders.encode_base64(part)
#                 part.add_header('Content-Disposition', 'attachment; filename= '+filename)
#                 msg.attach(part)
#                 #########
#                 text = msg.as_string()
#                 connection = smtplib.SMTP('smtp.gmail.com', 587)
#                 connection.starttls()
#                 connection.login(email_sender, 'sumptank420')
#                 connection.sendmail(email_sender, email_receiver, text )
#                 connection.quit()
#                 print ("Email Sent")
                while True:
                    time.sleep(1)
                    print("overflowing")
                    #plt.pause(0.1)
                    #temperaturebtnstate(read_temp())
                    #buttonState = GPIO.input (18)
                    if state == False: #Water level back to normal
                    #if state == False:
                        #plt.pause()
                        overflowbtnstate(state)
                        instructionshown(1000) #case 1000 Return normal
                        
                        #GPIO.output(26,GPIO.HIGH) # Turn off Emergency Lights
                        
                        print("Water Returned to Normal...")
                        #GPIO.output(12, False) #Led light Green on
                        #GPIO.output(6, True)   #Led light Red off
                        break
                    
            #AutoTopoff =not GPIO.input (5) # AutoTopoff means GPIO 5
            if False:
                #plt.pause()
                #toppingbtnstate(AutoTopoff)
                instructionshown(2) #Topping Tank Auto Filled
                
                #GPIO.output(17,GPIO.LOW)
                print ("Topping off Tank")
                #time.sleep(5)
                print ("Top off Complete...")
                #GPIO.output(17,GPIO.HIGH)
                time.sleep(1)
                print ("Water Level Normal...")
                while True:
                    #plt.pause(0.1)
                    print("topping tank")
                    #AutoTopoff =not GPIO.input (5)
                    #temperaturebtnstate(read_temp())
                    if False:
                        #toppingbtnstate(AutoTopoff)
                        instructionshown(1000) #Operations Normal
                        break
                    
                    
def overflowbtnstate(state):
    if state:
        btnoverflotile.label.set_text("Overflow")
        btnoverflotile.color='red'
        btnoverflotile.ax.set_facecolor('red')
        btnoverflotile.hovercolor='red'
    else:
        btnoverflotile.color='blue'
        btnoverflotile.ax.set_facecolor('blue')
        btnoverflotile.hovercolor='blue'
        btnoverflotile.label.set_text("Normal")

def toppingbtnstate(state):
    if state:
        btntoppingtile.label.set_text("Topping Tank")
        btntoppingtile.color='red'
        btntoppingtile.ax.set_facecolor('red')
        btntoppingtile.hovercolor='red'
    else:
        btntoppingtile.color='blue'
        btntoppingtile.ax.set_facecolor('blue')
        btntoppingtile.hovercolor='blue'
        btntoppingtile.label.set_text("Level Normal")
        
def flowbtnstate(state):
    if state:
        btnflowtile.label.set_text("Not normal")
        btnflowtile.color='red'
        btnflowtile.ax.set_facecolor('red')
        btnflowtile.hovercolor='red'
    else:
        btnflowtile.color='blue'
        btnflowtile.ax.set_facecolor('blue')
        btnflowtile.hovercolor='blue'
        btnflowtile.label.set_text("Flow Normal")

def temperaturebtnstate(temp):
    #print('sensingtemp')
    temp=round(temp,1)
    if temp<74:
        btntemptile.color='#F00505'
        btntemptile.ax.set_facecolor('#F00505')
        btntemptile.hovercolor='#F00505'
        btntemptile.label.set_text(temp)
    elif temp<75.9:
        btntemptile.color='#FEF001'
        btntemptile.ax.set_facecolor('#FEF001')
        btntemptile.hovercolor='#FEF001'
        btntemptile.label.set_text(temp)
    elif temp<78:
        btntemptile.color='#1BF118'
        btntemptile.ax.set_facecolor('#1BF118')
        btntemptile.hovercolor='#1BF118'
        btntemptile.label.set_text(temp)
    elif temp<80:
        btntemptile.color='#FEF001'
        btntemptile.ax.set_facecolor('#FEF001')
        btntemptile.hovercolor='#FEF001'
        btntemptile.label.set_text(temp)
    elif temp>=80:
        btntemptile.color='#F00505'
        btntemptile.ax.set_facecolor('#F00505')
        btntemptile.hovercolor='#F00505'
        btntemptile.label.set_text(temp)

        
def instructionshown(n):
    if n==1: #Overflow
        instructions='1: Make sure power is On\n\n'\
        +'2: Check Pump Controller\nis set to 11\n\n'\
        +'3: In case of Emergency\nset Pump Contoller to Max\nthis moves water out\nsump faster\n\n'\
        +'4: CALL DAD NOW!!!! \n(760) 270-1302\n\n'\
        +'5: If all else fails\n.... FUCK IT....'
        txtread1tile.set_text(instructions)
    elif n==2: # Topping Tank
        instructions='Tank is being Auto Filled'
        txtread1tile.set_text(instructions)
    elif n==3:
        instructions='Your\ninstructions\nhere case 3'
        txtread1tile.set_text(instructions)
    elif n==4:
        instructions='Your\ninstructions\nhere case 3'
        txtread1tile.set_text(instructions)
    else:
        instructions='Operations Normal...'
        txtread1tile.set_text(instructions)
    

        
def draw():
    plt.draw()
    plt.pause(0.001)

def lights(event):
    global lightstate
    global temp
    global state

    #temp=temp+5
    #temperaturebtnstate(temp)
    

    lightstate= not lightstate
    state= not state
    if lightstate:
        #GPIO.output(26,GPIO.LOW)
        btnlighttile.color='g'
        btnlighttile.ax.set_facecolor('g')
        btnlighttile.hovercolor='g'
        btnlighttile.label.set_text('Lights On')
    else:
        #GPIO.output(26,GPIO.HIGH)
        btnlighttile.color='black'
        btnlighttile.ax.set_facecolor('black')
        btnlighttile.hovercolor='black'
        btnlighttile.label.set_text('Lights Off')
    
    time.sleep(0.2)    
    
    
def close(event):
    global closing
    closing=False
    print("out")
    plt.close()
    
    
def dummy(event):
    pass

def readtempfun(temp):
    i=0
    while i<20:
        temp.value=i
        time.sleep(0.1)
        i=i+1
    
#if __name__ == '__main__':    
#initialization



closing=True
lightstate=False
temp=1
plt.switch_backend('TkAgg')
plt.style.use('dark_background')
fig, ax = plt.subplots()
mng = plt.get_current_fig_manager()
mng.resize(1024,600)
plt.subplots_adjust(left=0,bottom=0,right=0.01,top=0.01)
fig.canvas.toolbar.pack_forget()



#GPIO.setup(26,GPIO.OUT) #Relay to Control Lights 
#GPIO.setup(17,GPIO.OUT) #Relay to Top off Pump

#GPIO.setup (18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Setup Water Level Sensor
#GPIO.setup (5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Setup Auto Top off
# Setup LED Lights
#GPIO.setup(6,GPIO.OUT)
#GPIO.setup(12,GPIO.OUT) 
#GPIO.output(6, True)
#Make sure Pump and Lights start off
#GPIO.output(17,GPIO.HIGH)
#GPIO.output(26,GPIO.HIGH)

print ("Initializing...") #Starting Program
time.sleep(1)
print ("Complete...")
time.sleep(1)
print ("Water Level Normal...")    
    

#axtxtoverflow = plt.axes([0.2, 0.5, 0.3, 0.3])
#axtxttopping = plt.axes([0.5, 0.5, 0.3, 0.3])


#axbtnlights=plt.axes([0.4,0.13,0.2,0.1])


#txtoverflow = plt.text(axtxtoverflow, '',initial='Sump Water Level Normal',backgroundcolor='black')
#txttopping = plt.text(axtxttopping, '',initial='Tank Water Level Normal', backgroundcolor='black')

#txtoverflow = plt.text(-1.6,6,'Sump Water Level Normal',backgroundcolor='black',size=45)
#txttopping = plt.text(-1.5,3,'Tank Water Level Normal', backgroundcolor='black',size=45)
#txtoverflow.set_bbox(dict(facecolor='green', alpha=0.5, edgecolor='white'))
#txttopping.set_bbox(dict(facecolor='green', alpha=0.5, edgecolor='white'))
#btnlights=Button(axbtnlights,'Lights',color='black')

#close button
axbtnclose=plt.axes([0.9,0.02,0.05,0.05])    
btnclose=Button(axbtnclose,'close',color='black')
    
#Overflow tile
axbtnoverflotile=plt.axes([0.025,0.7,0.3,0.2])
btnoverflotile=Button(axbtnoverflotile,'Normal',color='blue',hovercolor='blue')
btnoverflotile.label.set_fontsize(28)
txtoverflow = plt.text(0.5,1.1,'Sump Water Level',backgroundcolor='black',horizontalalignment='center',verticalalignment='bottom',size=24)
txtoverflow.set_bbox(dict(facecolor='black', alpha=1, edgecolor='black'))

#temp tile
axbtntemptile=plt.axes([0.35,0.7,0.3,0.2])
btntemptile=Button(axbtntemptile,'Sensor Off',color='#1C6FF8',hovercolor='#1C6FF8')
btntemptile.label.set_fontsize(28)
btntemptile.label.set_color('black')
#temperaturebtnstate(temp)
txttemp = plt.text(0.5,1.1,'Temperature',backgroundcolor='black',size=24,horizontalalignment='center',verticalalignment='bottom')
txttemp.set_bbox(dict(facecolor='black', alpha=1, edgecolor='black'))

#read 1
axbtnread1tile=plt.axes([0.675,0.1,0.31,0.8])
btnread1tile=Button(axbtnread1tile,'',color='blue',hovercolor='blue')
txtread1tile = plt.text(0.03,0.98,'Operations Normal...',backgroundcolor='black',size=16,horizontalalignment='left',verticalalignment='top')
txtread1tile.set_bbox(dict(facecolor='blue', alpha=1, edgecolor='blue'))

#topping
axbtntoppingtile=plt.axes([0.025,0.4,0.3,0.2])
btntoppingtile=Button(axbtntoppingtile,'Normal',color='blue',hovercolor='blue')
btntoppingtile.label.set_fontsize(28)
txttoppingtile = plt.text(0.5,1.1,'Tank Water Level',backgroundcolor='black',size=24,horizontalalignment='center',verticalalignment='bottom')
txttoppingtile.set_bbox(dict(facecolor='black', alpha=1, edgecolor='black'))


#Flow Tile
axbtnflowtile=plt.axes([0.35,0.4,0.3,0.2])
btnflowtile=Button(axbtnflowtile,'Off',color='blue',hovercolor='blue')
btnflowtile.label.set_fontsize(28)
txtflowtile = plt.text(0.5,1.1,'Flow',backgroundcolor='black',size=24,horizontalalignment='center',verticalalignment='bottom')
txtflowtile.set_bbox(dict(facecolor='black', alpha=1, edgecolor='black'))


#light tile
axbtnlighttile=plt.axes([0.025,0.1,0.3,0.2])
btnlighttile=Button(axbtnlighttile,'Lights Off',color='black',hovercolor='black')
btnlighttile.label.set_fontsize(28)
#txtlighttile = plt.text(0.5,0.04,'Lights',backgroundcolor='black',size=24,horizontalalignment='center',verticalalignment='bottom')
#txtlighttile.set_bbox(dict(facecolor='black', alpha=1, edgecolor='black'))


#other tile
axbtnsometile=plt.axes([0.35,0.1,0.3,0.2])
btnsometile=Button(axbtnsometile,'Somethings',color='blue',hovercolor='blue')
btnsometile.label.set_fontsize(28)
txtsometile = plt.text(0.5,1.1,'Other',backgroundcolor='black',size=24,horizontalalignment='center',verticalalignment='bottom')
txtsometile.set_bbox(dict(facecolor='black', alpha=1, edgecolor='black'))



draw()



btnlighttile.on_clicked(lights)
btnclose.on_clicked(close)
btnoverflotile.on_clicked(dummy)
btntoppingtile.on_clicked(dummy)

thread1=threading.Thread(target=reading,daemon=True)
thread1.start()



while closing:
    plt.pause(0.2)
    print("dibujando")
    #draw()
    #print("checking")
