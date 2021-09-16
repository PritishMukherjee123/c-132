import csv
rows=[]

with open("planetdata.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers=rows[0]
Planet_data_row=rows[1:]
print(headers)
print(Planet_data_row[0])

headers[0]="row_num"
Solar_System_Planet_Count={}
for Planet_data in Planet_data_row:
    if Solar_System_Planet_Count.get(Planet_data[11]):
        Solar_System_Planet_Count[Planet_data[11]]+=1
    else:
        Solar_System_Planet_Count[Planet_data[11]]=1

max_solar_system=max( Solar_System_Planet_Count,key=Solar_System_Planet_Count.get)
print(max_solar_system)

temp_planet_data_rows= list(Planet_data_row)
for i in temp_planet_data_rows :
    planet_mass=i[3]
    if planet_mass.lower()=="unknown":
        Planet_data_row.remove(i)
        continue
    else :
        planet_mass_value=planet_mass.split(" ")[0]
        planet_mass_ref=planet_mass.split(" ")[1]
        if planet_mass_ref =="Jupiters":
            planet_mass_value= float(planet_mass_value)*317.8
        i[3]=planet_mass_value

    planet_radius=i[7]
    if planet_radius.lower()=="unknown":
        Planet_data_row.remove(i)
        continue
    else :
        planet_radius_value=planet_radius.split(" ")[0]
        planet_radius_ref=planet_radius.split(" ")[1]
        if planet_radius_ref =="Jupiter":
            planet_radius_value= float(planet_radius_value)*11.2
        i[7]=planet_radius_value

print(len(Planet_data_row))
koi_planets=[]
for i in Planet_data_row :
    if max_solar_system == i[11]:
        koi_planets.append(i)
print(len(koi_planets))

import plotly.express as px 
koi_planet_mass=[]
koi_planet_name=[]
for i in koi_planets :
    koi_planet_mass.append(i[3])
    koi_planet_name.append(i[1])

koi_planet_mass.append(1)
koi_planet_name.append("earth")
graph = px.bar(x=koi_planet_name,y=koi_planet_mass)
graph.show()

temp_planet_data_rows=list(Planet_data_row)
for i in temp_planet_data_rows:
    if i[1].lower()=="hd 100546 b":
        Planet_data_row.remove(i)

planet_mass =[]
planet_radius=[]
planet_name=[]
for i in Planet_data_row:
    planet_mass.append(i[3])
    planet_radius.append(i[7])
    planet_name.append(i[1])

planet_gravity=[]
for index , name in enumerate(planet_name):
    gravity=float(planet_mass[index])*5.972e+24/(float(planet_radius[index])*float(planet_radius[index])*6371000*6371000)
    gravity=gravity*6.674e-11
    planet_gravity.append(gravity)

graph=px.scatter(x=planet_radius,y=planet_mass,size=planet_gravity,hover_data=[planet_name])
graph.show()

low_gravity=[]
for index,gravity in enumerate(planet_gravity):
    if gravity<10 :
        low_gravity.append(Planet_data_row[index])

low_gravityplanets=[]
for index,gravity in enumerate(planet_gravity):
    if gravity<100 :
        low_gravityplanets.append(Planet_data_row[index])

print(len(low_gravity))
print(len(low_gravityplanets))

planet_type_values=[]
for i in Planet_data_row:
    planet_type_values.append(i[6])

print(list(set(planet_type_values)))

planet_masses=[]
planet_radiuses=[]
for i in Planet_data_row:
    planet_masses.append(i[3])
    planet_radiuses.append(i[7])

graph3=px.scatter(x=planet_radiuses,y=planet_masses)
graph3.show()

"""from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import seaborn as sb

X=[]
for  index,planet_mass in enumerate(planet_masses):
    temp_list=[planet_radiuses[index],planet_mass]
    X.append(temp_list)

Wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=42)
    kmeans.fit(X)
    Wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sb.lineplot(range(1,11),Wcss,marker="o",color="red")
plt.show()"""
planet_masses=[]
planet_radiuses=[]
planet_types=[]
for i in low_gravityplanets:
    planet_masses.append(i[3])
    planet_radiuses.append(i[7])
    planet_types.append(i[6])

graph4=px.scatter(x=planet_radiuses,y=planet_masses,color=planet_types)
graph4.show()

suitable_planets=[]
for i in low_gravityplanets : 
    if i[6].lower()=="terrestrial" or i[6].lower()=="super earth":
        suitable_planets.append(i)

print(len(suitable_planets))