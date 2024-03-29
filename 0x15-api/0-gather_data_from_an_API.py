#!/usr/bin/python3
''' api fetch '''
import requests
import sys


if __name__ == "__main__":
    userNameRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            sys.argv[1]
        )
    )
    userName = userNameRequest.json()["name"]
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            sys.argv[1]
        )
    )
    json = response.json()

    lists = []
    did = 0
    count = 0

    for idx in json:
        if idx["completed"]:
            lists.append(idx["title"])
            did += 1
        count += 1

    print("Employee {} is done with tasks({}/{}):".format(userName, did, count)
          )

    for idx in lists:
        print("\t " + idx)
