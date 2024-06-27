from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup,Comment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


def remove_scripts(soup):
    for script in soup(["script", "style"]):
        script.extract()

    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()   

    return soup
@app.route("/submit", methods=['POST'])
def scrape_url():
    print("aaya")
    if request.method == "POST":
        url = request.form["url"]

        response = requests.get(url)
        if response.status_code == 200:
                html_content = response.text

                
                
                soup = BeautifulSoup(html_content, 'html.parser')

                soup = remove_scripts(soup)
                
                
                
                all_tags = soup.find_all(True)
                
                

                scraped_content = "".join(tag.get_text(separator='', strip=True) for tag in all_tags)
                
                return render_template("name.html",scraped_content=scraped_content)
        else:
            print(f'Failed to retrieve page: {response.status_code}')

    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 


