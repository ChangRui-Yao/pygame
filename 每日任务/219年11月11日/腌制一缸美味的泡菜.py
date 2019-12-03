#------
import pickle
my_list = [123,3.14,'婉儿',['李白','韩信']]
pickle_file = open('my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()


#---怎么读取他？
pickle.file = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
