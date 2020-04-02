import pandas as pd
import numpy as np
path = "C:/Users/PycharmProjects/BOT/Dirct/rawdata.xlsx"
#DATA FRAME
df=pd.read_excel(path)
rows, col =df.shape
print("Rows:- ",rows,"Columns :- ",col)
#print(df.columns)

#1. Count of total ticket?
CTT= df["Ticket Closed"].count()
#print(CTT)

#2.	Count of Proactive and Reactive tickets?
React = df[df["  Proactive or Reactive Ticket?"]=="Reactive"]
print("Count of Reactive tickets : = ",React["Clarify Ticket Closed"].count())
#print("Reactive: - ",React.count())


Pro= df[df["  Proactive or Reactive Ticket?"]=="Proactive"]
print("Count of Proactive tickets : = ",Pro["Ticket Closed"].count())
#print("Proactive: - ",Pro.count())

#3.	Number of Duplicate tickets?

Dupli = df[df["Fault Area"]=="Duplicate ticket"]
Dupli2 = df[df["Fault Area"]=="Child-Caused"]
Dupli3 = df[df["Fault Area"]=="Child-Caused"]

Dup=Dupli.count()+Dupli2.count()+Dupli3.count()
print("Count of Duplicate cases: - ",Dup["Ticket Closed"])

#4.	Count of ticket as per severity?

Sev1=df[df["Severity"]==1]
Sev2=df[df["Severity"]==2]
Sev3=df[df["Severity"]==3]
print("Count of Severity 1 Cases :- ",Sev1["Ticket Closed"].count())
print("Count of Severity 2 Cases :- ",Sev2["Ticket Closed"].count())
print("Count of Severity 3 Cases :- ",Sev3["Ticket Closed"].count())

#5.	Count of Missed TTRS?

SLA_Achieved = df[df["SLA Achievement"]== "Achieved"]
SLA_Failed = df[df["SLA Achievement"]== "Failed"]

print("Count of Achieved Cases:- ",SLA_Achieved["Ticket Closed"].count())
print("Count of Failed Cases:- ",SLA_Failed["Ticket Closed"].count())

#6. Number of Proactive and Reactive tickets, excluding Duplicate tickets?

nd= df["  Proactive or Reactive Ticket?"][df["Fault Area"]!="Duplicate ticket"][df["Fault Area"]!="Child-Caused"][df["Fault Area"]!="Child-Caused"][df["  Proactive or Reactive Ticket?"]=="Reactive"]
print("Count of Reactive Cases after excluding duplicates :- ",nd.count())

pr= df["  Proactive or Reactive Ticket?"][df["Fault Area"]!="Duplicate ticket"][df["Fault Area"]!="Child-Caused"][df["Fault Area"]!="Child-Caused"][df["  Proactive or Reactive Ticket?"]=="Proactive"]
print("Count of Proactive Cases after excluding duplicates :- ",pr.count())

#7.	Count of tickets as per Fault Area?

var1 = df.pivot_table(index="Fault Area",values="Severity",aggfunc="count")
#print(var1)

#8.	Total number of cases taking only the Orange outages and PTT outages with severities.

var2= df["Service Category"][(df["Fault Area"] == "Ora Outage") | (df["Fault Area"]== "Provider Outage")]
var3= var2.values

k=[]
for i in range(0,len(var3)):
    k.append(var3[i])

temp=list(set(k))
print("Count of cases taking only the Ora outages and PTT outages with severities: - ")
for j in range(0,len(temp)):
    if temp[j] in k:
        y=temp[j]
        result=k.count(y)
        print(y,result)

#8.	Count of tickets for power issues on each services.

power1= df["Service Category"][(df["Fault Area"]== "Power Outage")]
power2= power1.values

k1=[]
for n in range(0,len(power2)):
    k1.append(power2[n])
temp2=list(set(k1))
print("Count of tickets for power issues as per services.: - ")
for j1 in range(0,len(temp2)):
    if temp2[j1] in k1:
        y1=temp2[j1]
        result2=k1.count(y1)
        print(y1,result2)

#9.	Closed Sev1/Sev2/Sev3 cases as per services and fault area.
sev= df["Severity"][(df["Fault Area"]== "Ora Outage")|(df["Fault Area"] == "Provider Outage")]
temp_lst=sev.values
k2=[]

for m in range(0,len(temp_lst)):
    k2.append(temp_lst[m])
temp3=list(set(k2))
print("Closed Sev1/Sev2/Sev3/Sev5 cases as per services and fault area: - ")
for j2 in range(0,len(temp3)):
    if temp3[j2] in k2:
        y2=temp3[j2]
        result3=k2.count(y2)
        print("Severity "+str(y2),":- ",result3)

#10.Count for Services as per Sev1/Sev2/Sev3 and fault area (Oranage /PTT).
test= df["Service Category"][(df["Service Category"]=="IPV")|(df["Service Category"]=="WAC")]
print(test.count())
fa= (df["Fault Area"]== "Ora Outage")|(df["Fault Area"] == "Provider Outage")
print(fa.count())


fd= df.loc[fa,["Severity","Service Category"]]

t1= fd["Service Category"][(fd["Severity"]==1)]
t2= fd["Service Category"][(fd["Severity"]==2)]
t3= fd["Service Category"][(fd["Severity"]==3)]
t4= fd["Service Category"][(fd["Severity"]==4)]
t5= fd["Service Category"][(fd["Severity"]==5)]

t=[t1,t2,t3,t4,t5]
for jk in range(len(t)):
    tvar= t[jk].values
    vv=[]
    for km in range(len(tvar)):
        vv.append(tvar[km])

    print("Severity "+str(jk+1)+ " Ora/PTT cases as per Service Categories :- ")
    vari=list(set(vv))
    for b in range(len(vari)):
        if vari[b] in vv:
            yy2=vari[b]
            r= vv.count(yy2)
            print(yy2," :- ",r)



