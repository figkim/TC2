from selenium import webdriver
from bs4 import BeautifulSoup
import os, time

driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')

driver.get('https://leetcode.com/problemset/all/?difficulty=Easy')

driver.find_element_by_xpath("//select[@class='form-control']/option[text()='all']").click()

prob_origin = 'https://leetcode.com'

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

prob_list = []

for prob_row in soup.select('tr')[1:]:
    if len(prob_row.select('td')) < 2:
        break
    prob_nums = prob_row.select('td')[1].text
    print(prob_nums)

    prob_name = prob_row.select('td')[2]['value']
    print(prob_name)

    prob_href = prob_row.select('td')[2].select('a')[0]['href']
    print(prob_origin + prob_href)

    prob_list.append((prob_nums, prob_name, prob_href))
    print()

for (prob_nums, prob_name, prob_href) in prob_list[36:]:
    driver.get(prob_origin + prob_href)
    time.sleep(30)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    try:
        prob = soup.select('div.content__u3I1')[0]        
    except:
        continue

    prob_dir = f'{int(prob_nums):03}_{prob_name.replace(" ", "_").lower()}'
    print(prob_dir)

    os.mkdir(f'../TC2/leetcode/2020/{prob_dir}')

    with open(f'../TC2/leetcode/2020/{prob_dir}/README.md', 'w') as f:
        f.write(f'{prob_origin+prob_href}\n\n')
        f.write(f'## {prob_nums}. {prob_name}\n\n')        
        for row in prob:
            f.write(str(row))
            f.write('\n')
