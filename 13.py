with open('col1.txt') as f1, open('col2.txt') as f2, open('merged.txt', 'w') as out:
    for c1, c2 in zip(f1.readlines(), f2.readlines()):
        c1 = c1.rstrip('\n')
        out.write('{}\t{}'.format(c1, c2))
