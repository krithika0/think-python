import requests,sys

def get_synonyms(tag):
  page=1
	p={'sort':'creation','order':'desc','site':'stackoverflow', 'tags':tag, 'pagesize':100,'page':page}
	has_more=True
	with open(tag+"-tag-synonyms.txt","a") as fout:
		while has_more:
			data=requests.get("https://api.stackexchange.com/2.2/tags/"+tag+"/synonyms",params=p).json()
			for row in data['items']:
				fout.write(row['name']+"\n")
			has_more=data['has_more']
			p['page']+=1
def get_tags(tag):
  page=1
	p={'sort':'popular','order':'desc','site':'stackoverflow', 'inname':tag, 'pagesize':100,'page':page}
	has_more=True
	with open(tag+"-tags.txt","w") as fout:
		while has_more:
			data=requests.get("https://api.stackexchange.com/2.2/tags",params=p).json()
			for row in data['items']:
				fout.write(row['name']+"\n")
			has_more=data['has_more']
			p['page']+=1

for tag in sys.argv[1:]:
	get_tags(tag)
