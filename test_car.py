from nose.tools import assert_true


def test_request():
    make = 'BMW'
    f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/\
    {make.capitalize()}?format=json'
    response = requests.get(url)
    assert_true(response.ok)
