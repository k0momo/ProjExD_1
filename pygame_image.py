import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()  
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        speed = 2 if not key_lst[pg.K_RIGHT] else -2
        w = bg_img.get_width()
        x = (tmr * speed) % (w * 2)
        screen.blit(bg_img,  [-x,      0])
        screen.blit(bg_img2, [-x +  w, 0])
        screen.blit(bg_img,  [-x + 2*w,0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        # print(tmr, x)
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()