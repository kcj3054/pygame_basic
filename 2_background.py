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
# 이벤트 루프 
running = True # 게임이 진행중인가? 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??? 
            running = False  

    #screen.fill(0, 0, 255))
    screen.blit(background, (0, 0))

    pygame.display.update() # 게임 화면을 다시 그리기 

# pygame. 종료 
pygame.quit()