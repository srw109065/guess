import random
ra = random.randint(1,5)
ra = int(ra)
times = 0

while True:
	guess = input("請你猜數字: ")
	guess = int(guess)
	if guess == ra:
		print("猜對囉")
		print("總共猜", times, "次")
		break
	else:
		if ra > guess:
			print("猜小了")
			times += 1
		elif ra < guess:
			print("猜大了")
			times += 1
		
