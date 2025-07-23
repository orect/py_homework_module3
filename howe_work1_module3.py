from datetime import datetime

def get_days_from_today(date):
    now = datetime.now()

    diff = now - date
    return diff.days

date = '2021-12-31'
result = get_days_from_today(datetime.strptime(date, '%Y-%m-%d'))
print(f"Days from today to {date}: {result} days")