def hotel_cost(city, nights):
    if city == 'Olkusz':
        return 15 * nights
    else:
        return 140 * nights
    
def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == "Los Angeles":
        return 475
    elif city == "Olkusz":
        return 111
    else:
        return "Wrong input"

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost
        
def trip_cost(city,days,spending_money):
    total = \
    (rental_car_cost(days) +
    hotel_cost(city, days) +
    plane_ride_cost(city) +
    spending_money)
    return total

x = trip_cost('Tampa', 12, 0)
y = trip_cost('Pittsburgh',23, 134)
z = trip_cost('Olkusz', 10, 100)
print (x)
print (y)
print (z)
