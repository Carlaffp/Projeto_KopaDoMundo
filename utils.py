from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(dicionario: dict):
    data = dicionario
    if data["titles"] < 0:
        raise NegativeTitlesError()

    first_cup_year = int(data["first_cup"].split("-")[0])
    world_first_cup = 1930

    if first_cup_year < world_first_cup or (first_cup_year - world_first_cup) % 4 != 0:
        raise InvalidYearCupError()
    now_date = datetime.now()
    now_year = now_date.year
    number_possible_titles = (now_year - first_cup_year) // 4 + 1
    if number_possible_titles <= data["titles"]:
        raise ImpossibleTitlesError()


