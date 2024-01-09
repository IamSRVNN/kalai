from app.geo_calc import get_current_coordinates, generate_random_coordinates
from app.delivery_person import Person
from app.app_vars import distance_range, response_time
import random
from inputimeout import inputimeout


def get_user_input(prompt, timeout, id_range):
    """
    Prompt the user for input and wait for a specified number of seconds for a response.

    Args:
    prompt: String, the prompt to display to the user.
    timeout: Float, the number of seconds to wait for a response.

    Returns:
    String, the user's input, or None if no input was received within the specified timeout.
    """
    try:
        user_input = inputimeout(prompt=prompt, timeout=timeout)
        if user_input:
            print(f"Delivery person {user_input} responded")
            return user_input
    except:
        print("No delivery person responded. Hence selecting a random delivery person")
        delivery_peron_id = random.choice(id_range)
        print(f"delivery peron {delivery_peron_id} chosen")


def display_delivery_person_details(delivery_person: Person):
    """
    Prints the details of the delivery person

    Args:
    delivery_person: Class instance of Person

    Returns:
    Nothing
    """
    display_str = f"""
    {"*" * 50}
    ID: {delivery_person.id}
    Location: {delivery_person.location}
    Distance to shop: {delivery_person.distance_to_shop()}
    Distance to customer: {delivery_person.distance_to_customer()}
    Battery remaining: {delivery_person.battery_percentage}
    {"-" * 50}
    """
    # print("*" * 50)
    # print(f"ID: {delivery_person.id}")
    # print(f"Location: {delivery_person.location}")
    # print(f"Distance to shop: {delivery_person.distance_to_shop()}")
    # print(f"Distance to customer: {delivery_person.distance_to_customer()}")
    # print(f"Battery remaining: {delivery_person.battery_percentage}")
    # print("-" * 50)

    return display_str


if __name__ == '__main__':
    # Generate shop location
    shop_location = get_current_coordinates()
    print(f"Shop location is {shop_location}")

    # Generate customer location
    customer_location = generate_random_coordinates(shop_location, distance_range)
    print(f"Customer location is {customer_location}")

    # Generate delivery Persons
    prompt_string = " "
    delivery_persons = []
    id_range = []
    for i in range(5):
        delivery_person = Person(shop_location, customer_location)
        delivery_persons.append(delivery_person)
        id_range.append(delivery_person.id)
        prompt_string += display_delivery_person_details(delivery_person)

    # Enter Prompt
    enhanced_prompt_string = f"""
    Following delivery persons are assigned for this order
    {prompt_string}
    Lets wait {response_time} seconds for their response
    """

    get_user_input(enhanced_prompt_string, response_time, id_range)
