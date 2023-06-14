import requests

def conn(host:tuple):
    return requests.get(
                f'http://{host[0]}:{host[1]}/conn', 
                headers={'User-Agent': 'MindKingClient'}, 
                timeout=5
            )