import requests
from bs4 import BeautifulSoup


def get_last_page_SO(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  s_page = soup.find("div",{"class":"s-pagination"})
  if s_page:
    links = s_page.find_all("a")
    pages = []
    for link in links[0:-1]:
      pages.append(int(link.find("span").string))
    last_page = pages[-1]
    return last_page
  else:
    return -1

def extract_job_SO(html):
    htitle = html.find("h2",{"class":"mb4"})
    hcompany = html.find("h3",{"class":"fc-black-700"})
    title = htitle.find("a")["title"]
    link = htitle.find("a")["href"]
    company = hcompany.find("span").string
    if company is not None:
      company = company.strip()
    location = hcompany.find("span",{"class":"fc-black-500"}).string
    if location is not None:
      location = location.strip()
    return {'TITLE': title,'COMPANY': company,'LOCATION': location,'Link':f"https://stackoverflow.com{link}"}

def extract_jobs_from_html_SO(l_page,url):
  jobs = []
  for page in range(l_page):
    print("==============================")
    print(f"Scrapping Stackoverflow {page} page ")
    result = requests.get(f"{url}&pg={page}")
    soup = BeautifulSoup(result.text, 'html.parser')
    job_div = soup.find_all("div",{"class": "-job"})
    for html in job_div:
     job_info = extract_job_SO(html)
     jobs.append(job_info)
  return jobs

def get_jobs(word):
  STACKOVERFLOW_URL=f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page_SO(STACKOVERFLOW_URL)
  if last_page == -1:
    return
  jobs = extract_jobs_from_html_SO(last_page,STACKOVERFLOW_URL)
  return jobs