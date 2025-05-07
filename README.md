Project File Combiner for LLM Analysis

This Python script scans a project directory, collects source code files from various programming languages, and combines them into a single Markdown file with syntax-highlighted code blocks, optimized for analysis by large language models (LLMs).

Features

*   Multi-Language Support: Processes files from popular programming languages including JavaScript, TypeScript, Python, C#, Java, C/C++, Go, Ruby, PHP, Rust, Kotlin, and more.
    
*   Syntax Highlighting: Outputs code in Markdown with appropriate language identifiers for syntax highlighting.
    
*   Directory Exclusion: Skips common build, dependency, and cache directories (e.g., node\_modules, venv, dist).
    
*   Error Handling: Gracefully handles file reading errors and continues processing.
    
*   Simple CLI: Uses a straightforward command-line interface with a single optional argument for the project directory.
    

Installation

1.  Prerequisites:
    
    *   Python 3.6 or higher.
        
    *   No external dependencies are required (uses standard library modules: os, pathlib, argparse).
        
2.  Download the Script:
    
    *   Clone this repository or download the script (combine\_project.py):
        
        bash
        
            git clone <repository-url>
        
        Or copy the script from the provided source.
        
3.  Place the Script:
    
    *   Save combine\_project.py in a convenient location, such as your project root or a scripts directory.
        

Usage

1.  Run the Script:
    
    *   Open a terminal and navigate to the directory containing combine\_project.py.
        
    *   Execute the script with an optional project directory path:
        
        bash
        
            python combine_project.py /path/to/project
        
    *   If no directory is provided, the script defaults to the current directory (.).
        
2.  Output:
    
    *   The script generates a file named project\_for\_llm.md in the current directory.
        
    *   This Markdown file contains:
        
        *   A header with project information.
            
        *   Sections for each source file, including the relative file path and its content in a syntax-highlighted code block.
            
3.  Example Command:
    
    bash
    
        python combine_project.py ./my-project
    
    This scans my-project, collects supported files, and creates project\_for\_llm.md.
    
4.  Sample Output (project\_for\_llm.md):
    
    markdown
    
        # Project Codebase
        
        This file contains the concatenated source code of relevant files for LLM analysis.
        
        ## src/main.py
        ```python
        print("Hello, Python!")
    
    src/App.cs
    
    csharp
    
        using System;
        Console.WriteLine("Hello, C#!");
    
    src/index.js
    
    javascript
    
        console.log("Hello, JavaScript!");
    

Supported Languages and File Types

The script supports a wide range of programming languages and file types, including:

*   Programming Languages:
    
    *   JavaScript/TypeScript (.js, .ts, .jsx, .tsx, .vue)
        
    *   Python (.py)
        
    *   C# (.cs)
        
    *   Java (.java)
        
    *   C/C++ (.c, .cpp, .h, .hpp)
        
    *   Go (.go)
        
    *   Ruby (.rb)
        
    *   PHP (.php)
        
    *   Rust (.rs)
        
    *   Kotlin (.kt)
        
*   Configuration and Markup:
    
    *   JSON (.json)
        
    *   YAML (.yaml, .yml)
        
    *   XML (.xml)
        
    *   HTML (.html)
        
    *   CSS (.css, .scss)
        
*   Other:
    
    *   Shell scripts (.sh)
        
    *   SQL (.sql)
        

Excluded Directories

The script automatically skips common directories to avoid processing irrelevant files:

*   Dependency folders: node\_modules, venv, .venv, vendor
    
*   Build/output folders: dist, build, target, bin, obj
    
*   Cache/IDE folders: \_\_pycache\_\_, .git, .idea, .vscode
    

Customization

To modify the script's behavior (e.g., add new file extensions, change excluded directories, or alter the output format), edit the following sections in combine\_project.py:

*   include\_extensions: Add or remove file extensions in the scan\_project function.
    
*   exclude\_dirs: Update the set of excluded directories in the scan\_project function.
    
*   lang\_map: Adjust the mapping of file extensions to Markdown language identifiers in the combine\_files function.
    

Limitations

*   The output file is always named project\_for\_llm.md and saved in the current directory.
    
*   Binary files may cause errors if they match supported extensions; consider adding explicit binary file detection if needed.
    
*   Large projects may produce very large Markdown files, which could impact LLM processing.
    

Contributing

Contributions are welcome! To contribute:

1.  Fork the repository.
    
2.  Create a feature branch (git checkout -b feature-name).
    
3.  Commit your changes (git commit -m "Add feature").
    
4.  Push to the branch (git push origin feature-name).
    
5.  Open a pull request.
    

Please include tests or examples demonstrating your changes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or feedback, please open an issue on the repository or contact the maintainer.

* * *

Notes

*   The README assumes the project is hosted in a repository (e.g., GitHub). If it's not, you can remove repository-specific instructions (e.g., cloning, contributing).
    
*   If you want to include a LICENSE file or specific maintainer contact details, let me know, and I can generate those or adjust the README.
    
*   The README is designed to be concise yet comprehensive, covering installation, usage, and customization for users of varying expertise.
    

Let me know if you need adjustments, such as adding specific sections, changing the tone, or including additional details!