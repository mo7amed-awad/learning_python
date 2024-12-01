import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title=[]
company_name =[]
location_name=[]
links=[]
salary=[]

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

src = result.content
#print(src)

soup = BeautifulSoup(src,"lxml")
#rint(soup)

job_titles = soup.find_all("h2",{"class":"css-m604qf"})
company_names=soup.find_all("a",{"class":"css-17s97q8"})
locations_names = soup.find_all("span",{"class":"css-5wys0k"})


for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(locations_names[i].text)


for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src,"lxml")
    salaries = soup.find("span", {"class": "css-4xky9y"})
    salary.append(salaries.text if salaries else "Not mentioned")
print(salaries)
file_list=[job_title,company_name,location_name,links,salary]
exported=zip_longest(*file_list)

with open("D:/programing/Learning-python/codezilla/web_scraping/jobs.csv","w") as myfile:
    wr= csv.writer(myfile)
    wr.writerow(["Job Title","Company Name","Location","Link","Salary"])
    wr.writerows(exported)