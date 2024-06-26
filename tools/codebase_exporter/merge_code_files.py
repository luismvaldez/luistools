import os
import csv
import argparse
from typing import List, Set
import nltk

def list_files(dir_path: str, ignore_list: Set[str], file_extensions: Set[str], exclude_files: List[str]) -> List[str]:
    """List files in dir_path excluding directories in ignore_list, files not ending with specified extensions, and specific files to exclude."""
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs if d not in ignore_list]
        for file in files:
            if file.split('.')[-1] in file_extensions and not any(file.endswith(exclude) for exclude in exclude_files):
                file_list.append(os.path.join(root, file))
    return file_list

def read_files(file_list: List[str]) -> str:
    """Read and concatenate the content of each file in file_list, separated by a header."""
    combined_content = ''
    for file_path in file_list:
        with open(file_path, 'r', errors='ignore') as f:
            combined_content += f'{"="*50}\n{file_path}\n{"="*50}\n{f.read()}\n'
    return combined_content

def write_to_file(content: str, output_path: str) -> None:
    """Write content to a file at output_path."""
    with open(output_path, 'w') as f:
        f.write(content)

def read_filenames_from_csv(csv_path: str) -> List[str]:
    """Read filenames from a CSV file at csv_path."""
    filenames = []
    with open(csv_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader, None)  # Skip the header row
        filenames = [row[0] for row in csv_reader]
    return filenames

def count_tokens(file_path: str) -> int:
    """Count tokens in a text file using NLTK tokenizer."""
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
        tokens = nltk.word_tokenize(content)
        return len(tokens)

def write_filenames_to_csv(file_list: List[str], csv_path: str) -> None:
    """Write each file path and its token count to a CSV file at csv_path."""
    with open(csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Filename', 'Token Count'])
        for file_path in file_list:
            token_count = count_tokens(file_path)
            csv_writer.writerow([file_path, token_count])

def merge_code_files(input_directory: str, output_file: str, csv_file: str = None, export_csv: str = None, ignore_list: Set[str] = None, file_extensions: Set[str] = None, exclude_files: List[str] = None) -> None:
    """Merge code files into a single file, prioritizing files listed in a CSV file if provided."""
    if csv_file:
        file_list = read_filenames_from_csv(csv_file)
    else:
        file_list = list_files(input_directory, ignore_list, file_extensions, exclude_files)
    
    combined_content = read_files(file_list)
    write_to_file(combined_content, output_file)
    
    if export_csv:
        write_filenames_to_csv(file_list, export_csv)

def main() -> None:
    """Entry point of the script, handling command-line arguments."""
    parser = argparse.ArgumentParser(description='Merge code files into a single file.')
    parser.add_argument('-d', '--dir', default='.', help='Directory to search for code files (default: current directory)')
    parser.add_argument('-o', '--output', default='merged_code.txt', help='Output file path (default: merged_code.txt)')
    parser.add_argument('-c', '--csv', help='CSV file containing filenames to include (optional)')
    parser.add_argument('-e', '--export-csv', help='Export filenames to a CSV file (optional)')
    parser.add_argument('--extensions', nargs='*', help='List of file extensions to include (e.g., py ts java)', default=['py', 'ts', 'md', 'java', 'c', 'cpp', 'cxx'])
    parser.add_argument('--exclude-files', nargs='*', help='List of filenames to exclude (e.g., dto.ts spec.ts)', default=[])
    args = parser.parse_args()

    ignore_list = {'node_modules', '__pycache__', '.git', '.vscode', 'objects', 'venv', 'logs', 'refs', 'hooks', 'env', 'build', 'dist', 'target'}
    file_extensions = set(args.extensions)
    exclude_files = args.exclude_files

    merge_code_files(args.dir, args.output, args.csv, args.export_csv, ignore_list, file_extensions, exclude_files)

    print(f'Code files merged successfully. Output file: {args.output}')
    if args.export_csv:
        print(f'Filenames and token counts exported to CSV file: {args.export_csv}')

if __name__ == '__main__':
    nltk.download('punkt')  # Download the punkt tokenizer if not already downloaded
    main()