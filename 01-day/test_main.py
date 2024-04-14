def test_band_name_generator():
    # Test case 1: city = "New York", pet = "Max"
    city = "New York"
    pet = "Max"
    expected_band_name = "New York Max"
    assert band_name_generator(city, pet) == expected_band_name

    # Test case 2: city = "London", pet = "Bella"
    city = "London"
    pet = "Bella"
    expected_band_name = "London Bella"
    assert band_name_generator(city, pet) == expected_band_name

    # Test case 3: city = "Paris", pet = "Charlie"
    city = "Paris"
    pet = "Charlie"
    expected_band_name = "Paris Charlie"
    assert band_name_generator(city, pet) == expected_band_name

    # Test case 4: city = "Tokyo", pet = "Luna"
    city = "Tokyo"
    pet = "Luna"
    expected_band_name = "Tokyo Luna"
    assert band_name_generator(city, pet) == expected_band_name

    # Test case 5: city = "Sydney", pet = "Oscar"
    city = "Sydney"
    pet = "Oscar"
    expected_band_name = "Sydney Oscar"
    assert band_name_generator(city, pet) == expected_band_name

def band_name_generator(city, pet):
    return city + " " + pet