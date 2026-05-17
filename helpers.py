import random


def generate_daily_sales(base_sale_rate):

    multiplier = random.uniform(0.7, 1.3)

    return int(base_sale_rate * multiplier)


def apply_weekend_boost(
    daily_sales,
    weekend_multiplier
):

    return int(
        daily_sales * weekend_multiplier
    )


def apply_holiday_boost(daily_sales):

    holiday_multiplier = random.uniform(
        1.3,
        1.8
    )

    return int(
        daily_sales * holiday_multiplier
    )