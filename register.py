import email
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
import pygame_menu
import pygame

# firestore 접근키
cred = credentials.Certificate(
    "./shootinggame-adf10-firebase-adminsdk-mb0cr-86331adc29.json")

# pyrebase authentication을 위한 접근키
firebaseConfig = {
    'apiKey': "AIzaSyCTG8WWk89CaPfUPwjNPObOce13gDC-Uro",
    'authDomain': "shootinggame-adf10.firebaseapp.com",
    'projectId': "shootinggame-adf10",
    'storageBucket': "shootinggame-adf10.appspot.com",
    'messagingSenderId': "205816370300",
    'appId': "1:205816370300:web:d9781abb8849788013e5f9",
    'measurementId': "G-YZ257BPC77",
    'databaseURL': "https://shootinggame-adf10-default-rtdb.firebaseio.com/"
}

firebase_admin.initialize_app(
    cred, {'databaseURL': "https://shootinggame-adf10-default-rtdb.firebaseio.com/"})

firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()
db = firestore.client()

# Login 함수
def Login(email, password):
    global user # 현재 로그인 유지를 위한 변수
    user = email
    login = 0
    try: 
        login = auth.sign_in_with_email_and_password(email, password) # 로그인 시도
        print("Successfully signed in!")
    except: # 로그인에 실패할 경우
        print("Invalid user or password. Try again")
    return login

# register
def register(email, password, confirmPassword):
    if password == confirmPassword:
        try:
            auth.create_user_with_email_and_password(email, password) # 회원가입 시도
            # 초기 데이터 셋팅
            data = { 
                "email": email,
                "item_apply": "basic",
                "item": ["basic"],
                "rank": 0,
                "coin": 0
            }
            db.collection("User").document(email).set(data)
            return 1
        except: # 이메일이 이미 존재하면 회원가입 불가
            print("Email already exists")
            return 0


def passwordReset(email): # 비밀번호 리셋 함수
    auth.send_password_reset_email(email)

