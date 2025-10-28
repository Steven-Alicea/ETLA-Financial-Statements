from pathlib import Path



def create_directory(directory):
    directory = Path(directory)
    directory.mkdir(parents=True ,exist_ok=True)

def get_sorted_csv_files(directory):
    directory = Path(directory)
    csv_files = list(directory.glob("*.csv"))
    csv_files.sort()
    return csv_files

def join_directory_and_file(directory, file_name):
    return Path(directory, file_name)
