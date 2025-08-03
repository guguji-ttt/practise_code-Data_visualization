from operator import itemgetter

import requests

from plotly.graph_objs import Bar, Layout
from plotly import offline

#执行API调用并储存响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status_code: {r.status_code}")

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #对于每篇文章，都执行一个API调用
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    #返回码确认调用正确
    print(f"Status_code: {r.status_code}")
    response_dict = r.json()
    
    #对于每篇文章，都创建一个字典
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comment': response_dict['descendants'],
        }
    
    #添加进总字典
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comment'), 
                          reverse=True)

title_links, Comment_lists = [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    title_url = submission_dict['hn_link']
    title_link = f"<a href='{title_url}'>{title}</a>"
    title_links.append(title_link)
    Comment_lists.append(submission_dict['comment'])
    
x_values = title_links
y_values = Comment_lists
#可视化
data = [{
    'type': 'bar',
    'x': x_values, 
    'y': y_values,
    'marker':{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)',}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': {
        'text': 'Hacker上最受欢迎的文章', 
        'font': {'size': 28},
        },
    'xaxis': {
        'title': {'text':'title',
                  'font':{'size': 24},},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': {'text':'comment_number',
                  'font': {'size': 24},},
        'tickfont': {'size': 14}
        },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='chart/hack_ar.html')