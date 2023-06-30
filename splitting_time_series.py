import re

config = {
    'fname': 'Book1.txt',
    'length': 200,
    'step': 50
}


def read_file_time_series(fname: str):
    data = []
    regexp = r'^[-+]?[0-9]*[.,]?[0-9]+(?:[eE][-+]?[0-9]+)?$'
    with open(fname) as file:
        for lines in file.readlines():
            match = re.search(regexp, lines)
            if match is not None:
                data.append(match[0])
    return data


def split_array(data, length: int, step: int):
    len_data = data.__len__()
    if length > len_data:
        print('Wrong size params - length')
        exit(0)

    res_series = [data[:length]]
    index_list = [x for x in range(length, len_data, step)]

    for index in range(1, index_list.__len__()):
        res_series.append(data[index_list[index] - length:
                               index_list[index]])

    return index_list, res_series


def splitting_time_series(config: dict):
    data = read_file_time_series(config['fname'])
    print('Read file - {}'.format(config['fname']))

    index_list, series = split_array(data,
                                     config['length'],
                                     config['step'])

    out_file_name = config['fname'].replace('.txt', '') \
                    + '_S{}_NL{}'.format(str(config['step']),
                                         str(config['length']))

    with open(out_file_name + '_index.txt', 'w') as file:
        file.write("\n".join(str(item) for item in index_list))
    print('Generation file - {}'.format(out_file_name + '_index.txt'))

    with open(out_file_name + '_series.txt', 'w') as file:
        s = ''
        for row in series:
            s += " ".join(map(str, row)) + '\n'
        file.write(s[:-1])
    print('Generation file - {}'.format(out_file_name + '_series.txt'))


def main():
    splitting_time_series(config=config)


if __name__ == '__main__':
    main()
