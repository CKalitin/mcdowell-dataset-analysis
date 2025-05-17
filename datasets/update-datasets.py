import requests
import os

urls = [
    "https://planet4589.org/space/gcat/tsv/launch/launch.tsv",
    "https://planet4589.org/space/gcat/tsv/tables/lv.tsv",
    "https://planet4589.org/space/gcat/tsv/tables/orgs.tsv",
    "https://planet4589.org/space/gcat/tsv/cat/psatcat.tsv",
    "https://planet4589.org/space/gcat/tsv/cat/satcat.tsv",
    "https://planet4589.org/space/gcat/tsv/tables/sites.tsv",
]

# Get the directory of the current script
save_directory = os.path.dirname(os.path.abspath(__file__))

for url in urls:
    # Extract the file name from the URL
    file_name = os.path.basename(url)
    file_path = os.path.join(save_directory, file_name)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Save the file
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except OSError as e:
        print(f"Error saving {file_name}: {e}")