import pandas as pd

df = pd.read_csv("D:\AIML_python\pandas\covid_data.csv")
print("Real Data",df)
# print(df.describe())

    
# added rates
df["Death_rate"] = df["Total_Deaths"] / df["Total_Cases"]*100
df["Recovery_Rate"] = df["Total_Recovered"] / df["Total_Cases"]*100

#highest and lowest death rates

highest_Drate = df["Death_rate"].max()
for i in range(15):
    if df.loc[i,"Death_rate"] == highest_Drate:
        print(f"highest death rate have {df.loc[i,'Country']} country")
lowest_recovery = df["Recovery_Rate"].min()
for i in range(15):
    if df.loc[i,"Recovery_Rate"] == lowest_recovery:
        print(f"lowest recovery rate have {df.loc[i,'Country']} country")

#filter by active 10% more than total
print(df[df["Active_Cases"] > ((df["Total_Cases"]*10)/100)])


# sorting by recovery rate
sorted_by_recovery = df.sort_values(by="Recovery_Rate", ascending=False)
print("\nSorted \n",sorted_by_recovery)

df.to_csv("D:\AIML_python\pandas\exp_covid_data.csv", index=False)