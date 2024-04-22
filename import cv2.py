import requests
from bs4 import BeautifulSoup
import os

# Function to download images from a webpage
def download_images(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Create a directory to save images
    os.makedirs('downloaded_images', exist_ok=True)
    
    # Download each image
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            img_filename = os.path.basename(img_url)
            img_path = os.path.join('downloaded_images', img_filename)
            # Use wget to download the image
            os.system(f'wget {img_url} -O {img_path}')
            print(f'Downloaded: {img_url}')

# Example URL
url = input("https://www.freepik.com/premium-photo/close-up-squirrel-eating-food_101002920.htm#position=2: ")

# Call the function to download images
download_images(url)
