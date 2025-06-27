import re


def filter_txt_file(txt_file):
    list_txt = re.split(r'[\n#\s]', txt_file)
    list_clean_symbols = list(filter(lambda x: x.lstrip('-').isdigit(), list_txt))
    list_negative_number_by_zero = [int(x) if int(x) >= 0 else 0 for x in list_clean_symbols]



    # print(list_txt)
    # print(list_clean_symbols)
    # print(type(list_clean_symbols))
    # print(list_negative_number_by_zero)
    # # print(sum_list)

    return


with open('../data/nums.txt', 'r', encoding='utf-8') as file:
    filter_txt_file(file.read())
