# Genera un entradas.txt para alf8.tpf
with open('entradas.txt', 'w') as f:
    for i in range(8760):
            if i == 0:
                    f.write('\t'.join(['G1',
                                       'G2',
                                       'G3',
                                       'G4',
                                       'G5',
                                       'G6',
                                       'G7']) + '\n')
            else:
                    f.write('\t'.join([str(i/10)]*7) + '\n')
