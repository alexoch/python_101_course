def clean_list(list_to_clean):
    list_new = []
    for i in range(len(list_to_clean)):
        if list_new.count(list_to_clean[i]) < 1 or type(list_new[list_new.index(list_to_clean[i])])!=type(list_to_clean[i]):
            list_new.append(list_to_clean[i])
    return list_new

print clean_list([32, 32.1, 32.0, -123])
