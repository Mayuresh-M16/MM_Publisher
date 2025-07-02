import hou
import os
import shotgun_api3
# This script uploads a video file to ShotGrid as a Version entry based on parameters from an HDA.
# It connects to ShotGrid, retrieves project and shot information,
# and uploads the specified video file to the corresponding ShotGrid entry. 


def version_shotgrid(kwargs):
    ## --------------------------------------
    ## Globals
    ## --------------------------------------
    # make sure to change this to match your Flow Production Tracking server and auth credentials.
    SERVER_PATH = "https://my-site.shotgrid.autodesk.com"  # Replace with your ShotGrid site URL
    SCRIPT_NAME = 'my_script'  # Replace with your ShotGrid script name
    SCRIPT_KEY = '27b65d7063f46b82e670fe807bd2b6f3fd1676c1'  # Replace with your ShotGrid script key
    ## --------------------------------------
    
    # Houdini HDA node
    hda = kwargs["node"]
    project_id = hda.parm("proj_name").eval()
    shot_id = hda.parm("shot_name").evalAsString()
    file_name = hda.parm("flip_name").eval()
    file_path = hda.parm("out_flip").eval()
    descrip = hda.parm("desp").evalAsString()

    
    # Get the path to the video file
    video_path = f"{file_path}{file_name}/video/{file_name}.mp4"
    
    # Ensure the video file exists
    if not os.path.isfile(video_path):
        raise RuntimeError(f"Video file does not exist at: {video_path}")

    # Connect to ShotGrid
    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    # Find the project
    project = project_id
    if not project:
        raise RuntimeError(f"Project '{project_name}' not found in ShotGrid.")

    # Find the Shot
    shot = shot_id
    if not shot:
        raise RuntimeError(f"Shot '{shot_code}' not found in project '{project_name}'.")

    # Create a Version entry
    version_data = {
        "project": {"type": "Project", "id": int(project_id)},
        "code": file_name,
        "description": descrip,
        "entity": {"type": "Shot", "id": int(shot_id)},
        "sg_path_to_movie": video_path,
        'user': {'type': 'HumanUser', 'id': 825} # Replace with your user ID or By default it will use Script Name
    }

    version = sg.create("Version", version_data)

    # Upload the video file
    sg.upload("Version", version["id"], video_path, field_name="sg_uploaded_movie")

    # Optionally, you can set the status of the version
    hou.ui.displayMessage(f"Version {version['code']} uploaded successfully to ShotGrid.", severity=hou.severityType.Message)

