class Date:
    __dates = []
    __formed_date = {}

    def __init__(self, date: str):
        Date.__dates.append(date)
        self.__date = date

    @classmethod
    def form_date(cls):
        try:
            for itm in Date.__dates:
                Date.__formed_date[itm] = [int(i) for i in itm.split("-") if i.isdigit()]
            return Date.__formed_date
        except TypeError:
            print("Value error")

    @staticmethod
    def validation(my_date):
        try:
            if 0 < Date.__formed_date[my_date.date][0] < 32 \
                    and 0 < Date.__formed_date[my_date.date][1] < 13 \
                    and Date.__formed_date[my_date.date][2] < 9999:
                return 'Дата введена корректно.'
            else:
                return 'Дата введена некорректно.'
        except IndexError:
            return False
        except AttributeError:
            return "Error attribute"

    @property
    def date(self):
        return self.__date

if __name__ == '__main__':
    test_1 = '05-05-2020'
    date_1 = Date(test_1)
    print(date_1.date)
    test_2 = '01-00-2020'
    date_2 = Date(test_2)




    print(date_2.date)
    print(Date.form_date())
    print(Date.validation(date_1))
    print(Date.validation(date_2))