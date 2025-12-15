
def calculate_total_risk_factor(age, vehicle_type,engine_type, location, accidents):
    multipliers = []

    # Age Multiplier
    if(age < 25):
        multipliers.append(1.3)
    elif 25 <= age <= 40:
        multipliers.append(1.1)
    else:
        multipliers.append(1)

    # Vehicle type multiplier
    if(vehicle_type == "car"):
        multipliers.append(1.2)
    else:
        multipliers.append(1.0)

    # engine type multiplier
    if(engine_type == "sports"):
        multipliers.append(1.5)
    else:
        multipliers.append(1.0)
    
    # location type multiplier
    if(location == "metro"):
        multipliers.append(1.4)
    else:
        multipliers.append(1.0)
    
    # accident multiplier (or) driving history multiplier
    if accidents == 0:
        multipliers.append(1.0)
    elif accidents == 1:
        multipliers.append(1.3)
    else:
        multipliers.append(1.6)

    total_risk_factor = 1.0
    for m in multipliers:
        total_risk_factor *= m
    
    if total_risk_factor <= 1.2:
        risk_level = "LOW"
    elif 1.2 < total_risk_factor <= 1.6:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return total_risk_factor, risk_level


