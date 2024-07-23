class Parent():
    def __init__(self, parent_name, parent_age, children):
        self.parent_name = parent_name
        self.parent_age = parent_age
        self.children = children

    def info_yourself(self):
        print('Имя родителя: ', self.parent_name)
        print('Возраст: ', self.parent_age)
        for i, i_child in enumerate(self.children):
            string = ''.join(i_child.child_name)
            print(f'Ребенок {i + 1}: {string} {i_child.child_age} ', end='')
            if i_child.flag_hunger:
                print('Голоден ', end='')
            else:
                print('Сыт ', end='')
            if i_child.flag_calmness:
                print('Спокойный ')
            else:
                print('Раздражен ')

    def to_calm(self, child):
        for i_child in self.children:
            string = ''.join(i_child.child_name)
            if string == child:
                i_child.flag_calmness = True

    def to_feed(self, child):
        for i_child in self.children:
            string = ''.join(i_child.child_name)
            if string == child:
                i_child.flag_hunger = False


class Child():
    def __init__(self, child_name, child_age, flag_calmness=False, flag_hunger=True):
        self.child_name = child_name,
        self.child_age = child_age
        self.flag_calmness = flag_calmness
        self.flag_hunger = flag_hunger


Amir = Child('Амир', 12)
Emil = Child('Эмиль', 7)
Diana = Child('Диана', 20)
Timur = Child('Тимур', 14)
Erick = Child('Эрик', 12)
Marsel = Child('Марсель', 7)
Ayaz = Child('Аяз', 20)
Mirhan = Child('Мирхан', 14)
parent1 = Parent('Марат', 43, [Amir, Emil])
parent2 = Parent('Эля', 48, [Diana, Timur])
parent3 = Parent('Роберт', 43, [Erick, Marsel])
parent4 = Parent('Наиль', 43, [Ayaz, Mirhan])
parent_list = [parent1, parent2, parent3, parent4]
while True:
    parent_member = input('Информацию по какому родителю хотите получить (1 - 4), Q - выход из прграммы? ')
    if  parent_member.lower() == 'q':
        break
    elif parent_member == '1':
        parent1.info_yourself()
        for i_child in parent1.children:
            string = ''.join(i_child.child_name)
            if not i_child.flag_calmness:
                choise_calmness = int(input(f'{string} раздражен, успокоить его (1 - да, 0 - нет) ?'))
                if choise_calmness:
                    parent1.to_calm(string)
            if i_child.flag_hunger:
                choise_hunger = int(input(f'{string} голоден, накормить его  (1 - да, 0 - нет) ?'))
                if choise_hunger:
                    parent1.to_feed(string)
    elif parent_member == '2':
        parent2.info_yourself()
        for i_child in parent2.children:
            string = ''.join(i_child.child_name)
            if not i_child.flag_calmness:
                choise_calmness = int(input(f'{string} раздражен, успокоить его (1 - да, 0 - нет) ?'))
                if choise_calmness:
                    parent2.to_calm(string)
            if i_child.flag_hunger:
                choise_hunger = int(input(f'{string} голоден, накормить его  (1 - да, 0 - нет) ?'))
                if choise_hunger:
                    parent2.to_feed(string)
    elif parent_member == '3':
        parent3.info_yourself()
        for i_child in parent3.children:
            string = ''.join(i_child.child_name)
            if not i_child.flag_calmness:
                choise_calmness = int(input(f'{string} раздражен, успокоить его (1 - да, 0 - нет) ?'))
                if choise_calmness:
                    parent3.to_calm(string)
            if i_child.flag_hunger:
                choise_hunger = int(input(f'{string} голоден, накормить его  (1 - да, 0 - нет) ?'))
                if choise_hunger:
                    parent3.to_feed(string)
    elif parent_member == '4':
        parent4.info_yourself()
        for i_child in parent4.children:
            string = ''.join(i_child.child_name)
            if not i_child.flag_calmness:
                choise_calmness = int(input(f'{string} раздражен, успокоить его (1 - да, 0 - нет) ?'))
                if choise_calmness:
                    parent4.to_calm(string)
            if i_child.flag_hunger:
                choise_hunger = int(input(f'{string} голоден, накормить его  (1 - да, 0 - нет) ?'))
                if choise_hunger:
                    parent4.to_feed(string)
    else:
        print('Такого родителя нет. Повторите ввод.')
