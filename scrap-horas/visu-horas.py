import matplotlib.pyplot as plt
import json
import numpy as np
import arrow

scrap=json.load(open("scrap-horas.json"))
estimations=scrap["estimations"]
full_explanations=scrap["explanations"]
explanations={}
for issue in full_explanations:
    explanations[issue]={}
    efforts=explanations[issue]
    for effort in full_explanations[issue]:
        if effort["date"]<'2018-10-02T00:00:00Z':
            continue
        print("===========")
        print(issue)
        print(effort)

        u=effort["user"]
        w=effort["work"]
        efforts[u]=efforts.get(u,0)+w

total_explanations={}
worked_most={}
for issue in explanations.keys():
    worked=None
    total_explanations[issue]=0
    for k,v in explanations[issue].items():
        print(k)
        total_explanations[issue]+=float(v)
        if worked==None:
            worked=k
        else:
            if explanations[issue][k]>explanations[issue][worked]:
                worked=k
    worked_most[issue]=worked

speed={}
for issue in explanations.keys():
    try:
        speed[issue]=float(estimations[issue])*60.0/float(total_explanations[issue])
    except Exception as e:
        print(e)

events={}
for issue in full_explanations:
    for effort in full_explanations[issue]:
        try:
            events[effort["date"]]={
                "real_hours":effort["work"],
                "estimation_hours":float(effort["work"])*float(speed[issue])
            }
        except Exception as e:
            print(e)


def mostrar_puntos(con_labels,por_repos):
    print(total_explanations)
    print(estimations)
    x=[]
    y=[]
    n=[]
    colors=[]

    for issue in total_explanations.keys() & estimations.keys():
        if total_explanations[issue]==0.0:
            continue
        
        x.append(estimations[issue])
        y.append(float(total_explanations[issue])/60.0)
        if por_repos:
            n.append(issue)
            if "mataco-server" in issue:
                colors.append("#FF0000")
            elif "mataco-app" in issue:
                colors.append("#00FF00")
            elif "mataco-control" in issue:
                colors.append("#0000FF")
        else:
            n.append(worked_most[issue])
            if "sofia" in worked_most[issue]:
                colors.append("#FF00FF")
            elif "Camila" in worked_most[issue]:
                colors.append("#00FF00")
            elif "santi" in worked_most[issue]:
                colors.append("#0000FF")
            elif "sbruzzi" in worked_most[issue]:
                colors.append("#FF0000")

    fig, ax = plt.subplots()
    ax.plot([0,10],[0,10])
    ax.plot([0,10],[0,20])
    ax.plot([0,10],[0,5])
    ax.scatter(x,y,c=colors)
    plt.xlabel("estimación")
    plt.ylabel("Total tiempo invertido")

    if con_labels:
        for i,txt in enumerate(n):
            ax.annotate(txt,(x[i],y[i]))

    plt.savefig("mostrar_puntos {} {}.png".format(con_labels,por_repos))
    plt.clf()


#mostrar_puntos(True,False)

def mostrar_columnas_repo():
    estimated={}
    for i in estimations:
        if total_explanations[i]==0:
            continue
        repo=i.split("/")[0]
        e=estimated.get(repo,0)
        estimated[repo]=e+estimations[i]
    totals={}
    for i in total_explanations:
        if total_explanations[i]==0:
            continue
        repo=i.split("/")[0]
        e=totals.get(repo,0)
        totals[repo]=e+float(total_explanations[i])/60.0
    
    x=[]
    y=[]
    n=[]
    for k in estimated.keys() & totals.keys():
        n.append(k)
        x.append(estimated[k])
        y.append(totals[k])
    print(n)
    locations=np.arange(len(n))
    plt.bar(x=locations,height=x,color="#FF005588")
    plt.bar(x=locations,height=y,color="#00FF5588")
    plt.legend("estimación","realidad")
    plt.xticks(locations,n)
    plt.savefig("columnas_repo.png")
    plt.clf()


def mostrar_columnas_personas():
    estimated={}
    for i in estimations:
        if total_explanations[i]==0:
            continue
        repo=worked_most[i]
        e=estimated.get(repo,0)
        estimated[repo]=e+estimations[i]
    totals={}
    for i in explanations:
        for p in explanations[i]:
            total_p=totals.get(p,0)
            totals[p]=total_p+explanations[i][p]/60.0
    
    x=[]
    y=[]
    n=[]
    for k in estimated.keys() & totals.keys():
        n.append(k)
        x.append(estimated[k])
        y.append(totals[k])
    print(n)
    locations=np.arange(len(n))
    plt.bar(x=locations,height=x,color="#FF005588")
    plt.bar(x=locations,height=y,color="#00FF5588")
    plt.legend("estimación","realidad")
    plt.xticks(locations,n)
    plt.savefig("columnas_personas.png")
    plt.clf()

def mostrar_burndown():
    print(events)

    times=sorted(events.keys())
    events_ordered=[events[t] for t in times]
    real_hours=[e["real_hours"] for e in events_ordered]
    estimation_hours=[e["estimation_hours"] for e in events_ordered]

    total_estimation=sum([estimations[i] for i in estimations])*60.0
    print(total_estimation/60.0)



    estimation_hours[0]=total_estimation-estimation_hours[0]
    real_hours[0]=total_estimation-real_hours[0]
    for i in range(1,len(times)):
        real_hours[i]=real_hours[i-1]-real_hours[i]
        estimation_hours[i]=estimation_hours[i-1]-estimation_hours[i]

    estimation_hours=[e/60.0 for e in estimation_hours]
    real_hours=[r/60.0 for r in real_hours]

    times=[arrow.get(t).timestamp for t in times]
    plt.plot(times,real_hours)
    plt.plot(times,estimation_hours)
    plt.plot([times[0],times[len(times)-1]],[0,0])
    plt.show()

def mostrar_lista():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    for issue in explanations.keys() & estimations.keys():
        if "ERROR" in issue:
            continue
        if not "mataco-app" in issue:
            continue
        print(issue,total_explanations[issue]/60.0,estimations[issue],sep=",")


#mostrar_lista()
#mostrar_burndown()
#mostrar_puntos(False,False)
#mostrar_puntos(False,True)
#mostrar_puntos(True,False)
#mostrar_puntos(True,True)
#mostrar_columnas_personas()
mostrar_columnas_repo()
##mostrar_columnas_repo()



