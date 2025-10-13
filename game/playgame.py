#雙人對戰
# 檔案: playgame.py
import pygame
from src.sprite import screen, center

def game(mode):
    run = True
    clock = pygame.time.Clock() # 控制幀率
    
    if mode == 'TwoPlayer':
        # 初始繪製一次棋盤
        center.init() 
        
        while run:
            mp = pygame.mouse.get_pos()
            
            # 1. 事件處理：將 event 傳給 center 或在這裡處理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                # 呼叫修改後的 check 方法
                center.check(event, mp)
            
            # 2. 繪製順序
            # 注意：screen.fill 或重畫背景的 code 應放在這裡，否則會有殘影
            # 假設你有一個畫背景的 function，或是重新呼叫 center.init()
            screen.fill((255, 255, 255)) # 清除畫面
            center.init()                # 畫出靜止的棋盤與棋子
            center.run(mp)               # 畫出正在拖拽的棋子
            
            pygame.display.flip()
            clock.tick(60) 

    pygame.quit()

# def game(mode):
#     run=True
#     if mode=='TwoPlayer':
#         while run:
#             mp=pygame.mouse.get_pos()
#             center.check(mp)
#             center.run(mp)  # 拖曳棋子的畫面繪製
#             pygame.display.flip()
#             for event in pygame.event.get():
#                 if event.type==pygame.MOUSEBUTTONDOWN:
#                     center.check(mp)
#                 if event.type==pygame.QUIT:
#                     pygame.quit()
#                 elif event.type == pygame.MOUSEBUTTONUP:
#                     center.move_piece(mp)  # 新增：處理棋子移動
#                     center.dragging = False
#                     center.drag_piece = None
#     pygame.quit()# 檔案路徑: game/playgame.py
    