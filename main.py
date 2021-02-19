#BeautifulSoup4 have the algorithms and methods for us to scrape the website 
from bs4 import BeautifulSoup
# Allow us to make requests to the websites 
import requests
import time

print('Please note skills that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}...')

def find_jobs():
  # From here we direct where do we want to get the information
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

  #lxml is a Python library which allows for easy handling of XML and HTML files, and helps bs4 to parse the data (parse = analyze individualy)
  soup = BeautifulSoup(html_text, 'lxml')

  #Find_all scrapes throuth all the classes in the same page
  #The first 'li' tells the method to go directly to where there is a <li>
  jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

  #For loop into all the jobs 
  for index,  job in enumerate(jobs):
    published_date = job.find('span', class_='sim-posted').span.text

    #Only print those that has few on the post, meaning that we want posts that has been posted recently ( a few days ago )
    #.replace is to delete the ' ' spaces btw the commas
    if 'few' in published_date:
      company_name = job.find('h3', class_='joblist-comp-name').text
      skills = job.find('span', class_='srp-skills').text.replace(' ','')

      #When you .header you are entering the header and if you do .h2 you entering h2
      #When you click into the post it will show the job description and here we are providingt he link of the full description of the job
      more_info = job.header.h2.a['href']
      if unfamiliar_skills not in skills:
        #.strip makes the strings align nicely when we print it ( they must be strings)
        with open(f'posts/{index}.txt', 'w') as f: 
          f.write(f"Company Name: {company_name.strip()}\n")
          f.write(f"Required Skills: {skills.strip()}\n")
          f.write(f'More Info: {more_info}\n')
          print(f'File saved: {index}')

#Exporting out into a file
if __name__ == '__main__':
  while True:
    find_jobs()
    time_wait = 10
    print(f'Wainting {time_wait} minutes...')
    time.sleep(time_wait * 60)