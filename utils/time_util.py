def seconds_to_dhms(seconds):
    days = seconds // (3600 * 24)
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    return days, hours, minutes, seconds
