import numpy as np


#radio_table = np.genfromtxt('outtable_onlyopts.txt',names=['name_radio', 'ra_radio', 'dec_radio', 'Area_observed','area_detectable','flux','loglum',
#	'loglum_detectable','num_opt','opt_name','ra_opt_NED','dec_opt_NED','redshift','mag_NED','note'],autostrip=True,dtype=['a20','f8','f8','f8','f8','f8','f8','f8','i8','a20','f8','f8','f8','a20','a100'])


#print radio_table['name_radio']
#exit()



radio_table=open('outtable_onlyopts.txt', 'r')

name_radio=[]
ra_radio=[]  
dec_radio=[]
area_observed=[]
area_detectable= [] 
flux=[] 
loglum=[]  
loglum_deteable=[] 
num_opt=[]
num_opt_couldDect=[]




for line in radio_table:
	line=line.split(",")
	name_radio.append(np.str(line[0]))
	ra_radio.append(np.float(line[1]))
	dec_radio.append(np.float(line[2]))
	area_observed.append(np.float(line[3]))
	area_detectable.append(np.float(line[4]))
	flux.append(np.float(line[5]))
	loglum.append(np.float(line[6])) 
	loglum_deteable.append(np.float(line[7]))  
	num_opt.append(np.int(line[8]))
	num_opt_couldDect.append(np.int(line[9]))


radio_table.close()



opt_table=open('outtable_continue.txt','r')


name_opt_NED=[] 
ra_opt_NED=[]
dec_opt_NED=[]   
redshift=[]   
mag_NED=[]   
note=[]
name_opt_SDSS=[] 
objid_SDSS=[]
ra_opt_SDSS=[]
dec_opt_SDSS=[]
mag_u=[]
mag_g=[]
mag_r=[]
mag_i=[]
mag_z=[]

for line in opt_table:
	line=line.split(",")
	name_opt_NED.append(np.str(line[0]))  
	ra_opt_NED.append(np.float(line[1])) 
	dec_opt_NED.append(np.float(line[2]))  
	redshift.append(np.float(line[3]))  
	mag_NED.append(np.str(line[4]))   
	note.append(np.str(line[5]))
	name_opt_SDSS.append(np.str(line[6])) 
	objid_SDSS.append(np.int(line[7]))
	ra_opt_SDSS.append(np.float(line[8]))
	dec_opt_SDSS.append(np.float(line[9]))
	mag_u.append(np.float(line[10]))
	mag_g.append(np.float(line[11]))
	mag_r.append(np.float(line[12]))
	mag_i.append(np.float(line[13]))
	mag_z.append(np.float(line[14]))

opt_table.close()

u_r=[u-r for u,r in zip(mag_u,mag_r)]
color_morph=[]
for i in range(len(name_opt_NED)):
	if u_r[i]>=2.17:
		color_morph.append('A')
	elif u_r[i]<=1.35 and u_r[i]!=0.0:
		color_morph.append('S')
	else:
		color_morph.append('UN')


#for i in range(len(color_morph)):
#	print i, mag_u[i], mag_r[i], u_r[i], color_morph[i]


note[16]='opt & radi,not in the same position'
note[66]='opt & radi,not in the same position'
note[72]='opt & radi,not in the same position'
note[73]='opt & radi,not in the same position'
note[74]='In the relic, optical a little off'
note[63]='optical a little off'
note[60]='near the relic'

radi_morph=list(np.zeros(len(name_opt_NED)))
opt_morph=list(np.zeros(len(name_opt_NED)))





radi_morph[0]='comp / circle / 5"'
opt_morph[0]='comp / circle-E2 / 5"'
radi_morph[1]='ext / lenticular / 11.5"'
opt_morph[1]='comp / circle-E2 / 6"'
radi_morph[2]='jet'
opt_morph[2]='  '
radi_morph[3]='jet'
opt_morph[3]='  '
radi_morph[4]='jet'
opt_morph[4]='  '
radi_morph[5]='jet'
opt_morph[5]='  '
radi_morph[6]='ext / Iregular / 35"'
opt_morph[6]='ext / loop galaxy-SBa / 27"'
radi_morph[7]='jet'
opt_morph[7]='  '
radi_morph[8]='jet'
opt_morph[8]='  '
radi_morph[9]='!!'
opt_morph[9]='!!'
radi_morph[10]='ext / triple radio sources / 23"'
opt_morph[10]='comp / circle-E2'
radi_morph[11]='? ext / triple radio sources / 23"'
opt_morph[11]='? ext / tow bars / 27"'
radi_morph[12]='ext / triple radio sources /10"'
opt_morph[12]='comp / circle-E2 / 10"'
radi_morph[13]='? ext / Iregular / 17.6"'
opt_morph[13]='? ext / arms-SBc or SC / 24" '
radi_morph[14]='ext / Iregular / 27"'
opt_morph[14]='ext / spiral-SC / 29"'
radi_morph[15]='? ext / triple radio sources / 23"'
opt_morph[15]='? ext / arms-SBa / 30"'
radi_morph[16]='ext / triple radio sources / 9"'
opt_morph[16]='ext / lenticular-S0 or E6 / 30"'
radi_morph[17]='comp / circle / 6"'
opt_morph[17]='comp / lenticular-S0 / 9"'
radi_morph[18]='? ext / so noisy / 5.5"'
opt_morph[18]='? comp / circle-E2 / 11"'
radi_morph[19]='ext / two radio sources / 8"'
opt_morph[19]='ext / lenticular-E2 or S0 / 9"'
radi_morph[20]='ext / lenticular / 17"'
opt_morph[20]='ext / lenticular-disk-S0 / 22"'
radi_morph[21]='? ext / faint-circle / 3"'
opt_morph[21]='? ext / lenticular-disk-S0 / 16"'
radi_morph[22]='comp / circle / 6.5"'
opt_morph[22]='comp(big) / lenticular-S0 / 13.6"'
radi_morph[23]='? ext / elliptical- affected by neighber source / 17"'
opt_morph[23]='? ext / arms- Sa / 17"'
radi_morph[24]='? ext / two radio source / 10"'
opt_morph[24]='ext / lenticular-E6 / 12"'
radi_morph[25]='comp / circle-noisy /  7"'
opt_morph[25]='comp / circle-E2 / 11.5"'
radi_morph[26]='comp / circle / 9"'
opt_morph[26]='comp / small lenticular-E6 / 11.5"'
radi_morph[27]='comp / circle / 7"'
opt_morph[27]='comp / circle-E2 / 6"'
radi_morph[28]='comp / two radio sources-noisy / 8.5"'
opt_morph[28]='comp / a bit lenticular / 8"'
radi_morph[29]='comp / circle / 7.6"'
opt_morph[29]='ext / elliptical disk-Sa / 7"'
radi_morph[30]='ext / two radio sources'
opt_morph[30]='ext / elliptical-E6 / 6"'
radi_morph[31]='ext / two radio sources / 9.5"'
opt_morph[31]='comp / circle-E2 /5"'
radi_morph[32]='ext / tow radio sources / 8.5"'
opt_morph[32]='ext / circle-E2 / 5"'
radi_morph[33]='ext / circle center / 10"'
opt_morph[33]='ext / disk-lenticular-S0 / 14"'
radi_morph[34]='ext / two radio sources / 10"'
opt_morph[34]='ext / lenticular-E6 / 8"'
radi_morph[35]='? ext / Iregular / 12"'
opt_morph[35]='? ext / lenticular-S0 / 15"'
radi_morph[36]='ext / Iregular / 18"'
opt_morph[36]='ext / circle center / 10"'
radi_morph[37]='ext / circle center / 11"'
opt_morph[37]='ext / lenticular-E6 /7"'
radi_morph[38]='comp / circle / 8"'
opt_morph[38]='comp / a bit lenticular-E2 / 7"'
radi_morph[39]='ext / egg shape / 9.5"'
opt_morph[39]='ext / disk- lenticular-E2 / 12.7"'
radi_morph[40]='comp / egg shape / 9.5"'
opt_morph[40]='ext / lenticular-S0 / 16"'
radi_morph[41]='ext/ circle center / 11"'
opt_morph[41]='ext / lenticular -S0 /13"'
radi_morph[42]='? ext / circle center / 15.6"'
opt_morph[42]='? ext / lenticular-not symmetric /33"'
radi_morph[43]='? nise'
opt_morph[43]='? ext/ circle center-E2/ 7.3"'
radi_morph[44]='ext / Iregular- noisy / 6"'
opt_morph[44]='ext / disk shape-S0 / 11"'
radi_morph[45]='ext / circle center / 9.2"'
opt_morph[45]='ext / lenticular-Sa-S0 /13"'
radi_morph[46]='comp / circle / 7.6"'
opt_morph[46]='ext / egg shape- lenticular-S0 / 7"'
radi_morph[47]='ext / circle center / 8.5"'
opt_morph[47]='ext / elliptical-E6 / 10"'
radi_morph[48]='comp / circle-noisy / 13.5"'
opt_morph[48]='ext / lenticular-S0 / 10"'
radi_morph[49]='ext / Iregular / 10.5"'
opt_morph[49]='ext / lenticular-S0 / 15"'
radi_morph[50]='ext / two radio sources / 12.5"'
opt_morph[50]='ext / lenticular-S0 / 15"'
radi_morph[51]='comp / circle-noisy /8.6"'
opt_morph[51]='ext / lenticular-E6 / 15"'
radi_morph[52]='ext / noisy / 6.2"'
opt_morph[52]='ext / lenticular-E6 / 15"'
radi_morph[53]='ext / lenticular / 11.5"'
opt_morph[53]='ext / lenticular-S0 / 17"'
radi_morph[54]='comp / circle / 5.8"'
opt_morph[54]='ext / circle center-E2 / 9.7"'
radi_morph[55]='ext / Iregular- circle center / 17.3"'
opt_morph[55]='ext / lenticular-S0 /21"'
radi_morph[56]='ext / two radio sources / 11/3"'
opt_morph[56]='ext / lenticular-S0 / 22.6"'
radi_morph[57]='ext / Iregular / 14.4"'
opt_morph[57]='ext / lenticular-E6 / 11"'
radi_morph[58]='ext / lenticular / 14.3"'
opt_morph[58]='ext / lenticular-S0 / 12.5"'
radi_morph[59]='ext / Iregular / 7"'
opt_morph[59]='ext / lenticular-S0 / 12.5"'
radi_morph[60]='ext / Iregular / 8.3"'
opt_morph[60]='ext / lenticular-S0 / 9.8"'
radi_morph[61]='comp / circle / 6.4"'
opt_morph[61]='comp / circle / 3.2"'
radi_morph[62]='comp / circle / 3.7"'
opt_morph[62]='ext / circle center-E2 / 14.3"'
radi_morph[63]='comp/ circle / 5"'
opt_morph[63]='comp/ circle-E2 /10.7"'
radi_morph[64]='ext / Iregular / 22"'
opt_morph[64]='ext / spiral-SBa / 30.6"'
radi_morph[65]='ext / circle center / 8.8"'
opt_morph[65]='comp / circle / 4.3"'
radi_morph[66]='ext / egg shape/ 10.4"'
opt_morph[66]='ext / lenticular-S0/ 10"'
radi_morph[67]='? ext / bar shap- Iregular / 31"'
opt_morph[67]='? ext / look like edge on / 28"'
radi_morph[68]='ext / circle center / 7"'
opt_morph[68]='ext / lenticular-S0 /11"'
radi_morph[69]='comp /circle / 8.2"'
opt_morph[69]= 'ext / circle center-E2 / 8"'
radi_morph[70]='comp / circle /5"'
opt_morph[70]='ext / lenticular-S0 / 11"'
radi_morph[71]='ext / circle center-halo around / 17"'
opt_morph[71]='ext / arms & bar-SBa / 15"'
radi_morph[72]='comp / circle / 6"'
opt_morph[72]='comp / circle / 3.5"'
radi_morph[73]='ext / circle center / 8.8"'
opt_morph[73]='? ext / lenticular-two sources-S0 /11"'
radi_morph[74]='comp / circle / 5"'
opt_morph[74]='comp / circle-E2 / 6"'
radi_morph[75]='ext / circle center / 7"'
opt_morph[75]='ext / elliptical-E6 / 13.5"'
radi_morph[76]='ext / circle center / 7"'
opt_morph[76]='ext / edge on lenticular-S0 / 16"'
radi_morph[77]='ext / Iregular / 6.3"'
opt_morph[77]='ext / lenticular-S0 / 19.3"'
radi_morph[78]='ext / Iregular / 10.5"'
opt_morph[78]='ext / elliptical-E6 / 11"'
radi_morph[79]='comp / noisy /7"'
opt_morph[79]='comp / elliptical-E6 / 15"'
radi_morph[80]='comp / noisy / 7.6"'
opt_morph[80]='comp / circle-E2 / 5"'
radi_morph[81]='comp / noisy / 6.4"'
opt_morph[81]='ext / look like arms-SBa / 16"'
radi_morph[82]='comp / circle / 7"'
opt_morph[82]='ext / bar & spiral-SBa / 23.2"' 

###### adding morphologies form paper Ledlow ############
morphMatch=open('finalMatch_info.txt','r')

morph_leddow=[]
numNED_matchMorph=[]
nameNED_matchMorph=[]   

for line in morphMatch:
	line=line.split(",")
	nameNED_matchMorph.append(np.str(line[1]).strip())
	morph_leddow.append(np.str(line[2]).strip())
	numNED_matchMorph.append(np.int(line[3]))
	

for a in name_opt_NED:
	for b,c,d in zip(nameNED_matchMorph,numNED_matchMorph,morph_leddow):
		if a==b:
			opt_morph[c-1]=d

#for i in range(len(opt_morph)):
#	print i+1, ',', opt_morph[i]


final_morph=list(np.zeros(len(name_opt_NED)))

final_morph[2]='AGN'
final_morph[3]='AGN'
final_morph[4]='AGN'
final_morph[5]='AGN'
final_morph[6]='SFG'
final_morph[7]='AGN'
final_morph[8]='AGN'
final_morph[13]='SFG'
final_morph[14]='SFG'
final_morph[15]='SFG'
final_morph[64]='SFG'
final_morph[71]='SFG'
final_morph[82]='SFG'




name_radio=[str(r).strip() for r in name_radio]
ra_radio=[str(format(r,"20.5f")).strip() for r in ra_radio]  
dec_radio=[str(format(r,"20.5f")).strip() for r in dec_radio]
area_observed=[str(format(r,"20.5f")).strip() for r in area_observed]
area_detectable= [str(format(r,"20.5f")).strip() for r in area_detectable] 
flux=[str(r).strip() for r in flux] 
loglum=[str(format(r,"20.3f")).strip() for r in loglum]  
loglum_deteable=[str(format(r,"20.3f")).strip() for r in loglum_deteable] 
num_opt=[str(r).strip() for r in num_opt]
num_opt_couldDect=[str(r).strip() for r in num_opt_couldDect]

name_opt_NED=[str(r).strip() for r in name_opt_NED]
ra_opt_NED=[str(format(r,"20.5f")).strip() for r in ra_opt_NED]
dec_opt_NED=[str(format(r,"20.5f")).strip() for r in dec_opt_NED]   
redshift=[str(format(r,"20.3f")).strip() for r in redshift]   
mag_NED=[str(r).strip() for r in mag_NED]   
note=[str(r).strip() for r in note]

name_opt_SDSS=[str(r).strip() for r in name_opt_SDSS] 
objid_SDSS=[str(r).strip() for r in objid_SDSS]
ra_opt_SDSS=[str(format(r,"20.5f")).strip() for r in ra_opt_SDSS]
dec_opt_SDSS=[str(format(r,"20.5f")).strip() for r in dec_opt_SDSS]
mag_u=[str(format(r,"20.2f")).strip() for r in mag_u]
mag_g=[str(format(r,"20.2f")).strip() for r in mag_g]
mag_r=[str(format(r,"20.2f")).strip() for r in mag_r]
mag_i=[str(format(r,"20.2f")).strip() for r in mag_i]
mag_z=[str(format(r,"20.2f")).strip() for r in mag_z]
u_r=[str(format(r,"20.2f")).strip() for r in u_r]
color_morph=[str(r).strip() for r in color_morph]
radi_morph=[str(r).strip() for r in radi_morph]
opt_morph=[str(r).strip() for r in opt_morph]
final_morph=[str(r).strip() for r in final_morph]



final_table=open('table_Jul23.txt','w')
final_table.write('Radio Name(A),  Opt Name(B),  Ra Radio,  Dec Radio,  Area observed,  Area detectable, '
	'flux(mJy),  log(lum)-W/Hz,  log(lum)-W/Hz-detectable,  num Opt,   num opt detectable,  Ra NED,  Dec NED,  z,  MagNED, objID SDSS,  '
	'Ra SDSS,  Dec SDSS,  Mag_u,  Mag_g,  Mag_r,  Mag_i,  Mag_z,  Note,  u-r, color classification,  radio morph  '
	'optical morph,   conclution' +"\n")
j=0
for i in range(len(name_opt_NED)):
	if ra_radio[j]!='-1000000.00000':
		final_table.write(',  '.join([name_radio[j],name_opt_NED[j],ra_radio[j],dec_radio[j],
			area_observed[j],area_detectable[j],flux[j],loglum[j],loglum_deteable[j],num_opt[j],num_opt_couldDect[j],
			ra_opt_NED[i],dec_opt_NED[i],redshift[i],mag_NED[i],objid_SDSS[i],ra_opt_SDSS[i],
			dec_opt_SDSS[i],mag_u[i],mag_g[i],mag_r[i],mag_i[i],mag_z[i],note[i],u_r[i],color_morph[i], radi_morph[i], opt_morph[i],
			final_morph[i]])+'\n')
	if ra_radio[j] =='-1000000.00000':
		final_table.write('-1000000,  '+name_opt_NED[i]+',  -1000000,  -1000000,  -1000000,  '
			'-1000000,  -1000000,  -1000000,  -1000000,  -1000000,  -1000000,  '+',  '.join([ra_opt_NED[i],
				dec_opt_NED[i],redshift[i],
				mag_NED[i],objid_SDSS[i],ra_opt_SDSS[i],dec_opt_SDSS[i],mag_u[i],mag_g[i],
				mag_r[i],mag_i[i],mag_z[i],note[i],u_r[i],color_morph[i], radi_morph[i], opt_morph[i],final_morph[i]])+'\n')
	j+=1
print j
print len(name_opt_NED)

for a,b,c,d in zip(name_opt_NED,opt_morph,radi_morph,final_morph):
	print a,', ',b, ', ',c,', ',d

final_table.close()

