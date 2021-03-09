import pygame


pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정 

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height));


#화면 타이틀 설정 
pygame.display.set_caption("chaeyoung") #게임이름 


#배경 이미지 불러오기 
background = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/backgournd.png')

#캐릭터(스프라이트) 불러오기 
#character = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/character.png')
#character = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/채영/backgorund_chaeyoung.jpg')
character = pygame.image.load('C:/Users/kcj30/OneDrive/바탕 화면/python/.vscode/PyGame/chaeyoung_1.png')

character_size = character.get_rect().size # 이미지의 크기를 구해옴 
character_width = character_size[0];
character_height = character_size[1];
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 
# 이벤트 루프 
running = True # 게임이 진행중인가? 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??? 
            running = False  

    #screen.fill(0, 0, 255))
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos) ); #캐릭터 그리기 .
    pygame.display.update() # 게임 화면을 다시 그리기 

# pygame. 종료 
pygame.quit()