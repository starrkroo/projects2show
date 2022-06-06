import datetime
import math

from config import TOKEN


def get_token() -> str:
    return config.TOKEN


def get_students() -> []:
    """
        returns number of desks
    """
    # rows = [int(input("Сколько занято парт на первом ряду: ")),
    #         int(input("Сколько занято парт на втором ряду: ")),
    #         int(input("Сколько занято парт на третьем ряду: "))
    # ]

    studs = """
Абдулаев Ахмед 
Абубакарова Зухра 
Азаев Якуб 
Алиасхабов Ахмед 
Гаджиев Ахмед 
Ибрагимов Арсен 
Магомедов Гаджимурад 
Магомедов Шахманай 
Махмудов Омар 
Минатуллаев Насрутдин 
Рамазанов Эльдар 
Сагидов Абдурахман 
Саидов Арслан
Саидова Рукият 
Уссаева Зумруд
Хидиров Марат 
Шанавазов Магомедсалам 
Шарапудинов Хасай 
Ясулов Магомед 
Мирзаев Алихан"""

    generated = studs.split('\n')[1::]
    return generated


def get_dates() -> []:
    current_month = 9
    current_year = datetime.datetime.today().year - 1
    date_list = []

    for k in range(9):

        d0 = datetime.datetime(year=current_year, month=current_month, day=1)
        d1 = datetime.datetime(year=current_year + 1 if current_month == 12 else current_year,
                               month=current_month + 1 if current_month != 12 else 1, day=1)
        # print("{}\t{}".format(d0, d1))

        stacked = [k for k in range(1, (d1 - d0).days + 1) if
                   datetime.date(current_year, current_month, k).weekday() <= 4]
        date_list.append(stacked)

        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1

    return date_list


def interface():
    """
        Function, that will fill database by values
    """

    #             day:month(from september 2020 to september 2021): desk_pair
    dictionary = {}
    students = get_students()
    dates = get_dates()

    current_month = 9
    students_counter = 0

    for month in range(len(dates)):
        for day in dates[month]:

            if students_counter + 1 == len(students):
                students_counter = 0

            dictionary.update(
                {
                    # day::month -> row::desk
                    "{}:{}".format(str(day), str(current_month if 9 <= current_month <= 12 else current_month + 1)):
                        "{}".format(
                            students[students_counter]
                        )
                }
            )

            students_counter += 1

        if current_month == 12:
            current_month = 0
        else:
            current_month += 1

    return dictionary


if '__main__' == __name__:
    # get_students()
    print(interface())

