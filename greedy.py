#!/usr/bin/python3
import operator;
def greedy(deger,yuk,kapasite,adet):
	oranlar = []
	while adet > 0 :
		if(yuk[adet-1] != 0):
			oranlar.append([(deger[adet-1]/yuk[adet-1]),esya[adet-1],yuk[adet-1],deger[adet-1]])
		elif(yuk[adet-1] == 0):
			oranlar.append([0,esya[adet-1],yuk[adet-1],deger[adet-1]])
		adet -= 1
	agirlik = 0
	test=[]
	esyalar = sorted(oranlar,key=operator.itemgetter(0),reverse=True)
	for e in esyalar:
		#e[0] = oranlar
		#e[1] = esya
		#e[2] = deger
		#e[3] = yuk
		if(agirlik + e[2] <= kapasite):
			agirlik = agirlik + e[2]
	
	return agirlik
			
esya = ["x1","x2","x3","x4","x5","x6"]
deger = [100, 600, 1200, 2400, 500, 2000]
#yuk = [8, 12, 13, 75, 22, 41]
#kapasite = 96
yuk = [3,2,4,0,8,4]
kapasite = 22
adet = len(deger)
print(greedy(deger,yuk,kapasite,adet))