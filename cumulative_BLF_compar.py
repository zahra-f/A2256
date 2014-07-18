#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt




dtypes = [
    ('name_radio', 'S4'),
    ('name_opt_NED','S10'),
    ('ra_radio','float'),
    ('dec_radio','float'),
    ('area_observed','float'),
    ('area_detectable','float'),
    ('flux','float'),
    ('loglum','float'),
    ('loglum_deteable','float'),
    ('num_op','int'),
    ('num_opt_couldDect','int'),
    ('ra_opt_NED','float'),
    ('dec_opt_NED','float'),
    ('redshift','float'),
    ('mag_NED','S10'),
    ('objid_SDSS','int'),
    ('ra_opt_SDSS','float'),
    ('dec_opt_SDSS','float'),
    ('mag_u','float'),
    ('mag_g','float'),
    ('mag_r','float'),
    ('mag_i','float'),
    ('mag_z','float'),
    ('note','S40')]
    

table = np.genfromtxt('table_May30.txt',delimiter=",",dtype=dtypes,
  usecols=(0,1,2,3,4,5,6,7,8,9,10,11,
            12,13,14,15,16,17,18,19,20,21,22,23))

#print table[:,np.array([0,1,2,3])]


#with open('table_May30.txt','r') as table:
#    lines = [tuple(line.split(",")) for line in table]



	
def toRadian(degree):
  return degree * np.pi/180.0

##### finding optical distances

z=0.058
dMpc=z*299792.458/70.
dpc=dMpc*10.**6
#print dpc
dm=dMpc*3.085677581e+22
Area=dm**2.*4.*np.pi


RaNED_rad=toRadian(table["ra_opt_NED"])
DecNED_rad=toRadian(table["dec_opt_NED"])

ra_cent=255.93146*np.pi/180.0
dec_cent=78.66662*np.pi/180.0
dis=[(np.arccos(np.sin(d)*np.sin(dec_cent)+np.cos(d)*np.cos(dec_cent)*
      np.cos(ra_cent-r)))*dMpc for r,d in zip(RaNED_rad,DecNED_rad)]


Area_observed_Ned=np.array([(i**2*np.pi) for i in dis])



#####



z=0.058
dMpc=z*299792.458/70.
dpc=dMpc*10.**6
#print dpc


names = ('mag_r', 'area_detectable','Area_observed', 'loglum', 'ra_opt_NED','dec_opt_NED')
i = (table['mag_r'] != 1000000) & (table['mag_r'] != -9999)
subtable = table[i]


###### finding absulute magnitudes ##############

mag_r_abs=np.array([m-5.*(np.log10(dpc)-1.) for m in subtable['mag_r']])


#####  sorting#####
i=mag_r_abs.argsort()

mag_r_abs=mag_r_abs[i]
subtable=subtable[i]
Area_observed_Ned=Area_observed_Ned[i]
########

############ 1 #############


print "######## 1 ##########"

k=(-23.40<mag_r_abs) & (mag_r_abs<=-21.60)  
mag_r_abs_1=mag_r_abs[k]
subtable_1=subtable[k]
Area_observed_Ned_1=Area_observed_Ned[k]



t=subtable_1['loglum'].argsort()[::-1]
## sorted and reversed
mag_r_abs_1=mag_r_abs_1[t]
subtable_1=subtable_1[t]
Area_observed_Ned_1=Area_observed_Ned_1[t]

print "############ sub I #############"


a=(-23.40<mag_r_abs_1) & (mag_r_abs_1<=-22.70)
mag_r_abs_1_1=mag_r_abs_1[a]
subtable_1_1=subtable_1[a]
Area_observed_Ned_1_1=Area_observed_Ned_1[a]



total_rate_1=[]
for i in range(len(subtable_1_1['area_detectable'])):
  count_opt=0.
  radio_opt=0.
  if subtable_1_1['area_detectable'][i]!=1000000:
    for e in Area_observed_Ned_1_1:
      if e<=subtable_1_1['area_detectable'][i]:
        count_opt+=1
    radio_opt=1/count_opt
    total_rate_1.append(radio_opt)


total_1=[]
summ=0
for e in total_rate_1:
  summ+=e
  total_1.append(summ)

print total_rate_1

logtot_1=[np.log10(e) for e in total_1]

print "number of radio galaxies in range I of optical magnitude is: ", len(logtot_1)

loglum_1=[e for e in subtable_1_1['loglum'] if e!=1000000]

p1=plt.plot(loglum_1,logtot_1,'r',marker='o',linestyle='--',label='A2256')
####### infors from Ledlow & owen 96 ########

total_rate_owen_1=[2./274.,5./274.,16./274.,11./274.,6./274.,12./274.,5./173.,5./41.,1./7.]
loglum_owen_1=[25.43,25.03,24.63,24.23,23.83,23.43,23.03,22.63,22.23]

total_ow_1=[]
summm=0
for e in total_rate_owen_1:
  summm+=e
  total_ow_1.append(summm)

logtot_ow_1=[np.log10(e) for e in total_ow_1]

p2=plt.plot(loglum_owen_1,logtot_ow_1,'b',marker='o',linestyle='--',label='Ledlow & Owen - 96')

#########################################

plt.xlabel('logL(W/Hz)')
plt.ylabel('log(Fraction of Galaxies)')
plt.legend([p1,p2], ['A2256','Ledlow & Owen - 96'])
plt.text(24.0,-0.3, '-23.40 < Mr < -22.70', ha='left')
plt.show()



print "############# sub II ############"

a=(-22.70<mag_r_abs_1) & (mag_r_abs_1<=-22.00)
mag_r_abs_1_2=mag_r_abs_1[a]
subtable_1_2=subtable_1[a]
Area_observed_Ned_1_2=Area_observed_Ned_1[a]



total_rate_2=[]
for i in range(len(subtable_1_2['area_detectable'])):
  count_opt=0.
  radio_opt=0.
  if subtable_1_2['area_detectable'][i]!=1000000:
    for e in Area_observed_Ned_1_2:
      if e<=subtable_1_2['area_detectable'][i]:
        count_opt+=1
    radio_opt=1/count_opt
    total_rate_2.append(radio_opt)


total_2=[]
summ=0
for e in total_rate_2:
  summ+=e
  total_2.append(summ)

print total_rate_2

logtot_2=[np.log10(e) for e in total_2]

print "number of radio galaxies in range I of optical magnitude is: ", len(logtot_1)

loglum_2=[e for e in subtable_1_2['loglum'] if e!=1000000]

p11=plt.plot(loglum_2,logtot_2,'r',marker='o',linestyle='--',label='A2256')

####### infors from Ledlow & owen 96 ########

total_rate_owen_2=[0,2./523.,8./523.,14./523.,14./523.,12./523.,9./331.,1./79.,0]
loglum_owen_2=[25.43,25.03,24.63,24.23,23.83,23.43,23.03,22.63,22.23]

total_ow_2=[]
summm=0
for e in total_rate_owen_2:
  summm+=e
  total_ow_2.append(summm)

logtot_ow_2=[np.log10(e) for e in total_ow_2]

p22=plt.plot(loglum_owen_2,logtot_ow_2,'b',marker='o',linestyle='--',label='Ledlow & Owen - 96')

#########################################


plt.xlabel('logL(W/Hz)')
plt.ylabel('log(Fraction of Galaxies)')
plt.legend([p11,p22], ['A2256','Ledlow & Owen - 96'])
plt.text(24.0,-0.3, '-22.70 < Mr < -22.00', ha='left')
plt.show()

print "################ sub III ############"

a=(-22.00<mag_r_abs_1) & (mag_r_abs_1<=-21.23)
mag_r_abs_1_3=mag_r_abs_1[a]
subtable_1_3=subtable_1[a]
Area_observed_Ned_1_3=Area_observed_Ned_1[a]



total_rate_3=[]
for i in range(len(subtable_1_3['area_detectable'])):
  count_opt=0.
  radio_opt=0.
  if subtable_1_3['area_detectable'][i]!=1000000:
    for e in Area_observed_Ned_1_3:
      if e<=subtable_1_3['area_detectable'][i]:
        count_opt+=1
    radio_opt=1/count_opt
    total_rate_3.append(radio_opt)


total_3=[]
summ=0
for e in total_rate_3:
  summ+=e
  total_3.append(summ)

print total_rate_3

logtot_3=[np.log10(e) for e in total_3]

print "number of radio galaxies in range I of optical magnitude is: ", len(logtot_1)

loglum_3=[e for e in subtable_1_3['loglum'] if e!=1000000]

p111=plt.plot(loglum_3,logtot_3,'r',marker='o',linestyle='--',label='A2256')

####### infors from Ledlow & owen 96 ########

total_rate_owen_3=[0.,0.,3./686.,4./686.,6./686.,11./686.,8./434.,1./104.,1./18.]
loglum_owen_3=[25.43,25.03,24.63,24.23,23.83,23.43,23.03,22.63,22.23]

total_ow_3=[]
summm=0
for e in total_rate_owen_3:
  summm+=e
  total_ow_3.append(summm)

logtot_ow_3=[np.log10(e) for e in total_ow_3]

p222=plt.plot(loglum_owen_3,logtot_ow_3,'b',marker='o',linestyle='--',label='Ledlow & Owen - 96')

#########################################


plt.xlabel('logL(W/Hz)')
plt.ylabel('log(Fraction of Galaxies)')
plt.legend([p111,p222], ['A2256','Ledlow & Owen - 96'])
plt.text(23.5,-0.3, '-22.00 < Mr < -21.23', ha='left')
plt.show()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            