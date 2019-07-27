import os
import json
import csv
def tsv_to_json (First, Second):
    A = []
    with open (Second, 'r') as tsv:
        firstline = tsv.readline()
        head = firstline.split()
        lines = tsv.readlines()
    for line in lines:
        values = [s.replace('\n', '') for s in line.split('\t')]
        D = dict(zip(head, values))
        A.append(D)
        B = json.dumps(A, indent=4)
        json_file = open (First,'w')
        json_file.write(B)
        json_file.close()
    return A   
print (tsv_to_json ())








