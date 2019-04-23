try:
            11/0
            print(num)
            open("xxx.txt")
            print('--1---')
except (NameError,FileNotFoundError):
            print("发生了什么异常")
except Exception as ret:
            print(ret)

try:
            open("xxx.txt")
            print(num)
            print('--1---')
except FileNotFoundError:
            print("发生了什么异常")
except Exception:
            print('未知异常')
print('success')
else:
            print('no Error')
finally:
            print('====finally====')
