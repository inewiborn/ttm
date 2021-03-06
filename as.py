#!/usr/bin/env python3

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

from bs4 import BeautifulSoup

from lib.app.Registry import Registry

r = Registry()
auth = HTTPBasicAuth(
    r.get_option('login'),
    r.get_option('password')
)

r = requests.post(url="https://office.techart.ru/home/tasks/", auth = auth)

print(r.text)

soup = BeautifulSoup(r.text, 'lxml')

tasks = soup.findAll('div', {'class': 'task-wrapper'})

for task in tasks:
    text = task.find('div', {'class': 'task-text'})
    #print(text.get_text())
    project = task.find('div', {'class': 'trail'})
    print(project.a['href'])
    print(project.get_text())
