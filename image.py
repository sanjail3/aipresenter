from pexels_api import API
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the secret key from the environment variable

pixel_api=os.getenv("PIXELS_API")

pexels_api = API(pixel_api)



def get_image(topic):
    if not os.path.exists('images'):
        os.makedirs('images')
    photos = pexels_api.search(topic)
    for index, photo in enumerate(photos['photos'], start=1):
        image_url = photo['src']['large']
        image_id = photo['id']
        image_filename = f'images/{index}.jpg'  # Save the images in the "images" directory

        response = requests.get(image_url)
        response.raise_for_status()

        with open(image_filename, 'wb') as file:
            file.write(response.content)

        print(f"Image saved: {image_filename}")
