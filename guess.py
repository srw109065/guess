import random
ra = random.randint(1,5)
ra = int(ra)
times = 3
times = int(times)
print(ra)

while times > 0:
	times -= 1
	guess = input("請你猜數字: ")
	guess = int(guess)
	if guess == ra:
		print("猜對囉")
		break
	else:
		if times == 0:
			print("遊戲結束")
		elif times > 0:
			print("猜錯囉", times, "次機會")
		
