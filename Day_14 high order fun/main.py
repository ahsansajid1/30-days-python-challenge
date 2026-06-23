from countries_data import countries

sorted_by_name = sorted(countries, key=lambda x: x["name"])
print(list(sorted_by_name))

