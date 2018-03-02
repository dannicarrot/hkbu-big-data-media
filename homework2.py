import requests
import csv
from bs4 import BeautifulSoup

list_name = []
list_score = []

def main(offset):
    resp = requests.get('https://www.pastemagazine.com/articles/music/reviews/?p='+str(offset))
    html_str = resp.text
    document = BeautifulSoup(html_str, 'html.parser')

    titles = document.find('ul', 'nof tagged-articles-list')
    titles = titles.find_all('li')
    for title in titles:
        name = title.find('a', attrs={'class': 'non title'})
        if isinstance(name, type(None)):
            continue
        list_name.append(name.text)

    grades = document.find('ul', 'nof tagged-articles-list')
    grades = grades.find_all('li')
    for grade in grades:
        score = grade.find('i', attrs={'class': 'number'})
        if isinstance(score, type(None)):
            continue
        list_score.append(score.text)
    print('len:', len(list_name))
    print('len:', len(list_score))

def write_file():
    with open("music.csv", 'w') as m:
        writer = csv.writer(m)
        for i in range(0,len(list_name)):
            name = list_name[i].encode('utf-8')
            score = list_score[i]
            writer.writerow([name,score])
        m.close()

if __name__ == '__main__':
    for i in range(10):
        main(offset= i+1)
        write_file()

