import os
from dotenv import load_dotenv
import google.generativeai as genai

from app.utils.get_blogs import crawl_blog



load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


async def get_summary(blog_url):
    blog = crawl_blog(url=blog_url)

    model = genai.GenerativeModel("gemini-1.5-pro-002")
    response = model.generate_content(f"Provide the summary of the given blog in which you get the blog title and the content. \n {blog}")
    print("Summary: ", response.text)
    
    return response.text
    