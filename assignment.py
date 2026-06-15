import random

a = random.randint(100,999)
print(a)

for n in range(10):
    b = int(input("3桁の数字を入力してください："))

    if a-b == 0:
        print("正解！ やるやん")
        break
    elif a-b < -20:
        print("もっと小さい数字です")
    elif a-b < 0:
        print("もう少しだけ小さい数字です")
    elif a-b <= 20:
        print("もう少しだけ大きい数字です")
    else:
        print("もっと大きい数字です")

    print("残りの試行回数は ",10-n-1," 回です")
