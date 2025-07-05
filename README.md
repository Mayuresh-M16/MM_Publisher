# MM_Publisher: Houdini Asset Publishing Tool

## Overview

The Houdini Asset Publishing Tool is an all-in-one solution that integrates various essential steps of the asset export and publishing process directly within Houdini. It automates the creation of organized working directories, manages version control, facilitates direct export of common asset formats, generates flipbooks, and enables one-click publishing to Flow Production, including shot creation and email notifications upon flipbook publication.

## Workflow Benefits
- **Efficiency:** Significantly reduces manual steps and repetitive tasks, allowing artists to focus more on creative work.

- **Consistency:** Enforces standardized naming conventions and folder structures, minimizing errors and improving project organization.

- **Collaboration:** Streamlines communication through automated notifications and centralized asset management in Flow Production.

This tool is designed to be an indispensable part of your Houdini workflow, enhancing productivity and integration with your production pipeline.

## Table of Contents
- **Requirements**
- **Installation**
- **Features**
- **Flow Production Integration / Shotgrid API**
- **Implementation**
- **Language and Tools Used**

## Requirements


## Installation

### 1. Get the Tool Itself:

- **What to do:** Download or acquire the main tool's files. This might involve cloning a GitHub repository, downloading a ZIP file, or running an installer package.

- **Why it's needed:** This is the core application you want to use, so you need to have its program files on your system.

### 2. Install FFmpeg and ImageMagick (and Note Their Locations):

- **What to do:** Install [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) and [ImageMagick](https://imagemagick.org/script/download.php)
 on your computer. These are separate, powerful utilities. As you install them, pay close attention to where they are installed on your system. You'll specifically need the "path" to their executable files (e.g., `ffmpeg.exe` and `magick.exe`).

- **Why they're needed:** Our tool relies on FFmpeg for video and audio processing (like converting formats, extracting frames, etc.) and ImageMagick for advanced image manipulation (resizing, watermarking, creating GIFs, etc.). It doesn't have these capabilities built-in; instead, it "calls upon" these external tools to do the heavy lifting. Without them, certain functions of our tool won't work.

### 3. Configure `MM_Publisher.json` with Paths:

- **What to do:** Locate a file named `MM_Publisher.json` (or similarly named configuration file) within the tool's directory. Open this file with a text editor (like Notepad, VS Code, Sublime Text, etc.). Inside, you'll find specific fields where you need to paste the exact paths you noted for FFmpeg and ImageMagick in the previous step. You'll also need to paste the path to where you installed this tool itself.

- **Why it's needed:** This configuration file acts like a roadmap for our tool. It tells the tool exactly where to find FFmpeg and ImageMagick on your system, so when it needs to use them, it knows exactly where to look. Similarly, providing the tool's own path helps it locate its internal resources or allows other parts of the system to correctly reference it.



## Features

### 1.  Automated Working Folder:

-  **Organized Structure:** Automatically sets up a standardized working folder structure for each asset, ensuring consistency across projects.


### 2. Direct Multi-Format Export:

- **FBX Export:** Seamlessly export animated models, cameras, and other scene data to FBX format, widely compatible with various DCC applications and game engines.

- **VDB Export:** Export volumetric data (e.g., clouds, smoke, fire) as VDB files, maintaining high fidelity for rendering and simulation.

- **ABC (Alembic) Export:** Export complex animated geometry and hierarchies as Alembic files, preserving animation data efficiently.

### 3. Integrated Flipbook Generation:

- **High-Quality Previews:** Generate flipbooks directly within the tool, providing quick and accurate visual previews of animations or simulations.

- **Customizable Settings:** Configure resolution, frame range, and output format for flipbooks to meet specific project requirements.

### 4. One-Click Publishing to Flow Production:

- **Shot Creation (Supervisor Mode via Tool):** Supervisor Mode allows for shot creation directly from the tool itself, eliminating the need to navigate to the Flow Production page. This is made possible through seamless ShotGrid API integration.

- **Direct Flipbook Upload:** Once a flipbook is generated, it is automatically uploaded and linked to the relevant shot in Flow Production.

- **Email Notification System:** Upon successful publication of a flipbook to Flow Production, an automated email notification is sent to designated team members or stakeholders, keeping everyone informed of progress and new versions.


## Flow Production Integration / Shotgrid API

### 1. Setting Up Your Personal Access Token (PAT)

A Personal Access Token (PAT) is required to authenticate your connection to Flow Production.

1. Navigate to your **Account Settings** in Flow Production.
2. Select **Legacy Login and Personal Access Token.**
3. Click on **Personal Access Tokens.**
4. For **Production Type**, choose "shortgrid".
5. Enter a **Token Name** (e.g., "MyAPI Token").
6. **Copy the generated token code.**
7. Return to the token input field, paste the code, and click **Bind.**

### 2. Getting the Python API

Before you begin, ensure you have **Git** and **Visual Studio Code** installed on your system.

1. Open your command prompt or terminal.
2. Clone the ShotGrid Python API repository using the following command:

   ````
   Bash
   
   git clone https://github.com/shotgunsoftware/python-api.git
   ````
   This command will clone the repository into your home directory.


### 3. Setting Up a Script on Flow Production

To connect your Python API to Flow Production, you'll need to create a script. **Administrator access is required** for this step.

1. Go to your **Account Settings** in Flow Production.
2. Select **Scripts.**
3. Click **Create a new script.**
4. Enter a descriptive **Name** for your script.
5. **Copy the generated Application Key and save it in a secure location.** This key will not be visible again after the script is created.
   

### 4. Connecting Python to the Python API

Now, let's install the Python API on your local system.

1. Open your terminal.
2. Navigate to the directory where you cloned the Python API (e.g., cd python-api).
3. Run the following command to install the API:
   
   ````
   Bash
   
   python setup.py install
    ````

### 5. Creating a ShotGrid API Instance   

This step establishes the connection between your Python environment and ShotGrid/Flow Production.

1. Open a Python editor (e.g., in Visual Studio Code).
2. Paste the following code, replacing the placeholder values with your actual data:

    ```
    Python
    
    SERVER_PATH = "https://my-site.shotgrid.autodesk.com" # Replace with your ShotGrid server path
    SCRIPT_NAME = 'my_script' # Replace with the name of the script you created in ShotGrid
    SCRIPT_KEY = '27b65d7063f46b82e670fe807bd2b6f3fd1676c1' # Replace with your copied Application Key
    ```

3. Save the file as `API_instance.py.`
4. Run the script from your terminal:
   ```
   Bash
   
   python API_instance.py
   ```
If successful, the script should output a list of data, indicating a successful connection.




## Implementation




## Language and Tools Used
- *Python*
- *Houdini*
- *Flow Production Tracking / Shotgrid*
- *Visual Code*
- *Github*
- *Json*
  
