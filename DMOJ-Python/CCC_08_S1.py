import sys

coldest_temp = 1000
coldest_city = ""

while True:
    city, temperature = sys.stdin.readline().split()
    city = str(city)
    temperature = int(temperature)

    if temperature < coldest_temp:
        coldest_temp = temperature
        coldest_city = city

    if city == "Waterloo":
        break;

print(coldest_city)