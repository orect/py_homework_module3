from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        today = datetime.today().date()
        
        delta = today - target_date
        return delta.days
    except ValueError:
        
        return "Invalid date format. Please use 'YYYY-MM-DD'."
