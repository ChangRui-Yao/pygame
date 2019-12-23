class MyFile(object):
    def __enter__(self):
        print("进入上文")
        self.file = open(self.file_name,self.file_model)
        return self.file
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("进入下文")
        self.file.close()
    def __init__(self,file_name,file_model):
        self.file_name = file_name
        self.file_model = file_model
if __name__ == "__main__":
    
    with MyFile("G:/GitPro/pygame/LINUX系统/linux实战/15.0/1.txt","r") as file:
        file_data = file.read()
        print(file_data)