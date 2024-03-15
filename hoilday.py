# Function to get a valid input using a prompt and a validation function
def get_valid_input(prompt, validation_func):
    while True:
        try:
            user_input = validation_func(input(prompt))
            return user_input
        except ValueError:
            print("Error: Enter a valid number.")
        except KeyError as e:
            print(f"Error: {e}")


# Function to validate city input
def get_valid_city_input(city_input):
    city_input = city_input.capitalize()
    if city_input in destination_cities.keys():
        return city_input
    raise KeyError("Enter a valid city.")


# Function to validate numerical input
def get_valid_numerical_input(numerical_input):
    return int(numerical_input)


# Function to calculate hotel cost based on number of nights and city
def get_hotel_cost(num_nights, city_flight):
    hotel_cost_per_night = destination_cities.get(city_flight, {}).get("hotel_cost")
    return num_nights * hotel_cost_per_night


# Function to get plane cost based on the destination city
def get_plane_cost(city_flight):
    return destination_cities.get(city_flight, {}).get("plane_cost")


# Function to calculate car rental cost based on number of days and city
def get_car_rental(rental_days, city_flight):
    car_rental_per_day = destination_cities.get(city_flight, {}).get("car_rental")
    return rental_days * car_rental_per_day


# Function to calculate total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental


# Dictionary containing destination cities and their associated costs
destination_cities = {
    "Paris": {"plane_cost": 42, "hotel_cost": 150, "car_rental": 10},
    "Istanbul": {"plane_cost": 91, "hotel_cost": 95, "car_rental": 5},
    "Barcelona": {"plane_cost": 31, "hotel_cost": 100, "car_rental": 7},
    "Amsterdam": {"plane_cost": 58, "hotel_cost": 80, "car_rental": 9},
    "Lisbon": {"plane_cost": 87, "hotel_cost": 120, "car_rental": 10},
}

# Display the list of destination cities
for i, city in enumerate(destination_cities.keys()):
    print(f"{i + 1}. {city}")

print()

# Get user inputs for destination city, number of nights, and number of rental days
city_flight = get_valid_input("Enter the destination city: ", get_valid_city_input)
num_nights = get_valid_input("Enter the number of days staying at a hotel: ", get_valid_numerical_input)
rental_days = get_valid_input("Enter the number of days renting a car: ", get_valid_numerical_input)

# Calculate individual costs
hotel_cost = get_hotel_cost(num_nights, city_flight)
plane_cost = get_plane_cost(city_flight)
car_rental = get_car_rental(rental_days, city_flight)
total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

# Display the final results
print(f"\n\nDestination city: {city_flight}")
print(f"Plane cost: {plane_cost}£")
print(f"Hotel cost for {num_nights} nights: {hotel_cost}£")
print(f"Car rental for {rental_days} days: {car_rental}£")
print(f"Total holiday cost: {total_cost}£")
