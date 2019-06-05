import json
import requests



rest_key="yvofkie1f17e7uqh12lxdieioc4micfg"
oa_key="mjXZOTPsxrsvhZ2HtviQJHEoYmeMJDhGaLShPs684W5qf9qCNl8OaZFmJlFMrRYctO7ULr9gn-ds58IoFHeWSg=="
oa_key_s="QwBCJ01mbSMuIRC0qAf6ax1ACxayuzSRXTkkOk7lTysEvIDe5LiwBO6ytbytXKdSFgepAkbMUQ48kXB3p1ZgPl581nrU_BXj"
baseurl_rest="https://apis.mapmyindia.com/advancedmaps/v1/"
baseurl_oa="https://atlas.mapmyindia.com/api/places/search/json?"
oauth_token_type=None
oauth_token=None
busfare={
    2:[8,10],
    4:[10,14],
    6:[15,20],
    8:[18,23],
    10:[22,27],
    12:[25,30],
    14:[28,33],
    17:[32,47],
    20:[34,39],
    25:[37,42],
    30:[42,47],
    35:[47,552],
    40:[52,57],
    45:[57,62],
    50:[62,67]
}


def get_dist(source,destination):
    print("Using MapMyIndia to Calculate Distance")
    url=baseurl_rest+rest_key+"/distance_matrix/driving/"+source+";"+destination
    print("URL: "+url)
    result=requests.get(url)
    acresults=json.loads(result.text)
    print(acresults)
    dist=acresults['results']['distances'][0][1]
    kdist=dist/1000
    kdist = round(kdist, 1)
    print ("Distance is "+str(dist)+" meters or "+str(kdist)+" km")
    return kdist

def calculatefare(dist,modes):
    modes=str(modes).lower()
    modearr=modes.split(";")
    for mode in modearr:
        if mode == "auto":
            ndist=dist-1.5
            if ndist<0:
                ndist=0
            fare=round(18+(ndist*12.5))
            print("fare by auto: "+str(fare))
        if mode =="bus":
            fareo=0
            faree=0
            if dist<=50:
                for i in busfare:
                    if dist<i:
                        fareo=busfare[i][0]
                        faree=busfare[i][1]
                        break
            else:
                bdist=dist-50
                fareo=62+((bdist//5)*5)
                faree=67+((bdist//5)*10)
            print ("fare by ordinary bus: "+str(fareo)+"\nfare by express bus: "+str(faree))

        if mode == "taxi":
            ndist=dist-1.5
            if ndist<0:
                ndist=0
            fare=round(22+(ndist*15))
            print ("fare by taxi: "+str(fare))

def get_coord(query):
    print("\nIdentifying Co-ordintes for on MapMyIndia:" +query)
    url = baseurl_oa + "query=" + query.replace("\s", "%20")
    global oauth_token_type
    global oauth_token
    if oauth_token_type==None:
        resp=requests.post("https://outpost.mapmyindia.com/api/security/oauth/token",{'grant_type':'client_credentials','client_id':oa_key,'client_secret':oa_key_s})
        respj=json.loads(resp.text)
        oauth_token=respj['access_token']
        oauth_token_type=respj['token_type']
        print("Acquired OAuth token:\n"+respj['token_type']+"\t"+respj['access_token'])
    else:
        print ("using previously acquired token")
    result=requests.get(url, headers={'Authorization':str(oauth_token_type)+str(oauth_token)})
    acresults=json.loads(result.text)
    coord=str(acresults['suggestedLocations'][0]['longitude'])+','+str(acresults['suggestedLocations'][0]['latitude'])
    return coord

s1="Rustomjee Royale"
d1="OM Jwellers Borivali"
s1_c=get_coord(s1)
d1_c=get_coord(d1)
print ("\nCo-ordinates identified are:\n"+s1+" :"+s1_c+"\n"+d1+" :"+d1_c)

print("\n\n\n")
dist=get_dist(s1_c,d1_c)

print("\n\nNow Calculating Fare")
calculatefare(dist,'auto;bus;taxi')