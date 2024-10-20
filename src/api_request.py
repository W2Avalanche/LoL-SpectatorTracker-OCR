import requests

def get_current_time():
    response = requests.get("https://127.0.0.1:2999/liveclientdata/gamestats", verify=False).json()
    return response["gameTime"]