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


## Implementation




## Language and Tools Used
- *Python*
- *Houdini*
- *Flow Production Tracking / Shotgrid*
- *Visual Code*
- *Github*
- *Json*
  
