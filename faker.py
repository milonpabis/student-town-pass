#     AGH LEGITYMACJA MIASTECZKO STUDENCKIE PASS
#     PROGRAM "PODRABIA" LEGITYMACJE STUDENCKIE TYLKO W CELU WEJSCIA NA MIASTECZKO ( NIE W CELACH KOMERCYJNYCH )
#     CELEM PROGRAMU NIE SA KORZYSCI MATERIALNE LUB PODRABIANIE FAKTYCZNE DOKUMENTU

#WYMAGANE BIALE TLO
#WYMAGANY FORMAT NAZWY IMIE_DRUGIEIMIE_NAZWISKO.JPG/PNG/JPEG
#WYMAGANE WYMIARY JAK DO LEGITYMACJI

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import PIL
import random as rd
import datetime as dt
import os
import io

DEBUG = False

DATE = dt.datetime.now()
IMAGE_SIZE = (238, 299)
FONT = ImageFont.truetype("fonts/FaktPro-Medium.ttf", size=39)
FONT_N = ImageFont.truetype("fonts/Roboto-Medium.ttf", size=27)
FONT_H = ImageFont.truetype("fonts/FaktPro-Medium.ttf", size=32)
FONT_CREATION = ImageFont.truetype("fonts/Roboto-Medium.ttf", size=29)
FONT_VALID = ImageFont.truetype("fonts/Roboto-Medium.ttf", size=23)
FONT_A = ImageFont.truetype("fonts/age.ttf", size=37)
MALE_PATTERN = "images/male_id1.jpg"
FEMALE_PATTERN = "images/female_id1.jpg"

UNIVERSITY_NAMES = {
    'AGH': 'Akademia Górniczo-Hutnicza im. Stanisława Staszica\nw Krakowie',
    'UJ': 'Uniwersytet Jagielloński',
    'UP': 'Uniwersytet Pedagogiczny im. Komisji Edukacyjnej\nw Krakowie',
    'UEK': 'Uniwersytet Ekonomiczny w Krakowie',
    'PK': 'Politechnika Krakowska im. Tadeusza Kościuszki'

}


class Faker:

    def __init__(self):

        self.directory: str = ""
        self.random: str = ""
        self.show_day: str = ""
        self.show_month: str = ""
        self.show_hour: str = ""
        self.photo: str = ""
        self.name: str = ""
        self.second_name: str = ""
        self.university: str = ""
        self.surname: str = ""
        self.year: str = ""
        self.month: str = ""
        self.day: str = ""
        self.album: str = ""
        self.pesel: str = ""
        self.age: str = ""
        self.sex: str = ""
        self.sex = "M"

        #self._fake()


    



    def _calculate_age(self) -> str:
        if int(self.month) < DATE.month or (int(self.month) == DATE.month and int(self.day) <= DATE.day):
            return str(DATE.year - int(self.year))
        else:
            return str(DATE.year - int(self.year) - 1)


    def _randomize(self) -> None:
        current_year = int(dt.datetime.now().year)
        self.year = str(rd.randint(current_year-22, current_year-21))
        self.month = str(rd.randint(1, 12))
        self.day = str(rd.randint(1, 28))
        self.album = f'4{rd.randint(10000, 99999)}'
        self.pesel = self._gen_pesel()


    def _gen_pesel(self) -> str:
        return f'{str(self.year)[2:]}{int(self.month) + 20}{self.day}{rd.randint(10000, 99999)}'


    def _fake(self) -> PIL.Image:
        image_sex = MALE_PATTERN
        if self.sex == 'F':
            image_sex = FEMALE_PATTERN

        if len(self.day) == 1:
            self.day = '0' + self.day

        if len(self.month) == 1:
            self.month = '0' + self.month

        if len(self.show_day) == 1:
            self.show_day = '0' + self.show_day

        if len(self.show_month) == 1:
            self.show_month = '0' + self.show_month

        pattern_image = Image.open(image_sex)
        mask_im = Image.open('images/ramka_blackout.png')
        if self.photo:
            try:
                image = Image.open(self.photo).resize(IMAGE_SIZE)

                back_im = image.copy()
                pattern_image.paste(back_im, (39, 415), mask_im)
            except:
                pass

        # --------------------------------------------------------------------- F I R S T   S E C O N D   N A M E
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (294, 416),  # Coordinates
            f'{self.name} {self.second_name}',  # Text
            (255, 255, 255),  # Color
            font=FONT
        )

        # --------------------------------------------------------------------- S U R N A M E
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (294, 463),  # Coordinates
            f'{self.surname}',  # Text
            (255, 255, 255),  # Color
            font=FONT
        )

        # --------------------------------------------------------------------- A L B U M
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (172, 359),  # Coordinates
            f'{self.album}',  # Text
            (0, 0, 0),  # Color
            font=FONT_N
        )

        # --------------------------------------------------------------------- D A T E   O F   B I R T H
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (294, 605),  # Coordinates
            f'{self.day}.{self.month}.{self.year}',  # Text
            (255, 255, 255),  # Color
            font=FONT_N,

        )

        # --------------------------------------------------------------------- P E S E L
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (294, 677),  # Coordinates
            self.pesel,  # Text
            (255, 255, 255),  # Color
            font=FONT_N,

        )

        # --------------------------------------------------------------------- A G E
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (675, 657),  # Coordinates
            self.age,  # Text
            (255, 255, 255),  # Color
            font=FONT_A,
            stroke_width=2

        )

        # --------------------------------------------------------------------- D I S P L A Y   D A T E
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (220, 1090),  # Coordinates
            f'{self.show_day}.{self.show_month}.{DATE.year} {self.show_hour}',  # Text
            (0, 0, 0),  # Color
            font=FONT_N
        )

        # --------------------------------------------------------------------- U N I V E R S I T Y
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (55, 969),  # Coordinates
            UNIVERSITY_NAMES.get(self.university, "AGH"),  # Text
            (0, 0, 0),  # Color
            font=FONT_N
        )

        # --------------------------------------------------------------------- S H O W   H O U R
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (50, 29),  # Coordinates
            self.show_hour,  # Text
            (0, 0, 0),  # Color
            font=FONT_H
        )

        # --------------------------------------------------------------------- C R E A T I O N   D A T E
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (658, 358),  # Coordinates
            f"21.09.{dt.datetime.now().year-1}",  # Text
            (0, 0, 0),  # Color
            font=FONT_CREATION
        )

        # --------------------------------------------------------------------- V A L I D   T I L L
        ImageDraw.Draw(
            pattern_image  # Image
        ).text(
            (631, 774),  # Coordinates
            f"31.10.{dt.datetime.now().year+2}",  # Text
            (38, 131, 120),  # Color
            font=FONT_VALID
        )


        #pattern_image.show()
        #if not DEBUG:
        #    print("SAVING", self.directory)
        #    pattern_image.save(self.directory)
        data = io.BytesIO()
        pattern_image.save(data, format='PNG')
        return data


    def set_name(self, name: str) -> None:
        self.name = name
        self.sex = "F" if self.name.endswith("A") else "M"

    def set_second_name(self, second_name: str) -> None:
        self.second_name = second_name

    def set_surname(self, surname: str) -> None:
        self.surname = surname

    def set_photo(self, photo: str) -> None:
        self.photo = photo

    def set_album(self, album: str) -> None:
        self.album = album

    def set_show_date(self, show_day: str, show_month: str, show_hour: str) -> None:
        self.show_day = show_day
        self.show_month = show_month
        self.show_hour = show_hour

    def set_pesel(self, pesel: str) -> None:
        self.pesel = pesel

    def set_university(self, university: str) -> None:
        self.university = university

    def set_directory(self, directory: str) -> None:
        self.directory = directory

    def set_random(self, random: bool) -> None:
        self.random = random

    def set_date(self, year: str, month: str, day: str) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.age = self._calculate_age()

    def set_age(self, age: str) -> None:
        self.age = age

    def set_sex(self, sex: str) -> None:
        self.sex = sex


if __name__ == "__main__":
    Faker(        year="2002",
                  month="12",
                  day="12", 
                  name="Jan", 
                  second_name="Kowalski", 
                  surname="Nowak", 
                  photo="images/ramka_blackout.png",
                  album="12345",
                  show_day="16",
                  show_month="5",
                  show_hour="12:00",
                  pesel="12345678901",
                  university="AGH",
                  directory="hej",
                  random=True)