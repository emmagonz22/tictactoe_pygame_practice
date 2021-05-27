import pygame as py
import sys 
from Animation import Animation 
py.init()

mainClock = py.time.Clock()
#Icon and caption
py.display.set_caption("Tic_tac_toe")

win = py.display.set_mode((864, 512))
font = py.font.Font("font/MAGICLINE.ttf",30)
x_and_o = py.font.Font("font/MAGICLINE.ttf",120)
menu_font = py.font.Font("font/MAGICLINE.ttf",80)

isX = True
global already_block
already_block = []
global pos_in_map
pos_in_map = [[7,7,7],
            [7,7,7],
            [7,7,7]]
global selected_block
selected_block = []
map_location = {0:[[134,90],[283,197],(174,80)], 1: [[287,90],[463,197],(327,80)], 2: [[468,90],[622,197],(508,80)], 
                3:[[134,202],[283,341],(174,202)], 4: [[287,202],[463,341],(327,202)],5:[[468,202],[622,341],(508,202)],
                6:[[134,346],[283,467],(174,346)],7: [[287,346],[463,467],(327,346)],8:[[468,346],[622,467],(508,346)]
                }
win_condition = {3 : "O win", 6: "X win"}
def game_Finished():
    vertical_sum = 0
    diagonal_sum = 0
    for pos in range(3):
        try:
            if(win_condition[sum(pos_in_map[pos])]):
                return True, win_condition[sum(pos_in_map[pos])]
        except:
            pass
        try:
            vertical_sum =  pos_in_map[0][pos] + pos_in_map[1][pos] + pos_in_map[2][pos]
            if(win_condition[vertical_sum]):
                return True, win_condition[vertical_sum]
        except:
            pass 
        try:
            
            diagonal_sum =  pos_in_map[0][2] + pos_in_map[1][1] + pos_in_map[2][0]
            if(win_condition[diagonal_sum]):
                return True, win_condition[diagonal_sum]
            diagonal_sum = 0
        except:
            pass
        try:
            diagonal_sum =  pos_in_map[2][2] + pos_in_map[1][1] + pos_in_map[0][0]
            if(win_condition[diagonal_sum]):
                return True, win_condition[diagonal_sum]
            
        except:
            pass          
    return False, "No Winner"
            
def draw_figure_in_pos(pos_x, pos_y, figure):
    if(figure == "X"):
        value = 2
    else:
        value = 1
    for i in range(9):
        if(map_location[i][0][0] < pos_x and map_location[i][1][0] > pos_x
            and map_location[i][0][1] < pos_y and map_location[i][1][1] > pos_y):
            
            if(i in already_block):
                continue
            if(i <= 2):
                pos_in_map[0][i] = value
            elif(i <= 5):
                pos_in_map[1][i - 3] = value
            else:
                pos_in_map[2][i - 6] = value
            already_block.append(i)
            selected_block.append((i, map_location[i], figure))
            print(pos_in_map)
            #print(selected_block)
            setIsX(not isX)
            break
def setIsX(turnChange):
    global isX
    isX = turnChange
def change_turn():
    if(isX):
        return "X"
    else:
        return "O"
def main_menu():
    click = False
    menu_image = py.image.load("images/menu_map.png")
    while True:

        start_button = py.Rect(100,200,160,40)
        option_button = py.Rect(340,200,170,40)
        py.draw.rect(win, (255,255,255),start_button)
        py.draw.rect(win, (255,255,255),option_button)
        win.blit(menu_image, (0,0))

        mouse_x, mouse_y = py.mouse.get_pos()
        if start_button.collidepoint((mouse_x, mouse_y)):
            if(click):
                game()
                click = not click
        if option_button.collidepoint((mouse_x, mouse_y)):
            if click:
                options()
                click = not click
        click = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
                
            if event.type == py.KEYDOWN:
                if event.key == py.K_p:
                    pause()
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        #tick()
        start_text = py.font.Font.render(font, "Start Button", 1, (0,0,0))
        option_text = py.font.Font.render(font, "Option Button", 1, (0,0,0))
        win.blit(start_text, (100,200))
        win.blit(option_text, (340,200))
        py.display.update()
        mainClock.tick(60)

def game():
    #Animatiom
    tic_tac_toe_anim = Animation(350,25,"tictactoe", "images/tictactoe", [7,7,7,7,7,7])
    tic_tac_toe_anim.add_animation_database('tictactoe')
    turn = Animation(650,25,"turn", "images/turn", [7,7,7])
    turn.add_animation_database('turn')
    ###
    py.mixer.init()
    py.mixer.music.load('music/WeAreOne.mp3')
    py.mixer.music.play(-1)
    mouse_click = False
    game_map = py.image.load("images/map.png")
    while True:
        if(mouse_click):
            draw_figure_in_pos(py.mouse.get_pos()[0], py.mouse.get_pos()[1], change_turn())
            mouse_click = False
        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_p:
                    pause()
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True
        #win.fill((0,0,0))
        win.blit(game_map, (0,0))
        tic_tac_toe_anim.animation_update()
        tic_tac_toe_anim.render(win)
        turn.animation_update()
        turn.render(win)
        win.blit(py.font.Font.render(x_and_o, change_turn(), 1, (255,255,255)),(700,75))
        if(len(selected_block) > 0):
            for i in range(len(selected_block)):
                draw_x_o = py.font.Font.render(x_and_o, selected_block[i][2], 1, (255,255,255))
                win.blit(draw_x_o, selected_block[i][1][2])
        end, player = game_Finished()
        if end:
            end = False
            return win_face(player)
        if len(already_block) == 9:
            return win_face(player)
        py.display.update()

def options():
    menu_image = py.image.load("images/menu_map.png")
    while True:
        for event in py.event.get():
    
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        #win.fill((0,0,0))
        win.blit(menu_image, (0,0))

        #win.blit(game_map, (0,0))
        
        py.display.update()
def pause():
    pause_screen = py.image.load("images/pause_screen.png")
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_p:
                    return
        win.blit(pause_screen, (0,0))


        py.display.update()
def win_face(winner):
        
    if winner == "No Winner":
        yAxis = 100
        xAxis = 200
    else:
        yAxis = 180
        xAxis = 300
    retry_button = py.Rect(100,228,180,60)
    retry_text = py.font.Font.render(menu_font, "Retry", 1, (255,255,255))
    
    quit_button = py.Rect(600,228,180,60)
    quit_text = py.font.Font.render(menu_font, "Quit", 1, (255,255,255))
    
    
    pause_screen = py.image.load("images/win_face.png")
    winner = py.font.Font.render(x_and_o, winner, 1, (255,255,255))
    click = True

    while True:
        mouse_x, mouse_y = py.mouse.get_pos()
        if retry_button.collidepoint((mouse_x, mouse_y)):
            if(click):

                already_block.clear()
                
                for i in range(3):
                    for n in range(3):
                        pos_in_map[i][n] = 7 
                selected_block.clear()
                click = False
                return game()
        elif quit_button.collidepoint((mouse_x, mouse_y)):
            if(click):
                py.quit()
                sys.exit()
        click = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_p:
                    return
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        win.blit(pause_screen, (0,0))
        win.blit(winner, (xAxis,yAxis))
        #py.draw.rect(win, (255,255,0),retry_button)

        win.blit(retry_text, (100,210))
        win.blit(quit_text, (600,210))
        py.display.update()
        
main_menu()

