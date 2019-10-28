import requests
# make an Api and store the response
# step 1 we import the requests model
# step 2 enter the url which we have to call
# step 3 store the request in variable r
# step 4 print the status code
# step 5 then we store the r.json in aanother variable
# step 6 printing the response key
# step 7 status code 200 means the call made succesfully and the keys has obtained.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code: ',r.status_code)
# store API response in variable
response_dict = r.json()
# process results
print(response_dict.keys())

# working with the response repository
print('total repository:',response_dict['total_count'])
# exploring information about the repositories
repo_dicts = response_dict['items']
print('repository returned: ',len(repo_dicts))
# examine the directory
repo_dict = repo_dicts[0]
print('\nkeys: ',len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
    
# total_count represent the total number of python repositories in github
# The value associated with 'items' is a list containing a number of dictionaries
# we store this list of dictionaries in repo_dicts. We then print the
# length of repo_dicts to see how many repositories we have information for
# We then print the number of keys in the dictionary to see how much information we have
# we print all of the dictionary’s keys to see what kind of information is included.

print('\nSelected information about the first repository: ')
print('name: ',repo_dict['name'])
print('id: ',repo_dict['id'])
print('owner: ',repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
print('forks_count:', repo_dict['forks_count'])

print('\nSelected information about each repository: ')
for repo_dict in repo_dicts:
    
    print('\nName: ',repo_dict['name'])
    print('id: ',repo_dict['id'])
    print('owner: ',repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    print('forks_count:', repo_dict['forks_count'])

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code: ',r.status_code)
# store API response in variable
response_dict = r.json()
print('total repository: ',response_dict['total_count'])
# explore information about the society
repo_dicts = response_dict['items']

names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# Make visualization.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')