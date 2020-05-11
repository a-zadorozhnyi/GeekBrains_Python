# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse():
    def __init__(self, adress, capacity: int):
        self.__adress = adress
        self.__capacity = capacity
        self.__tracking = {}
        self.__shipments = {}

    def receipt_equipmant(self, office_equipment: str, count: int):
        if isinstance(count, int) and count > 0:
            equipment_full_name = office_equipment.full_itm_name
            if equipment_full_name in self.__tracking:
                self.__tracking[equipment_full_name] += count
            else:
                self.__tracking[equipment_full_name] = count
            self.__capacity -= count
        else:
            print("Некорректное наименование товара или количество")
        return self.__tracking

    def dispatch_equipment(self, office_equipment, count: int, department: str):
        if isinstance(count, int) and count > 0:
            equipment_full_name = office_equipment.full_itm_name
            if equipment_full_name in self.__tracking:
                access_count = self.__tracking[equipment_full_name]
                if access_count >= count:
                    self.__tracking[equipment_full_name] -= count
                    self.__capacity += count
                    if department in self.__shipments:
                        self.__shipments[department] += count
                    else:
                        self.__shipments[department] = count
                else:
                    print(f"В наличии на складе имеется {access_count}шт {equipment_full_name}")
            else:
                print(f"There are not {equipment_full_name} at the warehouse")
        else:
            print("Wrong equipment's type or count")
        return self.__tracking

    @property
    def register(self):
        return self.__tracking

    @property
    def shipments(self):
        return self.__shipments

    @property
    def current_capacity(self):
        return self.__capacity


class OfficeEquipment():
    def __init__(self, itm_name: str, manufactorer: str, model: str):
        self._itm_name = itm_name
        self._manufactorer = manufactorer
        self._model = model

    def full_itm_name(self):
        pass

#types of office equipment

class Priner(OfficeEquipment):
    def __init__(self, itm_name:str, manufactorer: str, model: str, performance: int, printer_type: str):
        super().__init__(itm_name, manufactorer, model)
        self.__performance = performance
        self.__printer_type = printer_type

    @property
    def full_itm_name(self):
       return f'{self._itm_name} {self._manufactorer} {self._model} {self.__printer_type}'

class Copier(OfficeEquipment):
    def __init__(self, itm_name:str, manufactorer: str, model: str, copier_type: str):
        super().__init__(itm_name, manufactorer, model)
        self.__copier_type = copier_type

    @property
    def full_itm_name(self):
        print(f'{self._itm_name} {self._manufactorer} {self._model} {self.__copier_type}')

if __name__ == '__main__':
    wh_1 = Warehouse('N street, 142', 100)
    printer1 = Priner('Printer','HP', 'X-102', '100', 'laser')
    copier1 = Copier('Copier', 'Xerox', 'T-4', 'a good one')
    printer2 = Priner('Printer', 'HP', 'X-102', '100', 'laser')

    print(printer1.full_itm_name)
    print(wh_1.receipt_equipmant(printer1, 25))
    print(wh_1.receipt_equipmant(printer2, 25))
    print(wh_1.receipt_equipmant(copier1, 25))
    print(wh_1.dispatch_equipment(printer1, 40, "HR"))
    print(wh_1.current_capacity)
    print(wh_1.shipments)