import requests
import json
from nlp import process


def code(a):
    r=requests.get(a).text
    return r

def review(htmls):
    im=htmls
    final=[]
    for i in range(10):
      ind=im.index("class=\"t-ZTKy\"><div><div class=\"\"")
      im=im[ind+34:]
      important=im[:im.index("</div>")]
      br=important.count("<br/>")
      nextes=important.replace("<br/>"," ",br)
      final.append(nextes)

    return final

def page(a,profilter3):
    reviewes=[]
    for i in range(1,a):
        try:
            rev=requests.get(profilter3+"&page="+str(i))
            rec=review(rev.text)
            reviewes.append(rec)
        except:
            break
    return reviewes


common="https://www.flipkart.com"

a=input("Enter the product name : ")
req=code(f"https://www.flipkart.com/search?q={a}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
filter1=req.index("target=\"_blank\" rel=\"noopener noreferrer\"")
filter2=req[filter1:filter1+1000]
main=filter2.index("href=")
filter3=filter2[main:main+600]
filter4=filter3[6:filter3.index("\"><div>")]
filter4=common+filter4

pro=code(filter4)

#find all reviews link

ind=pro.index("class=\"_3UAT2v _16PBlm\"")

profilter1=pro[ind-500:ind]
profilter2=profilter1[profilter1.index("</span></div><a href=\""):len(profilter1)-7]
profilter3=common+profilter2[22:]

#comment page process
pages=200

reviewes=page(pages,profilter3)


dic={}
sen=1
for j in reviewes:
   for k in j:
      dic[str(sen)]=[k]
      sen+=1
json_object = json.dumps(dic, indent=4)
 
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
result=process(dic,a,((pages-1)*10)-1)
print(result[0])
print(result[1])