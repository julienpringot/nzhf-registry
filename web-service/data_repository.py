
from dataclasses import dataclass
from datetime import date
from typing import Optional


# @dataclass
# class Region:
#     region_id: int
#     region_name: str


@dataclass
class Club:
    club_id: int
    region_name: str
    club_name: str
    description: str
    logo_image: str  # Assuming it's a link to the image file
    contact_email: str
    website_link: Optional[str] = None
    facebook_link: Optional[str] = None
    instagram_link: Optional[str] = None


@dataclass
class Season:
    season_id: int
    season_name: str
    year: int


@dataclass
class Player:
    player_id: int
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    is_nz_citizen: bool
    email: str
    phone_number: str
    active: bool


@dataclass
class PlayerRegistration:
    registration_id: int
    player_id: int
    club_id: int
    season_id: int


class DataRepository:
    AUCKLAND_REGION = 'Auckland'
    CANTERBURY_REGION = 'Canterbury'
    OTAGO_REGION = 'Otago'
    WELLINGTON_REGION = 'Wellington'

    CLUBS = [
        Club(0, AUCKLAND_REGION, 'Auckland Handball', 'Auckland Regional Handall', 'auckland_logo', 'info@aucklandhandball.com', 'https://www.aucklandhandball.com/', 'https://www.facebook.com/aucklandhandball/', 'https://www.instagram.com/aucklandhandball/'),
        Club(1, CANTERBURY_REGION, 'Canterbury Quakes', 'Canterbury Handball', 'quakes_logo', 'enquiries@canterburyhandball.org.nz', 'https://canterburyhandball.org.nz/', 'https://www.facebook.com/CanterburyHandball/', ''),
        Club(2, OTAGO_REGION, 'Otago Handball', 'Otago Handball', 'otago_logo', 'otagohandball@gmail.com', 'https://handball.org.nz/dunedin', 'https://www.facebook.com/otagohandball/', ''),
    ]

    SEASON_2024 = Season(0, '2024', 2024)

    def __init__(self) -> None:
        self._players = {}

    @property
    def clubs(self):
        return self.CLUBS

    @property
    def current_season(self) -> Season:
        return self.SEASON_2024

    @property
    def players(self):
        return self._players.values()
