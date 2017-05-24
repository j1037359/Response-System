#*--coding:utf-8--*
import os
import pickle
from konlpy.tag import Kkma
from codecs import open as copen


#질의와 답변 데이터 분리
for i in os.listdir('./DataSet/Leave/'):
    print i
    f=copen('./DataSet/Leave/'+str(i),'r','utf-8')
    temp=f.read().split('\n')
    a=copen("./DataSet/4/A/"+str(i).replace('Q','A'),'w','utf-8')
    q=copen("./DataSet/4/Q/"+str(i),'w','utf-8')
    print temp[0]
    q.write(temp[0])
    a.write(temp[2])
    f.close()
    q.close()
    a.close()