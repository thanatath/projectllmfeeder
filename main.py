import os
from pathlib import Path
import argparse

def scan_project(directory):
    """Scan the project directory and return a list of relevant files."""
    # Comprehensive list of file extensions for popular programming languages
    include_extensions = {
        # JavaScript/TypeScript
        '.js', '.ts', '.jsx', '.tsx', '.vue',
        # Python
        '.py',
        # C#
        '.cs',
        # Java
        '.java',
        # C/C++
        '.c', '.cpp', '.h', '.hpp',
        # Go
        '.go',
        # Ruby
        '.rb',
        # PHP
        '.php',
        # Configuration and markup
        '.json', '.yaml', '.yml', '.xml', '.html', '.css', '.scss',
        # Shell
        '.sh',
        # SQL
        '.sql',
        # Rust
        '.rs',
        # Kotlin
        '.kt'
    }
    
    # Directories to exclude (common build, dependency, and cache folders)
    exclude_dirs = {
        'node_modules', '.nuxt', 'dist', '.git', '__pycache__',
        'venv', '.venv', 'build', 'target', 'bin', 'obj',  # Python, Java, C#
        '.idea', '.vscode',  # IDE folders
        'vendor',  # PHP
        '.vs'
    }

    relevant_files = []
    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            # Check if file has a relevant extension
            if Path(file).suffix.lower() in include_extensions:
                file_path = os.path.join(root, file)
                relevant_files.append(file_path)
    
    return relevant_files

def combine_files(files, output_file):
    """Combine contents of relevant files into a single Markdown file."""
    # Mapping of file extensions to Markdown code block language identifiers
    lang_map = {
        '.js': 'javascript',
        '.ts': 'typescript',
        '.jsx': 'javascript',
        '.tsx': 'typescript',
        '.vue': 'vue',
        '.py': 'python',
        '.cs': 'csharp',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.h': 'c',
        '.hpp': 'cpp',
        '.go': 'go',
        '.rb': 'ruby',
        '.php': 'php',
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.xml': 'xml',
        '.html': 'html',
        '.css': 'css',
        '.scss': 'scss',
        '.sh': 'bash',
        '.sql': 'sql',
        '.rs': 'rust',
        '.kt': 'kotlin'
    }

    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write a header for the combined file
        outfile.write("# Project Codebase\n\n")
        outfile.write("This file contains the concatenated source code of relevant files for LLM analysis.\n\n")

        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # Write file path as a header
                    relative_path = os.path.relpath(file_path)
                    outfile.write(f"## {relative_path}\n")
                    outfile.write("```")
                    # Add language identifier for syntax highlighting
                    ext = Path(file_path).suffix.lower()
                    lang = lang_map.get(ext, '')
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
    parser = argparse.ArgumentParser(description="Process project files for LLM analysis")
    parser.add_argument("project_dir", nargs="?", default=None, 
                        help="Folder for the project directory (default: current directory)")
    args = parser.parse_args()

    # Set the project directory
    project_dir = args.project_dir or "."  # Use current directory if None
    output_file = "project_for_llm.md"

    # Validate project directory
    if not os.path.isdir(project_dir):
        print(f"Error: '{project_dir}' is not a valid directory.")
        return

    # Scan for relevant files
    print(f"Scanning project directory: {project_dir}")
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