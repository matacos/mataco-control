import matplotlib.pyplot as plt
import json
import numpy as np

scrap=json.load(open("scrap-horas.json"))
estimations=scrap["estimations"]
full_explanations=scrap["explanations"]
explanations={}
for issue in full_explanations:
    explanations[issue]={}
    efforts=explanations[issue]
    for effort in full_explanations[issue]:
        if effort["date"]<'2018-09-14T04:52:27Z':
            continue
        u=effort["user"]
        w=effort["work"]
        efforts[u]=efforts.get(u,0)+w
        
        print(effort)

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
    ax.scatter(x,y,c=colors)
    plt.xlabel("estimación")
    plt.ylabel("Total tiempo invertido")

    if con_labels:
        for i,txt in enumerate(n):
            ax.annotate(txt,(x[i],y[i]))

    plt.show()


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
    plt.show()


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
    plt.show()

mostrar_puntos(False,False)
#mostrar_columnas_repo()



