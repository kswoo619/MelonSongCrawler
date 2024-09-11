from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
import csv
import datetime as dt

driver = webdriver.Chrome()
url = 'https://www.melon.com/new/index.htm'
try:
    response = driver.get(url)
except Exception as e:
    print(e)

songlink = []
for i in range(1, 51, 50):
    driver.execute_script("javascript:pageObj.sendPage('%d');" % i)
    time.sleep(2)
    btn = driver.find_elements(By.CLASS_NAME, 'btn.button_icons.type03.song_info')
    for l in btn:
        songlink.append(l.get_attribute('href'))
    
today = dt.datetime.now().strftime('%Y.%m.%d')
filename = f"Songdata_{today}.csv"
with open(filename, 'w+', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['num', 'song', 'artist', 'album', 'date', 'genre', 'lyric'])

    for i, link in tqdm(enumerate(songlink)):
        tmp = []
        try:
            driver.execute_script(link)
            time.sleep(2)
        except Exception as e:
            print('error', e)
            break
        try:
            tmp.append(i)
            tmp.append(driver.find_element(By.CLASS_NAME, 'song_name').text)
            tmp.append(driver.find_element(By.CLASS_NAME, 'artist').text)

            for i in range(2, 8, 2): # album, date, genre
                txt = driver.find_element(By.CSS_SELECTOR, f'#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child({i})').text
                tmp.append(txt)
            
            try:
                txt = driver.find_element(By.CLASS_NAME, 'lyric').text
            except:
                txt = driver.find_element(By.CLASS_NAME, 'lyric_none').text
                tmp.append('No Lyric')
            tmp.append(txt)

        except Exception as e:
            print(i, e)
            writer.writerow(tmp)
            break

        writer.writerow(tmp)
    else:
        print('Crawling Success!')