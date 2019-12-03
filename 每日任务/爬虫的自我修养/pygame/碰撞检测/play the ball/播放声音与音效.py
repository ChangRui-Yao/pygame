#----声音in一般分为两种    一种  背景音乐    另一种 音效
#--pygame  支持的 声音格式  有限   
#-背景音乐时刻伴随着与游戏存在的            一般情况下  使用ogg做背景音乐


#-音效某种条件下  会触发产生的              使用无压缩的wav  来做音效

#播放音效 需要mixer模块       Pygame.mixer.Sound()
                    #---使用之前需要一个Sound对象



#--播放背景音乐  需要music     Pygame.mixer.music


#--sound对象支持的方法                  play()  播放音效
                                #      stop()  停止播放
                                #      fadeout()  淡出
                                #       set_volume()  设置音量
                                #       get_volume()   获得音量
                                #       get_num_channels()  计算该音效播放多少次
                                #       get_length()        获得该音效的长度           多少秒
                                #       get_raw()           将该音效以二进制个是的字符串返回