import requests as r
def covid():
    d=r.get("https://api.covid19india.org/data.json")
    re=d.json()
    t=re['statewise']
    s=input("Enter State : ")
    for i in t:
        if str(i['state']).upper()==s.upper():
            print(i['state']+"::")
            print("Confirmed Cases : "+ i["confirmed"])
            print("Active Cases : "+ i["active"])
            print("Deaths : "+ i["deaths"])
            print("Recovered Cases : "+ i["recovered"])
            covid()
covid()
        
        
