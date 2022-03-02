task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for el in task_list:
    if el.isdigit():
        new_list.extend(['"', el.zfill(2), '"'])
    elif el[1:].isdigit() and el[0] == "-" or el[0] == "+":
        new_list.extend(['"', el.zfill(3), '"'])
    else:
        new_list.append(el)
print(new_list)
