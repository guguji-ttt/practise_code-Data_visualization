import requests

from plotly.graph_objs import Bar
from plotly import offline

#执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status_code: {r.status_code}")

#处理结果
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

#可视化
data = [{
    'type': 'bar',
    'x': repo_links, 
    'y': stars,
    'hovertext': labels,
    'marker':{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)',}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': {
        'text': 'Github上最受欢迎的Python项目', 
        'font': {'size': 28},
        },
    'xaxis': {
        'title': {'text':'Repository',
                  'font':{'size': 24},},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': {'text':'Stars',
                  'font': {'size': 24},},
        'tickfont': {'size': 14}
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='chart/python_repos_ppp.html')