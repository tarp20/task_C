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

    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/\
    {make.capitalize()}?format=json'
    data = requests.get(url).json()['Results']
    return any(model.capitalize() == car['Model_Name'] for car in data)
      


        
