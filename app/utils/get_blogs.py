import requests
from bs4 import BeautifulSoup

def crawl_blog(url):
    blog = None
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.content, 'html.parser')

        blog_title = soup.find('h1')  
        blog_content = soup.find('div')  

        if blog_title and blog_content:
            blog = "Title: " + blog_title.get_text(strip=True) + "\n" + "Content: " +blog_content.get_text(strip=True)
            return blog
        else:
            print("Couldn't find the blog title or content.")

    except requests.exceptions.RequestException as e:
        print("Error fetching the URL:", e)

# url = "https://medium.com/llm-study-diary-a-beginners-path-through-ai/comprehensive-review-of-langchain-part-1-4734d61a49e1"
# crawl_blog(url)