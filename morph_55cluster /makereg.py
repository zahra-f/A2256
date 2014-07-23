#! /usr/bin/env python
import numpy as np

### Getting data from user#######

imgename=raw_input('Enter the name of the image: ')

filename=raw_input('Enter Ra&Dec file (Ra, Dec) format: ')

outputname=raw_input('Enter an outputname: ')

####### reading Ra and Dec form file #######

fileobj=open(filename,'r')
ra=[]
dec=[]

for line in fileobj:
  line=line.strip().split(',')
  ra.append(np.str(line[0]))
  dec.append(np.str(line[1]))

fileobj.close()

####### Making region file #######
 
output=open(outputname+'.reg','w')
output.write('# Region file format: DS9 version 4.1'+'\n')
output.write('# Filename: '+imgename+'\n')
output.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'+'\n')
output.write('fk5'+'\n')
for i in range(len(ra)):
  output.write('circle( '+ra[i]+','+dec[i]+' ,15")'+'    #color=red   text={'+str(i+1)+'}'+'\n')
  
output.close()