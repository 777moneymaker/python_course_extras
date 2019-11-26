#!/usr/bin/python3
'''
Script opens 10 files in 'data' folder, then count's G/C percentage for every file'
__author__ = Milosz Chodkowski PUT
__field__ = Bioinformatics
__version__ = 1.0
'''
class GeneFiles:
    def __init__(self, files_count=10, folder='data'):
        self.percents, self.names = [], []
        self.valid_bases = {'a', 't', 'c', 'g', 'u'}
        self.file_names = ['{}/seq{}.genbank.txt'.format(folder, i) for i in range(1, files_count + 1)] # build list of file names
    
    def getPercentage(self):    
        for file_name in self.file_names:
            with open(file_name, 'r') as fh:
                gc_bases, base_count = 0, 0
                self.names.append(fh.readline().split()[1])
                oh = fh.read().split('ORIGIN')[1]
                for base in oh:
                    if base in self.valid_bases:
                        base_count += 1
                        if base == 'g' or base == 'c':
                            gc_bases += 1
                self.percents.append(gc_bases/base_count)
            fh.close()
        for name, percent in zip(self.names, self.percents):
            print('NAME:{} G/C PERCENTAGE: {:.2f} '.format(name, percent*100))

