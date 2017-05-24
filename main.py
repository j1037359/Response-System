#*--coding:utf-8--*
#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from os import path
from gtts import gTTS
import os
from konlpy.tag import Kkma
from konlpy.utils import pprint
import pickle
from codecs import open as copen
from sklearn.metrics.pairwise import cosine_similarity

if __name__ =="__main__":
    kkma=Kkma()
    temp=kkma.pos(u'준비')




    while 1:
        num = raw_input("1.가상강의\n2.장학\n3.학사\n4.휴학및복학\n")

        fname = "microphone-results.wav"

        # 마이크로 음성 획득
        r = sr.Recognizer()

        with open('./DataSet/vector_'+num+'.txt', 'rb') as f:
            vector = pickle.load(f)

        with open('./DataSet/feature_'+num+'.txt', 'rb') as f:
            feature = pickle.load(f)

        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        WAV_FILE = path.join(path.dirname(path.realpath(__file__)), fname)

        # WAVE파일
        with open(fname, "wb") as f:
            f.write(audio.get_wav_data())

        with sr.WavFile(WAV_FILE) as source:
            audio = r.record(source) # read the entire WAV file

        # Google SpeechRecognition을 통한 음성인식

        try:
            print("Google Speech Recognition results:")
            input2=r.recognize_google(audio,language='ko-KR',show_all=True)['alternative'][0]['transcript']
            print input2

            read_data = []

            for i in kkma.pos(unicode(input2)):
                read_data.append(i[0])

            input_vec = []

            for i in feature:
                if read_data.count(i) > 0:
                    input_vec.append(read_data.count(i))
                else:
                    input_vec.append(0)

            result = []
            result.append(input_vec)

            #코사인 유사도 분석
            temp=list(cosine_similarity(result, vector)[0])

            print max(cosine_similarity(result, vector)[0])

            #가장 유사한 데이터의 인덱스 추출
            index=temp.index(max(temp))+1

            print index


            print("Start Speech")

            with open('./dic/dic_'+num+'.p', 'rb') as f:
                answer = pickle.load(f)

            result_answer=answer[index]

            print result_answer

            #gTTS를 통한 음성합성
            tts = gTTS(text=result_answer, lang='ko')
            tts.save("result.mp3")
            os.system("result.mp3")

            num2 = raw_input("질의가 끝나셨습니까?(Y/N)")
            if num2 == 'y' or 'Y':
                break
            else:
                continue


        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

