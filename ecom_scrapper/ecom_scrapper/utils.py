import os
import pandas as pd

def read_domains(file_path):
    """Reads domains from a text file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def write_to_csv(data, output_file):
    """Writes the crawled data to a CSV file."""
    df = pd.DataFrame(data, columns=['Domain', 'ProductURL'])
    df.to_csv(output_file, index=False)
