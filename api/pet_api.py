from utils.request_helper import post_request, get_request, delete_request


def create_pet(payload):
    return post_request("/pet", payload)


def get_pet(pet_id):
    return get_request(f"/pet/{pet_id}")


def delete_pet(pet_id):
    return delete_request(f"/pet/{pet_id}")