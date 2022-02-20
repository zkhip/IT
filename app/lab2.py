import re
import os
import lab1

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
src_dir = os.path.abspath(os.path.join(script_dir, '../', 'src'))


def preprocess_file(filename):
    with open(filename, 'r') as f:
        whole_file = f.read().lower().replace('\n', ' ')
        whole_file = re.sub(r'[^a-zA-Z\s]', ' ', whole_file)
    return re.sub(r'\s{2,}', ' ', whole_file)


def calc_entropy(data, unit_len):
    units = [data[i: i + unit_len] for i in range(0, len(data), unit_len)]
    # print(units)
    symbol_count = dict()
    for el in units:
        if el in symbol_count:
            symbol_count.update({el: symbol_count.get(el) + unit_len})
        else:
            symbol_count.update({el: 1})

    frec = {key: float(value) / len(data) for key, value in symbol_count.items()}
    # print(f'Probabilities: {sorted(frec.items())}')
    # print(f'Check: {sum(frec.values())}')
    print(f'Shannon entropy with {unit_len} symbol in unit: {lab1.shannon_entropy(frec) / unit_len}')


def count_alphabet_entropy(filename: str) -> None:
    prepared_string = preprocess_file(filename)
    # print(prepared_string)
    for i in range(1, 3):
        calc_entropy(prepared_string, i)


def main() -> int:
    count_alphabet_entropy(os.path.join(src_dir, 'text.txt'))
    return 0


if __name__ == '__main__':
    main()