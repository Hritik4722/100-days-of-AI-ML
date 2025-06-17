import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\AIML_python\pand_mato\terrorismData.csv")
# print(df.head(5))

df = df.drop("Summary", axis=1)
df = df.fillna(0)
df["Casualties"] = df["Killed"]+df["Wounded"]

# #top countries with most attacks
# print("\ntop countries with most attacks")
# print(df["Country"].value_counts().head(10))

# #top 10 terrorist grps by number of attacks
# print("\ntop 10 terrorist grps by number of attacks")
# print(df["Group"].value_counts().head(10))

# #Total number of people killed per year.
# killed_num_year = df.groupby("Year")["Killed"].sum()
# print(killed_num_year)

# #number of attacks per region
# print("\nnumber of attacks per region")
# print(df["Region"].value_counts().head(10))

# #total number of attacks by weapon type
# print("\ntotal number of attacks by weapon type")
# print(df["Weapon_type"].value_counts().head(10))


total_att_year = df["Year"].value_counts().sort_values()
# print(total_att_year)

num_people_casual = df.groupby("Country")["Casualties"].sum()
# print(num_people_casual.head())

#attack type average people killed
avg_killed_type = df.groupby("AttackType")["Killed"].mean()
# print(avg_killed_type)

top_cities_attacked = df["City"].value_counts().sort_values(ascending=False).head(5)
# print(top_cities_attacked)


##########################################################################################
################################# Visualization ##########################################
##########################################################################################

#####number of attacks per year

year = df["Year"].unique()
plt.figure(figsize=(6,4))
plt.plot(year,total_att_year)
plt.title("Number of attacks per year")
plt.xlabel("Year")
plt.ylabel("No of Attacks")
# plt.show()

########Top 10 countries with most attack

country = df["Country"].value_counts().head(10)
x = country.index.tolist()
y = country.values.tolist()
plt.figure(figsize=(6,4))
plt.bar(x,y)
plt.title("Top 10 countries with most attack")
plt.xlabel("Country")
plt.ylabel("No of Attacks")
plt.tight_layout()
# plt.show()

####Distribution of attacks by weapon type

att_w_type = df["Weapon_type"].value_counts().head(6)
weapon_t = att_w_type.index.tolist()
no_attacks = att_w_type.values.tolist()
plt.figure(figsize=(6,4))
plt.pie(no_attacks,labels=weapon_t,autopct='%1.1f%%')
plt.tight_layout()
# plt.show()


####Distribution of casualties

casua = df["Casualties"]
plt.figure(figsize=(6,4))
plt.hist(casua.values.tolist(),bins=5,label="Distribution of casualties")
# plt.show()

####Average number of people killed per attack type

people_killed_avg =  df.groupby("AttackType")["Killed"].mean()
att_t = people_killed_avg.index.tolist()
avg_kill = people_killed_avg.values.tolist()
plt.figure(figsize=(6,4))
plt.bar(att_t,avg_kill)
plt.title("Average number of people killed per attack type")
plt.xlabel("Attack Type")
plt.ylabel("avg No of kilss")
plt.tight_layout()
# plt.show()


######Total casualties per country

total_caualties = df.groupby("Country")["Casualties"].sum().sort_values(ascending=False).head(10)
country_list = total_caualties.index.tolist()
no_casualty = total_caualties.values.tolist()
plt.figure(figsize=(6,4))
plt.barh(country_list,no_casualty)
plt.title("Total casualties per country")
plt.xlabel("country")
plt.ylabel("Total casualties")
plt.tight_layout()
# plt.show()

#######Top Cities Attacked

top_cities = df["City"].value_counts().head(10)
city_name = top_cities.index.tolist()
no_of_time = top_cities.values.tolist()
plt.figure(figsize=(6,4))
plt.bar(city_name,no_of_time)
plt.title("Top Cities Attacked")
plt.xlabel("City")
plt.ylabel("No. of time attacked")
plt.tight_layout()
# plt.show()

#####subplots

fig , ax = plt.subplots(2,2,figsize=(10,5))

#attacks per region (5)
att_reg = df["Region"].value_counts().head(5)
no_attack_reg = att_reg.values.tolist()
region_n = att_reg.index.tolist()
ax[0,0].bar(region_n,no_attack_reg)
ax[0,0].set_title("attacks per region")
ax[0,0].set_xlabel("name of region")
ax[0,0].set_ylabel("no of attack")




##Casualties per region
casualties_reg = df.groupby("Region")["Casualties"].sum().head(5)
no_casualty_reg = casualties_reg.values.tolist()
region_name = casualties_reg.index.tolist()
ax[0,1].bar(region_name,no_casualty_reg)
ax[0,1].set_title("Casualties per region")
ax[0,1].set_xlabel("name of region")
ax[0,1].set_ylabel("no of Casualty")




###Top 5 cities to be attacked
top_city = df["City"].value_counts().head(5)
name_city = top_city.index.tolist()
city_num_attack = top_city.values.tolist()
ax[1,0].bar(name_city,city_num_attack)
ax[1,0].set_title("Top 5 cities to be attacked")
ax[1,0].set_xlabel("name of city")
ax[1,0].set_ylabel("no of time attacked")
ax[1,0].tick_params(axis='x', rotation=45)


###Top terrorist groups
top_10_grp = df["Group"].value_counts().head(5)
name_grp = top_10_grp.index.tolist()
num_attacks = top_10_grp.values.tolist()
ax[1,1].bar(name_grp,num_attacks)
ax[1,1].set_title("Top terrorist groups")
ax[1,1].set_xlabel("name of Terrorist grps")
ax[1,1].set_ylabel("no of attacks")



fig.suptitle("Analyzation of terrorist activities")
plt.tight_layout()
plt.show()