prices = [57.8, 46.51, 97, 63.54, 72.54, 35.45, 83.1, 43.76, 23.65, 56.86, 13.65]
my_list = []
for price in prices:
    r = int(price)
    kk = round((price - r) * 100)
    my_list.append(f"{r} руб {kk:02d} коп")
print(", ". join(my_list))
id1 = id(prices)
prices.sort()
print(prices)
print(id(prices) == id1)
new_list = sorted(prices, reverse=True)
print(sorted(new_list[:4]))
