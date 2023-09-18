#!/usr/bin/env python
# coding: utf-8

# # List down all the Public and Private Repositories

# In[1]:


# !pip install requests
# !pip install pygithub


# In[ ]:


import requests

# Replace these with your GitHub username and personal access token
username = "YOUR_USERNAME"
access_token = "YOUR_ACCESSTOKEN"

# Define the API endpoint for listing user repositories, including public ones
url = f"https://api.github.com/user/repos?type=public"

# Set up headers with the access token for authentication
headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json"  # Specify API version
}

# Send a GET request to the GitHub API to list public repositories
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repositories = response.json()

    # Print the names of your public repositories
    print("Your public GitHub repositories:")
    for index, repo in enumerate(repositories):
        print(f"{index + 1}. {repo['name']}")
else:
    print(f"Failed to retrieve public repositories. Status code: {response.status_code}")
    
    

    
# Define the API endpoint for listing user repositories, including private ones
url = f"https://api.github.com/user/repos?type=private"

# Set up headers with the access token for authentication
headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json"  # Specify API version
}

# Send a GET request to the GitHub API to list private repositories
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repositories = response.json()

    # Print the names of your private repositories
    print("Your private GitHub repositories:")
    for index, repo in enumerate(repositories):
        print(f"{index + 1}. {repo['name']}")
else:
    print(f"Failed to retrieve private repositories. Status code: {response.status_code}")


# In[ ]:




