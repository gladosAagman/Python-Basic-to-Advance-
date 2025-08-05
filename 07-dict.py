cities = {"JBP": "MP", "MUMBAI": "MH", "Patna": "BIH"}
for k, v in cities.items():
    print(k, v)

    print(cities.get("JBP"))
    print(cities.get("INDORE"))
    print("JBP" in cities)
