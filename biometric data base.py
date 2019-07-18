import pandas as pd
import face_recognition as fs
import cv2

img=['aman.jpg','archit.jpg','darshan.png','smita.jpg']   
email_id=['amantotuka1998@gmail.com','archit12@gmail.com','darshan22@gmail.com','smitatotuka13@gmail.com']
data={'name':[],'encodings':[],'email.id':[]}

for i in range(4):
    data['email.id'].append(email_id[i])

for im in img:
    i=fs.load_image_file(im)
    fl=fs.face_locations(i)
    el=fs.face_encodings(i,fl)[0]
    data['encodings'].append(el)
    data['name'].append(im[:len(im) - 4]) 
       
df=pd.DataFrame(data)

df.to_csv('database.csv',index=False)

#print(el)
    
