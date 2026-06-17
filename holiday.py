
# User's total holiday cost
print("Welcome to the holiday trip calculator")
print("Available cities for holiday are: Durban, Cape Town, Port Elizabeth")


# This function repeatedly prompt the user for input until a non-negative integer is entered.
def get_valid_num(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid number: Please enter a number greater or equal to 0")
        except ValueError:
            print("Invalid number: Please enter a whole number such as 3")


city_flight = input("Please enter the city you will be flying to: ").title()
num_nights = get_valid_num("Please enter the number of nights spend at the hotel: ")
rental_days = get_valid_num("Please enter the number of car rental days: ")


def hotel_cost(nights_spent = num_nights):
    '''
    Calculate the hotel cost
    Parameters:
    num_nights (int): the number of nights spend at the hotel
    Returns:
    hotel_cost (int): price_night * num_nights
    '''
    price_night = 1800
    return (price_night * num_nights)


def plane_cost(destination = city_flight):
    '''
    Calculate the plane cost

    Parameters:
    city_flight (str): the city you will be flying to

    Returns:
    plane_cost (int): the plane cost to the destination city
    '''

    if city_flight == "Durban":
        return 2000
    elif city_flight == "Cape Town":
        return 3100
    elif city_flight == "Port Elizabeth":
        return 2700
    else:
        return 0


def car_rental(car_rental_duration = rental_days):
    '''
    Calculate the car rental cost

    Parameters:
    rental_days (int): the number of days for which the car is hired

    Returns:
    car_rental_cost(int): daily_rental_cost * rental_days
    '''
    daily_rental_cost = 350
    return (daily_rental_cost * rental_days)


def holiday_cost(hotel_cost, plane_cost, car_rental):
    return (hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days))


print(" ")
print("=" * 55)
print("                  Holiday detail summary")
print("=" * 55)
print("Destination city         : " + (city_flight))
print("Nights spent at the hotel: " + str(num_nights) + " nights at R1800 per night")
print("Car rental days          : " + str(rental_days) + " days at R350 per day")
print(" ")
print("Hotel total cost         : R" + str(hotel_cost(num_nights)))
print("Total flight cost        : R" + str(plane_cost(city_flight)))
print("Total rental cost        : R" + str(car_rental(rental_days)))
print("-" * 55)
print("The total cost of the holiday is R" + str(holiday_cost(hotel_cost, plane_cost, car_rental)))
print("=" * 55)