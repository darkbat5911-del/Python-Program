string_value = "teetergsderhd"

for i in string_value:
    print(i)
    if string_value.count(i) == 1:
        print("Non - repeated :", i)
        break