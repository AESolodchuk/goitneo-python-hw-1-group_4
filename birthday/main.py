from collections import defaultdict
from datetime import datetime, timedelta
import calendar


def get_birthdays_per_week(users):
    def next_monday(birthday_this_year, delta_days):
        for i in range(7 - delta_days):
            if (birthday_this_year + timedelta(days=i)).weekday() == 0:
                return True
            else:
                i += 1

    def append_users_birthday(birthday_weekday, name):
        users_birthday[birthday_weekday].append(name)

    weekend_days = [5, 6]
    users_birthday = defaultdict(list)
    users_birthday = {0: [], 1: [], 2: [], 3: [], 4: []}
    today_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = (
            birthday.replace(year=today_date.year + 1)
            if birthday.replace(year=today_date.year) < today_date
            else birthday.replace(year=today_date.year)
        )
        delta_days = (birthday_this_year - today_date).days
        if delta_days < 7:
            if birthday_this_year.weekday() in weekend_days and next_monday(
                birthday_this_year, delta_days
            ):
                append_users_birthday(0, name)
            elif birthday_this_year.weekday() not in weekend_days:
                append_users_birthday(birthday_this_year.weekday(), name)

    for key, value in users_birthday.items():
        if value:
            print(f"{calendar.day_name[key]:<9}: {", ".join(value):<}")
