"""
#1定义变量保存源文件夹的路径 和目标文件夹的路径
#2在目标路创建新的文件夹
#3获取源文件夹中所有的文件（列表）
#4遍历列表，得到所有的文件名
#5定义函数进行文件拷贝

文件拷贝：
参数：源文件夹路径    目标文件夹路径   文件名
1，拼接源文件和目标文件的具体路径
2，，打开源文件，创建目标文件
3，读取源文件的内容，写入到目标文件中（循环）

"""
import os
import multiprocessing
def copy_work(source_dir,dest_dir,file_name):

    print(multiprocessing.current_process())
    """"根据参数拷贝文件"""
    #    参数：源文件夹路径    目标文件夹路径   文件名
    #1，拼接源文件和目标文件的具体路径
    source_path = source_dir +"/" + file_name
    dest_path = dest_dir + "/" + file_name
    #2，，打开源文件，创建目标文件
    #print(source_path,"------->",dest_path)
    #3，读取源文件的内容，写入到目标文件中（循环）
    with open (source_path,"rb") as source_file:
        #创建目标文件
        with open (dest_path,"wb") as dest_file:

            while True:
                #读源文件保存在目标文件
                file_data = source_file.read(1024)
                #判断文件是否读完
                if file_data:
                    dest_file.write(file_data)
                else:
                    break




if __name__ == "__main__":
    #1定义变量保存源文件夹的路径 和目标文件夹的路径
    source_dir = "G:/GitPro/pygame/LINUX系统/linux实战/7.0/test"
    dest_dir = "C:/Users/lenovo/Desktop/test"
#2在目标路创建新的文件夹
    #3利用os模块  在指定目的地  创建文件夹
    try:
        os.mkdir(dest_dir)
    except Exception as e:
        print("文件夹已经存在")
#3获取源文件夹中所有的文件（列表）
    file_list = os.listdir(source_dir)#利用os模块的listdir获得这个文件夹里所有文件的目录
    #print(file_list)
    #创建进程池
    pool = multiprocessing.Pool(3)
    

#4遍历列表，得到所有的文件名
    for file_name in file_list:
        #print(file_name)
        #5定义函数进行文件拷贝
        #copy_work(source_dir,dest_dir,file_name)
       
        #进程池异步
        pool.apply_async(copy_work,(source_dir,dest_dir,file_name))
    
    pool.close()
    pool.join()