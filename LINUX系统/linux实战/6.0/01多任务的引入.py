import time
"""
#唱歌的函数
#跳舞的函数
调用

"""

def sing():
    for i in range(5):
        print("正在唱歌...")
        time.sleep(0.5)

def dance():
    for i in range(5):
        print("正在跳舞.................")
        time.sleep(0.5)

#-调用
if __name__ == "__main__":
    sing()
    dance()