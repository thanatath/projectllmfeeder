import os
from pathlib import Path

def scan_project(directory):
    """Scan the project directory and return a list of relevant files."""
    # File extensions to include
    include_extensions = {'.vue', '.js', '.ts', '.json'}
    # Directories to exclude
    exclude_dirs = {'node_modules', '.nuxt', 'dist', '.git', '__pycache__'}

    relevant_files = []
    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            # Check if file has a relevant extension
            if Path(file).suffix in include_extensions:
                file_path = os.path.join(root, file)
                relevant_files.append(file_path)
    
    return relevant_files

def combine_files(files, output_file):
    """Combine contents of relevant files into a single Markdown file."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write a header for the combined file
        outfile.write("# NuxtJS Project Codebase\n\n")
        outfile.write("This file contains the concatenated source code of relevant files for LLM analysis.\n\n")

        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # Write file path as a header
                    relative_path = os.path.relpath(file_path)
                    outfile.write(f"## {relative_path}\n")
                    outfile.write("```")
                    # Add language identifier for syntax highlighting (optional)
                    ext = Path(file_path).suffix
                    lang = {
                        '.vue': 'vue',
                        '.js': 'javascript',
                        '.ts': 'typescript',
                        '.json': 'json'
                    }.get(ext, '')
                    if lang:
                        outfile.write(lang)
                    outfile.write("\n")
                    # Write file content
                    outfile.write(content)
                    outfile.write("\n```\n\n")
            except Exception as e:
                outfile.write(f"## {relative_path}\n")
                outfile.write(f"Error reading file: {str(e)}\n\n")

def main():
    # Set the project directory (current directory or specify your own)
    project_dir = "."  # Change to your project path if needed
    output_file = "project_for_llm.md"

    # Scan for relevant files
    print("Scanning project directory...")
    relevant_files = scan_project(project_dir)
    
    if not relevant_files:
        print("No relevant files found.")
        return
    
    print(f"Found {len(relevant_files)} relevant files:")
    for file in relevant_files:
        print(f"- {file}")
    
    # Combine files into one
    print(f"\nCombining files into {output_file}...")
    combine_files(relevant_files, output_file)
    print(f"Done! Combined file created at {output_file}")

if __name__ == "__main__":
    main()
import os
from pathlib import Path

def scan_project(directory):
    """Scan the project directory and return a list of relevant files."""
    # File extensions to include
    include_extensions = {'.vue', '.js', '.ts', '.json'}
    # Directories to exclude
    exclude_dirs = {'node_modules', '.nuxt', 'dist', '.git', '__pycache__'}

    relevant_files = []
    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            # Check if file has a relevant extension
            if Path(file).suffix in include_extensions:
                file_path = os.path.join(root, file)
                relevant_files.append(file_path)
    
    return relevant_files

def combine_files(files, output_file):
    """Combine contents of relevant files into a single Markdown file."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write a header for the combined file
        outfile.write("# NuxtJS Project Codebase\n\n")
        outfile.write("This file contains the concatenated source code of relevant files for LLM analysis.\n\n")

        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # Write file path as a header
                    relative_path = os.path.relpath(file_path)
                    outfile.write(f"## {relative_path}\n")
                    outfile.write("```")
                    # Add language identifier for syntax highlighting (optional)
                    ext = Path(file_path).suffix
                    lang = {
                        '.vue': 'vue',
                        '.js': 'javascript',
                        '.ts': 'typescript',
                        '.json': 'json'
                    }.get(ext, '')
                    if lang:
                        outfile.write(lang)
                    outfile.write("\n")
                    # Write file content
                    outfile.write(content)
                    outfile.write("\n```\n\n")
            except Exception as e:
                outfile.write(f"## {relative_path}\n")
                outfile.write(f"Error reading file: {str(e)}\n\n")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Process NuxtJS project files For LLM analysis")
    parser.add_argument("project_dir", nargs="?", default=None, 
                    help="Folder for the project directory (default: current directory)")
    
    args = parser.parse_args()    
    
    # Set the project directory (current directory or specify your own)
    
    project_dir = args.project_dir
    
    output_file = "project_for_llm.md"

    # Scan for relevant files
    print("Scanning project directory...")
    relevant_files = scan_project(project_dir)
    
    if not relevant_files:
        print("No relevant files found.")
        return
    
    print(f"Found {len(relevant_files)} relevant files:")
    for file in relevant_files:
        print(f"- {file}")
    
    # Combine files into one
    print(f"\nCombining files into {output_file}...")
    combine_files(relevant_files, output_file)
    print(f"Done! Combined file created at {output_file}")

if __name__ == "__main__":
    main()