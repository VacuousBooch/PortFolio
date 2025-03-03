#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

print(capitals)
print("")
print("")
print("")


#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log)
print("")
print("")
print("")


#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log)
print("")
print("")
print("")


#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(travel_log)
print("")
print("")
print("")

