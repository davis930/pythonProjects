from datetime import datetime

birthday = datetime(1995, 1 ,2)
print(birthday.year, birthday.month, birthday.day)

print(datetime.now())
print(datetime(1997,5,27) -birthday)

days_in_the_year_so_far = datetime.now() - datetime(2023, 1, 1)
print(days_in_the_year_so_far)