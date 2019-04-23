import random
rand = random.randint(1,100)
for i in range(7):
            guess = int(input("请输入一个1~100的整数："))
            if guess==rand:
                        print("恭喜，猜对了")
                        break
            elif guess > rand:
                        print("猜大了！")
                        if i == 6:
                                    print ("次数用完了！")
                                    break
            elif guess < rand:
                        print("猜小了！")
                        if i == 6:
                                    print ("次数用完了！")
                                    break
            print ("您还有"+str(6-i)+"次机会！")
print ("game over!")
##print (rand)
