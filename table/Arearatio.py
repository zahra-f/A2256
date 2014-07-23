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
num_opt_fromtable=[]
for line in info:
  line = line.split(',')
  num.append(np.int(line[0]))
  ra.append(np.float(line[1]))
  dec.append(np.float(line[2]))
  flux.append(np.float(line[3]))
  num_opt_fromtable.append(np.int(line[4]))
  
info.close()
#flux is in microJy
r=[]
fluxJy=[(f*1.0e-6) for f in flux]
fluxJy=np.array(fluxJy)
#print(len(flux))

z=0.058
dMpc=z*299792.458/70.
dm=dMpc*3.085677581e+22
Area=dm**2.*4.*np.pi
#dMpc=248.3995

#### equation of flux Vs distance from center F=5.51*e-19*r^4-2.92*e(-15)*r^3+7.22*e(-12)*r^2-6.42*e-9*r+2.22*e-5

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




#closestR = []
#for f in fluxJy:
#  diff = np.abs(f - fiverms)
#  closestR.append(imgr[np.argmin(diff)])
Image_size=0.416667 #degree
image_radi= Image_size*(np.pi/180.)*dMpc


intrpolt=interp1d(fiverms,imgr, bounds_error=False)
rDetect=intrpolt(fluxJy)
rDetect[fluxJy>=fiverms.max()]=image_radi
rDetect[np.isnan(rDetect)] = 0



#rDetect=[r for r in rDetect if r>0.0]
Area_detectable=np.array([(i**2.*np.pi) for i in rDetect])



#print(len(Area_detectable))


# to compare with coma we have to omit sources in area bigget than 0.9 deg or 1/A=0.39297

ra_cent=255.93146*np.pi/180.
dec_cent=78.66662*np.pi/180.
ra_rad=[c*np.pi/180. for c in ra]
dec_rad=[c*np.pi/180. for c in dec]

dis=np.zeros(len(ra_rad))
Area_d=np.zeros(len(ra_rad))
for i in range(len(ra_rad)):
  dis[i]=(np.arccos(np.sin(dec_rad[i])*np.sin(dec_cent)+np.cos(dec_rad[i])*np.cos(dec_cent)*np.cos(ra_rad[i]-ra_cent)))*dMpc
  Area_d[i]=np.pi*dis[i]**2
  
ra,dec,Area_d,Area_detectable,flux,dis,num_opt_fromtable=zip(*[(a,b,c,d,e,f,g) for a,b,c,d,e,f,g in zip(ra,dec,Area_d,
  Area_detectable,flux,dis,num_opt_fromtable) if d!=0.000000])


fluxJy=[(f*1.0e-6) for f in flux]

F_SI= [(f*1e-26) for f in fluxJy]

lum=[(f*Area) for f in F_SI]
log_lum=[np.log10(l) for l in lum]

###flux could been detected

dis_pix=[d/(dMpc*8.333333333333*10**(-05)*np.pi/180) for d in dis]

flux_couldObs=[5.51*10**(-19)*r**4-2.92*10**(-15)*r**3+7.22*10**(-12)*r**2-6.42*10**(-9)*r+2.22*10**(-5) for r in dis_pix]

#intrpolt=interp1d(imgr,fiverms, bounds_error=False)
#flux_couldObs=intrpolt(dis_pix)

Fcould_SI= [(f*1e-26) for f in flux_couldObs]

lum_could=[(f*Area) for f in Fcould_SI]
log_lum_could=[np.log10(l) for l in lum_could]





'''
out_info_radio=open("out_radio.txt","w")
for i in range(len(log_lum)):
  data_list=(ra[i],dec[i],Area_d[i],Area_detectable[i],flux[i],log_lum[i],log_lum_could[i],num_opt_fromtable[i])
  out_info_radio.write("%s\n" % (',\t'.join(s) for s in data_list))

out_info_radio.close()
'''
  
optical=open('opt_positions_degree.txt','r')
ra_opt=[]
dec_opt= []
for line in optical:
  line = line.split(',')
  ra_opt.append(np.float(line[0]))
  dec_opt.append(np.float(line[1]))
  
ra_rad_opt=[c*np.pi/180. for c in ra_opt]
dec_rad_opt=[c*np.pi/180. for c in dec_opt]

dis_opt=np.zeros(len(ra_rad_opt))
Area_d_opt=np.zeros(len(ra_rad_opt))
for i in range(len(ra_rad_opt)):
  dis_opt[i]=(np.arccos(np.sin(dec_rad_opt[i])*np.sin(dec_cent)+np.cos(dec_rad_opt[i])*np.cos(dec_cent)*np.cos(ra_rad_opt[i]-ra_cent)))*dMpc
  Area_d_opt[i]=np.pi*dis_opt[i]**2 
  
nums_opt=np.zeros(len(Area_d))
for i in range(len(Area_d)):
  a=0
  for o in Area_d_opt:
    if o<=Area_d[i]:
      a+=1
  nums_opt[i]=a


  

# finiding the number of optical in area coulh have been detcted 
nums_opt_cdet=np.zeros(len(Area_detectable))
for i in range(len(Area_detectable)):
  a=0
  for o in Area_d_opt:
    if o<=Area_detectable[i]:
      a+=1
  nums_opt_cdet[i]=a
      


for i in range(len(log_lum)):
  print '%f    %f    %f    %f    %f    %f    %f    %f    %f' % (ra[i],dec[i],flux[i],log_lum[i],Area_d[i],Area_detectable[i],
    log_lum_could[i],nums_opt[i], nums_opt_cdet[i])


''' 
print len(Area_detectable), len(Area_d)

for i in range(len(nums_opt)):
  print nums_opt[i],nums_opt_cdet[i]



AreaRatio=[x/y for x,y in zip(nums_opt,nums_opt_cdet)]

for i in range(len(AreaRatio)):
  if AreaRatio[i]>=1.0:
    print '%f    %f    %f    %f    %f' % (i, Area_d[i],Area_detectable[i],ra[i],dec[i])
  else:
    print "None"


AreaRatio,dis = zip(*sorted(zip(AreaRatio,dis),key=lambda x:x[0]))  


pc= plt.plot(dis,AreaRatio,marker='o', color='b', label='')

plt.xlabel('R(Mpc)')
plt.ylabel('(Area Observed)/(Area detectable)')
plt.show()
'''

log_lum_could,log_lum= zip(*sorted(zip(log_lum_could,log_lum),key=lambda x:x[0]))

pc= plt.plot(dis,log_lum,marker='o', color='b', 'ro')
pc2=plt.plot(dis,log_lum_could,marker='*',color='red', 'ro')

plt.xlabel('R(Mpc)')
plt.ylabel('log(Lum(W/Hz))')
plt.show()

  