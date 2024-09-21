import os
from pathlib import Path
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

project_name = "Newproject"

# List of files to create
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitor.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/testing_pipelines.py",
    f"src/{project_name}/exception.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Loop through each file path in the list
for filepath in list_of_files:
    # Convert the file path to a Path object
    filepath = Path(filepath)
    filedir = filepath.parent  # Get the directory of the file
    filename = filepath.name   # Get the filename

    # Ensure filedir is not empty before creating directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        logging.info(f"Creating directory: {filedir} for {filename}")

    # Check if file doesn't exist or its size is 0
    if not filepath.exists() or filepath.stat().st_size == 0:
        # Open the file in write mode to create an empty file
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
