import pickle
import os
from konlpy.tag import Kkma
from codecs import open as copen
from sklearn.metrics.pairwise import cosine_similarity

kkma=Kkma()
#문장벡터
with open('vector.txt','rb') as f:
    vector=pickle.load(f)

#속성리스트
with open('feature.txt','rb') as f:
    feature=pickle.load(f)

#입력데이터
with copen('input.txt','r','utf-8') as f:
    input2=f.read().replace('\n',' ')

read_data=[]

#입력데이터 형태소분석
for i in kkma.pos(unicode(input2)):
    read_data.append(i[0])

input_vec=[]

#속성리스트를 통한 입력 벡터 생성
for i in feature:
    if read_data.count(i) > 0:
        input_vec.append(read_data.count(i))
    else:
        input_vec.append(0)

result=[]
result.append(input_vec)

print max(cosine_similarity(result, vector)[0])