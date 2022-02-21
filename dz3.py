percent = 'процент'
count = 1
while count <= 100:
    if count > 4 and count < 20:
        print(count, percent + 'ов')
    elif count % 10 == 1:
        print(count, percent)
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
        print(count, percent + 'а')
    else:
        print(count, percent + 'ов')
    count += 1