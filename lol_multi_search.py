from selenium import webdriver
from bs4 import BeautifulSoup

user_input = []
for i in range(5):
    user_input.append(input(''))

browser = webdriver.Chrome()
browser.get('https://your.gg/kr/ai/multisearch')
browser.maximize_window()

browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[3]/div/form/div[1]/div/textarea').send_keys(user_input)
browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[3]/div/form/div[2]/div/button').click()

soup = BeautifulSoup(browser.page_source, 'lxml')

text = soup.find_all('div',attrs={'class':'card-body'})
print(text[1].get_text())

