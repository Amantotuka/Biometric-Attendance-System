import pandas as pd
from ast import literal_eval
import face_recognition as fc
import cv2
import numpy as np
from datetime import date,datetime,timedelta
import pyttsx3, time
import smtplib
df=pd.read_csv('database.csv')
n=df.loc[:,'name'].values
email=df.loc[:,'email.id'].values
def speak(audio):
    k=pyttsx3.init()
    k.say(audio)
    k.runAndWait()

encList=[]

for i in range(0,len(df['name'])):
    enc=df['encodings'][i]
    encValues=enc[1:len(enc)-1]
    valueSplit=encValues.split('\n')
    
    temp=[]
    for i in valueSplit:
        spaceSplit=i.split(' ')
        for j in spaceSplit:
            if(j!=''):
                temp.append(float(j))
     #print(temp)

    encArray=np.array(temp).reshape(128,)
    #print(encArray)
    encList.append(encArray)
def email_send(m):
    my_password=open('password.txt','r')

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('amantotuka1998@gmail.com',my_password.read())
    emailid=['amantotuka1998@gmail.com','archit23@gmail.com','darshan12@gmail.com','smitatotuka13@gmail.com']

    
    d=pd.read_csv('attendence sheet'+ str(m) +'.csv')
    name=d.loc[:,'name'].values
    days=d.iloc[0:4,1:31].values
            
    total_attendance=[]
    count=0
    for j in range(len(name)):
        if 'p' in days[j,:]:
            k=count+1
            total_attendance.append(k)
        else :
            total_attendance.append(0)

            
    for k in range(4):
        print(total_attendance[k])
        message='your ward total attendance is {}'.format(total_attendance[k])
        s.sendmail('amantotuka1998@gmail.com',emailid[k],message)    
    
def attendence_name(name,A):
    total_attendance=0
    today=date.today()
    #print('aa')
    dl=today.strftime('%d/%m/%y')
    d=dl[:2]
    m=dl[3:5]
    if m[0]=='0':
       m=m[1:]
    for i in range(1,13):
        if str(i)==m:
           #print('bb')
           data=pd.read_csv('attendence sheet'+ m +'.csv')
           a=list(data[data['name']==name].index)
           if A==1:
              data.iloc[a[0],data.columns.get_loc('day'+d)]='p'
           elif A==0:
                data.iloc[a[0],data.columns.get_loc('day'+d)]='a'
    
                      
           data.to_csv('attendence sheet'+ m +'.csv',index=False)
    if (d==30):
       email_send(m) 
def camera_on():
    v=cv2.VideoCapture(0)
    end_time=datetime.now()+timedelta(seconds=8)
    while datetime.now()<end_time:
        
        #print(encList)
        r,live=v.read()
        fl=fc.face_locations(live)
        if(len(fl)>0):
            [x1,y1,x2,y2]=fl[0]
            cv2.rectangle(live,(y2,x1),(y1,x2),(0,0,255),5)
            E=fc.face_encodings(live,fl)[0]
            #print(fl,E)
            res=fc.compare_faces(encList,E)
            #print(res)
            r=True in res
            if(r==True):
               res.index(True) 
               name=n[res.index(True)] 
               attendence_name(name,1)  
        cv2.imshow('image',live)
        k=cv2.waitKey(5)
        if(k==ord('q')):
           cv2.destroyAllWindows()

def start():
    print('************welcome to attendance system*************')
    speak('welcome to attendane system')
    print("Please read the following instruction-: \n 1.press C to open camera.")
    k=ord(input('enter  '))
    if k==ord('C'):
       camera_on()
       time.sleep(9)
       print('your attendance is done')
       
            
start()      

