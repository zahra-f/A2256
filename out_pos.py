#! /usr/bin/env python
import numpy as np

fileobj=open('final_table.txt','r')
ra_r=[]
dec_r=[]

ra_o=[]
dec_o=[]

for line in fileobj:
  line=line.strip().split(',')
  ra_r.append(np.str(line[2]))
  dec_r.append(np.str(line[3]))
  ra_o.append(np.str(line[11]))
  dec_o.append(np.str(line[12]))
  
  
fileobj.close()

output_r=open('radio_2.txt','w')
for i in range(len(ra_r)):
  output_r.write(ra_r[i]+',   '+dec_r[i]+'\n')
output_r.close()


output_o=open('optical_2.txt','w')
for i in range(len(ra_o)):
  output_o.write(ra_o[i]+',   '+dec_o[i]+'\n')
output_o.close()