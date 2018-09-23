import requests
import getpass
import re
import json
from collections import namedtuple
Repo=namedtuple("Repo",["name","id"])
Issue=namedtuple("Issue",["number","title","repo"])
Comment = namedtuple("Comment",["user","minutes"])
user = input("usuario github?")
password = getpass.getpass("contraseña github?")
#print (user)

def get_issue_name(issue):
    return str(issue.repo.name)+"/"+str(issue.number)+" "+str(issue.title)


zenhub_access_token="8f54e10f8f0d8847b05fba048e13dcc14f41d2f4537fb6325455f0f454d0940cf239316e761aebcc"
def get_request_estimate(repo,issue_number):
    j_response=requests.get("https://api.zenhub.io/p1/repositories/{}/issues/{}?access_token={}".format(repo.id,issue_number,zenhub_access_token)).json()
    print(j_response)
    try:
        return float(j_response["estimate"]["value"])
    except:
        return None

def get_repo(repo_name):
    repo = requests.get("https://api.github.com/repos/matacos/{}".format(repo_name),auth=(user,password))
    return Repo(repo_name,repo.json()["id"])


def get_issues_of_page(repo,page):
    issues = requests.get("https://api.github.com/repos/matacos/{}/issues?state=all&filter=all&page={}".format(repo.name,page),auth=(user,password)).json()
    return [
        Issue(i["number"],i["title"],repo) for i in issues
    ]
def get_issues(repo):
    page=1
    issues=[]
    while True:
        current=get_issues_of_page(repo,page)
        issues+=current
        if len(current)==0:
            return issues
        page+=1

def get_issue_estimations(issues):
    estimations = [
        get_request_estimate(i.repo,i.number) for i in issues
    ]
    estimated_issues={}
    for i,e in zip(issues,estimations):
        if e!=None:
            estimated_issues[get_issue_name(i)]=e
    return estimated_issues

def get_minutes(text):
    
    regexes=[
        "\[(?P<HH>[0-9.]+)h\]",#[?h]
        "(?P<HH>[0-9.]+)H",#?H
        "(?P<HH>[0-9.]+)h",#5h
        "\[(?P<HH>[0-9.]+)h(?P<MM>[0-9.]+)m\]",#[?h!m]
        "\[(?P<HH>[0-9.]+)h(?P<MM>[0-9.]+)\]",#[?h!]
        "\[(?P<MM>[0-9.]+)m\]"#[?m]
    ]
    minutes=0
    hours=0
    for r in regexes:
        result=re.search(r,text)
        if result:
            try:
                hours = (result.group("HH"))
            except:
                pass
            try:
                minutes = (result.group("MM"))
            except:
                pass

    total_minutes=60*float(hours)+float(minutes)
    if total_minutes==0:
        print("CUIDADO: el comentario {} no informa tiempo".format(text))

    return total_minutes


def get_comments(issue):
    repo=issue.repo
    j_response=requests.get("https://api.github.com/repos/matacos/{}/issues/{}/comments".format(repo.name,issue.number),auth=(user,password)).json()
    #print(j_response)
    comments = [Comment(c["user"]["login"],get_minutes(c["body"])) for c in j_response]
    return comments

def get_time_explanation(issue):
    workers={}
    comments=get_comments(issue)
    for c in comments:
        total_minutes=workers.get(c.user,0)+c.minutes
        workers[c.user]=total_minutes
    return workers;
def get_time_explanations(issues):
    return {get_issue_name(i):get_time_explanation(i) for i in issues}


if __name__=="__main__":
    issues=[]
    for n in ["mataco-app","mataco-server","mataco-control"]:
        repo = get_repo(n)
        issues += get_issues(repo)
    estimations = get_issue_estimations(issues)
    explanations = get_time_explanations(issues)
    json.dump({
        "estimations":estimations,
        "explanations":explanations
    },open("scrap-horas.json","w"))
        
    
