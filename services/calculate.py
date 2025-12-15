from .risk import calculate_total_risk_factor

def calculate_final_premium(
    age,
    vehicle_type,
    engine_type,
    location,
    accidents,
    vehicle_value
):
    # 1️⃣ Calculate total risk factor
    total_risk_factor, risk_level = calculate_total_risk_factor(
        age,
        vehicle_type,
        engine_type,
        location,
        accidents
    )

    # 2️⃣ Base premium calculation
    if vehicle_type == "car":
        base_premium = 0.03 * vehicle_value
    else:
        base_premium = 0.04 * vehicle_value

    # 3️⃣ Final premium
    final_premium = base_premium * total_risk_factor

    return int(final_premium), round(total_risk_factor, 2), risk_level
