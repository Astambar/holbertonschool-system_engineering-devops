#!/usr/bin/python3
''' export to csv '''
import csv
import requests
import sys


if __name__ == "__main__":
    userRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1]))
    userName = userRequest.json()["username"]
    userId = userRequest.json()["id"]
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            sys.argv[1]))
    json = response.json()

    lists = []
    f = open('{}.csv'.format(userId), 'w')
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for idx in json:
        writer.writerow([userId, userName, idx["completed"], idx["title"]])
