import json
from pydantic import BaseModel


class Winner(BaseModel):
    country: str
    year: int
    competition: str


def get_world_cup_data() -> list[Winner]:
    data = json.load(open("worldcupdata.json", "r"))
    winners = [Winner(**w) for w in data]
    return winners


def get_womens_winners_by_country(country_name: str) -> list[Winner]:
    # filter by country
    # f = lambda w: w.country == country_name and w.competition == "women"
    return list(filter(lambda w: w.country == country_name and w.competition == "women", get_world_cup_data()))


def get_mens_winners_by_country(country_name: str) -> list[Winner]:
    return [winner for winner in get_world_cup_data() if winner.country == country_name and winner.competition == "men"]


def get_winners_by_country(country_name: str) -> list[Winner]:
    return [winner for winner in get_world_cup_data() if winner.country == country_name]


def get_mens_winners_all() -> list[Winner]:
    return list(filter(lambda w: w.competition == "men", get_world_cup_data()))


def print_world_cup_data(data: list[Winner]):
    # sort by year before printing
    data.sort(key=lambda w: w.year)
    for winner in data:
        print(f"{winner.year} - {winner.country} ({winner.competition})")


if __name__ == '__main__':
    data = get_world_cup_data()
    # print_world_cup_data(data)
    # print_world_cup_data(get_womens_winners_by_country("Spain"))
    # print_world_cup_data(get_mens_winners_by_country("Spain"))

    # print_world_cup_data(get_winners_by_country("Spain"))
    print_world_cup_data(get_mens_winners_all())
