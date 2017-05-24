#*--coding:utf-8--*
import pickle
import os
from konlpy.tag import Kkma
from codecs import open as copen

kkma=Kkma()

vector=[]

with open('DataSet/feature_1.txt','rb') as f:
    feature=pickle.load(f)

#질의 데이터 형태소분석
for i in os.listdir('./DataSet/1/Q/'):
    print i
    f=copen('./DataSet/1/Q/'+str(i),'r','utf-8')
    sentence=f.read().replace('\n',' ')
    temp=[]
    for j in kkma.pos(unicode(sentence)):
        temp.append(j[0])
    vecTemp=[]

    #feacture 차원의 문장 벡터 생성
    for j in feature:
        if temp.count(j) > 0:
            vecTemp.append(temp.count(j))
        else:
            vecTemp.append(0)
    vector.append(vecTemp)
    f.close()

print vector

#질의에 대한 문장 벡터
with open('DataSet/vector_4.txt','wb') as f:
    pickle.dump(vector,f)