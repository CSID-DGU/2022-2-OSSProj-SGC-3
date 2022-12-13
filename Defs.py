import enum


class Sounds(enum.Enum):
    # game volume
    volume_small = 0.3

    # sounds
    bgm = 'resource/sound/8BitSuperAudioArcade_AllenGrey.wav'
    star = 'resource/sound/MagicTower.wav'
    gameover = 'resource/sound/Fail.wav'
    coin = 'resource/sound/Coin.wav'
    meteor = 'resource/sound/Rock.mp3'
    bomb = 'resource/sound/FallingBombWhist SDT2021401.wav'
    blind = 'resource/sound/Blind.wav'
    coins = 'resource/sound/CoinsReward.wav'
    mirror = 'resource/sound/IllusionMagic.wav'
    bullet = 'resource/sound/Bullet.wav'


class Images(enum.Enum):
    # main background
    background = 'resource/image/background.jpg'

    # game background
    bg_space = 'resource/image/bg_space.png'
    bg_chess = 'resource/image/bg_chess.png'
    bg_green = 'resource/image/bg_green.png'
    bg_pirate = 'resource/image/bg_pirate.png'
    bg_card = 'resource/image/bg_card.png'
    bg_desert = 'resource/image/bg_desert.png'
    bg_planet = 'resource/image/bg_planet.png'
    bg_world = 'resource/image/bg_world.png'

    # game logo
    logo = 'resource/image/logo-silver.png'

    # HELP page 키 설명
    key_left = 'resource/image/arrowkey_left.png'
    key_right = 'resource/image/arrowkey_right.png'

    # game character
    shoot = 'resource/image/shoot.png'

    # coin
    coin1 = 'resource/image/coin1.png'
    coin2 = 'resource/image/coin2.png'
    coin3 = 'resource/image/coin3.png'
    coin4 = 'resource/image/coin4.png'
    coin5 = 'resource/image/coin5.png'
    coin6 = 'resource/image/coin6.png'

    # star
    star1 = 'resource/image/star1.png'
    star2 = 'resource/image/star2.png'
    star3 = 'resource/image/star3.png'
    star4 = 'resource/image/star4.png'
    star5 = 'resource/image/star5.png'
    star6 = 'resource/image/star6.png'
    star7 = 'resource/image/star7.png'

    # 차원별 enemies
    # chess
    black_knight = 'resource/image/chess_black_knight.png'
    white_king = 'resource/image/chess_white_king.png'

    # green
    bat = 'resource/image/green_bat.png'
    lizard = 'resource/image/green_lizard.png'

    # pirate
    pirate_ship = 'resource/image/pirate_ship.png'
    kraken = 'resource/image/pirate_kraken.png'

    # card
    card_jack = 'resource/image/card_jack.png'
    card_queen = 'resource/image/card_queen.png'

    # desert
    snake = 'resource/image/desert_snake.png'
    desert_scolpion = 'resource/image/desert_scolpion.png'

    # meteor
    meteor = 'resource/image/meteorite.png'

    # weapons
    bullets_256 = 'resource/image/bullets_256px.png'
    missile_256 = 'resource/image/missile_256px.png'
    missile2_256 = 'resource/image/missile2_256px.png'
    bomb_256 = 'resource/image/bomb_256px.png'

    # modes
    # blind mode
    blind = 'resource/image/blind_mode.png'

    # bomb mode
    bomb = 'resource/image/bomb.png'

    # mirror mode
    mirror = 'resource/image/mirror_mode.png'

    # double mode
    double = 'resource/image/double.png'


class Content(enum.Enum):
    # main
    main = '__main__'

    # captions
    gamename = 'Next Dimension'
    gameplay = 'Game Play'
    gameend = 'Game End'

    # game weapon mode
    basic = 'basic'

    # button name
    signin_btn = 'Sign in'
    signup_btn = 'Sign up'
    quit_btn = 'Quit'
    start_btn = 'Game Start'
    rank_btn = 'Rank'
    store_btn = "Store"
    help_btn = 'Help'
    about_btn = 'About'
    sound_btn = "Sound"
    back_btn = 'Back'
    submit_btn = 'Submit'
    reset_btn = "Reset Password"
    buyitem_btn = "Buy Item"
    applyitem_btn = "Apply Item in Game"
    givecoin_btn = "Give Coin as a gift"
    buy_btn = "Buy"
    apply_btn = 'Apply'
    restart_btn = 'Restart'
    main_btn = 'Main'

    # RANK page table title
    rank_rowname = ["RANK", "Email", "SCORE"]

    # HELP page
    help_title = 'Story & Game Rule'
    story = 'In 2300 AD, you can no longer live on Earth\n'\
        'and received a mission to find a new dimension for live.\n'\
        'Now you must find a new dimension\nwhile avoiding enemy attacks.\n'\
        'Good Luck!\n'
    rule = 'Use left and right arrow key to move your character'
    ruletable_row1 = '  Press left key to go left'
    ruletable_row2 = '  Press right key to go right'
    hp = 'Enemies have different HPs'
    hptable_row1 = '  Attack 1 time to kill'
    hptable_row2 = '  Attack 2 time to kill'

    # ABOUT page
    about_title = 'License & Source'
    license = 'License'
    license_detail = 'The GPL(3.0) License'
    source = 'Source'
    basecode1 = 'Kill-Console/PythonShootGame(The GPL License)'
    basecode2 = 'CSID-DGU/2021-2-OSSProj-PlusAlpha-9(The MIT License)'
    imagesource = 'pixabay'
    soundesource = 'envato elements'
    creators = '\nCreated by\n'\
        'Dongguk University OSSProj\n'\
        'Seojeong Yun, Gaeun Lee, Seyeon Park'
    github = 'Click here to go to our github link'

    # SIGNIN or SIGNUP page
    pwref = '* Please set the password to at least 8 digits'
    signupmsg = 'Successfully signed up!'
    signup = 'Success'
    errormsg = 'Check your email or password again'
    error = 'Error'
    resetmsg = 'Please reset your password via email'
    reset = 'Reset'
    email_input = "email : "
    email = 'email'
    pw_input = "password : "
    pw = 'password'
    confirm_pw_input = "conFirm password : "

    # STORE page
    store_title = 'Store'
    category1 = 'Weapons'
    applied_item = "Current Applied Item"
    coin = "Your Current Coin"
    item_category = 'Weapons'
    gift_info = "Enter an email to gift coins"
    giveok_msg = 'Coin gift completed'
    giveno_msg = 'You have less than you want to give.'
    giveok_msgtitle = 'Success'
    giveno_msgtitle = 'Failed'
    have_msg = 'This item has already been purchased'
    have_msgtitle = 'Already Have'
    buy_msg = 'Purchase completed'
    buy_msgtitle = 'Buy Item'
    cannotBuy_msg = "Item cannot be purchased due to insufficient coins"
    cannotBuy_msgtitle = "Unable to purchase"

    # BUY page
    items = ["bullets", "missile", "missile2", "dagger"]
    img_path = 'resource/image/'
    img_have = '_check.png'
    img_price = '_price.png'
    img_size256 = '_256px.png'
    img_size16 = '_16px.png'

    # APPLY page
    reload = "reload"

    # GIFT page
    coin_input = "coin : "

    # GAME END page
    end = 'Game End'
    score = 'Score: '
    rank = 'Rank: '
    coins = 'Total Coins: '

    # none
    none = ''

    # RANK page
    tb_rank = "rank"


class Item(enum.Enum):
    # 아이템 가격 coin
    bullets_price = 10000
    missile_price = 50000
    missile2_price = 100000
    dagger_price = 1000000


class Url(enum.Enum):
    basecode1 = 'https://github.com/Kill-Console/PythonShootGame'
    basecode2 = 'https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9'
    pixabay = 'https://pixabay.com/ko/'
    envato = 'https://elements.envato.com/'
    ourgithub = 'https://github.com/CSID-DGU/2022-2-OSSProj-SGC-3'


class Color(enum.Enum):
    black = 'black'
    white = 'white'


class Display(enum.Enum):
    # screen size
    w_init = 1/3
    h_init = 8/9
    angle = 0

    # 스크린 최소값
    minscreen_x = 400
    minscreen_y = 600

    # game screen 사이즈 조절
    width_divide3 = 3
    width_divide2 = 2

    # enemy hp
    hp_low = 1
    hp_high = 2

    # clock
    clock_init = 0
    clock_t = 45

    # scale
    small_scale = (0.1, 0.1)
    medium_scale = (0.4, 0.4)
    large_scale = (1, 1)

    # padding
    padding_large = (50, 0, 50, 0)  # content title
    padding_small = (3, 1, 3, 1)  # content table
    # rank table padding
    rank_padding = [5, 20]  # 테이블 기본 패딩값
    rank_idx_padding = [10, 40]  # 테이블 index만 굵고 패딩 더 줌

    # table padding
    table_padding = [5, 20]
    table_title_padding = [10, 40]

    # fontsize
    title_fontsize = 35
    description_fontsize = 20
    reference_fontsize = 16

    # margin
    large_margin = 100
    small_margin = 30


class StarMode(enum.Enum):
    mode0 = 0
    mode1 = 1
    mode2 = 2
    mode3 = 3


class Score(enum.Enum):
    # score
    score_init = 0
    score_coin = 10


class Dimension(enum.Enum):
    # game dimension
    dim0 = 0  # space
    dim1 = 1  # chess
    dim2 = 2  # green
    dim3 = 3  # pirate
    dim4 = 4  # card
    dim5 = 5  # desert
    # --- 1round ---
    dim6 = 6  # chess
    dim7 = 7  # green
    dim8 = 8  # pirate
    dim9 = 9  # card
    dim10 = 10  # desert
    dim11 = 11  # ending


class Frequency(enum.Enum):
    # shoot frequency
    fq_init = 0
    random1_fq_min = 1
    random1_fq_max = 40

    random2_fq_min = 15
    random2_fq_max = 60

    fq_medium = 1000
    fq_low = 3000

    random_star_start = 0
    random_star_end = 3


class Speed(enum.Enum):
    bg = 4
    zero = 0
    bullet = 10
    player = 9
    enemy1 = 2.1
    enemy2 = 1.8
    coin = 10
    blind = 5
    bomb = 20
    mode = 3
    meteor = 20


class Utilization(enum.Enum):
    x = 0   # rect(Tuple)'s x
    y = 1   # rect(Tuple)'s y
    edge = 0  # screen's edge


class BackGround(enum.Enum):
    space = 0
    chess = 1
    green = 2
    pirate = 3
    card = 4
    desert = 5
    ending = 6
    s_ending = 7


class Resize(enum.Enum):
    display = 500
    standard = 10
    shoot = 1
    enemy1 = 9
    enemy2 = 10
    # resizable에 따른 변화 - 빈도는 숫자에 반비례, 속도는 숫자에 비례
    #  0  500 1000 1500 2000 이상 - 화면 크기 기준
    #  9   10  11   12   13  플레이어 속도
    # 10   9    8    7    6  총알 발사 빈도
    # 90   81  72   63   54  적1 출현 빈도
    # 100  90  80   70   60  적2 출현 빈도


class Game(enum.Enum):
    d_weight = 3000
    d_height = 10000
    e_height = 2000
    p_margin = 20
    dim = 40
    end = 20
    end_message1 = "This is the end of the universe."
    end_message2 = "There's no dimension here for you to live on."
    end_message3 = "Get everything you can and try again."
    close_message1 = "Congratulations!"
    close_message2 = "You've found your dimension to live in!"


class Plane(enum.Enum):
    # shoot.png에서 해당 이미지의 위치 (x, y, width, height)
    # plane image rect
    p1 = 0, 99, 102, 126
    p2 = 165, 360, 102, 126
    p3 = 165, 234, 102, 126
    p4 = 330, 624, 102, 126
    p5 = 330, 498, 102, 126
    p6 = 432, 624, 102, 126
    # bullet image rect
    bullet = 1004, 987, 9, 21
    # enemy(space) image rect
    e1 = 534, 612, 57, 43
    e2 = 267, 347, 57, 43


class Divide(enum.Enum):
    # mainGame.py 참조
    player = 8     # 나눠지는 숫자 - 이미지가 n에 맞게 +1 씩 바뀌면 너무 빨리 변해서 조절하는 용도
    player_i = 8   # 나누는 숫자 (ex/ 이미지 1~5번 전환 => k=8; num=k//8; 이미지[num]; k+=1;)
    player_d = 47  # palyer hit 이미지 한계 (이미지개수*조절수i - 1)
    # gameRole.py 참조
    coin = 240   # 객체의 화면상 위치 % 값 => ex/ 0~239의 정수 반복
    coin_i = 40  # 위 결과값 // 값 => ex/ 000...111...222...333...444...555 반복
    star = 210
    star_i = 30
    star_r = 70  # 랜덤박스(star) 위치 조절 (화면 높이&너비의 1/70씩 이동)


class Font(enum.Enum):
    size = 36
    e_size = 48
    color = 128, 128, 128
    e_color = 200, 200, 200
    margin = 10


class Rank(enum.Enum):
    rank_col = 0
    email_col = 1
