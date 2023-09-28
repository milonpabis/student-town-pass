#     AGH LEGITYMACJA MIASTECZKO STUDENCKIE PASS
#     PROGRAM "PODRABIA" LEGITYMACJE STUDENCKIE TYLKO W CELU WEJSCIA NA MIASTECZKO ( NIE W CELACH KOMERCYJNYCH )
#     CELEM PROGRAMU NIE SA KORZYSCI MATERIALNE LUB PODRABIANIE FAKTYCZNE DOKUMENTU

#WYMAGANE BIALE TLO
#WYMAGANY FORMAT NAZWY IMIE_DRUGIEIMIE_NAZWISKO.JPG/PNG/JPEG
#WYMAGANE WYMIARY JAK DO LEGITYMACJI

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random as rd
import datetime as dt
import os

DATE = dt.datetime.now()
IMAGE_SIZE = (238, 299)
FONT = ImageFont.truetype("fonts/FaktPro-Medium.ttf", size=39)
FONT_N = ImageFont.truetype("fonts/Roboto-Medium.ttf", size=27)
FONT_A = ImageFont.truetype("fonts/age.ttf", size=37)
MALE_PATTERN = "images/male_id.jpg"
FEMALE_PATTERN = "images/female_id.jpg"


class Faker:

    def __init__(self, year: str, month: str, day: str, name: str, second_name: str, surname: str, photo: str,
                 album: str, show_day: str, show_month: str, pesel: str, directory: str,
                 random: bool = False):

        self.directory = directory
        self.random = random
        self.show_day = show_day
        self.show_month = show_month
        self.photo = photo
        self.name = name
        self.second_name = second_name
        self.surname = surname

        if self.random:
            self._randomize()
        else:
            self.year = year
            self.month = month
            self.day = day
            self.album = album
            self.pesel = pesel

        self.age = self._calculate_age()
        self.sex = "M"

        if self.name.endswith("A"):
            self.sex = "F"

        self._fake()



    def _calculate_age(self):
        if int(self.month) < DATE.month or (int(self.month) == DATE.month and int(self.day) <= DATE.day):
            return str(DATE.year - int(self.year))
        else:
            return str(DATE.year - int(self.year) - 1)

    def _randomize(self):
        self.year = rd.randint(2002, 2005)
        self.month = rd.randint(1, 12)
        self.day = rd.randint(1, 28)
        self.album = f'4{rd.randint(10000, 99999)}'
        self.pesel = self._gen_pesel()

    def _gen_pesel(self):
        return f'{str(self.year)[2:]}{int(self.month) + 20}{self.day}{rd.randint(10000, 99999)}'

    def _fake(self):
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
        image = Image.open(self.photo).resize(IMAGE_SIZE)

        back_im = image.copy()
        pattern_image.paste(back_im, (39, 415), mask_im)

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
            f'{self.show_day}.{self.show_month}.{DATE.year} 22:28',  # Text
            (0, 0, 0),  # Color
            font=FONT_N
        )

        #pattern_image.show()
        pattern_image.save(self.directory)
