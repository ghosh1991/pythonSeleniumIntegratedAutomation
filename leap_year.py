""" User enters the year  """

year = int(input("Enter Year: "))

"""  Leap Year Check 1 stands for Leap year and 0 stands for non Leap year """

if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 100 == 0:
    print(0)
elif year % 400 ==0:
    print(1)
else:
    print(0)

    print("testing the git")