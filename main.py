from faker import Faker
from gui import Window, QApplication

im = r"F:\Desktop\repos\sandbox\PIL\portrety\klaudia_karyna_drogoń.jpg"


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()

    # Faker(year="2003", month="1", day="4", name="MILOSZ", second_name="BORYS", surname="PABIS", photo=im,
    # album="417356", show_day="28", show_month="9", pesel="04230909696",
    # directory=r"F:\Desktop\kurwa.jpg", random=False)
