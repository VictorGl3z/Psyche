def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return "overtime charged"
    else:
        return "no charges yet"
