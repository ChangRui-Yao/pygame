def my_break():
	#break
	bingo = "姜枫"
	answer = input("请输入我的名字：")
	while True:
		if answer == bingo:
			break
		answer = input("答案正确才能退出：")
	print("真厉害，不玩了")
	#continue
	for i in range(10):
		if i%2 != 0:
			print(i)
			continue
		i += 2
		print(i)
	#明白康特牛的作用判断如果if后面的条件成立，也就是说他除以二的余数为0，
		#就跳出去执行 i+=2的操作
my_break()
