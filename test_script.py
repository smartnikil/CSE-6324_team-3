from brownie.test import strategy as st
import numpy as np

#testing code
t_strat = st('int16[4][3]', unique=True)
print(t_strat)
i_tot = 100
out_list = []
for k in range(i_tot):
    cnt = 0
    tot = 100
    for i in range(tot):
        gen_ex = t_strat.example()
        a = np.array(gen_ex).size
        b = len(set(list(sum(gen_ex,()))))
        if a == b:
            cnt += 1
        else:
            print('Duplicate values found : {}'.format(gen_ex))
    if cnt/tot == 1.0:
        out_list.append(k)

print('Overall accuracy : {}'.format(len(out_list)/i_tot))
