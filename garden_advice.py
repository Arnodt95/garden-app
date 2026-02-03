def build_advice_data():
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
        "spring": "Plant new seedlings and keep soil moist as temperatures "
                  "rise.\n",
        "autumn": "Mulch garden beds and reduce watering as it cools down.\n",
    }

    plant_type_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Harvest regularly to encourage more growth.",
        "tree": "Water deeply and mulch around the base "
                "(not against the trunk).",
    }

    return season_advice, plant_type_advice


def generate_advice(season: str, plant_type: str, season_advice: dict,
                    plant_type_advice: dict) -> str:
    advice = ""
    advice += season_advice.get(season, "No advice for this season.\n")
    advice += plant_type_advice.get(plant_type,
                                    "No advice for this type of plant.")
    return advice


def main():
    # Hardcoded values (unchanged from the original style)
    season = "summer"
    plant_type = "flower"

    season_advice, plant_type_advice = build_advice_data()
    advice = generate_advice(season, plant_type, season_advice,
                             plant_type_advice)

    print(advice)


if __name__ == "__main__":
    main()
