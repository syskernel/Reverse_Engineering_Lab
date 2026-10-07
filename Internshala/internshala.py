import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
    }
url = "https://internshala.com/jobs/"
page = 0
job_details = []

while True:
    page += 1
    print(f"Fetching Page {page}", url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        try:
            for d in soup.body.find_all('div', class_="logged_out_jd_summary"):
                title = d.a.text.strip()                                            # Title
                company = d.p.text.strip()                                          # Company Name
                hiring_class = d.find('div', class_="actively-hiring-badge")        # Hiring
                if hiring_class is None:
                    hiring = 'N/A'
                else:
                    hiring = hiring_class.text.strip()

                row_1 = d.find('div', class_="detail-row-1")
                locations = []                                                      # Location
                for a in row_1.find_all('a'):
                    location = a.text.strip()
                    locations.append(location)
                locations = ", ".join(locations)    

                row_2 = row_1.find_all('div', class_="row-1-item")
                try:
                    salary = row_2[0].find('span', class_="desktop").text.strip()             # Salary
                except AttributeError:
                    salary = 'N/A'

                experience = row_2[1].text.strip()                                          # Experience    

                responsibility = d.find('div', class_="about_job").text.removeprefix('Key Responsibilities:')       # Reponsibility
                responsibility = " ".join(responsibility.split())                   

                skills = []                                                             # Skills
                for skl in d.find_all('div', class_='job_skill'):                       
                    skill = skl.text.strip()
                    skills.append(skill) 
                skills = ", ".join(skills)  

                published = d.find('div', class_="color-labels").text.strip()           # Published
                published = " ".join(published.split()) 

                job_details.append({
                    "TITLE" : title,
                    "COMPANY NAME" : company,
                    "CURRENT STATUS" : hiring,
                    "LOCATION" : locations,
                    "SALARY" : salary,
                    "EXPERIENCE" : experience,
                    "RESPONSIBILITIES" : responsibility,
                    "REQUIRED SKILLS" : skills,
                    "PUBLISHED" : published
                })

        except Exception as e:
            print(f"Unexpected error on page {page}: {e}")

        next_url = soup.find(id="navigation-forward-mobile").get('href')
        if next_url == None:
            break
        else:
            url = "https://internshala.com" + next_url
    else:
        print(f"Error {response.status_code} : {response.text}")

df = pd.DataFrame(job_details)
df.to_excel('jobdetails.xlsx', index= False)
print("Successfully fetched all pages and stored in the excel file!")