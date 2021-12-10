import random
ra = random.randint(1,5)

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
			
		
