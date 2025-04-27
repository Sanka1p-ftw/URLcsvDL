import requests
file_url = 'https://raw.githubusercontent.com/Sanka1p-ftw/URLcsvDL/4f630f3b3735e3d71a8e4bb77fd9398601b7f0f6/netflix_titles.csv'
response = requests.get(file_url)
with open('downloaded_netflix_titles.csv', 'wb') as file:
	file.write(response.content)
print("Dataset downloaded successfully!")