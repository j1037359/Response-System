#*--coding:utf-8--*
from codecs import open as copen
import os
import pickle

for i in range(1,5):
    #분리된 데이터를 dictionaly 형식으로 저장
    temp={}
    print i
    count=1
    for j in os.listdir('./DataSet/'+str(i)+'/Q'):
        f=copen("./DataSet/"+str(i)+"/Q/"+j,'r','utf-8')
        a=j.replace("Q","A")
        p=copen("./DataSet/"+str(i)+"/A/"+a,'r','utf-8')
        qu=f.read()
        an=p.read()
        temp[count]=an
        f.close()
        p.close()
        count+=1

    with open('./DataSet/dic_'+str(i)+'.p', 'wb') as w:
       pickle.dump(temp, w)


