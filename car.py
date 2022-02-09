import requests
import json


def is_car_exist(make, model):
    '''
    програма проверяет существует ли машина основываясь на сервисе 
    https://vpic.nhtsa.dot.gov 
    нужно ввести make - марка и model - модель 

    Данный сервис не предполагает поиск по модели , а отображает все доступные 
    модели 
    '''
    if type(make) and type(model) not in [str]:
        raise TypeError('Enter String')
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/\
    {make.capitalize()}?format=json'
    try:
        r = requests.get(url)
        if r.status_code != 200:
            raise requests.ConnectionError(f'Expected status code 200, \
                                             but got {r.status_code}')
    except requests.exceptions.Timeout:
        return 'Bad Response'
    data = r.json()['Results']
    return any(model.capitalize() == car['Model_Name'] for car in data)
    



