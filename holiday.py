#let's define our first function hostel_cost
def hotel_cost(num_nights):
    # Assuming a fixed price per night
    price_per_night = 100
    #let's calculate the total cost for the hostel stay based on the number of night
    total_cost = num_nights * price_per_night
    return total_cost

#let's define our second function plane_cost
def plane_cost(city_flight):
    # Assuming prices for different cities
    if city_flight == "Birmingham":
        return 500
    elif city_flight == "Glasgow":
        return 800
    elif city_flight == "New York":
        return 1000
    else:
        return 0

#let's define our third function car_rental
def car_rental(rental_days):
    # Assuming a fixed daily rental cost
    daily_rental_cost = 50
    #let's calculate the total cost for the car rental based on the number of rental days
    total_cost = rental_days * daily_rental_cost
    return total_cost

'''the holiday_cost function combines the costs of hotel, flight, 
and car rental to calculate the total cost of the holiday'''

def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    total_cost = total_hotel_cost + total_plane_cost + total_car_rental_cost
    return total_cost

city_flight = input("Enter the city you will be flying to (Birmingham/New York/Glasgow): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

print("Holiday Details:")
print("City: ", city_flight)
print("Number of nights: ", num_nights)
print("Number of rental days: ", rental_days)
print("Total cost: $", total_holiday_cost)
