import os
import requests
# Dropbox URLs for required files
MISA_DS_URL = "https://www.dropbox.com/scl/fi/59ypmunnxai36c1rn1ury/MISA_ds_2.0.6.nc.zip?rlkey=fh4f9o71ffh94h9n9da93lxf3&st=l6221tjs&dl=1"
GEO_DS_URL = "https://www.dropbox.com/scl/fi/d5bpuc0w1lpagqvi70gea/master_geo_ds_2.0.6.nc?rlkey=g2m2jn5woavpbs1go20dt52xv&st=71jvwffu&dl=1"


# Paths to save downloaded files
MISA_DS_PATH = "ancillary/processed_ncs/MISA_ds_2.0.6.nc"
MASTER_GEO_DS_PATH = "ancillary/processed_ncs/master_geo_ds_2.0.6.nc"


# Utility to download files from Dropbox
def download_file(url, save_path):
    """Download a file from a URL if it doesn't exist locally."""
    if not os.path.exists(save_path):
        print(f"Downloading file from {url}...")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):  # 8 KB chunks
                    f.write(chunk)
            print(f"File downloaded and saved to {save_path}.")
        else:
            raise RuntimeError(f"Failed to download file. HTTP Status Code: {response.status_code}")
        
# Download required files
download_file(MISA_DS_URL, MISA_DS_PATH)
#unzip the downloaded file
import zipfile
with zipfile.ZipFile(MISA_DS_PATH, 'r') as zip_ref:
    zip_ref.extractall(os.path.dirname(MISA_DS_PATH))
download_file(GEO_DS_URL, MASTER_GEO_DS_PATH)