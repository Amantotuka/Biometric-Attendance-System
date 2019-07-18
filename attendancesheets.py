import pandas as pd
def attendance_file(st):
    dic_att={'name':[]}
    for i in range(1,10):
        dic_att["day0"+str(i)]=[]
    for v in range(10,31):
        dic_att["day"+str(v)]=[]
    data=pd.read_csv('database.csv')
    dn=(data['name'].values)
    for i in dn:
        dic_att['name'].append(i)
        for j in range(1,10):
            dic_att["day0"+str(j)].append(0)
        for k in range(10,31):
            dic_att["day"+str(k)].append(0)
    df=pd.DataFrame(dic_att)
    df.to_csv(st+'.csv',index=False)

for i in range(1,13):
    attendance_file('attendence sheet'+str(i))

