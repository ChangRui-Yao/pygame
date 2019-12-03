import pygame
import sys
#---初始化pygame
pygame.init()

sise = width,height = 600,400
screen = pygame.display.set_mode(sise)#---------------在这里利用pygame的display创建了一个大小为sise的窗口
pygame.display.set_caption("打印字体")#----设置窗口标题
bg = (0,0,0)#---颜色255255255    




font = pygame.font.Font(None,20)#---------用font函数实例化一个对象 第一个参数是字体  第二个是尺寸
                                       #-----None  他会使用你电脑上的默认字
line_height = font.get_linesize()  #----在这里获取他的行高
position = 0#--------刚开始position是零

screen.fill(bg)#--填充颜色




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit()
        s = font.render(str(event),True,(0,255,0))   #-------这里我将渲染好的这个surface对象赋值给s
        #---render 渲染函数   第一个参数 要渲染的文本 str字符串化进来的这个event
        #                     第二个参数   是否消除锯齿   True就可以
        #                      第三个参数   颜色     RGB  
        screen.blit(s,(0,position))
        #---------------把渲染好的东西放到 这个画布上面   第一个参数s   第二个参数 位置 (0,position)
        #0代表x轴为零     position 是一个变量每一行每一行的
        position += line_height
        if position > height:#---如果这个行高大于页面所有就重新全部刷黑色然后在这里  position = 0
            position = 0
            screen.fill(bg)

    pygame.display.flip()