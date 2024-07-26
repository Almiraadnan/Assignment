def fuel_cost(distance,fuel_per_liter=280):
    cost = distance * fuel_per_liter
    return cost

distance = 100
cost = fuel_cost(distance)
print(f"the fuel cost for {distance}km is rs. {cost}")