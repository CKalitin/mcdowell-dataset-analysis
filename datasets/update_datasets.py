import requests
import os

urls = [
    "https://planet4589.org/space/gcat/tsv/cat/auxcat.tsv",
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
        
# Print launch dataset date updated
launch_file_path = os.path.join(save_directory, "launch.tsv")
if os.path.exists(launch_file_path):
    with open(launch_file_path, 'r') as file:
        file.readline() # Skip first line
        date = " ".join(file.readline().strip().replace("  ", " ").split(" ")[2:5])
        print(f"Launch dataset cutoff: {date}")