def hotelcost(nights):
    return 100*nights
def planecost(city):
    if "hyderabad"==city:
        return 140
    elif "banglore"==city:
        return 110
    elif "mumbai"==city:
        return 149
    elif "chennai"==city:
        return 190
def rentalcarcost(days):
    if days>=7:
        return 30*days-10
    elif days>=3:
        return 30*days-5
    else:
        return 40*days
def trpicost(city,days,expenses):
    return rentalcarcost(days)+hotelcost(days)+planecost(city)+expenses
    

print("cost of car rental is",rentalcarcost)
print("cost of plane ride is",planecost)
print("cost of hotel is",hotelcost)
print("total cost is",trpicost("hyderabad",9,400))