import json
from textblob import TextBlob

file=open('sample.json',encoding="utf8")
data=json.load(file)

# txt=TextBlob("i hate the life")
# a=[]
def process(data,name,pages):
  for i in range(1,pages):
      txt=TextBlob(data[str(i)][0])
      data[str(i)].append(txt.sentiment.polarity)
  neg=0
  pos=0
  for j in range(1,pages):
      if data[str(j)][1]<0:
          neg+=1
      else:
          pos+=1
  like=(pos/(pages-1))*100
  dislike=(neg/(pages-1))*100
  liked=f"{like}% Peoples like this product namely {name}"
  disliked=f"{dislike}% People dislike this product namely {name}"
  return [liked,disliked]