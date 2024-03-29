#!/usr/bin/python3
''' export data in the JSON format '''
import json
import requests
import sys


if __name__ == "__main__":

    userNameRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    users = userNameRequest.json()

    dataDict = {}

    for user in users:
        userId = user["id"]
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                userId))
        todos = response.json()

        dataDict[str(user["id"])] = []
        for todo in todos:
            dataDict[str(user["id"])].append({
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dataDict, f)
