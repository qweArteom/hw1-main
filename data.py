from models import Departure, Tour, session
from data import departures, tours

for code, name in departures.items():
    departure = Departure(code=code, name=name)
    session.add(departure)

for tour_id, tour_data in tours.items():
    tour = Tour(
        title=tour_data["title"],
        description=tour_data["description"],
        departure=tour_data["departure"],
        picture=tour_data["picture"],
        price=tour_data["price"],
        stars=int(tour_data["stars"]),
        country=tour_data["country"],
        nights=tour_data["nights"],
        date=tour_data["date"]
    )
    session.add(tour)

session.commit()