# Show_Github_Repos
A Python Script to display all of your Public and Private repositories using Personal Access Token 

# GitHub Repository Listing Script
This Python script is designed to retrieve and list both your public and private GitHub repositories using the GitHub API. It provides a convenient way to view your repositories directly from the command line.

## Prerequisites
Before running this script, ensure you have the following prerequisites in place:

1. **GitHub Account**: You need an active GitHub account.
2. 
3. **GitHub Personal Access Token**: Generate a GitHub Personal Access Token to authenticate with the GitHub API. Instructions on creating a token can be found [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). (Login to github, goto settings -> developer settings -> personal access token -> tokens(classic) -> click on "generate new token (classic)" -> tick the checkbox of "repo" -> click generate

4. **Python**: Ensure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

5. **Required Python Libraries**: Install the required Python libraries using the following command:
   pip install requests
   pip install pygithub

Usage:
1. Clone or download this repository to your local machine.

2. Open the Python script (github_repo_listing.py) in a text editor.

3. Replace the following variables in the script with your own values:
   username: Your GitHub username.
   access_token: Your GitHub Personal Access Token.

4. Save the script with your changes.

5. Open a editor or terminal or command prompt and navigate to the directory containing the script.

6. Run the script using the following command:
   python github_repo_listing.py

The script will make API requests to GitHub to list your public and private repositories and display them in the terminal.

License
This script is provided under the MIT License. You are free to use and modify it as needed.

Acknowledgments
This script utilizes the GitHub API to interact with your GitHub repositories. Special thanks to the GitHub team for providing this API.

Happy coding!
