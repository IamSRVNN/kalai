from math import sin, cos, radians
import random
from geopy.distance import geodesic
import requests

__all__ = ["generate_random_coordinates", "calculate_distance", "get_current_coordinates"]


def get_current_coordinates():
    """
    Get the current coordinates using the ipinfo.io API.

    Returns:
    Tuple, containing the latitude and longitude of the current coordinates.
    """
    response = requests.get("https://ipinfo.io/json")
    response_data = response.json()
    latitude = response_data["loc"].split(",")[0]
    longitude = response_data["loc"].split(",")[1]
    return float(latitude), float(longitude)


def generate_random_coordinates(current_coordinate, range_km):
    """
    Generate random coordinates within a specific range from a given coordinate.
    The function calculates the new latitude and longitude using the Haversine formula.

    Args:
    current_coordinate: Tuple, containing the latitude and longitude of the current coordinate.
    range_km: Float, the range in kilometers within which the new coordinates should be generated.

    Returns:
    Tuple, containing the latitude and longitude of the new coordinate.
    """
    lat, lon = current_coordinate
    max_distance = range_km
    min_distance = 0
    distance = random.uniform(min_distance, max_distance)
    bearing = random.uniform(0, 360)

    # Calculate the new latitude and longitude using the Haversine formula
    new_lat = lat + (distance / 111.32) * cos(radians(bearing))
    new_lon = lon + (distance / (111.32 * cos(radians(lat)))) * sin(radians(bearing))

    return new_lat, new_lon


def calculate_distance(coord1, coord2):
    """
    Calculate the distance_kms between two coordinates in kilometers.

    Args:
    coord1: Tuple, containing the latitude and longitude of the first coordinate.
    coord2: Tuple, containing the latitude and longitude of the second coordinate.

    Returns:
    Float, the distance_kms between the two coordinates in kilometers.
    """
    distance = geodesic(coord1, coord2).kilometers
    return distance


if __name__ == '__main__':
    # Example usage
    current_coordinate = get_current_coordinates()  # Example current coordinate (latitude, longitude)
    print(f"Current co-ordinate is {current_coordinate}")

    range_km = 10  # Example range in kilometers
    new_coordinate = generate_random_coordinates(current_coordinate, range_km)
    print(f"Newly generated random co-ordinate is {new_coordinate}")

    distance_kms = calculate_distance(current_coordinate, new_coordinate)
    print(f"Distance between current co-ord and the randomly generated co-ord is {distance_kms}")
