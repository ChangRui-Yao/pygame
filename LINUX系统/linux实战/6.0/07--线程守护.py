import time
import threading


def work1():
    for i in range(10):
        print("正在执行work...",i)
        time.sleep(0.5)


if __name__ == "__main__":
    thread_work = threading.Thread(target=work1)
    #子线程守护主线程    thread_work.setDaemon(True)表示I帧线程守护主线程（主线程结束，子线程结束）
    thread_work.setDaemon(True)

    thread_work.start()

    time.sleep(2)
    print("game_over")

    exit()