import pygame
import Duo_player
import single_player
# Khởi tạo Pygame
pygame.init()
screen_size = 700
screen = pygame.display.set_mode((screen_size+2, screen_size+2))
pygame.display.set_caption('SNAKE GAME BY THANH & QUY__MENU')
clock = pygame.time.Clock()

#Màu sắc
WHITE = (255, 255, 255)
WHITE2 = (100, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
RED2 = (255,102,102)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
GREEN2 = (0, 153, 0)
BLUE = (0,0,255)
BLUE2 = (0,204,204)
BP = (120,0,255)
PURPLE = (153,0,153)
PINK = (255,0,255)
# Load và resize background
background_image = pygame.image.load("menu_background.png")
background_image = pygame.transform.scale(background_image, (screen_size, screen_size))
# Khởi tạo trò chơi
font = pygame.font.Font(None, 30)        
input_speed = '16'
def draw_menu():
    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))
    title_font = pygame.font.Font(None, 20)
    title_text = title_font.render("© GAME MADE BY PHUOC THANH & QUANG QUY", True, WHITE)
    title_rect = title_text.get_rect(center=(165, 10))
    screen.blit(title_text, title_rect)

    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("SNAKE GAME", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_size//2-50, screen_size//5+100))
    screen.blit(title_text, title_rect)

    menu_font = pygame.font.Font(None, 40)
    menu_font_sel = pygame.font.Font(None, 60)
    opt_spacing = 60  # Khoảng cách giữa các lựa chọn

    # Tọa độ y cho lựa chọn đầu tiên
    opt_y = screen_size//2-opt_spacing

    # Hiển thị các lựa chọn
    sp_text_norm = menu_font.render("Single mode", True, WHITE)
    sp_text_sel = menu_font_sel.render("Single mode", True, RED2)
    sp_text = sp_text_sel if option == 0 else sp_text_norm
    sp_rect = sp_text.get_rect(center=(screen_size//2+180, opt_y+180))
    screen.blit(sp_text, sp_rect)

    mp_text_norm = menu_font.render("Co-op mode", True, WHITE)
    mp_text_sel = menu_font_sel.render("Co-op mode", True, RED2)
    mp_text = mp_text_sel if option == 1 else mp_text_norm
    mp_rect = mp_text.get_rect(center=(screen_size//2+180, opt_y + opt_spacing+180))
    screen.blit(mp_text, mp_rect)

    st_text_norm = menu_font.render("Settings", True, WHITE)
    st_text_sel = menu_font_sel.render("Settings", True, RED2)
    st_text = st_text_sel if option == 2 else st_text_norm
    st_rect = st_text.get_rect(center=(screen_size//2+180, opt_y + 2 * opt_spacing+180))
    screen.blit(st_text, st_rect)


def settings_menu():
    global snake_speed,input_speed
    input_speed = ''
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Settings", True, WHITE)
    title_rect = title_text.get_rect(midtop=(screen_size//2, screen_size//4))
    screen.blit(title_text, title_rect)

    speed_font = pygame.font.Font(None, 36)
    speed_text = speed_font.render("Snake Speed: _______ ", True, WHITE)
    speed_rect = speed_text.get_rect(midtop=(screen_size//2-200, screen_size//3))
    screen.blit(speed_text, speed_rect)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_BACKSPACE:
                    input_speed = input_speed[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_speed.isdigit():
                        snake_speed = int(input_speed)
                    return
                else:
                    input_speed += event.unicode
        speed_text = speed_font.render(f"Snake Speed: {input_speed.rjust(0, ' ' )}", True, WHITE)
        screen.blit(speed_text, speed_rect)
        pygame.display.update()
# Hướng dẫn game
def draw_turtorial():
    font = pygame.font.Font(None, 21)
    turtorial = [
        "W, A, S, D and Arrow keys: control snakes",
        "R, Right_Ctrl: Toggle rainbow color for snakes",
        "Space: pause game",
        "Tab: open/close grid",
        "Esc: return menu"
    ]
    y = screen_size-(screen_size//7)
    for line in turtorial:
        text = font.render(line, True, WHITE)
        screen.blit(text, (10, y))
        y += text.get_height() + 5
# Vòng lặp chính
run = True
menu_option = 0  # 0: Menu chính, 1: Chơi game, 2: Cài đặt
option = 0  # 0: Chơi đơn, 1: nhiều người chơi, 2:settings
# Vòng lặp chính
run = True
menu_option = 0  # 0: Menu chính, 1: Chơi game, 2: Cài đặt
option = 0  # 0: Chơi đơn, 1: nhiều người chơi, 2: cài đặt
quit_game = True
if __name__ == '__main__':
    # Mã chương trình chính ở trên
    while run:
        if menu_option == 0:  # Menu chính
            draw_menu()
            draw_turtorial()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        option = (option - 1) % 3  # Chuyển sang lựa chọn trước đó
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        option = (option + 1) % 3  # Chuyển sang lựa chọn tiếp theo
                    elif event.key == pygame.K_RETURN:
                        if option == 0:  # Chọn Singleplayer
                            menu_option = 1
                            singleplayer_mode = True
                            multiplayer_mode = False
                        elif option == 1:  # Chọn Multiplayer
                            menu_option = 3  # Chuyển đến chế độ multiplayer
                            singleplayer_mode = False
                            multiplayer_mode = True
                        else:  # Chọn Settings
                            menu_option = 2
        if not input_speed.isdigit():
            input_speed = '16'
        elif menu_option == 1:  # Chơi đơn
            single_player.single_mode('Start', int(input_speed))
            menu_option = 0
        elif menu_option == 2:  # Cài đặt
            settings_menu()
            menu_option = 0  # Quay lại menu chính sau khi thoát cài đặt
        elif menu_option == 3:  # Chơi 2 người chơi
            Duo_player.duo_mode('Start', int(input_speed))
            menu_option = 0  # Quay lại menu chính sau khi kết thúc trò chơi

    # Đoạn mã để giữ cửa sổ console mở (di chuyển ra ngoài vòng lặp)
    print("Press Enter to exit...")
    
pygame.quit()