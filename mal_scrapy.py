
from unicodedata import name
from urllib import response
import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://myanimelist.net/topanime.php')

#print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('h3') #find all h3 tags. Which is where the info is stored

""" for link in links:
    print(link.a.text) #print the text of the link AKA the title of the anime
    print(link.a['href']) #print the link to the anime page """


#* This function gets the synopsis of the anime 
#* and then returns it as a string so it can be saved to a file
def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    synopsis = soup.find('p', itemprop='description').text
    #print(synopsis)
    return synopsis

def get_ranking(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ranking = soup.find('div', class_='score-label').text
    return ranking

def get_name(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('h1', class_='title-name').text
    return name


#* This function saves the info we got from the get_info function to a file
def save_to_file(Anime_info):
    with open('anime_info.txt', 'a') as f:
        f.write(Anime_info[0] + '\n')
        f.write(Anime_info[1] + '\n')
        f.write(Anime_info[2] + '\n')



short_list = [links[0],links[1],links[3]]
def main():
    for link in short_list:  #! Change this out with link in links after testing
        Anime_info = []
        url = link.a['href']
        name = get_name(url)
        info = get_info(url)
        ranking = get_ranking(url)
        Anime_info.append("Name of Anime: " + name)
        Anime_info.append("MAL Score: " + ranking)
        Anime_info.append("Anime Synopsis: " + info)
        
        save_to_file(Anime_info)
    


#get_info('https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood')

#* Call the main function
main()

  
    
#! Open Browser
#! Go to https://myanimelist.net/topanime.php   
#! Sort through each link 
#! Get the info off the page for each anime and save it to a file
    