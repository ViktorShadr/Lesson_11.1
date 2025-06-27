import re


def filter_txt_file(txt_file):
    list_txt = re.split(r'[\n#\s]', txt_file)
    list_clean_symbols = list(filter(lambda x: x.lstrip('-').isdigit(), list_txt))

    return [int(x) if int(x) >= 0 else 0 for x in list_clean_symbols]


with open('../data/nums.txt', 'r', encoding='utf-8') as file:
    sum_list = float(sum(filter_txt_file(file.read())))
    print(f'the sum is {sum_list}')
