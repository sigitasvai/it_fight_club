
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = datetime.now().strftime("%m/%d/%Y")
print("date and time:",date_time)

# def main():
#     a = datetime.today()
#
#     print(a)
#
#
# if __name__ == "__main__":
#     main()

