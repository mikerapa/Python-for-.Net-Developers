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


def print_world_cup_data(data: list[Winner]):
    # sort by year before printing
    data.sort(key=lambda w: w.year)
    for winner in data:
        print(f"{winner.year} - {winner.country} ({winner.competition})")


if __name__ == '__main__':
    data = get_world_cup_data()
    print_world_cup_data(data)
