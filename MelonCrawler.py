from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
import csv
# songname, artist, album, date, genre, lyric

# open browser
driver = webdriver.Chrome()

for idx in tqdm(range(1, 452, 50)):
    url = f'https://www.melon.com/new/index.htm#params%5BareaFlg%5D=I&po=pageObj&startIndex={idx}'
    try:
        response = driver.get(url)
    except Exception as e:
        print(e)
        break

    songlink = []
    btn = driver.find_elements(By.CLASS_NAME, 'btn.button_icons.type03.song_info')
    for i in btn:
        songlink.append(i.get_attribute('href'))
    
    crawled_data = []
    for i, link in enumerate(songlink):
        tmp = []
        try:
            driver.execute_script(link)
            time.sleep(2)
        except Exception as e:
            print('error', e)
            continue
        
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

        crawled_data.append(tmp)

with open('newsong_0904.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['num', 'song', 'artist', 'album', 'date', 'genre', 'lyric'])

    for line in crawled_data:
        writer.writerow(line)