from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Hobby(Enum):
    SPORTS = 1
    READING = 2
    MUSIC = 3


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    date_of_birth: date
    subjects: str
    hobbies: Hobby
    picture: str
    current_address: str
    state: str
    city: str


student = User("Vasilisa",
               "Pupkina",
               "vpupkina@gmail.com",
               Gender.FEMALE,
               "8800555332",
               date(2010, 8, 16),
               "Chemistry",
               Hobby.MUSIC,
               "pic.png",
               "some address",
               "NCR",
               "Delhi")