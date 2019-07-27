from itertools import permutations
N = 8
sol = 0
cols = range(N)
for combo in permutations(cols):
    if N == len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1
        # print ('Sulution'+str(sol)+':'+str(combo)+'\n')
        print ('\n'.join('.  '*i+'Q  '+'.  '*(N-i-1)for i in combo))
        print ('>> ',sol,'\n\n')