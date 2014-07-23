#! /usr/bin/env python
import pyfits
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

infoNED=open("table_May30.txt","r")
numNED=[]
RaNED=[]        
DecNED=[]


for line in infoNED:
 	line=line.strip().split(",")
 	numNED.append(np.str(line[1]))
	RaNED.append(np.float(line[11]))
	DecNED.append(np.float(line[12]))


infoNED=open("radec_tomach.txt","r")
ra_hr=[]
ra_min=[]
ra_sec=[]
dec_d=[]
dec_arcmin=[]
dec_arcsec=[]


for line in infoNED:
 	line=line.strip().split(",")
 	ra_hr.append(np.float(line[0]))
 	ra_min.append(np.float(line[1]))
 	ra_sec.append(np.float(line[2]))
 	dec_d.append(np.float(line[3]))
 	dec_arcmin.append(np.float(line[4]))
 	dec_arcsec.append(np.float(line[5]))


ra_deg=[15.*(h+1./60.*m+1./3600.*s) for h,m,s in zip(ra_hr,ra_min,ra_sec)]
dec_deg=[d+1./60.*m+1./3600.*s for d,m,s in zip(dec_d,dec_arcmin,dec_arcsec)]

#for a,b in zip(ra_deg,dec_deg):
#	print a, ', ',b




def toRadian(degree):
	radian=[d*np.pi/180.0 for d in degree]
	return radian

def dist(raT,decT,ra,dec):
	dis=[np.arccos(np.sin(d)*np.sin(decT)+np.cos(d)*np.cos(decT)*np.cos(r-raT)) for r,d in zip(ra,dec)]
	dis_deg=[d*180./np.pi for d in dis]
	return dis_deg

RaNED_rad=toRadian(RaNED)
DecNED_rad=toRadian(DecNED)
Ra_rad=toRadian(ra_deg)
Dec_rad=toRadian(dec_deg)



alldist_N=[]
for i in range(len(Ra_rad)):
	raT=Ra_rad[i]
	decT=Dec_rad[i]
	alldist_N.append(dist(raT,decT,RaNED_rad,DecNED_rad))


mins_NED=[]
for e in alldist_N:
	e=np.array(e)
	e1=np.argmin(e)
	mins_NED.append(e1)


match=[]
i=0
for e in alldist_N:
	if e[mins_NED[i]]<0.015:
		match.append(e[mins_NED[i]])
	i+=1


for i in range(len(match)):
	print i


print "len ",len(match)
print len(ra_deg)







