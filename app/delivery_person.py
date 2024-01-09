import random
from .geo_calc import generate_random_coordinates, calculate_distance
from .app_vars import distance_range, num_of_delivery_persons

delivery_person_possible_ids = list(range(1, num_of_delivery_persons+1))
random.shuffle(delivery_person_possible_ids)
class Person:
    def __init__(self, shop_co_ord, cust_co_ord):
        self.cust_co_ord = cust_co_ord
        self.shop_co_ord = shop_co_ord
        self.id = delivery_person_possible_ids.pop()
        self.battery_percentage = random.randint(1, 100)
        self.location = self.get_location()

    def get_location(self):
        return generate_random_coordinates(self.shop_co_ord, distance_range)

    def distance_to_shop(self):
        return calculate_distance(self.location, self.shop_co_ord)

    def distance_to_customer(self):
        return self.distance_to_shop() + calculate_distance(self.shop_co_ord, self.cust_co_ord)

