from operator import itemgetter

import requests

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

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comment: {submission_dict['comment']}")