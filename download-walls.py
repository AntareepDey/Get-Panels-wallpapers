import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def fetch_json(url):
    """
    Fetch JSON data from a given URL.
    
    Args:
        url (str): The URL to fetch JSON data from.
    
    Returns:
        dict or None: The JSON data as a dictionary if successful, None otherwise.
    """
    try:      
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Raise an exception for bad status codes

        return response.json()  # Return JSON data
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Error: The response is not valid JSON")
    
    return None

def extract_dhd_links(data):
    """
    Extract 'dhd' links from the JSON data.
    
    Args:
        data (dict): The JSON data.
    
    Returns:
        list: A list of 'dhd' links.
    """
    dhd_links = []
    
    if isinstance(data, dict) and 'data' in data:
        for item in data['data'].values():
            if isinstance(item, dict) and 'dhd' in item:
                dhd_links.append(item['dhd'])
    
    return dhd_links

def download_images(links, output_folder):
    """
    Download images from a list of URLs and save them to an output folder.
    
    Args:
        links (list): A list of image URLs.
        output_folder (str): The folder to save the downloaded images.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Download each image from the list of URLs
    for url in links:
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Extract the filename from the URL
            filename = os.path.basename(urlparse(url).path)
            
            # If the filename doesn't have an extension, add .png
            if not Path(filename).suffix:
                filename += '.png'

            # Save the image to the output folder
            output_path = os.path.join(output_folder, filename)
            with open(output_path, 'wb') as img_file:
                img_file.write(response.content)

            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

def main():
    """
    Main function to fetch JSON data, extract image links, and download images.
    """
    # URL of the JSON data
    url = "https://storage.googleapis.com/panels-api/data/20240916/media-1a-i-p~s"

    # Fetch the JSON data
    json_data = fetch_json(url)

    if json_data:
        # Extract image links from the JSON data
        wall_links = extract_dhd_links(json_data)
    else:
        print("Failed to fetch JSON data.")
        return

    # Output folder for the downloaded images
    output_folder = 'wallpapers_test'

    # Download images from the extracted links
    download_images(wall_links, output_folder)

# Run the main function
if __name__ == "__main__":
    main()