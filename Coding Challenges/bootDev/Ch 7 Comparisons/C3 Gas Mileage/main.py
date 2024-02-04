def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    total = miles_one_way * 2
    gallons_needed = total / miles_per_gallon
    gallons_needed = gallons_needed - gallons_in_car
    if gallons_needed <= 0:
        return True
    else:
        return False
