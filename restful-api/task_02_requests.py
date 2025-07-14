#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        parsedJsonData = response.json()
        for i in parsedJsonData:
            print(i['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        parsedJsonData = response.json()

        listOfDict = []

        for i in parsedJsonData:
            item = {'id': i['id'], 'title': i['title'], 'body': i['body']}
            listOfDict.append(item)

        with open('posts.csv', 'w') as file:
            f = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            f.writeheader()
            f.writerows(listOfDict)
