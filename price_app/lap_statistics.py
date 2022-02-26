import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

dt= pd.read_csv("laptops.csv", encoding='latin-1')
data["Product"] = data["Product"].str.split("(").apply(lambda x: x[0])
data["Cpu_Speed"] = data["Cpu"].str.split(" ").apply(lambda x: x[-1]).str.replace("GHz", "")
data["Cpu_Vender"] = data["Cpu"].str.split(" ").apply(lambda x: x[0])
data["Cpu_Type"] = data["Cpu"].str.split(" ").apply(lambda x: x[1:4] if x[1] == "Celeron" and "Pentium" and "Xeon" else (x[1:3] if (x[1] == "Core" or x[0] == "AMD") else x[0]) )
data["Cpu_Type"] = data["Cpu_Type"].apply(lambda x: ' '.join(x))
data["Cpu_Type"]

split_mem = data['Memory'].str.split(' ', 1, expand=True)
data['Storage Type'] = split_mem[1]
data['Memory'] = split_mem[0]
data["Memory"].unique()

data["Ram"] = data["Ram"].str.replace("GB", "")

df_mem= data['Memory'].str.split('(\d+)',  expand=True)
data['Memory'] = pd.to_numeric(df_mem[1])
data.rename(columns={'Memory':'Memory (GB or TB)'}, inplace=True)

def mem(x):
    if x == 1:
        return 1024
    elif x == 2:
        return 2048
data['Memory (GB or TB)'] = data['Memory (GB or TB)'].apply(lambda x: 1024 if x==1 else x)
data['Memory (GB or TB)'] = data['Memory (GB or TB)'].apply(lambda x: 2048 if x==2 else x)
data.rename(columns={'Memory (GB or TB)':'Storage (GB)'}, inplace=True)

data["Weight"] = data["Weight"].str.replace("kg", "")

gpu_distribution_list = data["Gpu"].str.split(" ")
#data["Gpu_Vender"] = data["Gpu"].str.split(" ").apply(lambda x: x[0:2]  if x[0] == "Intel" else x[0]  if x[0] == "Intel Iris" else x[0])
data["Gpu_Vender"] = data["Gpu"].str.split(" ").apply(lambda x: x[0])
data["Gpu_Type"] = data["Gpu"].str.split(" ").apply(lambda x: x[1:])
data["Gpu_Type"] = data["Gpu_Type"].apply(lambda x: ' '.join(x))

data['Touchscreen'] = data['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)
data['Ips'] = data['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0)

def cat_os(inp):
    if inp == 'Windows 10' or inp == 'Windows 7' or inp == 'Windows 10 S':
        return 'Windows'
    elif inp == 'macOS' or inp == 'Mac OS X':
        return 'Mac'
    else:
        return 'Others/No OS/Linux'

data['OpSys'] = data['OpSys'].apply(cat_os)

data = data.reindex(columns=["Company", "TypeName", "Inches", "Touchscreen", "Ips", "Cpu_Vender", "Cpu_Type","Ram", "Storage (GB)", "Storage Type", "Gpu_Vender", "Gpu_Type", "Weight", "OpSys", "Price_euros" ])
data["Ram"] = data["Ram"].astype("int")
data["Storage (GB)"] = data["Storage (GB)"].astype("int")
data["Weight"] = data["Weight"].astype("float")

sns.set(rc={"figure.figsize":(9, 5)})
data["Company"].value_counts().plot(kind="bar")
