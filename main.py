# -------------------- Library --------------------


import pygame
import random
import time
import math

pygame.init()


# -------------------- Music --------------------


pygame.mixer.init()
pygame.mixer.music.load("file/Theme.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# -------------------- Classes --------------------


class Button:
    def __init__(self, bt_x, bt_y, bt_image, bt_scale):
        width = bt_image.get_width()
        height = bt_image.get_height()
        self.image = pygame.transform.scale(bt_image, (int(width * bt_scale), int(height * bt_scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (bt_x, bt_y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


# -------------------- Functions --------------------


def render():
    global m_c

    if pl_c:
        screen.blit(bg_c, (0, 0))
        screen.blit(bg_c, (xbg, 0))
        screen.blit(bg_c, (xbg - dim_x, 0))
        screen.blit(pipe1_c, (xo, dim_y - sz_h2))
        screen.blit(pipe2_c, (xo, 0))
        screen.blit(gr_c, (0, dim_y - dim_y / 10))
        screen.blit(gr_c, (xgr, dim_y - dim_y / 10))
        screen.blit(gr_c, (xgr - dim_x, dim_y - dim_y / 10))
        if l_c:
            screen.blit(life_b_d, (xl, yl))
        if c_c:
            screen.blit(clock_d, (xc, yc))
        if c_c_c > 600:
            screen.blit(clock_d, (xc, yc))
            pygame.draw.rect(screen, (c_cl_r, c_cl_g, 0), (xc, szc_on + 15, c_bar, 10), 0, 2)
        if r_c:
            screen.blit(requiem_d, (xr, yr))
        if r_c_c > 600:
            screen.blit(requiem_d, (xr, yr))
            pygame.draw.rect(screen, (r_cl_r, r_cl_g, 0), (xr, szr_on + 15, r_bar, 10), 0, 2)
        if rf_c:
            screen.blit(requiem_f_d, (x, rfy))
        if las_on:
            screen.blit(laser_d, (x_las, y_las))
        if las_c_on:
            screen.blit(laser_sign_d, (x_las - h_las - 10, y_las))
        screen.blit(bird_c, (x, y))
        if s_c:
            screen.blit(shield_b_d, (xs, ys))
        if s_b:
            screen.blit(shield_b_d, (xs, ys))
            pygame.draw.rect(screen, (s_cl_r, s_cl_g, 0), (xs, szs_on + 15, s_bar, 10), 0, 2)
        if pa_c:
            screen.blit(peanut_b_d, (xp, yp))
        if p_b:
            screen.blit(peanut_b_d, (xp, yp))
            pygame.draw.rect(screen, (p_cl_r, p_cl_g, 0), (xp, szp_on + 15, p_bar, 10), 0, 2)
        if hp > 0:
            screen.blit(score_s_d, (12, 52))
            screen.blit(score_s_d, (8, 48))
            screen.blit(score_s_d, (8, 52))
            screen.blit(score_s_d, (12, 48))
            screen.blit(score_d, (10, 50))
            screen.blit(life1_i_d, (10, 10))
            if hp > 1:
                screen.blit(life2_i_d, (50, 10))
                if hp > 2:
                    screen.blit(life3_i_d, (90, 10))
        if not c_l:
            screen.blit(clock_v_d, (xc_v, yc_v))
        else:
            screen.blit(clock_v_d, (0, 0))
    if st_c:
        screen.blit(start_s_d, (dim_x / 2 - 175 - 2, dim_y / 2 - 50 - 2))
        screen.blit(start_s_d, (dim_x / 2 - 175 + 2, dim_y / 2 - 50 + 2))
        screen.blit(start_s_d, (dim_x / 2 - 175 - 2, dim_y / 2 - 50 + 2))
        screen.blit(start_s_d, (dim_x / 2 - 175 + 2, dim_y / 2 - 50 - 2))
        screen.blit(start_d, (dim_x / 2 - 175, dim_y / 2 - 50))
        if bt_menu_d.draw(screen):
            m_c = True
    if st_c_c:
        screen.blit(start_s_d, (dim_x / 2 - 100 - 2, dim_y / 2 - 50 - 2))
        screen.blit(start_s_d, (dim_x / 2 - 100 + 2, dim_y / 2 - 50 + 2))
        screen.blit(start_s_d, (dim_x / 2 - 100 - 2, dim_y / 2 - 50 + 2))
        screen.blit(start_s_d, (dim_x / 2 - 100 + 2, dim_y / 2 - 50 - 2))
        screen.blit(start_d, (dim_x / 2 - 100, dim_y / 2 - 50))
    if st_c or st_c_c or m_c:
        screen.blit(score_s_d, (12, 52))
        screen.blit(score_s_d, (8, 48))
        screen.blit(score_s_d, (8, 52))
        screen.blit(score_s_d, (12, 48))
        screen.blit(score_d, (10, 50))
    if go_c:
        screen.blit(game_over_box_d, (dim_x - dim_x / 4 * 3, dim_y - dim_y / 4 * 3 + 75))
        screen.blit(game_over_d, game_over_c)
        screen.blit(score_s_p_d, (spp_x - 2, spp_y - 2))
        screen.blit(score_s_p_d, (spp_x + 2, spp_y + 2))
        screen.blit(score_s_p_d, (spp_x - 2, spp_y + 2))
        screen.blit(score_s_p_d, (spp_x + 2, spp_y - 2))
        screen.blit(score_p_d, (spp_x, spp_y))
        screen.blit(score_s_bp_d, (spp_x_b - 2, spp_y_b - 2))
        screen.blit(score_s_bp_d, (spp_x_b + 2, spp_y_b + 2))
        screen.blit(score_s_bp_d, (spp_x_b - 2, spp_y_b + 2))
        screen.blit(score_s_bp_d, (spp_x_b + 2, spp_y_b - 2))
        screen.blit(score_bp_d, (spp_x_b, spp_y_b))
        if bp_c:
            screen.blit(best_score_d, (spp_x_b - 85, spp_y_b - 40))
        if p >= 20:
            screen.blit(medal_d, (300, 310))
    pygame.display.flip()
    time.sleep(fps)


def collision(xa, ya, wa, ha, xb, yb, wb, hb):
    if (xb + wb < xa) or (xb > xa + wa) or (yb + hb < ya) or (yb > ya + ha):
        return False
    else:
        return True


# -------------------- Game Loop --------------------


f = open("file/BestScore.txt", "r+")
bp = int(f.read())
f.close()

boosts = [True, True, True, True , True]

hp_boost_f = open("file/HPBoost.txt", "r+")
if int(hp_boost_f.read()) == 1 and bp >= 20:
    boosts[0] = True
else:
    boosts[0] = False
hp_boost_f.close()

shield_boost_f = open("file/ShieldBoost.txt", "r+")
if int(shield_boost_f.read()) == 1 and bp >= 30:
    boosts[1] = True
else:
    boosts[1] = False
shield_boost_f.close()

time_boost_f = open("file/TimeBoost.txt", "r+")
if int(time_boost_f.read()) == 1 and bp >= 40:
    boosts[2] = True
else:
    boosts[2] = False
time_boost_f.close()

requiem_boost_f = open("file/RequiemBoost.txt", "r+")
if int(requiem_boost_f.read()) == 1 and bp >= 50:
    boosts[3] = True
else:
    boosts[3] = False
requiem_boost_f.close()

peanut_boost_f = open("file/PeanutBoost.txt", "r+")
if int(peanut_boost_f.read()) == 1 and bp >= 60:
    boosts[4] = True
else:
    boosts[4] = False
peanut_boost_f.close()

on_c = True
while on_c:

    # -------------------- Variable --------------------

    # Screen
    dim_x = 1000
    dim_y = dim_x * 9 / 16
    fps = .005
    cd = 300
    ps = 0

    # Bird
    sz = int(dim_x / 20)
    x = dim_x / 7.5
    vx = 0
    y = dim_y / 2 - sz / 2
    vy = 0
    g = .0981
    p = 0
    hp = 3
    b_f = 0
    b_cl = (sz * .3) / 2
    b_cl_sz = sz - b_cl * 2
    c_d = 0

    # Pipe
    sz_w2 = int(dim_x / 25)
    sz_h2 = int(math.fabs(dim_y / random.randint(17, 43) * 10))
    sp = random.randint(200, 300) / 100
    sz_h2_top = int(math.fabs(dim_y - sz_h2 - dim_y / sp))
    xo = dim_x
    vxo = 2

    # Laser
    y_las = 0
    x_las = dim_x
    vx_las = 30
    h_las = 50
    w_las = h_las * 5.55
    las_c = 200
    las_c_r = 0
    las_f = 500

    # Life Boost
    xl = dim_x
    yl = 0
    vxl = 1.5
    szl = 37.5

    # Clock
    xc = dim_x
    yc = 0
    vxc = 1.5
    szc = 37.5
    c_c_c = 600
    szc_on = szc + 20
    c_cl_r = 0
    c_cl_g = 255
    c_bar = 0
    xc_v = 0
    yc_v = 0
    szc_v = 0
    szc_v_x = dim_x
    szc_v_y = dim_y

    # Shield Boost
    xs = dim_x
    ys = 0
    vxs = 1.5
    szs = 37.5
    szs_on = szs + 20
    s_b_c = 1000
    s_bar = 0
    s_cl_r = 0
    s_cl_g = 255

    # Requiem
    xr = dim_x
    yr = 0
    vxr = 1.5
    szr = 37.5
    rfy = dim_y + sz * 2
    r_c_c = 600
    szr_on = szr + 20
    r_cl_r = 0
    r_cl_g = 255
    r_bar = 0

    # Peanut Anya
    xp = dim_x
    yp = 0
    vxp = 1.5
    szp = 37.5
    szp_on = szs + 20
    p_b_c = 1000
    p_bar = 0
    p_cl_r = 0
    p_cl_g = 255
    p_v = 0

    # Background
    xbg = dim_x
    xv_bg = 1
    xgr = dim_x
    spp_x = dim_x / 2 + 150
    spp_y = dim_y / 2 + 15
    spp_x_b = dim_x / 2 + 150
    spp_y_b = dim_y / 2 + 115

    # Booleans Check
    hp_c = True
    st_c = True
    c = True
    go_c = False
    pl_c = False
    l_c = False
    s_c = False
    s_b = False
    las_on = False
    las_l = False
    las_c_on = False
    c_c = False
    c_l = False
    r_c = False
    rfy_c = False
    rf_c = False
    pa_c = False
    p_b = False
    bp_c = False
    st_c_c = False
    ct_c = False
    m_c = False
    p_c = False
    p_c_c = False
    f_c = False

    screen = pygame.display.set_mode((dim_x, dim_y))

    # -------------------- Image/Text Load --------------------

    # Bird
    bird = pygame.image.load("file/Bird1.png")
    bird_c = pygame.transform.scale(bird, (sz, sz))

    # Background
    bg = pygame.image.load("file/BG.png")
    bg_c = pygame.transform.scale(bg, (dim_x, dim_y))
    gr = pygame.image.load("file/Gr.png")
    gr_c = pygame.transform.scale(gr, (dim_x, dim_y / 10))

    # Pipe
    pipe = pygame.image.load("file/Pipe.png")
    pipe1_c = pygame.transform.scale(pipe, (sz_w2, sz_h2))
    pipe2_c = pygame.transform.scale(pipe, (sz_w2, sz_h2_top))
    pipe2_c = pygame.transform.flip(pipe2_c, False, True)

    # Laser
    laser = pygame.image.load("file/Laser.png")
    laser_d = pygame.transform.scale(laser, (w_las, h_las))
    laser_sign = pygame.image.load("file/LaserSign.png")
    laser_sign_d = pygame.transform.scale(laser_sign, (h_las, h_las))
    laser_sign_c = laser_sign_d.get_rect(center=(dim_x - sz, y_las))

    # Score
    score = pygame.font.SysFont("Arial", 50)
    score_d = score.render(str(p) + " / " + str(bp), True, (255, 255, 255))
    score_s_d = score.render(str(p) + " / " + str(bp), True, (0, 0, 0))
    score_go = pygame.font.SysFont("Arial", 40)
    score_p_d = score_go.render(str(p), True, (255, 255, 255))
    score_s_p_d = score_go.render(str(p), True, (0, 0, 0))
    score_bp_d = score_go.render(str(bp), True, (255, 255, 255))
    score_s_bp_d = score_go.render(str(bp), True, (0, 0, 0))

    # Medal
    medal = pygame.image.load("file/Coin1.png")
    medal_d = pygame.transform.scale(medal, (48 * 2.5, 48 * 2.5))

    # Life
    life_i = pygame.image.load("file/HP.png")
    life1_i_d = pygame.transform.scale(life_i, (37.5, 37.5))
    life2_i_d = pygame.transform.scale(life_i, (37.5, 37.5))
    life3_i_d = pygame.transform.scale(life_i, (37.5, 37.5))

    # Life Boost
    life_b_d = pygame.transform.scale(life_i, (szl, szl))

    # Clock
    clock = pygame.image.load("file/Clock.png")
    clock_d = pygame.transform.scale(clock, (szc, szc))
    clock_v = pygame.image.load("file/TimeStop.png")
    clock_v_d = pygame.transform.scale(clock_v, (szc_v, szc_v))

    # Shield Boost
    shield_i = pygame.image.load("file/Shield.png")
    shield_b_d = pygame.transform.scale(shield_i, (szs, szs))

    # Requiem
    requiem = pygame.image.load("file/Requiem.png")
    requiem_d = pygame.transform.scale(requiem, (szr, szr))
    requiem_f = pygame.image.load("file/RequiemFull.png")
    requiem_f_d = pygame.transform.scale(requiem_f, (sz * 2, sz * 2))

    # Peanut
    peanut_i = pygame.image.load("file/Peanut.png")
    peanut_b_d = pygame.transform.scale(peanut_i, (szp, szp))

    # Start
    start = pygame.font.SysFont("Arial", 75)
    start_d = start.render("Press SPACE to play", True, (255, 255, 255))
    start_s_d = start.render("Press SPACE to play", True, (0, 0, 0))

    # Game Over
    game_over = pygame.image.load("file/GameOver.png")
    game_over_d = pygame.transform.scale(game_over, (dim_x / 2, dim_x / 2 / 3.90625))
    game_over_box = pygame.image.load("file/GameOverBox.png")
    game_over_box_d = pygame.transform.scale(game_over_box, (dim_x / 2, dim_x / 2 / 1.8472))
    game_over_c = game_over_d.get_rect(center=(dim_x / 2, dim_y / 2 - 150))
    best_score = pygame.image.load("file/BestScore.png")
    best_score_d = pygame.transform.scale(best_score, (54, 27))

    # Setting Menu
    menu_box = pygame.image.load("file/MenuBox.png")
    menu_box_d = pygame.transform.scale(menu_box, (dim_x / 2, dim_x / 2))
    settings = pygame.image.load("file/Settings.png")
    settings_d = pygame.transform.scale(settings, (dim_x / 4, dim_x / 4 * 0.4318))

    # Pause Menu
    pause = pygame.image.load("file/Pause.png")
    pause_d = pygame.transform.scale(pause, (dim_x / 4, dim_x / 4 * 0.4318))

    # Button
    bt_menu = pygame.image.load('file/menu_btn.png').convert_alpha()
    bt_menu_d = Button(dim_x - 62.5, 10, bt_menu, 0.3)
    bt_menu_cl = False
    bt_heart = pygame.image.load('file/yes_btn.png').convert_alpha()
    bt_heart_d = Button(dim_x - dim_x / 4 * 3 + 20, 150, bt_heart, 0.25)
    bt_heart_no = pygame.image.load('file/no_btn.png').convert_alpha()
    bt_heart_no_d = Button(dim_x - dim_x / 4 * 3 + 20, 150, bt_heart_no, 0.25)
    bt_shield = pygame.image.load('file/yes_btn.png').convert_alpha()
    bt_shield_d = Button(dim_x - dim_x / 4 * 3 + 20, 200, bt_shield, 0.25)
    bt_shield_no = pygame.image.load('file/no_btn.png').convert_alpha()
    bt_shield_no_d = Button(dim_x - dim_x / 4 * 3 + 20, 200, bt_shield_no, 0.25)
    bt_time = pygame.image.load('file/yes_btn.png').convert_alpha()
    bt_time_d = Button(dim_x - dim_x / 4 * 3 + 20, 250, bt_time, 0.25)
    bt_time_no = pygame.image.load('file/no_btn.png').convert_alpha()
    bt_time_no_d = Button(dim_x - dim_x / 4 * 3 + 20, 250, bt_time_no, 0.25)
    bt_requiem = pygame.image.load('file/yes_btn.png').convert_alpha()
    bt_requiem_d = Button(dim_x - dim_x / 4 * 3 + 20, 300, bt_requiem, 0.25)
    bt_requiem_no = pygame.image.load('file/no_btn.png').convert_alpha()
    bt_requiem_no_d = Button(dim_x - dim_x / 4 * 3 + 20, 300, bt_requiem_no, 0.25)
    bt_peanut = pygame.image.load('file/yes_btn.png').convert_alpha()
    bt_peanut_d = Button(dim_x - dim_x / 4 * 3 + 20, 350, bt_peanut, 0.25)
    bt_peanut_no = pygame.image.load('file/no_btn.png').convert_alpha()
    bt_peanut_no_d = Button(dim_x - dim_x / 4 * 3 + 20, 350, bt_peanut_no, 0.25)
    bt_play = pygame.image.load('file/play_btn.png').convert_alpha()
    bt_play_d = Button(dim_x / 2 - 95, 250, bt_play, 5)
    bt_restart = pygame.image.load('file/restart_btn.png').convert_alpha()
    bt_restart_d = Button(dim_x / 2 + 20, 250, bt_restart, 5)

    # -------------------- Sound --------------------

    # World
    Wing = pygame.mixer.Sound("file/Wing.wav")
    Hit = pygame.mixer.Sound("file/Hit.wav")
    Point = pygame.mixer.Sound("file/Point.wav")
    Die = pygame.mixer.Sound("file/Die.wav")
    Laser = pygame.mixer.Sound("file/Laser.wav")

    # Power up
    TimeStop = pygame.mixer.Sound("file/TimeStop.wav")
    ShieldBreak = pygame.mixer.Sound("file/ShieldBreak.wav")
    Shield = pygame.mixer.Sound("file/Shield.wav")
    Requiem = pygame.mixer.Sound("file/Requiem.wav")
    Life = pygame.mixer.Sound("file/Life.wav")
    Anya = pygame.mixer.Sound("file/Anya.wav")

    # Volume
    pygame.mixer.Sound.set_volume(Wing, 0.3)
    pygame.mixer.Sound.set_volume(Hit, 0.5)
    pygame.mixer.Sound.set_volume(Point, 0.75)
    pygame.mixer.Sound.set_volume(Die, 0.25)
    pygame.mixer.Sound.set_volume(Laser, 0.5)
    pygame.mixer.Sound.set_volume(TimeStop, 0.5)
    pygame.mixer.Sound.set_volume(ShieldBreak, 1)
    pygame.mixer.Sound.set_volume(Shield, 1)
    pygame.mixer.Sound.set_volume(Requiem, 1.5)
    pygame.mixer.Sound.set_volume(Life, 0.25)
    pygame.mixer.Sound.set_volume(Anya, 1)

    # -------------------- Processor --------------------

    # Start
    while st_c:
        pl_c = True

        # Setting Menu
        while m_c:
            screen.blit(menu_box_d, (dim_x - dim_x / 4 * 3, 25))
            screen.blit(settings_d, (dim_x - dim_x / 2 - dim_x / 8, 25))

            # HP Boost
            if boosts[0]:
                if bt_heart_d.draw(screen):
                    boosts[0] = False
                    hp_boost_f = open("file/HPBoost.txt", "r+")
                    hp_boost_f.truncate(0)
                    hp_boost_f.write("0")
                    hp_boost_f.close()
            else:
                if bt_heart_no_d.draw(screen) and bp >= 20:
                    boosts[0] = True
                    hp_boost_f = open("file/HPBoost.txt", "r+")
                    hp_boost_f.truncate(0)
                    hp_boost_f.write("1")
                    hp_boost_f.close()
            screen.blit(life1_i_d, (dim_x - dim_x / 4 * 3 + 110, 152.5))

            # Shield Boost
            if boosts[1]:
                if bt_shield_d.draw(screen):
                    boosts[1] = False
                    shield_boost_f = open("file/ShieldBoost.txt", "r+")
                    shield_boost_f.truncate(0)
                    shield_boost_f.write("0")
                    shield_boost_f.close()
            else:
                if bt_shield_no_d.draw(screen) and bp >= 30:
                    boosts[1] = True
                    shield_boost_f = open("file/ShieldBoost.txt", "r+")
                    shield_boost_f.truncate(0)
                    shield_boost_f.write("1")
                    shield_boost_f.close()
                    hp_boost_f.close()
            screen.blit(shield_b_d, (dim_x - dim_x / 4 * 3 + 110, 202.5))

            # Time Boost
            if boosts[2]:
                if bt_time_d.draw(screen):
                    boosts[2] = False
                    time_boost_f = open("file/TimeBoost.txt", "r+")
                    time_boost_f.truncate(0)
                    time_boost_f.write("0")
                    time_boost_f.close()
            else:
                if bt_time_no_d.draw(screen) and bp >= 40:
                    boosts[2] = True
                    time_boost_f = open("file/TimeBoost.txt", "r+")
                    time_boost_f.truncate(0)
                    time_boost_f.write("1")
                    time_boost_f.close()
            screen.blit(clock_d, (dim_x - dim_x / 4 * 3 + 110, 252.5))

            # Requiem Boost
            if boosts[3]:
                if bt_requiem_d.draw(screen):
                    boosts[3] = False
                    requiem_boost_f = open("file/RequiemBoost.txt", "r+")
                    requiem_boost_f.truncate(0)
                    requiem_boost_f.write("0")
                    requiem_boost_f.close()
            else:
                if bt_requiem_no_d.draw(screen) and bp >= 50:
                    boosts[3] = True
                    requiem_boost_f = open("file/RequiemBoost.txt", "r+")
                    requiem_boost_f.truncate(0)
                    requiem_boost_f.write("1")
                    requiem_boost_f.close()
            screen.blit(requiem_d, (dim_x - dim_x / 4 * 3 + 110, 302.5))

            # Peanut Anya Boost
            if boosts[4]:
                if bt_peanut_d.draw(screen):
                    boosts[4] = False
                    peanut_boost_f = open("file/PeanutBoost.txt", "r+")
                    peanut_boost_f.truncate(0)
                    peanut_boost_f.write("0")
                    peanut_boost_f.close()
            else:
                if bt_peanut_no_d.draw(screen) and bp >= 60:
                    boosts[4] = True
                    peanut_boost_f = open("file/PeanutBoost.txt", "r+")
                    peanut_boost_f.truncate(0)
                    peanut_boost_f.write("1")
                    peanut_boost_f.close()
            screen.blit(peanut_b_d, (dim_x - dim_x / 4 * 3 + 110, 352.5))

            # Keys
            keys_menu = pygame.key.get_pressed()
            if keys_menu[pygame.K_ESCAPE]:
                m_c = False
            if bt_menu_d.draw(screen):
                m_c = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            pygame.display.flip()
            time.sleep(fps)

        # Bird
        if b_f < 1:
            bird = pygame.image.load("file/Bird1.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        elif b_f < 2:
            bird = pygame.image.load("file/Bird2.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        elif b_f < 3:
            bird = pygame.image.load("file/Bird3.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        else:
            b_f = 0

        if bp < 20:
            ps = 0 - sum(boosts)
        elif bp < 30:
            ps = 1 - sum(boosts)
        elif bp < 40:
            ps = 2 - sum(boosts)
        elif bp < 50:
            ps = 3 - sum(boosts)
        elif bp < 60:
            ps = 4 - sum(boosts)
        else:
            ps = 5 - sum(boosts)
        
        p = ps * 5
        score_d = score.render(str(p) + " / " + str(bp), True, (255, 255, 255))
        score_s_d = score.render(str(p) + " / " + str(bp), True, (0, 0, 0))

        # Background
        if xbg < 0:
            xbg = dim_x

        if xgr < 0:
            xgr = dim_x

        xbg -= xv_bg
        xgr -= vxo

        # Keys
        pygame.event.get()
        keys_start = pygame.key.get_pressed()
        if keys_start[pygame.K_UP] or keys_start[pygame.K_SPACE]:
            st_c = False
            st_c_c = True
        if keys_start[pygame.K_m]:
            pygame.quit()
            exit(0)

        render()

    # Start count down
    while st_c_c:

        # Bird
        if b_f < 1:
            bird = pygame.image.load("file/Bird1.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        elif b_f < 2:
            bird = pygame.image.load("file/Bird2.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        elif b_f < 3:
            bird = pygame.image.load("file/Bird3.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        else:
            b_f = 0

        if y < dim_y - dim_y / 10 - sz:
            vy += g
            y += vy

        if y > dim_y - dim_y / 10 - sz - 1:
            y = dim_y - dim_y / 10 - sz - 1
            vy -= g

        if y < 0:
            vy = -vy
            y = 0

        bird_c = pygame.transform.scale(bird, (sz, sz))
        bird_c = pygame.transform.rotate(bird_c, vy * -10)

        # Count down
        if cd >= 225:
            start_d = start.render("3", True, (255, 255, 255))
            start_s_d = start.render("3", True, (0, 0, 0))
        elif cd >= 150:
            start_d = start.render("2", True, (255, 255, 255))
            start_s_d = start.render("2", True, (0, 0, 0))
        elif cd >= 75:
            start_d = start.render("1", True, (255, 255, 255))
            start_s_d = start.render("1", True, (0, 0, 0))
        elif cd >= 0:
            start_d = start.render("Go!", True, (255, 255, 255))
            start_s_d = start.render("Go!", True, (0, 0, 0))
        else:
            st_c_c = False

        if cd == 75:
            pygame.mixer.Sound.play(Point)

        cd -= 1

        # Background
        if xbg < 0:
            xbg = dim_x

        if xgr < 0:
            xgr = dim_x

        xbg -= xv_bg
        xgr -= vxo

        # Keys
        pygame.event.get()
        keys_play = pygame.key.get_pressed()
        if not keys_play[pygame.K_UP] and not keys_play[pygame.K_SPACE]:
            f_c = False
        if keys_play[pygame.K_UP] and not f_c or keys_play[pygame.K_SPACE] and not f_c:
            f_c = True
            vy = -3.5
            pygame.mixer.Sound.play(Wing)

        render()

    # Play
    while pl_c and hp > 0:

        # Pause Menu
        while p_c:
            screen.blit(pause_d, (dim_x - dim_x / 2 - dim_x / 8, 100))

            # Keys
            keys_menu = pygame.key.get_pressed()
            if not keys_menu[pygame.K_ESCAPE]:
                p_c_c = False
            if keys_menu[pygame.K_ESCAPE] and not p_c_c:
                p_c_c = True
                p_c = False
            if not keys_menu[pygame.K_UP] and not keys_menu[pygame.K_SPACE]:
                f_c = False
            if keys_menu[pygame.K_UP] and not f_c or keys_menu[pygame.K_SPACE] and not f_c:
                p_c_c = True
                p_c = False
                f_c = True
            if bt_play_d.draw(screen):
                p_c = False
            if bt_restart_d.draw(screen):
                p_c = False
                pl_c = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            pygame.display.flip()
            time.sleep(fps)

        # Bird
        if b_f < 1:
            bird = pygame.image.load("file/Bird1.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        elif b_f < 2:
            bird = pygame.image.load("file/Bird2.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        elif b_f < 3:
            bird = pygame.image.load("file/Bird3.png")
            bird_c = pygame.transform.scale(bird, (sz, sz))
            b_f += 0.1
        else:
            b_f = 0
        
        if y <= dim_y - dim_y / 10 - sz:
            vy += g
            y += vy
        elif c:
            hp -= 1
            hp_c = False
            if hp > 0:
                pygame.mixer.Sound.play(Hit)

        if y > dim_y - dim_y / 10 - sz - 1 and not c:
            y = dim_y - dim_y / 10 - sz - 1
            vy -= g

        if y < 0 and c:
            vy = -vy
            y = 0
            hp -= 1
            if hp > 0:
                pygame.mixer.Sound.play(Hit)

        if y < 0 and not c:
            vy = -vy
            y = 0

        if x > dim_x - sz:
            print("You win")
            break

        vx = 0.0625
        x += vx
        c_d -= 1

        bird_c = pygame.transform.scale(bird, (sz, sz))
        bird_c = pygame.transform.rotate(bird_c, vy * -10)

        # Pipe
        if xo < 0 - sz_w2:
            xo = dim_x
            sp = random.randint(200, 300) / 100
            sz_h2 = int(dim_y / random.randint(17, 43) * 10)
            sz_h2_top = int(dim_y - sz_h2 - dim_y / sp)
            if sz_h2_top <= 0:
                sz_h2_top = sz
            pipe1_c = pygame.transform.scale(pipe, (sz_w2, sz_h2))
            pipe2_c = pygame.transform.scale(pipe, (sz_w2, sz_h2_top))
            pipe2_c = pygame.transform.flip(pipe2_c, False, True)
            p += 1
            if p_b:
                p += 1
            if p % 10 == 0:
                pygame.mixer.Sound.play(Point)
            if bp <= p and not ct_c:
                bp = p
                f = open("file/BestScore.txt", "r+")
                f.truncate(0)
                f.write(str(bp))
                f.close()
                bp_c = True
            hp_c = True
            score_d = score.render(str(p) + " / " + str(bp), True, (255, 255, 255))
            score_s_d = score.render(str(p) + " / " + str(bp), True, (0, 0, 0))

        if collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xo, dim_y - sz_h2, sz_w2, sz_h2) or collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xo, 0, sz_w2, sz_h2_top):
            if hp_c and not s_b and c:
                hp -= 1
                if hp > 0:
                    pygame.mixer.Sound.play(Hit)
                hp_c = False
            if hp_c and s_b and c:
                s_b_c = 1000
                pygame.mixer.Sound.play(ShieldBreak)
                hp_c = False

        xo -= vxo
        vxo += 0.0025

        # Laser
        las_c_r = random.randint(0, int(las_f))
        if las_c_r < 1 and las_c < 0 and bp >= 10:
            las_l = True
            x_las = dim_x
            las_c = 400
            y_las = random.randint(int(dim_y / 12.5), int(dim_y - dim_y / 5))

        if las_c > 300:
            las_c_on = True
        if las_c == 300:
            pygame.mixer.Sound.play(Laser)
            las_on = True
            las_c_on = False

        if las_c < 100 and las_on:
            las_on = False

        if las_c < 300 and las_on:
            x_las -= vx_las

        if x_las + w_las < 0:
            x_las = dim_x
            las_on = False
            p += 1
            if p_b:
                p += 1
            if p % 10 == 0:
                pygame.mixer.Sound.play(Point)
            if bp <= p and not ct_c:
                bp = p
                f = open("file/BestScore.txt", "r+")
                f.truncate(0)
                f.write(str(bp))
                f.close()
                bp_c = True
            score_d = score.render(str(p) + " / " + str(bp), True, (255, 255, 255))
            score_s_d = score.render(str(p) + " / " + str(bp), True, (0, 0, 0))

        if las_f >= 0:
            las_f -= 0.125
        else:
            las_f = 0
        las_c -= 1

        if las_on and collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, x_las, y_las, w_las, h_las):
            if las_l and not s_b and c:
                hp -= 1
                las_l = False
                if hp > 0:
                    pygame.mixer.Sound.play(Hit)
            if las_l and s_b and c:
                s_b_c = 1000
                pygame.mixer.Sound.play(ShieldBreak)
                las_l = False

        # Life Boost
        l_c_r = random.randint(0, 1000)
        if hp >= 3:
            l_c = False

        if l_c_r < 1 and not l_c and boosts[0] and bp >= 20:
            l_c = True
            xl = dim_x
            yl = random.randint(int(dim_y / 12.5), int(dim_y - dim_y / 5))

        if l_c:
            xl -= vxl
            if collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xl, yl, szl, szl):
                hp += 1
                pygame.mixer.Sound.play(Life)
                xl = 0 - szl
            if xl <= 0 - szl:
                l_c = False

        # Clock
        c_c_r = random.randint(0, 1400)
        if c_c_r < 1 and c_c_c < 0 and not c_c and boosts[2] and bp >= 30:
            c_c = True
            xc = dim_x
            yc = random.randint(int(dim_y / 12.5), int(dim_y - dim_y / 5))

        if c_c:
            xc -= vxc
            if collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xc, yc, szc, szc):
                c_c_c = 800 * .25 + 600
                xc = 0 - szc
                c_bar = szc_on
                c_cl_r = 0
                c_cl_g = 255
                szc_v = 0
                pygame.mixer.Sound.play(TimeStop)
            if xc <= 0 - szc:
                c_c = False

        c_c_c -= 1
        c_bar -= szc_on / 400 * 2
        c_cl_r += 255 / 400 * 2
        c_cl_g -= 255 / 400 * 2

        if c_cl_g < 0:
            c_cl_g = 0
        if c_cl_r > 255:
            c_cl_r = 255

        if c_c_c > 600:
            fps = .02
            xc = dim_x - szs_on - szc_on - 20
            yc = 10
            clock_d = pygame.transform.scale(clock, (szc_on, szc_on))
            xc_v = x - szc_v / 2
            yc_v = y - szc_v / 2
            if szc_v < dim_x * 3 and not c_l:
                szc_v += 75
                clock_v = pygame.image.load("file/TimeStop.png")
                clock_v_d = pygame.transform.scale(clock_v, (szc_v, szc_v))
            else:
                c_l = True
            if c_l:
                clock_v = pygame.image.load("file/TimeStopLag.png")
                clock_v_d = pygame.transform.scale(clock_v, (szc_v_x, szc_v_y))
        else:
            clock_d = pygame.transform.scale(clock, (szc, szc))
            szc_v = 0
            c_l = False
            clock_v_d = pygame.transform.scale(clock_v, (szc_v, szc_v))

        if c_c_c < 600 and fps > .005:
            fps -= .00025
        elif fps < .005:
            fps = .005

        # Shield Boost
        s_c_r = random.randint(0, 1000)
        if s_b_c > 1000:
            s_b = True
        else:
            s_b = False
            if s_b_c > 0:
                xs = 0 - szs

        s_b_c -= 1

        if s_c_r < 1 and not s_c and s_b_c <= 0 and boosts[1] and bp >= 40:
            s_c = True
            xs = dim_x
            ys = random.randint(int(dim_y / 12.5), int(dim_y - dim_y / 5))

        if s_c:
            xs -= vxs
            if collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xs, ys, szs, szs):
                s_b_c = 1600
                xs = 0 - szs
                s_bar = szs_on
                s_cl_r = 0
                s_cl_g = 255
                pygame.mixer.Sound.play(Shield)
            if xs <= 0 - szs:
                s_c = False

        if s_b:
            shield_b_d = pygame.transform.scale(shield_i, (szs_on, szs_on))
            xs = dim_x - szs_on - 10
            ys = 10
        else:
            shield_b_d = pygame.transform.scale(shield_i, (szs, szs))

        s_bar -= szs_on / 600
        s_cl_r += 255 / 600
        s_cl_g -= 255 / 600

        if s_cl_g < 0:
            s_cl_g = 0
        if s_cl_r > 255:
            s_cl_r = 255

        # Requiem
        r_c_r = random.randint(0, 1400)
        if r_c_r < 1 and r_c_c < 0 and not r_c and boosts[3] and bp >= 50:
            r_c = True
            xr = dim_x
            yr = random.randint(int(dim_y / 12.5), int(dim_y - dim_y / 5))

        if r_c:
            xr -= vxr
            if collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xr, yr, szr, szr):
                r_c_c = 800 * .25 + 600
                xr = 0 - szr
                rfy = dim_y + sz * 2
                rfy_c = False
                r_bar = szr_on
                r_cl_r = 0
                r_cl_g = 255
                rf_c = True
                pygame.mixer.Sound.play(Requiem)
            if xr <= 0 - szr:
                r_c = False

        r_c_c -= 1
        r_bar -= szr_on / 400 * 2
        r_cl_r += 255 / 400 * 2
        r_cl_g -= 255 / 400 * 2

        if r_cl_g < 0:
            r_cl_g = 0
        if r_cl_r > 255:
            r_cl_r = 255

        if r_c_c > 600:
            xr = dim_x - szc_on - szs_on - szr_on - 30
            yr = 10
            requiem_d = pygame.transform.scale(requiem, (szr_on, szr_on))
            if xo > dim_x:
                xo = 0 - sz_w2
                sp = random.randint(200, 300) / 100
                sz_h2 = int(dim_y / random.randint(17, 43) * 10)
                sz_h2_top = int(dim_y - sz_h2 - dim_y / sp)
                if sz_h2_top <= 0:
                    sz_h2_top = sz
                pipe1_c = pygame.transform.scale(pipe, (sz_w2, sz_h2))
                pipe2_c = pygame.transform.scale(pipe, (sz_w2, sz_h2_top))
                pipe2_c = pygame.transform.flip(pipe2_c, False, True)
                p += 1
                if p_b:
                    p += 1
                if p % 10 == 0:
                    pygame.mixer.Sound.play(Point)
                if bp <= p and not ct_c:
                    bp = p
                    f = open("file/BestScore.txt", "r+")
                    f.truncate(0)
                    f.write(str(bp))
                    f.close()
                    bp_c = True
                hp_c = True
                score_d = score.render(str(p) + " / " + str(bp), True, (255, 255, 255))
                score_s_d = score.render(str(p) + " / " + str(bp), True, (0, 0, 0))
            if xgr > dim_x:
                xgr = 0
            if xbg > dim_x:
                xbg = 0
            if vxo > 0:
                vxo = -vxo
                xv_bg = -xv_bg
                vxl = -vxl
                vxc = -vxc
                vxs = -vxs
                vxp = -vxp
            if x_las < dim_x and vx_las > 0:
                vx_las = -vx_las
            if x_las + w_las > 0:
                las_c += 1
            if x_las >= dim_x and las_on:
                x_las = dim_x
                las_c_on = True
            if rfy > y and not rfy_c:
                rfy -= 20
            else:
                rfy_c = True
            if rfy_c:
                rfy = y
        else:
            requiem_d = pygame.transform.scale(requiem, (szr, szr))
            if vxo < 0:
                vxo = -vxo
                xv_bg = -xv_bg
                vxl = -vxl
                vxc = -vxc
                vxs = -vxs
                vxp = -vxp
            if vx_las < 0:
                vx_las = -vx_las
                x_las = dim_x
                las_c_on = False
            if rfy < dim_y + sz * 2:
                rfy += 20
            else:
                rf_c = False

        # Peanut
        p_c_r = random.randint(0, 1000)
        if p_b_c > 1000:
            p_b = True
        else:
            p_b = False
            if p_b_c > 0:
                xp = 0 - szp

        p_b_c -= 1

        if p_c_r < 1 and not pa_c and p_b_c <= 0 and boosts[4] and bp >= 60:
            pa_c = True
            xp = dim_x
            yp = random.randint(int(dim_y / 12.5), int(dim_y - dim_y / 5))

        if pa_c:
            xp -= vxp
            if collision(x + 10, y + b_cl + 10, sz - 10, b_cl_sz - 5, xp, yp, szp, szp):
                p_b_c = 1500
                xp = 0 - szp
                p_bar = szp_on
                p_cl_r = 0
                p_cl_g = 255
                p_v = 0
                pygame.mixer.Sound.play(Anya)
            if xp <= 0 - szp:
                pa_c = False

        if p_b:
            peanut_i = pygame.image.load("file/PeanutAnya.png")
            peanut_b_d = pygame.transform.scale(peanut_i, (szp_on, szp_on))
            xp = dim_x - szc_on - szs_on - szr_on - szp_on - 40
            yp = 10
            pygame.mixer.music.set_volume(p_v)
        else:
            peanut_i = pygame.image.load("file/Peanut.png")
            peanut_b_d = pygame.transform.scale(peanut_i, (szp, szp))
        if p_b_c < 1050:
            if p_v < 0.5:
                p_v += 0.025
            else:
                p_v = 0.5
            pygame.mixer.music.set_volume(p_v)

        p_bar -= szp_on / 500
        p_cl_r += 255 / 500
        p_cl_g -= 255 / 500

        if p_cl_g < 0:
            p_cl_g = 0
        if p_cl_r > 255:
            p_cl_r = 255
        
        # Background
        if xbg < 0:
            xbg = dim_x

        if xgr < 0:
            xgr = dim_x

        xbg -= xv_bg
        xgr -= vxo

        # Keys
        pygame.event.get()
        keys_play = pygame.key.get_pressed()
        if not keys_play[pygame.K_UP] and not keys_play[pygame.K_SPACE]:
            f_c = False
        if keys_play[pygame.K_UP] and not f_c or keys_play[pygame.K_SPACE] and not f_c:
            f_c = True
            vy = -3.5
            pygame.mixer.Sound.play(Wing)
        if keys_play[pygame.K_DOWN]:
            vy = 3.5
        if not keys_play[pygame.K_ESCAPE]:
            p_c_c = False
        if keys_play[pygame.K_ESCAPE] and not p_c_c:
            p_c_c = True
            p_c = True

        if keys_play[pygame.K_LSHIFT]:
            ct_c = True
            if keys_play[pygame.K_a] and hp < 3:
                hp += 1
            if keys_play[pygame.K_s]:
                s_b_c = 1600
                xs = dim_x - szs_on - 10
                s_bar = szs_on
                s_cl_r = 0
                s_cl_g = 255
            if keys_play[pygame.K_d]:
                c_c_c = 800 * .25 + 600
                xc = dim_x - szs_on - szc_on - 20
                c_bar = szc_on
                c_cl_r = 0
                c_cl_g = 255
            if keys_play[pygame.K_c]:
                if c and c_d < 0:
                    c = False
                    c_d = 200
                if not c and c_d < 0:
                    c = True
                    c_d = 200
            if keys_play[pygame.K_f]:
                r_c_c = 800 * .25 + 600
                xr = dim_x - szc_on - szs_on - szr_on - 30
                rfy = y
                r_bar = szr_on
                r_cl_r = 0
                r_cl_g = 255
                rf_c = True
            if keys_play[pygame.K_g]:
                p_b_c = 1600
                xp = dim_x - szc_on - szs_on - szr_on - szp_on - 40
                p_bar = szp_on
                p_cl_r = 0
                p_cl_g = 255
            if keys_play[pygame.K_x]:
                hp = 0

        render()

    # Lose Visual
    fps = .005
    if hp <= 0:
        if p_v < 0.5:
            p_v += 0.025
        else:
            p_v = 0.5
        pygame.mixer.music.set_volume(p_v)
        pygame.mixer.Sound.play(Die)
        while y <= dim_y - dim_y / 10 - sz:
            vy += g
            y += vy
            bird_c = pygame.transform.scale(bird, (sz, sz))
            bird_c = pygame.transform.rotate(bird_c, vy * -10 + 5)

            render()

        go_c = True

    # Lose
    while go_c:

        if p_v < 0.5:
            p_v += 0.025
        else:
            p_v = 0.5
        pygame.mixer.music.set_volume(p_v)
        
        # Keys
        pygame.event.get()
        keys_stop = pygame.key.get_pressed()
        if keys_stop[pygame.K_n]:
            go_c = False
        if keys_stop[pygame.K_m]:
            go_c = False
            on_c = False

        # Medal
        if p < 40:
            medal = pygame.image.load("file/Coin1.png")
            medal_d = pygame.transform.scale(medal, (48 * 2.5, 48 * 2.5))
        elif p < 60:
            medal = pygame.image.load("file/Coin2.png")
            medal_d = pygame.transform.scale(medal, (48 * 2.5, 48 * 2.5))
        elif p < 80:
            medal = pygame.image.load("file/Coin3.png")
            medal_d = pygame.transform.scale(medal, (48 * 2.5, 48 * 2.5))
        else:
            medal = pygame.image.load("file/Coin4.png")
            medal_d = pygame.transform.scale(medal, (48 * 2.5, 48 * 2.5))

        # Score
        score_p_d = score_go.render(str(p), True, (255, 255, 255))
        score_s_p_d = score_go.render(str(p), True, (0, 0, 0))
        score_bp_d = score_go.render(str(bp), True, (255, 255, 255))
        score_s_bp_d = score_go.render(str(bp), True, (0, 0, 0))

        render()

pygame.quit()
exit(0)
