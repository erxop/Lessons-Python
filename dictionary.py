#accessing items 
place = {
    "country" : "France",
    "continent" : "Europe",
    "capital" : "Paris"
}
x = place["continent"]
print(x)

y = place["country"]
print(y)

z = place["capital"]
print(z)

# adding an item
place["official language"] = "French"
print(place)  

#changing an item
place["country"] = "Switzerland"
print(place)

#removing an item
place.pop("official language")
print(place)

del place["continent"]
print(place)

place.popitem()
print(place)

for x in place:
    print(x)
    for y in place:
        print(y)
        for z in place:
            print(z)

for x in place:
    print(place[x])
    for y in place:
        print(place[y])
        for z in place:
            print(place[z])
