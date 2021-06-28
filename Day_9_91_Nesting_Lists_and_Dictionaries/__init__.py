#Nesting

capitals = {
    "France":  "Paris",
    "Germany":  "Berlin"
}


# Value is a dictionary or list.
travel_log = {
    "France":  {"cities_visited":  ["Paris", "Lille", "Dijon"]},
    "Germany":  ["Berlin", "Hamburg", "Stuttgart"]
}


# Nesting Dictionary in a list.
travel_log = [
    {
        "country":  "France",
        "cities_visited":  ["Paris", "Lille", "Dijon"],
        "total_visits":  12
    },
    {
        "country":  "Germany",
        "cities_visited":  ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":  5
    }
]