site = {
    "html": {
        "head": {"title": "Мой сайт"},
        "body": {
            "h2": "Здесь будет мой заголовок",
            "div": "Тут, наверное, какой-то блок",
            "p": "А вот здесь новый абзац",
        },
    }
}


def find_key(site, user_key, deep=-1):
    if deep == 0:
        return None
    else:
        if user_key in site:
            return site[user_key]
        for sub_site in site.values():
            if isinstance(sub_site, dict):
                res = find_key(sub_site, user_key, deep - 1)
                if res:
                    break
        else:
            res = None
        return res


user_key = input("Введите ключ: ")
question = input("Хотите ввести глубину поиска (Y/N): ").lower()
if question == "y":
    while True:
        deep = int(input("Введите глубину поиска: "))
        if deep > 0:
            break
        else:
            print("Глубина не может быть 0 и отрицательной. Повторите ввод.")
    value = find_key(site, user_key, deep)
else:
    value = find_key(site, user_key)
if value:
    print("ключ: {key}".format(key=user_key))
    print("значение ключа: {user}".format(user=value))
else:
    print("Такого ключа нет")

# зачтено
