# Hardcoded values for the season and plant type
season = "summer"
plant_type = "flower"

# Advice stored in dictionaries (supports multiple seasons and plant types)
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
    "spring": "Plant new seedlings and keep soil moist as temperatures rise.\n",
    "autumn": "Mulch garden beds and reduce watering as it cools down.\n"
}

plant_type_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Harvest regularly to encourage more growth.",
    "tree": "Water deeply and mulch around the base (not against the trunk)."
}

# Default messages if the key is not found
default_season_msg = "No advice for this season.\n"
default_plant_msg = "No advice for this type of plant."

# Build final advice using dictionary lookups
advice = ""
advice += season_advice.get(season, default_season_msg)
advice += plant_type_advice.get(plant_type, default_plant_msg)

# Print the generated advice
print(advice)
