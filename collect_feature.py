#*--coding:utf-8--*
import os
import pickle
from konlpy.tag import Kkma
from codecs import open as copen

kkma=Kkma()

feature_list=set()

#Q&A 데이터에서 feature 추출
for i in os.listdir('./DataSet/Leave/'):
    print i
    f=copen('./DataSet/Leave/'+str(i),'r','utf-8')
    temp=f.read().replace('\n',' ')
    for j in kkma.pos(unicode(temp)):
        if j[1] in ['NNG','NNP','NNB','NP','VA']:
            feature_list.add(j[0])

    f.close()
print len(feature_list)


p=open('DataSet/feature_4.txt','wb')
pickle.dump(list(feature_list),p)
p.close()


