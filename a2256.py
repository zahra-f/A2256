#! /usr/bin/env python
#import pyfits
import numpy as np
import matplotlib.pyplot as plt

#####********58 has been deleted

info=open('info.txt','r')
num= []
ra=[]
dec= []
flux= []
for line in info:
  line = line.split(',')
  num.append(np.int(line[0]))
  ra.append(np.float(line[1]))
  dec.append(np.float(line[2]))
  flux.append(np.float(line[3]))
  
#flux is in microJy
r=[]
print(len(flux))


#finding the distance to cluster
z=0.058
dMpc=z*299792.458/70.
print(dMpc)
#dMpc=248.3995

#finding area:
 
#r(Mpc)=dMpc*r(radi)
#Areaimg(Mpc^2)=r(Mpc)**2*3.14159265359
#1/A
#  r[i]=1000/3 (1+np.sqrt(-29+1500000 *flux[i]))


# change flux to Jy and find the radiuse which the source van be detacted
r=[]
fluxJy=[]
#### List comprehension
fluxJy=[(f*1.0e-6) for f in flux]
r = [(1000./3.)*(1+np.sqrt(-29.+1500000. * f)) for f in fluxJy]

#for i in range(len(r)):
#  print '%f    %f' % (flux[i],r[i])

print(len(r))

##r is in pixels so need to change it to radi
#r_radi=[(0.00000145444104333*i) for i in r]
r_Mpc=[(i*0.299999999999988*248.3995/206264.8) for i in r]
#r_Mpc=[(i*dMpc) for i in r_radi]
Area_detectable=[(i**2.*np.pi) for i in r_Mpc]
#print(len(Area_detectable))


# Finding luminosity
dm=dMpc*3.085677581e+22
Area=dm**2.*4.*np.pi
#print(Area)

Image_size=0.416667
Area_image= (Image_size*0.0174532925*dMpc)**2.*np.pi

for idx, area in enumerate(Area_detectable):
  if area > Area_image:
    Area_detectable[idx]= Area_image
    
inv_Area=[(1/a) for a in Area_detectable]


f_SI=[]
F_SI= [(f*1e-26) for f in fluxJy]

lum=[(f*Area) for f in F_SI]
#print(lum)
log_lum=[np.log10(l) for l in lum]
#print(log_lum)


log_lum,inv_Area = zip(*sorted(zip(log_lum,inv_Area),key=lambda x:x[0]))
log_lum = list(log_lum)
log_lum.reverse()
inv_Area = list(inv_Area)
inv_Area.reverse()
print log_lum
print inv_Area


for i in range(len(log_lum)):
  print '%f    %f' % (log_lum[i],inv_Area[i])
  
A=np.zeros(len(inv_Area))

for i in range(len(inv_Area)):
  A[i] = np.sum(inv_Area[:i]) + inv_Area[i]
  
  
##### Comapre to coma###########

comainfo=open('comainfo.txt','r')
log_lum_coma= []
inv_Area_coma=[]

for line in comainfo:
  line = line.split(',')
  log_lum_coma.append(np.float(line[0]))
  inv_Area_coma.append(np.float(line[1]))

log_lum_a2256=[]
log_lum_a2256=[c for c in log_lum if c>20.6000]
print(log_lum_a2256)

  
  
p= plt.plot(log_lum,A,marker='o',linestyle='--', color='r', label='')

#pc= plt.plot(Lc,Ac,marker='o',linestyle='--', color='b', label='')

#plt.legend([pc,p], ['Coma(Miller et al)','A2256'])
plt.text(20.6, 18, 'Only for galaxies with in r=0.9 Mpc', ha='left')

plt.xlabel('logL(W/Hz)')
plt.ylabel('cum counts/Area (Mpc-2)')
plt.show()