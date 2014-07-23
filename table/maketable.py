#! /usr/bin/env python
import pyfits
import numpy as np

###### raading optica NED data ########

infoNED=open("info_NED.txt","r")
numNED=[]
RaNED=[]        
DecNED=[]
zNED=[]
MagNED=[]
NoteNED=[]

##first line --> #,       Ra ,        Dec ,       redshift,       Mag/Qual Filter,   Note

for line in infoNED:
  line=line.strip().split(",")
  numNED.append(np.int(line[0]))
  RaNED.append(np.float(line[1]))
  DecNED.append(np.float(line[2]))
  zNED.append(np.float(line[3]))
  MagNED.append(str(line[4]))
  NoteNED.append(str(line[5]))
  
infoNED.close()

####### reading radio data #######

   ##Ra            Dec        log(Lum)  detactable area(Mpc^2)  Optical galaxies could have been detected

infoRadio=open("radio_info.txt","r")
RaRadio=[] 
DecRadio=[]
Area_obsr=[]
Area_detectable=[]
flux=[]
log_lum=[]
log_lum_could=[]
num_opt=[]
num_opt_couldDect=[]


for line in infoRadio:
  line=line.strip().split(",")
  RaRadio.append(np.float(line[0]))
  DecRadio.append(np.float(line[1]))
  flux.append(np.float(line[2]))
  log_lum.append(np.float(line[3]))
  Area_obsr.append(np.float(line[4]))
  Area_detectable.append(np.float(line[5]))
  log_lum_could.append(np.float(line[6]))
  num_opt.append(np.int(line[7]))
  num_opt_couldDect.append(np.int(line[8]))


infoRadio.close()

###### reading optical SDSS data########

####col0  objID ra  dec run rerun camcol  field type  modelMag_u  modelMag_g  modelMag_r  modelMag_i  modelMag_z

sdssinfo=open("SDSS_table_2.txt","r")
nameSDSS=[] 
objid=[]
RaSDSS=[]
DecSDSS=[]
Mag_u=[]
Mag_g=[]
Mag_r=[]
Mag_i=[]
Mag_z=[]



for line in sdssinfo:
  line=line.strip().split(',')
  nameSDSS.append(np.str(line[0]))
  objid.append(np.int(line[1]))
  RaSDSS.append(np.float(line[2]))
  DecSDSS.append(np.float(line[3]))
  Mag_u.append(np.float(line[9]))
  Mag_g.append(np.float(line[10]))
  Mag_r.append(np.float(line[11]))
  Mag_i.append(np.float(line[12]))
  Mag_z.append(np.float(line[13]))

sdssinfo.close()

#print "RR" ,RaRadio
#print "DR", DecRadio
#print "RO",RaNED
#print "DO",DecNED



def toRadian(degree):
  radian=[d*np.pi/180.0 for d in degree]
  return radian

def dist(raT,decT,ra,dec):
  dis=[np.arccos(np.sin(d)*np.sin(decT)+np.cos(d)*np.cos(decT)*np.cos(r-raT)) for r,d in zip(ra,dec)]
  disn=[d*3600.*180./np.pi for d in dis]
  return disn


#def find(dislist):
#    return np.where(dislist==min(dislist))

 

 ###### main ########
##### matching NED #####
RaRadio_rad=toRadian(RaRadio)
DecRadio_rad=toRadian(DecRadio)
RaNED_rad=toRadian(RaNED)
DecNED_rad=toRadian(DecNED)

    
alldist_N=[]
for i in range(len(RaRadio_rad)):
  raT=RaRadio_rad[i]
  decT=DecRadio_rad[i]
  alldist_N.append(dist(raT,decT,RaNED_rad,DecNED_rad))
mins_NED=[]
for e in alldist_N:
  e=np.array(e)
  e1=np.argmin(e)
  mins_NED.append(e1)


 ###### matching SDSS #######

RaSDSS_rad=toRadian(RaSDSS)
DecSDSS_rad=toRadian(DecSDSS)



nameNED=['B'+str(i+1) for i in range(len(RaNED))]


########################

RaRadio=[str(r) for r in RaRadio]
DecRadio=[str(d) for d in DecRadio]
Area_obsr=[str(l) for l in Area_obsr]
Area_detectable=[str(a) for a in Area_detectable]
flux=[str(f) for f in flux]
log_lum=[str(l) for l in log_lum]
log_lum_could=[str(l) for l in log_lum_could]
num_opt=[str(n) for n in num_opt]
num_opt_couldDect=[str(n) for n in num_opt_couldDect]

RaNED=[str(r) for r in RaNED]
DecNED=[str(d) for d in DecNED]
zNED=[str(z) for z in zNED]

nameSDSS=[str(r) for r in nameSDSS] 
objid=[str(r) for r in objid]
RaSDSS=[str(r) for r in RaSDSS]
DecSDSS=[str(r) for r in DecSDSS]
Mag_u=[str(r) for r in Mag_u]
Mag_g=[str(r) for r in Mag_g]
Mag_r=[str(r) for r in Mag_r]
Mag_i=[str(r) for r in Mag_i]
Mag_z=[str(r) for r in Mag_z]


NoteNED=[e.strip() for e in NoteNED]



'''
outtable=open("outtable_onlyopts.txt", "w")
#outtable.write('Radio Name(A),  Ra Radio,  Dec Radio,  Area observed,  Area detectable,'
#  '  flux(mJy),  log(lum),  log(lum) detectable,  num Opt,  num opt couldDect.  Opt Name(B),  RaOpt,  DecOpt,   z,   MagNED,   Note' +"\n")
for i in range(len(RaRadio)):
  outtable.write('A'+str(i+1)+',  '+',  '.join([RaRadio[i], DecRadio[i],Area_obsr[i],Area_detectable[i],
    flux[i],log_lum[i],log_lum_could[i],num_opt[i],num_opt_couldDect[i]])+',  '+ 'B'+str(i+1)+',  '+ ',  '.join([RaNED[mins_NED[i]],
     DecNED[mins_NED[i]],zNED[mins_NED[i]], MagNED[mins_NED[i]], NoteNED[mins_NED[i]]])+'\n')

outtable.close()
'''
#######
outopt=open('outtable_onlyopts.txt','w')
for i in range(len(RaRadio)):
  outopt.write('A'+str(i+1)+',  '+',  '.join([RaRadio[i], DecRadio[i],Area_obsr[i],Area_detectable[i],
    flux[i],log_lum[i],log_lum_could[i],num_opt[i],num_opt_couldDect[i]])+',  '+'B'+str(i+1)+',   '+',   '.join([RaNED[mins_NED[i]] , 
    DecNED[mins_NED[i]],zNED[mins_NED[i]], MagNED[mins_NED[i]], NoteNED[mins_NED[i]]])+'\n')
j=0
for i in range(len(RaNED)):
  if i not in mins_NED:
    j+=1
    outopt.write('-1000000,  -1000000,  -1000000,  -1000000,  -1000000,  '
    '100000,  -1000000,  -1000000,  -1000000,  -1000000'+',  '+'B'+str(j+len(RaRadio))+',  '+',  '.join([RaNED[i] , DecNED[i],zNED[i], MagNED[i], NoteNED[i]])+'\n')

outopt.close()
######

intable=open('outtable_onlyopts.txt','r')
RaNED_corr=[]
DecNED_corr=[]
zNED_corr=[]
MagNED_corr=[]
NoteNED_corr=[]

for line in intable:
  line=line.strip().split(',')
  RaNED_corr.append(np.str(line[11]))
  DecNED_corr.append(np.str(line[12]))
  zNED_corr.append(np.str(line[13]))
  MagNED_corr.append(np.str(line[14]))
  NoteNED_corr.append(np.str(line[15]))

intable.close()






outtable_con=open("outtable_continue.txt", "w")
#outtable_con.write('name Opt(NED),  RaNED,  DecNED,  zNED,  MagNED,  NoteNED,  name Opt(SDSS),  objID SDSS,'
#  '  Ra SDSS, Dec SDSS, Mag_u,  Mag_g,  Mag_r,  Mag_i,  Mag_z'+'\n')




j=0
for i in range(len(nameNED)):
  if nameNED[i] in nameSDSS:
    outtable_con.write(',  '.join([nameNED[i],RaNED_corr[i],DecNED_corr[i],zNED_corr[i],MagNED_corr[i],NoteNED_corr[i],nameSDSS[j],objid[j],
      RaSDSS[j],DecSDSS[j],Mag_u[j],Mag_g[j],Mag_r[j],Mag_i[j],Mag_u[j]])+'\n')
    j+=1
  else:
    outtable_con.write(',  '.join([nameNED[i],RaNED_corr[i],DecNED_corr[i],zNED_corr[i],MagNED_corr[i],NoteNED_corr[i]])+',  -1000000,  -1000000,  -1000000,'
      '  -1000000,  -1000000,  -1000000,  -1000000,  -1000000,  -1000000'+'\n')


outtable_con.close()
'''

#### optical doesn't have radio #####

allOpt=open("all_opt_radec.txt","w")
for i in range(len(RaRadio)):
  allOpt.write(',   '.join([RaNED[mins_NED[i]] , DecNED[mins_NED[i]] , zNED[mins_NED[i]] , MagNED[mins_NED[i]] , NoteNED[mins_NED[i]]])+'\n')
for i in range(len(RaNED)):
  if i not in mins_NED:
    allOpt.write(',   '.join([RaNED[i] , DecNED[i] , zNED[i] , MagNED[i] , NoteNED[i]])+'\n')

allOpt.close() 



outopt=open('OptPos.txt','w')
for i in range(len(RaRadio)):
  outopt.write('B'+str(i+1)+',   '+',   '.join([RaNED[mins_NED[i]] , DecNED[mins_NED[i]]])+'\n')
j=0
for i in range(len(RaNED)):
  if i not in mins_NED:
    j+=1
    outopt.write('B'+str(j+len(RaRadio))+',   '+',   '.join([RaNED[i] , DecNED[i]])+'\n')

outopt.close()



outradio=open('RadioPos.txt','w')
for i in range(len(RaRadio)):
  outradio.write('A'+str(i+1)+',   '+',   '.join([RaRadio[i], DecRadio[i]])+'\n')

outradio.close()

'''
