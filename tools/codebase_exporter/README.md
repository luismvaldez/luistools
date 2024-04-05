
# Codebase Exporter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

Code File Merger is a Python script that allows you to merge multiple code files into a single file while providing useful features such as file exclusion and CSV export with filenames exported from the codebase. It supports various programming languages and file extensions.

## Features

- Merge multiple code files into a single file
- Exclude specific directories, files, and file extensions
- Prioritize files listed in a CSV file
- Export file paths to a CSV file
- Use exported CSV file as input to include only specific files and exclude others

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/code-file-merger.git
   ```

2. Install the required dependencies using `requirements.txt`:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

```shell
python code_file_merger.py [-h] [-d DIR] [-o OUTPUT] [-c CSV] [-e EXPORT_CSV]
                           [--extensions EXTENSIONS [EXTENSIONS ...]]
                           [--exclude-files EXCLUDE_FILES [EXCLUDE_FILES ...]]
```

### Arguments

- `-d DIR, --dir DIR`: Directory to search for code files (default: current directory)
- `-o OUTPUT, --output OUTPUT`: Output file path (default: merged_code.txt)
- `-c CSV, --csv CSV`: CSV file containing filenames to include (optional)
- `-e EXPORT_CSV, --export-csv EXPORT_CSV`: Export filenames to a CSV file (optional)
- `--extensions EXTENSIONS [EXTENSIONS ...]`: List of file extensions to include (default: py, ts, md, java, c, cpp, cxx)
- `--exclude-files EXCLUDE_FILES [EXCLUDE_FILES ...]`: List of filenames to exclude (default: dto.ts, spec.ts, type.ts, types.ts)

### Examples

- Merge code files and export file paths to a CSV file:

  ```shell
  python code_file_merger.py -d /path/to/code/directory -o merged_code.txt -e filenames.csv
  ```

- Use exported CSV file to include only specific files and exclude others:

  ```shell
  python code_file_merger.py -d /path/to/code/directory -o merged_code.txt -c filenames.csv
  ```
