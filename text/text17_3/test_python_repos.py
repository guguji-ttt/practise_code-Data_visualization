import requests
import pytest

def fetch_github_python_repos():
    """获取GitHub上Python仓库数据"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果请求失败会自动抛出异常
    return response.json(), response

def test_github_python_repos():
    """测试GitHub Python仓库API"""
    # 获取数据
    response_dict, r = fetch_github_python_repos()
    
    # 1. 测试状态码为200
    assert r.status_code == 200
    
    # 2. 测试返回的仓库总数大于某个值（假设至少10000个Python仓库）
    assert response_dict['total_count'] > 10000, "Python仓库总数应超过10000"
    
    # 3. 测试返回的条目数（默认返回30个）
    repo_dicts = response_dict['items']
    assert len(repo_dicts) == 30, "默认应返回30个仓库"
    
    # 4. 测试每个仓库都有必要的字段
    required_fields = {'name', 'html_url', 'stargazers_count', 'owner'}
    for repo in repo_dicts:
        assert all(field in repo for field in required_fields), f"仓库缺少必要字段: {required_fields}"
    
    # 5. 测试返回的仓库是按星标数降序排列的
    stars = [repo['stargazers_count'] for repo in repo_dicts]
    assert stars == sorted(stars, reverse=True), "仓库应按星标数降序排列"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])