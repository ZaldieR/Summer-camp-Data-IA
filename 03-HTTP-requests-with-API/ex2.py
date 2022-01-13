#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests

token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IjJMOXdiUnFMOVBwYzJ5aTk0VzhXa1dJNWI4UjFxa3l4THc3VGtzRmktWGciLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjIzODMwMjM1LCJuYmYiOjE2MjM4MzAyMzUsImV4cCI6MTYyMzgzNDEzNSwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsidXJuOnVzZXI6cmVnaXN0ZXJzZWN1cml0eWluZm8iLCJ1cm46bWljcm9zb2Z0OnJlcTEiLCJ1cm46bWljcm9zb2Z0OnJlcTIiLCJ1cm46bWljcm9zb2Z0OnJlcTMiLCJjMSIsImMyIiwiYzMiLCJjNCIsImM1IiwiYzYiLCJjNyIsImM4IiwiYzkiLCJjMTAiLCJjMTEiLCJjMTIiLCJjMTMiLCJjMTQiLCJjMTUiLCJjMTYiLCJjMTciLCJjMTgiLCJjMTkiLCJjMjAiLCJjMjEiLCJjMjIiLCJjMjMiLCJjMjQiLCJjMjUiXSwiYWlvIjoiQVVRQXUvOFRBQUFBalFhaEUrSi9pZnRzVGdJckRoY2RpSUlWMlFoMTBSNXkyZDNYemlNOWtoSjBnV3RtdzJ3TFdVa1IrdVliT0N5cnRJVFJlamVta213eU94dkw0dE9ua0E9PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggZXhwbG9yZXIgKG9mZmljaWFsIHNpdGUpIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkxvcmVuem8iLCJnaXZlbl9uYW1lIjoiTWF0aGlzIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiOTIuMTY3LjQxLjIxMyIsIm5hbWUiOiJNYXRoaXMgTG9yZW56byIsIm9pZCI6IjRjOGI0YjdiLThhNTItNDg3NC05NGFkLWM4NDk4NjE5OGVlZiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS0zNzY2NiIsInBsYXRmIjoiMTQiLCJwdWlkIjoiMTAwMzIwMDA3QTRCQUE3MCIsInJoIjoiMC5BWFFBeXJRY2tHSzRLVUNUQnVYTkQyMmZoclhJaTk3NTJiRklxSzIzU05weVVHUjBBR2cuIiwic2NwIjoiR3JvdXAuUmVhZC5BbGwgR3JvdXAuUmVhZFdyaXRlLkFsbCBvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWQgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJSQW50TW55MmJVQ1hDaTIxSndCWXIwQXN5SG9CRTdzUVhrTVg0UmMtRTNjIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkVVIiwidGlkIjoiOTAxY2I0Y2EtYjg2Mi00MDI5LTkzMDYtZTVjZDBmNmQ5Zjg2IiwidW5pcXVlX25hbWUiOiJtYXRoaXMubG9yZW56b0BlcGl0ZWNoLmV1IiwidXBuIjoibWF0aGlzLmxvcmVuem9AZXBpdGVjaC5ldSIsInV0aSI6Inc3UlRydVduOEVpNWg5MjZkbnd3QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiNkpfTWhOTGh4SGhvd1BIWjF5NV9aWjNWaDZsNUJyLVRsQWtlNm8weEZiQSJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.kkBZlgghio0gK5Ii0IGYYb-4V5OwtV2zO5s2ijNbqa-X_WQQgQU9BE5StXiwlpc5RrwECg_xTkOaQ0low2HktT3ara9UhwaSeunZeOGssAu5k-QggXmg87gmoRx0Pnwy9TnsE1kQ9gA1CMLhzUi18DM37tEq5R7W-GNSyX5MLoyAJ3Cj1d4JminaFac2tgzih3IVxRl63I57LPe966PyA33hZWp1X9vP8SlgmPu7uXh49s5BnPJV1ewCuHXdR35haX-dMLjcHXm3tFSGX0JSu5do5SQ6RKqdcSxJ6oIXGRXRVDW8XG-4i-c7jWmeuA_uBPcYFdaEAopMff4I9aPTNw"


# In[7]:


url = f"https://graph.microsoft.com/beta/me/memberOf/"


# In[10]:


def member_of():
    res = {}
    url = "https://graph.microsoft.com/beta/me/memberOf/"
    content = requests.get(url, headers={'Authorization': token})
    data = content.json()
    for i in data['value']:
        res[i['displayName']] = i['id']
    return res

teams = member_of()
for name, id in teams.items():
    print(name, id)


# In[13]:


def get_channels(team_id):
    res = {}
    url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels"
    content = requests.get(url, headers={'Authorization': token})
    data = content.json()
    for i in data['value']:
        res[i['displayName']] = i['id']
    return res

channels = get_channels("c1995755-c035-4c13-bc82-6b65b5c1d206")
for name, id in channels.items():
    print(name, id)


# In[ ]:




