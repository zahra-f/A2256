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

k=(-23.40<mag_r_abs) & (mag_r_abs<=-20.60)
mag_r_abs_1=mag_r_abs[k]
subtable_1=subtable[k]
Area_observed_Ned_1=Area_observed_Ned[k]




t=subtable_1['loglum'].argsort()[::-1]
## sorted and reversed
mag_r_abs_1=mag_r_abs_1[t]
subtable_1=subtable_1[t]
Area_observed_Ned_1=Area_observed_Ned_1[t]




total_rate_1=[]
for i in range(len(subtable_1['area_detectable'])):
  count_opt=0.
  radio_opt=0.
  if subtable_1['area_detectable'][i]!=1000000:
    for e in Area_observed_Ned_1:
      if e<=subtable_1['area_detectable'][i]:
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

loglum_1=[e for e in subtable_1['loglum'] if e!=1000000]

plt.plot(loglum_1,logtot_1,'r',marker='o',linestyle='--')
plt.xlabel('logL(W/Hz)')
plt.ylabel('log(Fraction of Galaxies)')
plt.text(22.5,-0.4, '-23.40 < Mr < -20.60', ha='left')
plt.show()


############ 2 #############
print "######## 2 ##########"


j=(-20.60<mag_r_abs) & (mag_r_abs<=-19.55)
mag_r_abs_2=mag_r_abs[j]
subtable_2=subtable[j]
Area_observed_Ned_2=Area_observed_Ned[j]

r=subtable_2['loglum'].argsort()[::-1]
mag_r_abs_2=mag_r_abs_2[r]
subtable_2=subtable_2[r]
Area_observed_Ned_2=Area_observed_Ned_2[r]


total_rate_2=[]
for i in range(len(subtable_2['area_detectable'])):
  count_opt=0.
  radio_opt=0.
  if subtable_2['area_detectable'][i]!=1000000:
    for e in Area_observed_Ned_2:
      if e<=subtable_2['area_detectable'][i]:
        count_opt+=1
    radio_opt=1/count_opt
    total_rate_2.append(radio_opt)

print total_rate_2

total_2=[]
summ=0
for e in total_rate_2:
  summ+=e
  total_2.append(summ)

logtot_2=[np.log10(e) for e in total_2]

print "number of radio galaxies in range II of optical magnitude is: ", len(logtot_2)

loglum_2=[e for e in subtable_2['loglum'] if e!=1000000]

plt.plot(loglum_2,logtot_2,'r',marker='o',linestyle='--')
plt.xlabel('logL(W/Hz)')
plt.ylabel('log(Fraction of Galaxies)')
plt.text(22.0, -0.8, '-20.60 < Mr < -19.55', ha='left')
plt.show()


############ 3 #############
print "######## 3 ##########"

h=(-19.55<mag_r_abs) & (mag_r_abs<=-12.10)
mag_r_abs_3=mag_r_abs[h]
subtable_3=subtable[h]
Area_observed_Ned_3=Area_observed_Ned[h]

g=subtable_3['loglum'].argsort()[::-1]
mag_r_abs_3=mag_r_abs_3[g]
subtable_3=subtable_3[g]
Area_observed_Ned_3=Area_observed_Ned_3[g]


total_rate_3=[]
for i in range(len(subtable_3['area_detectable'])):
  count_opt=0.
  radio_opt=0.
  if subtable_3['area_detectable'][i]!=1000000:
    for e in Area_observed_Ned_3:
      if e<=subtable_3['area_detectable'][i]:
        count_opt+=1
    radio_opt=1/count_opt
    total_rate_3.append(radio_opt)

total_3=[]
summ=0
for e in total_rate_3:
  summ+=e
  total_3.append(summ)

logtot_3=[np.log10(e) for e in total_3]

print "number of radio galaxies in range III of optical magnitude is: ", len(logtot_3)
    

print total_rate_3

loglum_3=[e for e in subtable_3['loglum'] if e!=1000000]

plt.plot(loglum_3,logtot_3, 'r',marker='o',linestyle='--')
plt.xlabel('logL(W/Hz)')
plt.ylabel('log(Fraction of Galaxies)')
plt.text(21.5, -0.8, '-19.55 < Mr < -12.10', ha='left')
plt.show()


print "######## end ##########"

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            