import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply
import time
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

bg_size = width,height = 480,700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战---坠神")

background = pygame.image.load('G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/background.png').convert()

BLACK = (0,0,0)
GREEN = (0,255,0)#-绘制血槽需要的颜色数据
RED = (255,0,0)
WHITE = (255,255,255)

#-载入游戏音乐 音效
pygame.mixer_music.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/game_music.ogg")
pygame.mixer_music.set_volume(0.1)
bullet_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_flying_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/enemy3_flying.wav")
enemy3_flying_sound.set_volume(0.1)
enemy1_down_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.1)
enemy2_down_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_enemies(gourp1,gourp2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        gourp1.add(e1)
        gourp2.add(e1)

def add_mid_enemies(gourp1,gourp2,num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        gourp1.add(e2)
        gourp2.add(e2)

def add_big_enemies(gourp1,gourp2,num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        gourp1.add(e3)
        gourp2.add(e3)
def inc_speed(target,inc):
    for each in target:
        each.speed += inc



def main():
    #--背景音乐开始 循环
    pygame.mixer_music.play(-1)
    #---生成我方飞机
    me = myplane.MyPlane(bg_size)
    #生成敌方飞机 并把他们全放在这个enemies里
    enemies = pygame.sprite.Group()
    #-生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)


    #-生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)

    #-生成敌方大飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)

    #-生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4#--定义4颗子弹  加上他的速度  大约有80%的射程
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))#---生成位置  rect.midtop  图片中央上方

    #-生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8#--定义4颗子弹  加上他的速度  大约有80%的射程
    for i in range(BULLET2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx -33,me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx +30,me.rect.centery)))

    #---控制帧率
    clock = pygame.time.Clock()

    #--中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0


    #_--统计用户得分
    score = 0
    score_font = pygame.font.Font(None,36)#--显示得分的字体
    score_font.set_bold(True)


    #--标识是否暂停游戏
    puased = False
    puase_nor_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/pause_nor.png").convert_alpha()
    puase_pressed_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/resume_pressed.png").convert_alpha()
    
    puased_rect = puase_nor_image.get_rect()
    puased_rect.left,puased_rect.top = width - puased_rect.width - 10,10
    puased_image = puase_nor_image


    #--设置游戏难度级别
    level = 1


    #--全屏炸弹
    bomb_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font(None,48)
    bomb_num = 3

    #----每30秒获得一次补给
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT#---自定义事件
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)#-设定事件每10秒触发一次


    #--超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1

    #---解除我方无敌状态计时器
    wudi_time = USEREVENT + 2

    #--限制重复打开记录文件
    read = False

    #--标识是否使用超级子弹
    is_double_bullet = False

    #用于切换我方飞机图片
    switch_iamge = True

    #用于延迟我方图片切换速度
    delay = 100
 
    #--我方飞机生命次数
    life_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3

    #----结束界面
    gameover_font = pygame.font.Font(None,48)
    again_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()


    runing = True

    while runing:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #--响应点击暂停开始
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and puased_rect.collidepoint(event.pos):#---event.pos会返回当前鼠标的位置
                    puased = not puased               #collidepoint 会自动检测传入的这个点是否在矩形内
                    if puased:                       #-是返回True 不是返回Flase
                        pygame.time.set_timer(SUPPLY_TIME,0)
                        pygame.mixer_music.pause()#--如果暂停   补给发放停止  背景音乐 音效暂停
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME,30 * 1000)
                        pygame.mixer_music.unpause()
                        pygame.mixer.unpause()

            elif event.type == MOUSEMOTION:#-----当你的鼠标在这个界面有任何移动
                if puased_rect.collidepoint(event.pos):
                    if puased:
                        puased_image = resume_pressed_image
                    else:
                        puased_image = puase_pressed_image
                else:
                    if puased:
                        puased_image = resume_nor_image
                    else:
                        puased_image = puase_nor_image

            elif event.type == KEYDOWN:#---如果空格 炸了 飞机死了
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        if bomb_num == 0:
                            bomb_num += 1 #---终极sb行为  没了 固定加1ha哈哈哈
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if random.choice([True,False]):
                    bomb_supply.reset()#---事件产生
                else:
                    bullet_supply.reset()


            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME,0)

            elif event.type == wudi_time:
                me.wudi = False
                pygame.time.set_timer(wudi_time,0)


        #--根据得分情况绘制难度
            if level == 1 and score >50000:
                level = 2
                upgrade_sound.play()#--播放提升难度的音效
                #--增加3架小飞机  增加2架中型飞机  和1架 大飞机
                add_small_enemies(small_enemies,enemies,3)
                add_mid_enemies(mid_enemies,enemies,2)
                add_big_enemies(big_enemies,enemies,1)
                #--小飞机速度提升
                inc_speed(small_enemies,1)
            elif level == 2 and score >300000:
                level = 3
                upgrade_sound.play()#--播放提升难度的音效
                #--增加5架小飞机  增加3架中型飞机  和2架 大飞机
                add_small_enemies(small_enemies,enemies,5)
                add_mid_enemies(mid_enemies,enemies,2)
                add_big_enemies(big_enemies,enemies,1)
                #--小飞机速度提升
                inc_speed(small_enemies,1)
                #--中飞机速度提升
                inc_speed(mid_enemies,1)
            elif level == 3 and score >600000:
                level = 4
                upgrade_sound.play()#--播放提升难度的音效
                #--增加8架小飞机  增加4架中型飞机  和3架 大飞机
                add_small_enemies(small_enemies,enemies,5)
                add_mid_enemies(mid_enemies,enemies,2)
                add_big_enemies(big_enemies,enemies,1)
                #--小飞机速度提升
                inc_speed(small_enemies,2)
                #--中飞机速度提升
                inc_speed(mid_enemies,1)
            elif level == 4 and score >800000:
                level = 5
                upgrade_sound.play()#--播放提升难度的音效
                #--增加5架小飞机  增加3架中型飞机  和2架 大飞机
                add_small_enemies(small_enemies,enemies,3)
                add_mid_enemies(mid_enemies,enemies,1)
                add_big_enemies(big_enemies,enemies,2)
                #--小飞机速度提升
                inc_speed(small_enemies,1)
                #--中飞机速度提升
                inc_speed(mid_enemies,2)
                #--大飞机速度提升
                inc_speed(big_enemies,1)

        #--绘制背景
        screen.blit(background,(0,0))
        

        if life_num and not puased:               
            #------检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUP()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDOWN()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLEFT()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRIGHT()
            


        

            #---绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False


            #---绘制双倍子弹补给并检测是否获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image,bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply,me):
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME,18 * 1000)
                    bullet_supply.active = False


            #--发射普通子弹  每十帧一颗
            if not(delay % 10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33,me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+30,me.rect.centery))
                    bullet2_index = (bullet2_index + 2 ) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1 ) % BULLET1_NUM
            
            
            #--检测子弹是否击中敌方飞机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:#---在这里加了一个判断 如果是中型或者大型飞机
                                e.hit = True
                                e.energy -= 1                    #--先将他的energy-1  如果等于零 才毁灭
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            #--绘制大型飞机
            for each in big_enemies:
                if each.active:#-判断活着
                    each.move()
                    if each.hit:
                        #--绘制被击中特效
                        screen.blit(each.image_hit,each.rect)
                        each.hit = False#-绘制结束 hit为false  
                    else:
                        if switch_iamge:#--绘制正常形态
                            screen.blit(each.image1,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)

                    #--绘制血槽#--line画一条直线的line  颜色黑色 底部血槽起点 终点 宽度
                    pygame.draw.line(screen,BLACK,\
                        (each.rect.left,each.rect.top - 5),\
                            (each.rect.right,each.rect.top - 5),\
                                2)
                    #-当生命值大于20% 绘制绿色  否则红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen,energy_color,\
                        (each.rect.left,each.rect.top - 5),\
                            (each.rect.left + each.rect.width * energy_remain,\
                                each.rect.top - 5),2)


                    #--大型飞机即将出现在画面中出现音效
                    if each.rect.bottom > -50:
                        enemy3_flying_sound.play(-1)
                else:
                    #---毁灭
                    if not(delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6#--默认索引进是0 绘制第一张   +1除6 除不尽 继续循环 然后第二张
                        if e3_destroy_index == 0:                      #---一直进来索引为5的图片  也就是最后一张 +1%6除尽了  0了
                            enemy3_flying_sound.stop()
                            score += 10000      #--大型飞机毁灭 +10000
                            each.reset()                                #--执行 each.reset()
            #--绘制中型飞机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image2_hit,each.rect)
                        each.hit = False

                    else:
                        screen.blit(each.image,each.rect)
                    #--绘制血槽 颜色黑色 底部血槽起点 终点 宽度
                    pygame.draw.line(screen,BLACK,\
                        (each.rect.left,each.rect.top - 5),\
                            (each.rect.right,each.rect.top - 5),\
                                2)
                    #-当生命值大于20% 绘制绿色  否则红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen,energy_color,\
                        (each.rect.left,each.rect.top - 5),\
                            (each.rect.left + each.rect.width * energy_remain,\
                                each.rect.top - 5),2)
                else:
                    #--毁灭
                    if not(delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 6000                    
                            each.reset()

            #--绘制小型敌机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    #---毁灭
                    if not(delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000                   
                            each.reset()         


            #---检测我方飞机是否碰撞
            memies_down = pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)#--检测me这个精灵  enemes一组精灵  如果碰撞 返回一个列表
            if memies_down and not me.wudi:
                me.active = False
                for i in memies_down:
                    i.active = False

            if me.active:
                #--绘制我方飞机
                if switch_iamge:
                    screen.blit(me.image1,me.rect)
                else:
                    screen.blit(me.image2,me.rect)
            else:
                #---毁灭
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index],me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(wudi_time,3 * 1000)

                        

            #----绘制炸弹
            bomb_text = score_font.render("X %d" % bomb_num,True,WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image,(10,height - 10 -bomb_rect.height))
            screen.blit(bomb_text,(20 + bomb_rect.width,height - 5 -bomb_rect.height))


            #---绘制我方飞机数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,\
                        (width-10-(i+1)*life_rect.width,\
                            height-10-life_rect.height))

            #--绘制得分
            score_text = score_font.render("Score : %s" % str(score),True,WHITE)#-用render函数将得分渲染成surface对象
                                                #---渲染的东西  抗锯齿  颜色
            screen.blit(score_text,(10,5))

        #--绘制游戏结束画面
        elif life_num == 0:

            #-背景音乐停止
            pygame.mixer_music.stop()

            #-停止全部音效
            pygame.mixer.stop()

            #-停止发放补给
            pygame.time.set_timer(SUPPLY_TIME,0)
            if not read:
                read = True
            #-打开记录文件
            #----读取历史最高分
            with open("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/成绩.txt","r") as f:
                record = int(f.read())

            #-如果玩家高于历史 则存档
            if score > record:
                with open("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/飞机大战/成绩.txt","w")as f:
                    f.write(str(score))
        
            #--绘制结束界面
            record_text = score_font.render("Best:%d"% record,True,RED)#--最高分
            screen.blit(record_text,(50,50))

            gameover_text1 = gameover_font.render("You Score",True,WHITE)
            gameover_text1_rect = gameover_text1.get_rect()#--你的成绩
            gameover_text1_rect.left,gameover_text1_rect.top = \
               (width - gameover_text1_rect.width)//2,height // 3
            screen.blit(gameover_text1,gameover_text1_rect)


            gameover_text2 = gameover_font.render(str(score), True, GREEN)
            gameover_text2_rect = gameover_text2.get_rect()#---成绩
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                    gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)#--继续游戏

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)        #-结束游戏


            #---检查用户鼠标操作
            #-如果按下左键
            if pygame.mouse.get_pressed()[0]:
                #--获取鼠标坐标
                pos = pygame.mouse.get_pos()
                #---如果用户点击重新开始
                if again_rect.left < pos[0] < again_rect.right and\
                    again_rect.top < pos[1] < again_rect.bottom:
                    #调用main()重新开始
                    main()
                #如果点击退出
                if gameover_rect.left < pos[0] < gameover_rect.right and\
                    again_rect.top < pos[1] <gameover_rect.bottom:
                    pygame.quit()
                    sys.exit()


        
        #--绘制暂停按钮
        screen.blit(puased_image,puased_rect)

        #---切换我方飞机
        if not (delay % 5):
            switch_iamge = not switch_iamge#(只有delay能被五整出 才会not打开切换开关)
        delay -= 1
        if not delay:#(每一帧-=1 如果没有重新给100)
            delay = 100
        
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    


