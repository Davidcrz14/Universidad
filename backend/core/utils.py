import uuid
from django.utils import timezone

def generate_unique_id():
    return str(uuid.uuid4())

def format_date(date):
    return date.strftime('%Y-%m-%d')

def get_current_datetime():
    return timezone.now()
