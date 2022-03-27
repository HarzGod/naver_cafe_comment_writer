from selenium import webdriver
import pyperclip
import pyautogui
import time

naver_id = (input('네이버 계정 아이디 입력 : ')) # input으로 입력받은 값을 변수에 저장
naver_pw = (input('네이버 계정 비밀번호 입력 : ')) # input으로 입력받은 값을 변수에 저장
url = (input('게시글 모바일 URL 입력 : ')) # input으로 입력받은 값을 변수에 저장
count = (input('도배 할 갯수 입력 : ')) # input으로 입력받은 값을 변수에 저장
comment = (input('도배 할 메세지 입력 : ')) # input으로 입력받은 값을 변수에 저장

login = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com" #네이버 로그인 페이지의 링크를 login이라는 변수에 저장
browser = webdriver.Chrome() # browser라는 변수에 webdriver.Chrome()을 저장
browser.implicitly_wait(10) # browser라는 변수를 불러오고, 창을 엶
browser.maximize_window() # browser라는 변수를 불러오고, maximize_window라는 셀레니움 코드를 이용해 창을 최대화
browser.get(login) # 'login'이라는 변수에 저장되어있는 URl으로 창을 엶

id = browser.find_element_by_css_selector("#id") # 페이지 css에서 네이버 아이디 입력칸의 id를 확인하는 셀레니움 코드를 'id'라는 변수에 저장
id.click() # id라는 변수를 불러와 네이버 아이디 입력칸을 클릭
pyperclip.copy(f"{naver_id}") # pyperclip.copy를 이용해서 네이버 아이디를 복사
pyautogui.hotkey("ctrl", "v") # pyperclip으로 복사한 네이버 아이디를 pyautogui.hotkey를 통해 붙여넣음 ( 네이버 캡챠 우회 효과 )

pw = browser.find_element_by_css_selector("#pw") # 페이지 css에서 네이버 비밀번호 입력칸의 id를 확인하는 셀레니움 코드를 'pw'라는 변수에 저장
pw.click() # pw라는 변수를 불러와 네이버 비밀번호 입력칸을 클릭
pyperclip.copy(f"{naver_pw}") # pyperclip.copy 를 이용해서 네이버 비밀번호를 복사
pyautogui.hotkey("ctrl", "v") # pyperclip으로 복사한 네이버 아이디를 pyautogui.hotkey를 통해 붙여넣음 ( 네이버 캡챠 우회 효과 )
time.sleep(1) # 1초 쉬기

login_btn = browser.find_element_by_css_selector("#log\.login") #페이지 css에서 로그인 버튼의 id를 확인하는 셀레니움 코드를 'login_btn'이라는 변수에 저장
login_btn.click() #login_btn이라는 변수를 불러와 네이버 로그인 버튼 클릭
time.sleep(1) # 1초 쉬기

browser.get(url) # 'login'이라는 변수에 저장되어있는 URl으로 창을 엶
time.sleep(1) # 1초 쉬기

for i in range(count): #반복문
    comment_write = pyautogui.locateCenterOnScreen('write.png') # 'comment_write'라는 변수에 스크린에서 특정 이미지를 찾아주는 코드 'pyautogui.locateCenterOnScreen('write.png')'를 저장
    pyautogui.click(comment_write) # 'comment_write'이라는 변수를 불러와 pyautogui.click으로 클릭해서 댓글 작성창을 엶
    time.sleep(1) # 1초 쉬기
    pyautogui.write(f'{comment}') # pyautogui.write를 이용해 'comment'라는 변수에 저장된 문장을 댓글 작성창에 입력
    send_btn = pyautogui.locateCenterOnScreen('send.png') # 'send_btn'이라는 변수에 스크린에서 특정 이미지를 찾아주는 코드 'pyautogui.locateCenterOnScreen('send.png')'를 저장
    pyautogui.click(send_btn) # 'send_btn'이라는 변수를 불러와 pyautogui.click으로 클릭해서 댓글을 보냄
    time.sleep(1) # 1초 쉬기
    up = pyautogui.locateCenterOnScreen('up.png') # 'up'라는 변수에 스크린에서 특정 이미지를 찾아주는 코드 'pyautogui.locateCenterOnScreen('up.png')'를 저장
    pyautogui.click(up) # 'up'이라는 변수를 불러와 pyautogui.click으로 클릭해서 창을 맨 위로 올림