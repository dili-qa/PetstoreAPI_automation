Feature: Pet API

  Scenario: Create, Get and Delete Pet
    Given user has pet payload
    When user creates a pet
    Then pet should be created successfully

    When user fetches pet by id
    Then pet data should match

    When user deletes the pet
    Then pet should be deleted successfully