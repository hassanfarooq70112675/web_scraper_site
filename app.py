from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    print("Index route accessed")
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    print("Scrape route accessed")
    url = request.form['url']
    print(f"Scraping URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    with open('website_content.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    return 'Scraping complete. Check the website_content.txt file.'

if __name__ == '__main__':
    app.run(debug=False)
    



