import pygame


pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정 

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height));


#화면 타이틀 설정 
pygame.display.set_caption("chaeyoung") #게임이름 



# FPS 
clock = pygame.time.Clock()

#배경 이미지 불러오기 
background = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/backgournd.png')

#캐릭터(스프라이트) 불러오기 
#character = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/character.png')
character = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/chaeyoung_1.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴 
character_width = character_size[0];
character_height = character_size[1];
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 

#이동할 좌표 
to_x = 0
to_y = 0

#이동속도 
character_speed = 0.5

#적 enemy 캐릭터 
enemy = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/enemy.png');
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴 
enemy_width = enemy_size[0];
enemy_height = enemy_size[1];
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 
enemy_y_pos = (screen_height / 2)- (enemy_height / 2)  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 

# 이벤트 루프 
running = True # 게임이 진행중인가? 

while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정 .

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??? 
            running = False  

    if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인 
        if event.key == pygame.K_LEFT:
            to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
            to_x += character_speed
        elif event.key == pygame.K_UP:
            to_y -= character_speed
        elif event.key == pygame.K_DOWN:
            to_y += character_speed

    character_x_pos += to_x * dt;
    character_y_pos += to_y * dt;

    if character_x_pos < 0:
        character_x_pos = 0;
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width;

    if character_y_pos < 0:
        character_y_pos = 0;
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height;
    
    #충돌처리 
    character_rect = character.get_rect();
    character_rect.left = character_x_pos;
    character_rect.top = character_y_pos;

    enemy_rect = enemy.get_rect();
    enemy_rect.left = enemy_x_pos;
    enemy_rect.top = enemy_y_pos;

    #충돌체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        

    #screen.fill(0, 0, 255))
    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos) ); #캐릭터 그리기 .

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)); #적 캐릭터그리기 

    pygame.display.update() # 게임 화면을 다시 그리기 

# pygame. 종료 
pygame.quit()