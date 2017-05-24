# 대구대 민원 자동 응답 시스템
## 요약 :
음성인식과 음성합성을 통한 자동 응답 시스템을 구현.

입력받은 사용자의 음성 질의를 텍스트로 변환하고, 형태소 분석을 통해 형태소 단위로 나눈다. 이를 사전에 수집한 질의 데이터로 생성한
속성리스트를 통하여 문장 벡터를 생성한다. 사용자 질의 문장벡터와 사전에 수집한 문장벡터를 유사도 분석을 통해 비교하여 가장 유사한 질의를 찾고 이에 해당하는 답변을 음성합성을 통해 사용자에게 출력하여준다.

## 언어 및 라이브러리 :
* Python 2.7 또는 2.6
* SpeechRecognition 라이브러리 (pip install SpeechRecognition)
* KoNLPy 라이브러리
* gTTS 라이브러리
* scikit-learn 라이브러리
## 시스템 구조 :
### 데이터
>대구대학교 Q&A 게시판의 내용을 수집(약 80개의 데이터셋으로 실험).

>데이터를 학사, 휴학 및 복학, 장학, 가상강의 카테고리별로 분류하여 속성리스트 생성 및 단어벡터 생성(pickle파일로 저장)

### 음성인식
>SpeechRecognition의 Google Cloud Speech API를 이용


    import speech_recognition as sr

    #음성파일획득
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    #구글 음성인식
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



### 유사도 계산
>scikit-learn에서 제공하는 코사인 유사도를 분석을 통해 사용자의 질의와 가장 유사한 질의를 선택


    from sklearn.metrics.pairwise import cosine_similarity
    cosine_similarity(result, vector)

### 음성합성
>gTTS를 이용하여 사용자의 질의에 해당하는 답변을 mp3파일로 생성하여 사용자에게 출력
    
    
    #gTTS를 통한 음성합성
    tts = gTTS(text=result_answer, lang='ko')
    tts.save("result.mp3")
    os.system("result.mp3")
## 참고문서
[Speech Recognition] (https://github.com/Uberi/speech_recognition)

[KoNLPy] (http://konlpy-ko.readthedocs.io/ko/v0.4.3/)

[gTTS] (http://pythonprogramminglanguage.com/text-to-speech/) 
