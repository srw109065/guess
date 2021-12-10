import random

n = input("請填入最小數字: ")
n = int(n) 
x = input("請填入最大數字: ")
x = int(x) 

ra = random.randint(n,x)
times = 0

while True:
	times += 1
	guess = input("請你猜數字: ")
	guess = int(guess)
	if guess == ra:
		print("猜對囉")
		print("你猜", times, "次")
		break
	else:
		if ra > guess:
			print("猜小了")
			
		elif ra < guess:
			print("猜大了")
	print("你猜", times, "次")
			
		
