# TODO здесь писать код
menu_str = "утиное филе;фланк-стейк;банановый пирог;плов"
print("Доступное мен:{menu}.".format(menu=menu_str))
menu_modif = menu_str.split(";")
menu_str1 = ", ".join(menu_modif)
print("Сейчас в меню есть: {menu}.".format(menu=menu_str1))
