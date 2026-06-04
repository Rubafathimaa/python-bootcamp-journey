keys = ["names", "ages", "city"]
values = ["ali", 20, "calicut"]

def create_dict(keys, values):
    return dict(zip(keys, values))
result = create_dict(keys, values)
print(result)