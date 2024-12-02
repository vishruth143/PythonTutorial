# People/Telescope profile with all new skills/technologies/experience/ tools
def remove_duplicates(data_list):
    unique = []
    for num in data_list:
        if num not in unique:
            unique.append(num)
    return unique

l = [3, 4, 5, 4, 5, 4, 3, 6]
print(remove_duplicates(l))