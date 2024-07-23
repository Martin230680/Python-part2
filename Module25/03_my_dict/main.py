# TODO здесь писать код
class MyDict(dict):
    def get(self, key, default_value=0):

        super().get(key, default_value)
        return dict.get(self, key) or default_value


new_dict = MyDict()
new_dict['Mazda'] = 100
new_dict['FORD'] = 2000
new_dict['Geely'] = 30
print(new_dict)
print(new_dict.get('FORD'))
print(new_dict.get('Renault'))

# if key in self:
#     return self[key]
# else:
#     return default_value