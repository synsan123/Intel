











openai.api_key = "사용자의 OpenAI API 키 값" 

#folder_path와 file_name을 결합하여 file_path = './data/embedding.csv'
folder_path = './data'
file_name = 'embedding.csv'
file_path = os.path.join(folder_path, file_name)

# if : embedding.csv 파일이 존재하면, 파일을 읽어서 데이터프레임 df를 로드한다.
if  




# 그렇지 않다면 text열과 embedding열이 존재하는df를 신규 생성해야 한다.    
else:
    # 57개의 서울 청년 정책 txt 파일명을 txt_files에 저장한다.





    # txt_files로부터 57개의 청년 정책 데이터를 로드하여 df를 신규 생성한다.








    # 데이터프레임의 text 열에 대해서 embedding을 추출





    # 추후 사용을 위해 df를 embedding.csv 파일로 저장
    # 이렇게 저장해두면 추후 실행했을 때 df를 만드는 과정을 생략할 수 있다. 


# 주어진 질의로부터 유사한 문서를 반환하는 검색 시스템
# 함수 return_answer_candidate 내부에서 유사도 계산을 위해 cos_sim을 호출한다.












# 챗봇의 답변을 만들기 위해 사용될 프롬프트를 만드는 함수



















# 위의 create_prompt 함수가 생성한 프롬프트로부터 챗봇의 답변을 만드는 함수 








# 챗봇의 마스코드 이미지 삽입
st.image('images/ask_me_chatbot.png')

# 화면에 보여주기 위해 챗봇의 답변을 저장할 공간 할당 



# 화면에 보여주기 위해 사용자의 답병르 저장할 공간 할당 



# 사용자의 입력이 들어오면 user_input에 저장하고 Send 버튼을 클릭하면 submitted의 값이 True로 변환




# submitted의 값이 True면 챗봇이 답변을 하기 시작

    # 프롬프트 생성

    # 생성 한 프롬프트를 기반으로 챗봇의 답변을 생성

    # 화면에 보여주기 위해 사용자의 질문과 챗봇의 답변을 각각 저장 



# 사용자의 질문과 챗봇의 답변을 순차적으로 화면에 출력



