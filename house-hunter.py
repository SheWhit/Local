import time
import signal
import docx
from docx import Document
import re
import PyDictionary
import json
from bs4 import BeautifulSoup
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_UNDERLINE
# from selenium import JavascriptExecutor




# TODO: Pull Unique list of terms to look for
final_list_of_sentences = []
test = True
text_file = open("keywords.txt", "r")
keywords = text_file.read()
# keywords = json.loads(keywords)
# skippable = keywords['skippable']
# possitive_verb = keywords['possitive_verb']
# negative_verb = keywords['negative_verb']
# possitive_noun = keywords['possitive_noun']
# negative_noun = keywords['negative_noun']
# possitive_adjective = keywords['possitive_adjective']
# negative_adjective = keywords['negative_adjective']
# possitive_adverb = keywords['possitive_adverb']
# negative_adverb = keywords['negative_adverb']
# conjunctions = keywords['conjunctions']
link_file = open('link_list.txt', 'r')
list_of_links = link_file.read()
list_of_links = json.loads(list_of_links)
company = ''
job_title = ''
skill = ''

# submitted = list_of_links['submitted']



def ask_to_add_word_to_list(word, definition, type):
    print(definition)
    repeat = True
    while repeat:
        answer = input(f'Do you want to add \"{word}\" to the list? ({type})[g/b]')
        if answer in ['G', 'g', 'B', 'b', '', 'skip']:
            repeat = False
        if answer in ['G', 'g']:
            return True
        if answer in ('b', 'B'):
            return False
        if answer in ['skip', '']:
            return 'Skip'

import json
import re

def get_html_content():
    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get("https://www.trulia.com/County/UT/Salt_Lake_Real_Estate/")
    new = driver.page_source
    soup = BeautifulSoup(new, 'html.parser')
    something = soup.find_all("div", attrs={"data-testid": "search-result-list-container"})
     for value in something:
        print(value)
    # thingy3 = json.loads(thingy2)
    # thingy = soup.body.find_all(attrs={"data-testid": "search-result-list-container"})
    # thingy2 = soup.find_all(attrs={"data-hero-element-id": "srp-home-card"})

    # list_of_job_urls = []

    # search_box = driver.find_element_by_name('q')
    # search_box.send_keys('Software Developer')
    # search_box.submit()


if __name__ == "__main__":
   get_html_content()
