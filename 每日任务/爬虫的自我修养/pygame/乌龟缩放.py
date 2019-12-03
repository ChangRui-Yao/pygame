import pygame
import sys
from pygame.locals import *
#---初始化pygame
pygame.init()
s = pygame.display.list_modes()#----这里获取了当前屏幕支持的所有分辨率
print(s)
sise = width,height = 600,400
speed = [-2,1]              #----这里有一个speed  -2 上下位置-2    1 水平加1
bg = (0,0,0)#-------这里是一个元组   实际上三个元素是RGB   red green blue


clock = pygame.time.Clock()#----------在这里实例化一个clock对象   这是调节帧率

fullscreen = False              #--全屏设置   默认False

#---创建指定大小的窗口     创建窗口他会返回一个surface对象
screen = pygame.display.set_mode(sise,RESIZABLE)#---------------在这里利用pygame的display创建了一个大小为sise的窗口实际有三个参数
                #----RESIZABLE当用户拖拽屏幕会生成
#---------设置窗口标题
pygame.display.set_caption("初次见面多多关照")

#设置放的缩小的比率
ratio = 1.0


otutrtle = pygame.image.load("G:/PersonPro/PythonPro/每日任务/爬虫的自我修养/pygame/turtle4.png")
tutrtle = otutrtle
otutrtle_rect = otutrtle.get_rect()
position = tutrtle_rect = otutrtle_rect

l_head = tutrtle
r_head = pygame.transform.flip(tutrtle,True,False)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                tutrtle = l_head
                speed = [-1,0]
            if event.key == K_RIGHT:
                tutrtle = r_head
                speed = [1,0]
            if event.key == K_UP:
                speed = [0,-1]
            if event.key == K_DOWN:
                speed = [0,1]

            #---全屏(F11)
            if event.key == K_q:
                fullscreen = not fullscreen
                if fullscreen and sise != (1024,786):
                    sise = width,height = s[0]
                    screen = pygame.display.set_mode((s[0]),FULLSCREEN | HWSURFACE)
                else:
                    sise = width,height = 600,400
                    screen = pygame.display.set_mode(sise,RESIZABLE)
                    position = tutrtle.get_rect()

        #-------放大缩小老鼠（=,-）,空格键返回原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                #最大放大一倍  最小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0
                tutrtle = pygame.transform.smoothscale(otutrtle,\
                    (int(otutrtle_rect.width * ratio),\
                    int(otutrtle_rect.height * ratio)))
                l_head = tutrtle
                r_head = pygame.transform.flip(tutrtle,True,False)
                position = tutrtle.get_rect()

        #----用户调整尺寸
        if event.type == VIDEORESIZE:
            sise = event.size
            width,height = sise
            screen = pygame.display.set_mode(sise,RESIZABLE)
            #otutrtle_rect = otutrtle.get_rect()
            #position = tutrtle_rect = otutrtle_rect



    #------移动图像
    position = position.move(speed)#-----是如何让将一张图像到另一张图像上去的

    if position.left < 0 or position.right > width:
        #------翻转图像
        tutrtle = pygame.transform.flip(tutrtle,True,False)#-------这里传入三个参数 第一个对象 第二个设置水平翻转
                                           #------第三个设置垂直翻转
        #----反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    #填充背景
    screen.fill(bg)#-----移动后 将画布刷成白色  然后在下面贴上去  这两步是在内存中进行
    #更新图像
    screen.blit(tutrtle,position)#--这个意思是把图像绘制到tutrtle 里边
    #更新界面
    pygame.display.flip()#---双缓冲 模式  等一切绘制完毕 然后 把他更新出来
    #延迟10毫秒
    #pygame.time.delay(10)
    clock.tick(200)