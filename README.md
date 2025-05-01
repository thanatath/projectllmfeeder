* * *

🧠 NuxtJS Codebase Collector for LLM Analysis
=============================================

This utility is designed to scan a NuxtJS (or general JavaScript/TypeScript-based) project and concatenate relevant source files into a single Markdown file. The output is formatted for **Large Language Model (LLM)** consumption, enabling effective code analysis, summarization, or documentation generation.

📦 Features
-----------

*   ✅ Recursively scans directories for `.vue`, `.js`, `.ts`, and `.json` files.
    
*   🚫 Automatically skips unnecessary folders like `node_modules`, `dist`, and `.git`.
    
*   🧾 Outputs a Markdown file with syntax-highlighted code blocks.
    
*   🧠 Optimized for use with LLMs such as GPT for auditing or refactoring assistance.
    

* * *

🛠 Usage
--------

### 🔧 Requirements

*   Python 3.7+
    
*   No external dependencies required.
    

### 📥 Installation

`git@github.com:thanatath/projectllmfeeder.git` 
`cd nuxt-codebase-collector`

### ▶️ Run

#### Default (current directory):

`python collect_code.py`

#### Specify a project directory:

bash

คัดลอกแก้ไข

`python collect_code.py /path/to/your/project`

This will generate a file named `project_for_llm.md` in the current working directory.

* * *

📁 Output Format
----------------

Each file is added under its relative path as a header with code content wrapped in language-specific code blocks:

<pre> ## pages/index.vue \`\`\`vue &lt;template&gt; &lt;div&gt;Hello&lt;/div&gt; &lt;/template&gt; ... \`\`\` </pre>

* * *

🔒 Exclusions
-------------

By default, the following folders are skipped to reduce noise and avoid redundant content:

markdown

คัดลอกแก้ไข

`node_modules, .nuxt, dist, .git, __pycache__`

You can adjust these in the `exclude_dirs` set inside the script.

* * *

🤖 Use Case
-----------

Ideal for:

*   Feeding clean project code to LLMs.
    
*   Performing code reviews or audits with AI assistance.
    
*   Creating snapshots of a codebase for documentation or versioning.
    

* * *

🧙‍♂️ Example
-------------


`python main.py ~/projects/my-nuxt-app`

*   ✅ Scans and lists relevant files.
    
*   📝 Outputs `project_for_llm.md` with clean formatting.
    
*   🔍 Ready to use with GPT, Claude, or other LLM tools.
    

* * *

📄 License
----------

MIT License — use freely and modify as needed.

* * *

Let me know if you'd like a logo badge, GitHub Actions CI config, or packaging setup (e.g., `setup.py` or CLI entry point).