import urllib.request, json


def auto_insert_nightorder(in_json):

    with urllib.request.urlopen("https://script.bloodontheclocktower.com/data/nightsheet.json") as url:
        data = json.load(url)
        print(data)