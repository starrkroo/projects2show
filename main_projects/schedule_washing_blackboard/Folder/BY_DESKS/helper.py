
import datetime
import math


def get_token() -> str:
    return ''

def get_students() -> []:
    """
        returns number of desks
    """
    # rows = [int(input("Сколько занято парт на первом ряду: ")),
    #         int(input("Сколько занято парт на втором ряду: ")),
    #         int(input("Сколько занято парт на третьем ряду: "))
    # ]

    rows = [4, 4, 4]

    answer = []
    for row_counter in range(3):
        answer.append([k+1 for k in range(rows[row_counter])])

    return answer

    # return [math.ceil(len(answer[k])/2) for k in range(len(rows))]


def get_dates() -> []:
    current_month = 9
    current_year = datetime.datetime.today().year-1
    date_list = []

    for k in range(9):

        d0 = datetime.datetime(year=current_year, month=current_month, day=1)
        d1 = datetime.datetime(year=current_year+1 if current_month == 12 else current_year, month=current_month+1 if current_month != 12 else 1, day=1)
        # print("{}\t{}".format(d0, d1))

        stacked = [k for k in range(1, (d1-d0).days+1) if datetime.date(current_year, current_month, k).weekday() <= 4]
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

    students__col = -1
    students__row = 0
    current_month = 9

    for month in range(len(dates)):
        for day in dates[month]:
            # TODO: сделать проверку на день недели, чтобы не записывать в список выходные дни
            
            if students__row == len(students):
                students__row = 0

            if students__col == len(students[students__row])-1:
                students__col = 0

                if students__row == len(students)-1:
                    students__row = 0
                else:
                    students__row += 1
            else:
                students__col += 1
            
            dictionary.update(
                {
                    # day::month -> row::desk
                    "{}:{}".format(str(day), str(current_month if 9 <= current_month <= 12 else current_month + 1)):
                        "{}:{}".format(str(students__row+1), students[students__row][students__col])
                }
            )

        if current_month == 12:
            current_month = 0
        else:
            current_month += 1

    return dictionary


if '__main__' == __name__:
    print(interface())

