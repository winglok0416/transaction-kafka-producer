import json


def save_data_to_txt(data: [json]):
    with open('../data.txt', 'w') as f:
        for datum in data:
            f.writelines(datum)
            f.write("\n")