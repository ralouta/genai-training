# Project Overview
This project leverages Azure OpenAI services to perform various tasks, including image extraction and document summarization. The workspace is structured to facilitate easy setup and execution of these tasks using Python scripts and Jupyter notebooks.

## Setup Instructions

### Clone the Repository

1. Connect to esri vpn US-East
2. Install [Visual Studio Code](https://code.visualstudio.com/) if you don't have it.
3. Install [git](https://git-scm.com/downloads)
4. Run the following commands:
   ```sh
   git clone https://github.com/ralouta/genai-training.git
   cd genai-training

### Set Up the Python Environment
Run the **`setup.bat`** script to set up the Python environment and install dependencies:

### Edit Configuration
Update the `config.toml` file in the `Examples/` directory with your own OpenAI API key:

## Directory Structure
- `chains/`: Contains Python scripts for different processing chains.
  - `image_extract.py`: Script for extracting information from images.
  - `__pycache__/`: Compiled Python files.
- `images/`: Directory for storing images used in the project.
- `Examples/`: Contains example Jupyter notebooks and configuration files.
  - `Example 1.ipynb`: Example notebook demonstrating how to use the Azure OpenAI services.
  - `config.toml`: Configuration file for setting up Azure OpenAI services.
- `genai-auto-py3/`: Contains various DLL files and environment setup scripts.
- `models/`: Directory for storing model-related files.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.me`: This README file.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `setup.bat`: Batch script for setting up the Python environment.

## Usage

### Running Jupyter Notebooks
Open and run the example notebooks in the `Examples/` directory to see how to use the Azure OpenAI services.

### Running Python Scripts
Execute the Python scripts in the `chains/` directory for specific tasks.

## Dependencies
The project requires the following Python packages, which are listed in the `requirements.txt` file:
- `openai`
- `toml`
- `chromadb`
- `langchain_openai`
- `langchain_community`
- `langchain_chroma`
- `gpt4all`
- `pypdf`
- `docx2txt`

## Directory Structure
- `chains/`: Contains Python scripts for different processing chains.
  - `image_extract.py`: Script for extracting information from images.
  - `__pycache__/`: Compiled Python files.
- `images/`: Directory for storing images used in the project.
- `Examples/`: Contains example Jupyter notebooks and configuration files.
  - `Example 1.ipynb`: Example notebook demonstrating how to use the Azure OpenAI services.
  - `config.toml`: Configuration file for setting up Azure OpenAI services.
- `genai-auto-py3/`: Contains various DLL files and environment setup scripts.
- `models/`: Directory for storing model-related files.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.me`: This README file.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `setup.bat`: Batch script for setting up the Python environment.

## License
This projects needs an ArcGIS Desktop license

## Acknowledgments
Special thanks to the contributors and the open-source community for their invaluable support and resources.