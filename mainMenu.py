import pygame
from datetime import datetime
import pygame_menu
from os import system
import button
import register
import pyautogui as pg
from register import db, firestore
import dataLoad
from Defs import *

pygame.mixer.init()


# game variables
gamesound = pygame.mixer.Sound(Sounds.bird.value)  # example sound

pygame.init()
infoObject = pygame.display.Info()
size = [int(infoObject.current_w*Display.w_init.value),
        int(infoObject.current_h*Display.h_init.value)]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption(Content.main.value)

# 창이 resize되었는지 여부 체크
def on_resize() -> None:
    window_size = screen.get_size()
    new_w, new_h = window_size[Utilization.x.value], window_size[Utilization.y.value]
    menu.resize(new_w, new_h)
    print(f'New menu size: {menu.get_size()}') # check


# 로그인 전 보여지는 메뉴 화면(로그인, 회원가입)


def show_signinup():
    menu.clear()
    menu.add.image(Images.logo.value,
                   angle=Display.angle.value, scale=Display.large_scale.value)
    menu.add.button('Sign in', login)
    menu.add.button('Sign up', sign_up)
    menu.add.button('Quit', pygame_menu.events.EXIT)

# 로그인 후 보여지는 메뉴 화면


def start_the_game():
    import mainGame


def show_mode():
    menu.clear()
    menu.add.image(Images.logo.value,
                   angle=Display.angle.value, scale=Display.large_scale.value)
    menu.add.button('Game Start', start_the_game)
    menu.add.button('Rank', rank)
    menu.add.button("Store", store)
    menu.add.button('Help', help)
    menu.add.button('About', about)
    menu.add.toggle_switch("Sound", False, sound)
    menu.add.button('Quit', pygame_menu.events.EXIT)


def rank():
    menu.clear()
    print("rank DB")  # 추후 Rank DB 생성되면 연결하기!
    menu.add.button('Back', show_mode)

# help 페이지


def help():
    menu.clear()
    menu.add.label(Content.help_title.value, font_size=Display.title_fontsize.value, padding=Display.padding_large.value)
    # story
    menu.add.label(Content.story.value, font_size=Display.description_fontsize.value)

    # game rule
    # key control
    menu.add.label(Content.rule.value, font_size=Display.description_fontsize.value)
    # key images
    left_img = menu.add.image(Images.key_left.value,
                              angle=Display.angle.value, scale=Display.small_scale.value)
    right_img = menu.add.image(Images.key_right.value,
                               angle=Display.angle.value, scale=Display.small_scale.value)
    # key table
    table = menu.add.table(font_size=Display.description_fontsize.value, padding=Display.padding_small.value)
    table.add_row([left_img, Content.ruletable_row1.value])
    table.add_row([right_img, Content.ruletable_row2.value])
    menu.add.vertical_margin(Display.small_margin.value)

    # enemy HP detail
    menu.add.label(Content.hp.value, font_size=Display.description_fontsize.value)
    # enemy1 images
    enemy1_img1 = menu.add.image(Images.black_knight.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy1_img2 = menu.add.image(Images.bat.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy1_img3 = menu.add.image(Images.pirate_ship.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy1_img4 = menu.add.image(Images.card_jack.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy1_img5 = menu.add.image(Images.snake.value, angle=Display.angle.value, scale=Display.large_scale.value)
    # enemy2 images
    enemy2_img1 = menu.add.image(Images.white_king.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy2_img2 = menu.add.image(Images.lizard.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy2_img3 = menu.add.image(Images.kraken.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy2_img4 = menu.add.image(Images.card_queen.value, angle=Display.angle.value, scale=Display.large_scale.value)
    enemy2_img5 = menu.add.image(Images.desert_scolpion.value, angle=Display.angle.value, scale=Display.large_scale.value)
    # enemy table
    table2 = menu.add.table(font_color=Color.black.value, font_size=Display.description_fontsize.value,
                            padding=Display.padding_small.value, background_color=Color.white.value)
    table2.add_row([enemy1_img1, enemy1_img2, enemy1_img3, enemy1_img4, enemy1_img5, Content.hptable_row1.value])
    table2.add_row([enemy2_img1, enemy2_img2, enemy2_img3, enemy2_img4, enemy2_img5, Content.hptable_row2.value])
    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.button('Back', show_mode)

# about 페이지


def about():
    menu.clear()
    menu.add.label(Content.about_title.value, font_size=Display.title_fontsize,
                   padding=Display.padding_large)  # about page title
    menu.add.label('Source', font_size=Display.description_fontsize)
    menu.add.url(Url.basecode1, Content.basecode1.value, underline=False, font_color=Color.white, font_size=Display.reference_fontsize)
    menu.add.url(Url.basecode2, Content.basecode2.value, underline=False, font_color=Color.white, font_size=Display.reference_fontsize)
    menu.add.url(Url.pixabay, Content.imagesource.value,font_color=Color.white, underline=False, font_size=Display.reference_fontsize)
    menu.add.url(Url.soundeffectplus, Content.soundesource.value, underline=False, font_color='white', font_size=Display.reference_fontsize)

    menu.add.label(Content.creators.value, font_size=Display.description_fontsize)

    menu.add.url(Url.ourgithub, Content.github.value, font_color=Color.white, font_size=Display.reference_fontsize)
    menu.add.vertical_margin(Display.small_margin)
    menu.add.button('Back', show_mode)

# True가 반환될경우 소리가 켜지고 아니면 꺼짐


def sound(sound):
    if sound == True:
        gamesound.play()
    else:
        gamesound.stop()

# 회원가입 기능

def sign_up():
    menu.clear()
    email = menu.add.text_input("email : ", id='email')
    password = menu.add.text_input("password : ", password=True, id='password')
    menu.add.label(Content.pwref.value, font_size=Display.reference_fontsize.value)
    conFirmPassword = menu.add.text_input("conFirm password : ", password=True, id='password')
    menu.add.button('Submit', sign_up_button, email, password, conFirmPassword)
    menu.add.button('Back', show_signinup)
# 회원가입 제출 버튼
def sign_up_button(email, password, conFirmPassword):
    registerReturn = register.register(
        email.get_value(), password.get_value(), conFirmPassword.get_value())
    if registerReturn == 1:
        print(pg.alert(text=Content.signupmsg.value, title=Content.signup.value))
        show_mode()  # 메인 메뉴 페이지로 넘어가기
    else:
        print(pg.alert(text=Content.errormsg.value, title=Content.error.value))

# 비밀번호 재설정 버튼

def resetPassword():
    menu.clear()
    email = menu.add.text_input("email : ", id='email')
    menu.add.button('Submit', resetPassword_Button, email)
    menu.add.button('Sign In', login)
    menu.add.button('Back', show_signinup)


def resetPassword_Button(email):
    register.passwordReset(email.get_value())
    print(pg.alert(text=Content.resetmsg.value, title=Content.reset.value))

# 로그인

def login():
    menu.clear()
    # 개발시 편의를 위해 default값 추가함 (추후 삭제 예정)
    email = menu.add.text_input("Email : ", id='email', default=Content.default_email.value) # check
    password = menu.add.text_input("Password : ", password=True, id='password')
    menu.add.button('Submit', loginButton, email, password)  # submit 버튼을 누르면 로그인 시도
    menu.add.button("Reset Password", resetPassword)
    menu.add.button('Back', show_signinup)


def loginButton(email, password):
    global user
    user = email.get_value()
    login = register.Login(email.get_value(), password.get_value())
    if login != 0:  # 로그인에 성공하면 다음으로 넘어감
        #print(pg.alert(text='로그인에 성공하셨습니다.', title='Successfully signed in!'))
        show_mode()  # 메인 메뉴 페이지로 넘어가기
    else:
        print(pg.alert(text=Content.errormsg.value, title=Content.error))

# 상점
def store():
    menu.clear()
    menu.add.label(Content.store_title.value, font_size=Display.title_fontsize.value, padding=Display.padding_large.value)  # page title
    menu.add.button("Buy Item",Buy_page)
    menu.add.button("Apply Item in Game",apply_item_page)
    menu.add.button("Give Coin as a gift",give_coin_page)
    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.button("Back", show_mode)

def Buy_page():
    menu.clear()
    menu.add.label(Content.coin.value) # 현재 코인 표시
    menu.add.label(dataLoad.coin_get(user))
    menu.add.label('Weapons')
    item_list=["bullets","missile","missile2","bomb"]
    buy_list = dataLoad.item_buyList_get(user)
    for item in item_list:
        if item in buy_list:
            image_path='resource/image/'+item+'_check.png'
            menu.add.image(image_path,
                        angle=Display.angle.value, scale=Display.medium_scale.value)
            menu.add.button("Buy", Buy_check)
        else:
            weapon_image_path='resource/image/'+item+'_256px.png'
            price_image_path='resource/image/'+item+'_price.png'
            menu.add.image(weapon_image_path,
                    angle=Display.angle.value, scale=Display.medium_scale.value)
            menu.add.image(price_image_path,
                    angle=Display.angle.value, scale=Display.medium_scale.value)
            menu.add.button("Buy", Buy, user,item)

    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.button("Back", store)


def apply_item_page():
    menu.clear()
    buy_list = dataLoad.item_buyList_get(user)
    for item in buy_list:  # 사용자가 구매한 아이템 리스트 보여줌
        image_path = 'resource/image/'+item+"_256px.png"
        menu.add.image(image_path, angle=Display.angle.value, scale=Display.medium_scale.value)  # 구매한 아이템 이미지
        menu.add.button("Apply", apply_current_item,user,item)  # 아이템 적용 버튼

    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.label(Content.applied_item.value)
    item = dataLoad.item_apply_get(user)  # 현재 게임에 적용된 아이템 보여줌
    image_path = 'resource/image/'+item+"_256px.png" #### Defs.py에 추가

    menu.add.image(image_path, angle=Display.angle.value, scale=Display.medium_scale.value)

    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.button("Back", store)

def give_coin_page(): # 코인 선물 페이지
    menu.clear()
    menu.add.label("Enter the email of the friend you want to give")
    friend_email = menu.add.text_input("email : ")
    coin = menu.add.text_input("coin : ")
    menu.add.button("Submit",giveButton,friend_email,coin)

    menu.add.vertical_margin(Display.small_margin.value)
    menu.add.button("Back", store)

def giveButton(friend_email,coin): 
    dataLoad.coin_give(friend_email.get_value(),coin.get_value())
    print(pg.alert(text='선물이 완료되었습니다', title='Give Coin'))

def Buy(user,item): #아이템 구매 함수
    dataLoad.item_buy(user,item)

def Buy_check():
    print(pg.alert(text='이미 구매한 아이템입니다.', title='Already Buy'))

def apply_current_item(user,item):
    dataLoad.item_apply(user,item)

def give_coin(user,coin):
    dataLoad.coin_give(user,coin)

# 여기서부터가 메인화면
menu_image = pygame_menu.baseimage.BaseImage(
    image_path=Images.background.value, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
mytheme = pygame_menu.themes.THEME_GREEN.copy()

mytheme.background_color = menu_image
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

# 첫 화면 페이지(로그인, 회원가입 버튼)
menu = pygame_menu.Menu(Content.none.value, size[Utilization.x.value], size[Utilization.y.value], theme=mytheme)


if __name__ == '__main__':
    # 첫 화면 페이지(로그인, 회원가입 버튼)
    show_signinup()
    menu.enable()
    on_resize() # Set initial size
    print("mainMenu",__name__) # check
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                # Update the surface
                screen = pygame.display.set_mode((event.w, event.h),
                                                 pygame.RESIZABLE)
                # Call the menu event
                on_resize()
            pygame.display.update()

        menu.update(events)
        menu.draw(screen)

        pygame.display.flip()

else:
    size = [int(infoObject.current_w),
        int(infoObject.current_h)]
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    show_mode()
    menu.enable()
    on_resize() # Set initial size
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                # Update the surface
                screen = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                # Call the menu event
                on_resize()

        menu.update(events)
        menu.draw(screen)

        pygame.display.flip()

    
# menu.mainloop(screen)
# pygame.quit()