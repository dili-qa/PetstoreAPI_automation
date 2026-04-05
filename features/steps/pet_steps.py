from behave import given, when, then
from api.pet_api import create_pet, get_pet, delete_pet
from data.pet_data import PET_DATA
from utils.response_validator import (
    validate_status_code,
    validate_json_value
)


@given("user has pet payload")
def step_impl(context):
    context.payload = PET_DATA


@when("user creates a pet")
def step_impl(context):
    context.response = create_pet(context.payload)


@then("pet should be created successfully")
def step_impl(context):
    validate_status_code(context.response, 200)


@when("user fetches pet by id")
def step_impl(context):
    pet_id = context.payload["id"]
    context.response = get_pet(pet_id)


@then("pet data should match")
def step_impl(context):
    validate_json_value(context.response, "id", context.payload["id"])
    validate_json_value(context.response, "name", context.payload["name"])


@when("user deletes the pet")
def step_impl(context):
    pet_id = context.payload["id"]
    context.response = delete_pet(pet_id)


@then("pet should be deleted successfully")
def step_impl(context):
    validate_status_code(context.response, 200)