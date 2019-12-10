#!/usr/bin/python3
'''
Script opens 10 files in 'data' folder.
Then count's G/C percentage for every file.
'''
import os

__author__ = 'Milosz Chodkowski PUT'
__field__ = 'Bioinformatics'
__version__ = 1.0


class GeneFiles:
    def __init__(self, files_count=10, folder='data'):
        self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.percents, self.names = [], []
        self.valid_bases = {'a', 't', 'c', 'g', 'u'}
        self.file_names = ['{}/{}/seq{}.genbank.txt'.format(
            self.THIS_FOLDER, folder, i) for i in range(1, files_count + 1)]

    def getPercentage(self):
        for file_name in self.file_names:
            with open(file_name, 'r') as my_file:
                gc_bases, base_count = 0, 0
                self.names.append(my_file.readline().split()[1])
                oh = my_file.read().split('ORIGIN')[1]
                for base in oh:
                    if base in self.valid_bases:
                        base_count += 1
                        if base == 'g' or base == 'c':
                            gc_bases += 1
                self.percents.append(gc_bases / base_count)
            my_file.close()
        for name, percent in zip(self.names, self.percents):
            print('NAME:{} G/C PERCENTAGE: {:.2f} '.format(name, percent * 100))


if __name__ == '__main__':
    G = GeneFiles()
    G.getPercentage()
