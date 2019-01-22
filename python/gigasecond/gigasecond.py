from datetime import datetime, timedelta

def add_gigasecond(moment):
    return moment + timedelta(seconds=pow(10,9))
