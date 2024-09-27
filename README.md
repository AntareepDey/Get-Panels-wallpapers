## Get-Panels-wallpapers
A few days ago, a popular YouTuber released an app called *Panels*, showcasing stunning HD wallpapers. However, excitement quickly turned to outrage when users discovered that the app required pricey in-app purchases to unlock these wallpapers. It didn’t take long for the internet to expose a little secret—these wallpapers were publicly accessible in a Google Cloud bucket all along!

This script is your **free pass** to those beautiful HD wallpapers without breaking the bank. By crawling the storage bucket URL, this app fetches all the high-definition wallpapers directly to your machine, no fees or subscriptions required. Whether you're looking to refresh your desktop background or gather some stunning visuals, this app lets you grab as many wallpapers as you want.

### Why You’ll Love This Script:
- **Free Access to HD Wallpapers**: Forget about expensive apps—the wallpapers are out there, and now, they’re yours for free.
- **Easy to Use**: No need for complex setups—just run the script and start enjoying a treasure trove of wallpapers.

**Warning**: This script will keep working as long as the wallpaper links remain publicly available. If the links are taken down, don’t worry—I’ve already indexed them locally, and I’ll update the repository to ensure you’re never left hanging.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone or download this repository** to your local machine:
    ```bash
    git clone AntareepDey/Get-Panels-wallpapers
    ```

### Windows Setup

1. Ensure that Python is installed. You can verify by running:
    ```bash
    python --version
    ```

2. Install dependencies using the following command in `cmd` or `PowerShell`:
    ```bash
    pip install requests
    ```

### macOS/Linux Setup

1. Ensure Python 3 is installed. You can verify by running:
    ```bash
    python3 --version
    ```

2. Install dependencies:
    ```bash
    pip3 install requests
    ```
    

## Usage

1. **Change the Output Directory**:
    By default, images will be saved to the `wallpapers` folder. If you want to change this, modify the `output_folder` variable in the `main()` function:

    ```python
    output_folder = 'your_output_folder'
    ```

    For example, to save the images to a folder named `images`, update it as:

    ```python
    output_folder = 'images'
    ```

2. **Run the Script**:
    Execute the script as described in the installation steps above (based on your OS).

    For example:
    ```bash
    python3 download-walls.py  # For macOS/Linux
    python download-walls.py   # For Windows
    ```

3. **Download Progress**:
    The script will print the status of each image as it downloads. If there is an error downloading a particular image, it will print an error message.

    Example:
    ```
    Downloaded: image1.png
    Error downloading http://example.com/image2.png: 404 Client Error: Not Found
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
