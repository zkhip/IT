import os
import random
from math import log2

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
artefacts_dir = os.path.abspath(os.path.join(script_dir, '../', 'artefacts'))


def generate_file(alphabet, filename, count) -> None:
    weights = list(alphabet.values())
    letters = list(alphabet.keys())
    with open(filename, 'w') as file:
        for i in range(count):
            file.write(''.join(random.choices(letters, weights)))


def shannon_entropy(frequency):
    return -sum(p * log2(p) for p in frequency.values())


def entropy_calculation(filename, unit_len):
    with open(filename, 'r') as file:
        data = file.read()
    units = [data[i: i + unit_len] for i in range(0, len(data), unit_len)]
    # print(units)
    symbol_count = dict()
    for el in units:
        if el in symbol_count:
            symbol_count.update({el: symbol_count.get(el) + unit_len})
        else:
            symbol_count.update({el: 1})
    frec = {key: value / len(data) for key, value in symbol_count.items()}
    # print(f'Probabilities: {sorted(frec.items())}')
    # print(f'Check: {sum(frec.values())}')
    print(f'Shannon entropy with {unit_len} symbol in unit: {shannon_entropy(frec) / unit_len}')


def entropy(alphabet, filename, count) -> None:
    print(f'Alphabet: {alphabet}')
    generate_file(alphabet, filename, count)
    for i in range(1, 4):
        entropy_calculation(filename, i)
    print()


def main() -> int:
    equal = {'q': 0.2, 'w': 0.2, 'e': 0.2, 'r': 0.2, 't': 0.2}
    diff = {'q': 0.1, 'w': 0.3, 'e': 0.2, 'r': 0.1, 't': 0.3}
    entropy(equal, os.path.join(artefacts_dir, 'equals.txt'), 12400)
    entropy(diff, os.path.join(artefacts_dir, 'diffs.txt'), 12400)
    return 0


if __name__ == '__main__':
    main()
