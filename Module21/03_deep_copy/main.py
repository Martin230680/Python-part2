import copy

site = {
    "html": {
        "head": {"title": "Куплю/продам телефон недорого"},
        "body": {
            "h2": "У нас самая низкая цена на iphone",
            "div": "Купить",
            "p": "продать",
        },
    }
}


def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site


site_list = []
product_list = []
number_sites = int(input("Сколько сайтов: "))
for _ in range(number_sites):
    product_name = input("Введите название продукта для нового сайта: ")
    product_list.append(product_name)
    key = {
        "title": f"Куплю/продам {product_name} недорого",
        "h2": f"У нас самая низкая цена на {product_name}",
    }
    temp_site = copy.deepcopy(site)
    for i in key:
        find_key(temp_site, i, key[i])
    site_list.append(temp_site)
    for j in range(len(site_list)):
        print(f"Сайт для {product_list[j]}:")
        print(site_list[j], "\n")

# зачтено
