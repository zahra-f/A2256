#! /usr/bin/env python
import pyfits
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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
#print(len(flux))


#finding the distance to cluster
z=0.058
dMpc=z*299792.458/70.
#dMpc=248.3995

#finding area:
rmsANDr=open('RmsFluxwR.txt', 'r')
imgr=[]
fiverms=[]
for n in rmsANDr:
  n=n.split(",")
  imgr.append(np.float(n[0]))
  fiverms.append(np.float(n[1]))
rmsANDr.close()

fiverms=np.array(fiverms)
imgr=np.array(imgr)

# get rid of far values in plot to fit better
fiverms=np.delete(fiverms,6)
imgr=np.delete(imgr,6)

fiverms=np.delete(fiverms,13)
imgr=np.delete(imgr,13)

fiverms=np.delete(fiverms,16)
imgr=np.delete(imgr,16)



imgr=[r*8.333333333333*10**(-05)*np.pi/180.*dMpc for r in imgr] #pixsize_image=8.333333333333E-05 



# change flux to Jy and find the radiuse which the source van be detacted
fluxJy=[]
fluxJy=[(f*1.0e-6) for f in flux]
fluxJy=np.array(fluxJy)



#closestR = []
#for f in fluxJy:
#  diff = np.abs(f - fiverms)
#  closestR.append(imgr[np.argmin(diff)])
Image_size=0.416667 #degree
image_radi= Image_size*(np.pi/180.)*dMpc

#print np.min(fiverms)
#print fluxJy.min()

intrpolt=interp1d(fiverms,imgr, bounds_error=False)
rDetect=intrpolt(fluxJy)
rDetect[fluxJy>=fiverms.max()]=image_radi
rDetect[np.isnan(rDetect)] = 0


# 5rms vs r function f= 5.51*10**(-19)*x**4-2.92*10**(-15)*x**3+7.22*10**(-12)*x**2-6.42*10**(-9)*x+2.22*10**(-5)

Area_detectable=np.array([(i**2.*np.pi) for i in rDetect])

# change flux to Jy and find the radiuse which the source van be detacted



# Finding luminosity
dm=dMpc*3.085677581e+22
Area=dm**2.*4.*np.pi
#print(Area)


  

# to compare with coma we have to omit sources in area bigget than 0.9 deg or 1/A=0.39297

ra_cent=255.93146*0.017
dec_cent=78.66662*0.017
ra_rad=[c*0.017 for c in ra]
dec_rad=[c*0.017 for c in dec]

dis=np.zeros(len(ra_rad))
Area_d=np.zeros(len(ra_rad))
for i in range(len(ra_rad)-1):
  dis[i]=(np.arccos(np.sin(dec_rad[i])*np.sin(dec_cent)+np.cos(dec_rad[i])*np.cos(dec_cent)*np.cos(ra_rad[i]-ra_cent)))*dMpc
  Area_d[i]=np.pi*dis[i]**2


f_SI=[]
F_SI= [(f*1e-26) for f in fluxJy]

lum=[(f*Area) for f in F_SI]
log_lum=[np.log10(l) for l in lum]


Area_d,log_lum,Area_detectable=zip(*[(x,y,z) for x,y,z in zip(Area_d,log_lum,Area_detectable) if z!=0.0])
inv_Area=[(1/a) for a in Area_detectable]

#for i in range(len(log_lum)):
#  print '%f    %f    %f' % (log_lum[i],inv_Area[i],num[i])
  



#print len(inv_Area), len(log_lum) 

log_lum,inv_Area, Area_d= zip(*sorted(zip(log_lum,inv_Area,Area_d),key=lambda x:x[0]))

log_lum = list(log_lum)
log_lum.reverse()
inv_Area = list(inv_Area)
inv_Area.reverse()
Area_d= list(Area_d)
Area_d.reverse()

#print log_lum
#print inv_Area

  

  
  
##### Comapre to coma###########

comainfo=open('comainfo.txt','r')
log_lum_coma= []
inv_Area_coma=[]

for line in comainfo:
  line = line.split(',')
  log_lum_coma.append(np.float(line[0]))
  inv_Area_coma.append(np.float(line[1]))
  
bin=np.array([20.3,20.9,21.5,22.1,22.7,23.3,23.9])
countperea_coma=np.array([4.3,4.8,4.5,1.1,0.8,0.4,0.4])

errM=np.array([1.55,1.1,1.1,0.75,0.67,0.4,0.4])
errM2=np.array(errM)
errM2[errM>=countperea_coma] = countperea_coma[errM>=countperea_coma]*.9999999




####################

log_lum_a2256=[]
log_lum_a2256=[c for c in log_lum if c>20.00]
#print(len(log_lum_a2256))

for i in range(len(log_lum)):
  print '%f    %f    %f    %f' % (ra[i],dec[i],log_lum[i],inv_Area[i])

log_lum_a2256,inv_Area,Area_d=zip(*[(x,y,z) for x,y,z in zip(log_lum_a2256,inv_Area,Area_d) if z<=2.54469])
for i in log_lum_a2256:
  print i
print len(log_lum_a2256)

inv_A_comafor2256=[]
while(len(inv_A_comafor2256)<len(log_lum_a2256)):
  inv_A_comafor2256.append(0.392975)

  
lum_a22561,A_comafor22561=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if  20.0<=x<=20.6])
num_22561=len(A_comafor22561)
inv_A_comafor22561=0
for a in A_comafor22561:
  inv_A_comafor22561+=a
  
lum_a22562,A_comafor22562=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if  20.6<x<=21.2])
num_22562=len(A_comafor22562)
inv_A_comafor22562=0
for a in A_comafor22562:
  inv_A_comafor22562+= a
  
lum_a22563,A_comafor22563=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if  21.2<x<=21.8])
num_22563=len(A_comafor22563)
inv_A_comafor22563=0
for a in A_comafor22563:
  inv_A_comafor22563+= a
  
lum_a22564,A_comafor22564=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if  21.8<x<=22.4])
num_22564=len(A_comafor22564)
inv_A_comafor22564=0
for a in A_comafor22564:
  inv_A_comafor22564+= a
  
lum_a22565,A_comafor22565=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if  22.4<x<=23.0])
num_22565=len(A_comafor22565)
inv_A_comafor22565=0
for a in A_comafor22565:
  inv_A_comafor22565+= a
  
lum_a22566,A_comafor22566=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if  23.0<x<=23.6])
num_22566=len(A_comafor22566)
inv_A_comafor22566=0
for a in A_comafor22566:
  inv_A_comafor22566+= a 
                                                                                        
lum_a22567,A_comafor22567=zip(*[(x,y) for x,y in zip(log_lum_a2256,inv_A_comafor2256) if 23.6<x<=24.2])
num_22567=len(A_comafor22567)

inv_A_comafor22567=0
for a in A_comafor22567:
  inv_A_comafor22567+= a

countperea_a2256=[inv_A_comafor22561,inv_A_comafor22562,  inv_A_comafor22563, inv_A_comafor22564, inv_A_comafor22565, inv_A_comafor22566,inv_A_comafor22567]

countperea_a2256=np.array(countperea_a2256)


num_2256=[num_22561,num_22562,num_22563,num_22564,num_22565,num_22566,num_22567]


print num_2256
print countperea_a2256
print bin
print "7",A_comafor22567
print "6",A_comafor22566
print "5",A_comafor22565
print "4",A_comafor22564
print "3",A_comafor22563
print "2",A_comafor22562
print "1",A_comafor22561


Err_2256=np.zeros(len(countperea_a2256))
for i in range(len(countperea_a2256)):
  Err_2256[i]=np.sqrt(countperea_a2256[i]**2/(num_2256[i]+1))
  
  

Err_2256I=np.array(Err_2256)
Err_2256I[Err_2256>=countperea_a2256] = countperea_a2256[Err_2256>=countperea_a2256]*.9999999 

p= plt.plot(bin,countperea_a2256,marker='o',linestyle='--', color='r', label='')
perr=plt.errorbar(bin,countperea_a2256,yerr=[Err_2256I,Err_2256],color='r')

pc= plt.plot(bin,countperea_coma,marker='o',linestyle='--', color='b', label='Coma(Miller et al)')
pcerr=plt.errorbar(bin,countperea_coma,yerr=[errM2,errM],color='b')

plt.legend([pc,p], ['Coma(Miller et al)','A2256'])
plt.text(20.7, 33, 'Only for galaxies with in r=0.9 Mpc', ha='left')

plt.xlabel('logL(W/Hz)')
plt.ylabel('cum counts/Area (Mpc-2)')
plt.show()

exit()
