import numpy as np

table=open('table_May30.txt', 'r')

name_radio=[]
name_opt_NED=[] 
ra_radio=[]  
dec_radio=[]
area_observed=[]
area_detectable= [] 
flux=[] 
loglum=[]  
loglum_deteable=[] 
num_opt=[]
num_opt_couldDect=[]
ra_opt_NED=[]
dec_opt_NED=[] 
redshift=[]   
mag_NED=[] 
objid_SDSS=[]
ra_opt_SDSS=[]
dec_opt_SDSS=[] 
mag_u=[]
mag_g=[]
mag_r=[]
mag_i=[]
mag_z=[]
note=[]
u_r=[]
color_morph=[]
radi_morph=[]
opt_morph=[]
final_morph=[]




for line in table:
	line=line.split(",")
	name_radio.append(np.str(line[0]))
	name_opt_NED.append(np.str(line[1])) 
	ra_radio.append(np.float(line[2]))
	dec_radio.append(np.float(line[3]))
	area_observed.append(np.float(line[4]))
	area_detectable.append(np.float(line[5]))
	flux.append(np.float(line[6]))
	loglum.append(np.float(line[7])) 
	loglum_deteable.append(np.float(line[8]))  
	num_opt.append(np.int(line[9]))
	num_opt_couldDect.append(np.int(line[10]))  
	ra_opt_NED.append(np.float(line[11])) 
	dec_opt_NED.append(np.float(line[12]))  
	redshift.append(np.float(line[13]))  
	mag_NED.append(np.str(line[14]))   
	objid_SDSS.append(np.int(line[15]))
	ra_opt_SDSS.append(np.float(line[16]))
	dec_opt_SDSS.append(np.float(line[17]))
	mag_u.append(np.float(line[18]))
	mag_g.append(np.float(line[19]))
	mag_r.append(np.float(line[20]))
	mag_i.append(np.float(line[21]))
	mag_z.append(np.float(line[22]))
	note.append(np.str(line[23]))
	u_r.append(np.float(line[24]))
	color_morph.append(np.str(line[25]))
	radi_morph.append(np.str(line[26]))
	opt_morph.append(np.str(line[27]))
	final_morph.append(np.str(line[28]))


table.close()

half_num_opt_couldDect=[e/2 for e in num_opt_couldDect]


p1= plt.plot(redshift,loglum,marker='o', color='blue')
p2=plt.plot(num_opt_couldDect,log_lum, marker='-',color='red')
p3=plt.plot(half_num_opt_couldDect,log_lum, marker='-',color='green')

plt.xlabel('redshift')
plt.ylabel('log(Lum(W/Hz))')
plt.show()


