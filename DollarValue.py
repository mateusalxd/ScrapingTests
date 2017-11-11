#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://economia.uol.com.br/cotacoes/cambio/dolar-comercial-estados-unidos/"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

browser = webdriver.Chrome(executable_path = "/home/mateus/bin/browsers-drivers/chromedriver", chrome_options = chrome_options)
browser.get(url)

element = browser.find_element_by_class_name("infoTable")
print(element.text)

browser.close()
