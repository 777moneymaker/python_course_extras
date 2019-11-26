#!/usr/bin/python3
# zad 20
file_names = ['data/seq{}.genbank.txt'.format(i) for i in range(1, 11)]
for file_name in file_names:
    with open(file_name, 'r') as fh:
        print(fh.readline().split()[1])
    fh.close()

# zad 21
percents, names = [], []
valid_bases = {'a', 't', 'c', 'g'}
file_names = ['data/seq{}.genbank.txt'.format(i) for i in range(1, 11)]
for file_name in file_names:
    with open(file_name, 'r') as fh:
        names.append(fh.readline().split()[1])

for file_name in file_names:
    gc_bases, base_count = 0, 0
    with open(file_name, 'r') as fh:
        f = fh.read().split('ORIGIN')[1]
        for base in f:
            if base in valid_bases:
                base_count += 1
                if base == 'g' or base == 'c':
                    gc_bases += 1
        percents.append(gc_bases/base_count)
for name, percent in zip(names, percents):
    print('NAME:{} G-C PERCENTAGE: {:.2f} '.format(name, percent*100))