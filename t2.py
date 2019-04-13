while 1:
	start=input("Enter start bus stop:")
	end=input("Enter end bus stop:")
	if start==end:
		print("Source and destination cannot be the same")
	else:
		break

stop=open("stops.txt","r")
stopData=stop.readlines()
m=0
n=0
tripListStart=[]
tripListEnd=[]
route_id_start=[]
route_id_end=[]
trips=[]
froute=[]
ftrip=[]
fstop=[]
arr3=[]
arr4=[]
fstrip=[]
fetrip=[]
tem=[]

for line in stopData:
	arr=line.split(",")
	arr4.append(arr)
	if start==arr[2]:
		start_stop_id=arr[0]
		m=1
	if end==arr[2]:
		end_stop_id=arr[0]
		n=1
	if m and n:
		break
if m and n:
	stop_times=open("stop_times.txt","r")
	stop_times_data=stop_times.readlines()
	for line in stop_times_data:
		arr=line.split(",")
		arr[4]=arr[4][:-1]
		arr3.append(arr)
		if arr[3]==start_stop_id:
			tripListStart.append(arr[0])
		if arr[3]==end_stop_id:
			tripListEnd.append(arr[0])

	route=open("trips.txt","r")
	route_data=route.readlines()
	for line in route_data:
		trips.append(line.split(','))

	for i in range(len(trips)):
		temp=trips[i][2]
		temp=temp[:-1]
		trips[i][2]=temp	

	for trip in tripListStart:
		for item in trips:
			if trip==item[2]:
				route_id_start.append(item[0])
				break

	route_id_start=list(set(route_id_start))	

	for trip in tripListEnd:
		for item in trips:
			if trip==item[2]:
				route_id_end.append(item[0])
				break

	route_id_end=list(set(route_id_end))
	
	for stop in route_id_start:
		for e in trips:
			if stop==e[0]:
				fstrip.append(e[2])
				break

	for stop in route_id_end:
		for e in trips:
			if stop==e[0]:
				fetrip.append(e[2])
				break

	for i in fstrip:
		for j in fetrip:
			if i==j:
				fstop.append(i)

	if len(fstop)==0:
		print("No single route possible!")
	else:
		for trip in fstop:
			glf=0
			f=0
			for s in arr3:
				if (s[0]==trip and s[3]==start_stop_id) or (f==1):
					if s[0]!=trip:
						glf=1
						break
					tem.append(s[3])
					if s[3]==end_stop_id:
						break
					f=1
			if glf==1:
				print("No single route possible!")
			else:
				c=1
				for st in tem:
					for line in arr4:
						if line[0]==st:
							print(c,".",line[2],end="\t")
							c+=1
							break
				print()
				tem.clear()

else:
	print("Bus stops not found!")
