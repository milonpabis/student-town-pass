from faker import Faker

im = r"F:\Desktop\repos\sandbox\PIL\portrety\klaudia_karyna_drogoń.jpg"


if __name__ == "__main__":
    Faker(year="2002", month="12", day="4", name="MILOSZ", second_name="BORYS", surname="PABIS", photo=im,
          album="417356", show_day="28", show_month="9", show_hour="22:50", pesel="",
          directory=r"F:\Desktop\kurwa.jpg", random=False)