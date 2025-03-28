from datetime import datetime

def format_date(date):
    return f"{date.strftime('%Y-%m-%d %H:%M:%S')}.{date.microsecond // 1000:03d}"