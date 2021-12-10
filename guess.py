import random
ra = random.randint(1,5)
ra = int(ra)


while True:
	guess = input("請你猜數字: ")
	guess = int(guess)
	if guess == ra:
		print("猜對囉")
		break
	else:
		if ra > guess:
			print("猜小了")
		elif ra < guess:
			print("猜大了")
		
