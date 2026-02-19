#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder API and optionally print or save them."""

import requests
import json
import csv


def fetch_and_print_posts():
    """Fetch posts and print their titles along with HTTP status code."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()

    print(f"Status Code: {response.status_code}")

    posts = response.json()

    for post in posts:
        print(post['title'])


def fetch_and_save_posts():
    """Fetch posts and save them as a CSV file named 'posts.csv'."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()

    posts = response.json()

    list_posts = []

    for post in posts:
        list_posts.append({
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        })

    with open("posts.csv", 'w', newline="", encoding="utf-8")as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

        writer.writeheader()
        writer.writerows(list_posts)
