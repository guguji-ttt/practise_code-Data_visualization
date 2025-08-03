import requests

#执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status_code: {r.status_code}")
#将API响应赋给一个变量。
response_dict = r.json()

#展示r对象的键值
#print(response_dict.keys())

print(f"Total Repositories: {response_dict['total_count']}")

#探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")



'''
#研究第一个仓库
repo_dict = repo_dicts[0]
#展示第一个仓库的键值（即选项标题）
print(f"\nKeys:{len(repo_dicts)}")
for key in sorted(repo_dict.keys()):
    print(key)
'''
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Update: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")