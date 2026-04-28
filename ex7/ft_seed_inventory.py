def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    units = {
        "packets": "packets available",
        "grams": "grams total"
    }

    if unit in units:
        print(f"{seed_type.capitalize()} seeds: {quantity} {units[unit]}")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: "
              f"covers {quantity} square meters")
    else:
        print("Unkown unit type")
