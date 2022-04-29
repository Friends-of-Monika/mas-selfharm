#!/bin/python
import os
import tokenize

for file in (file for file in next(os.walk('.'))[2] if file.endswith('.rpy')):
    print('File {0}:'.format(file))
    
    with open(file, 'rb') as f:
        for token in (token for token in tokenize.tokenize(f.readline) if token.type == tokenize.STRING):
            print('\tLine {0}: {1}'.format(token[2][0], token[1]))

    print()
