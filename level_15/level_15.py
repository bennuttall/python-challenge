import datetime as dt

leap_month, leap_day = 2, 29
month, day = 1, 26
monday = 0
month_name = "January"

def years_that_fit():
    for year in range(1006, 1997, 10):
        try:
            dt.date(year, leap_month, leap_day)
        except ValueError:
            continue
        d = dt.date(year, month, day)
        if d.weekday() == monday:
            yield year

year = list(years_that_fit())[-2]

tomorrow = (day+1, month_name, year)
print("Google: %s %s %s" % tomorrow)
