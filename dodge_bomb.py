import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


delta = {  
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}


def check_bound(obj_rct: pg.Rect):
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル
    画面外ならTrue、画面外ならFakse
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    """こうかとん"""
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400) 
    kk_RIGHT = pg.transform.flip(kk_img, True, False)
    KK_LEFT = pg.transform.rotozoom(kk_img, 0, 1.0)
    KK_DAWN = pg.transform.rotozoom(kk_img, 90, 1.0)
    KK_HS = pg.transform.rotozoom(kk_img, 45, 1)
    KK_HU = pg.transform.rotozoom(kk_img, -45, 1.0)
    KK_UP = pg.transform.flip(pg.transform.rotozoom(kk_img, -90, 1.0), True, False)
    KK_MU = pg.transform.flip(pg.transform.rotozoom(kk_img, -45, 1.0), True, False)
    KK_MS = pg.transform.flip(pg.transform.rotozoom(kk_img, 45, 1.0), True, False)
    """ばくだん"""
    s = 10 #爆弾の大きさ
    bd_img = pg.Surface((20, 20))  
    bd_img.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), s)
    bd_rct = bd_img.get_rect()  
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bd_rct.center = (x, y)  
    vx, vy = +5, +5
    
    
    """ばくだん２"""
    bd_img2 = pg.Surface((20, 20))  
    bd_img2.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bd_img2, (255, 0, 0), (10, 10), 10)
    bd_rct2 = bd_img2.get_rect()  
    x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bd_rct2.center = (x2, y2) 
    vx2, vy2 = +9, +9  

    """範囲制限"""
    #kiken = pg.Surface((1600, 60))
    #pg.draw.rect(kiken, (255, 255, 0), (20))
    


    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bd_rct):
        
            return    
        elif kk_rct.colliderect(bd_rct2):
            return
        
            

        screen.blit(bg_img, [0, 0])
        

        """こうかとん"""
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]  
                sum_mv[1] += mv[1]  
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True, True):
           kk_rct.move_ip(-sum_mv[0], -sum_mv[1]) 
        if key_lst[pg.K_RIGHT]:
            kk_img = kk_RIGHT
        elif key_lst[pg.K_LEFT]:
            kk_img = KK_LEFT
        elif key_lst[pg.K_DOWN]:
            kk_img = KK_DAWN
        if key_lst[pg.K_LEFT] and key_lst[pg.K_DOWN]:
            kk_img = KK_HS
        if key_lst[pg.K_UP] and key_lst[pg.K_LEFT]:
            kk_img = KK_HU
        elif key_lst[pg.K_UP]:
            kk_img = KK_UP
        if key_lst[pg.K_UP] and key_lst[pg.K_RIGHT]:
            kk_img = KK_MU
        if key_lst[pg.K_DOWN] and key_lst[pg.K_RIGHT]:
            kk_img = KK_MS
        screen.blit(kk_img, kk_rct)  

        """"ばくだん"""
        bd_rct.move_ip(vx, vy)
        yoko , tate = check_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1  
        screen.blit(bd_img, bd_rct)
        if tmr <= 300:
            s += 10
            
        if tmr <= 600:
            s += 20

        """ばくだん２"""
        if tmr > 600:
            bd_rct2.move_ip(vx2, vy2)
            yoko , tate = check_bound(bd_rct2)
            if not yoko:
                vx2 *= -1
            if not tate:
                vy2 *= -1 
            screen.blit(bd_img2, bd_rct2)

        """危険エリア"""
        #screen.blit(kiken, [0, 0])

        
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()