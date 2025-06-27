import csv
from os import write
from os.path import split


def filter_orders_by_cost(lst_orders, coast):
    header = next(lst_orders)
    filtered_rows = list(filter(lambda row: float(row[2]) >= coast, lst_orders))
    return filtered_rows, header


with open('../data/orders.csv', 'r') as f:
    orders = csv.reader(f)
    # print(orders)
    result, head_1 = filter_orders_by_cost(orders, 20)

with open('../data/orders_2.csv', 'w', encoding='utf-8', newline='') as w:
    writer = csv.writer(w)
    writer.writerow(head_1)  # записываем заголовок
    writer.writerows(result)  # записываем отфильтрованные строки


# print(result)