##!/usr/bin/env python
#
## --------------------------------------
## Imports
## --------------------------------------
import shotgun_api3
from pprint import pprint # useful for debugging
import hou
## --------------------------------------
## Globals
## --------------------------------------
# make sure to change this to match your Flow Production Tracking server and auth credentials.
SERVER_PATH = "https://my-site.shotgrid.autodesk.com" # Replace with your ShotGrid site URL
SCRIPT_NAME = 'my_script' # Replace with your ShotGrid script name
SCRIPT_KEY = '27b65d7063f46b82e670fe807bd2b6f3fd1676c1' # Replace with your ShotGrid script key
## --------------------------------------
## Function to run
## --------------------------------------    
def create_shot_in_shotgrid(kwargs):
    """
    Creates a new Shot entry in ShotGrid/Flow Productiom based on parameters from an HDA."""
    # --------------------------------------
    hda = kwargs["node"]
    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
    shot_parm = hda.parm("new_shot")
    des_parm = hda.parm("desp")
    proj_parm = hda.parm("proj_name")
    seq_parm = hda.parm("seq_name")
    
    shot_name = shot_parm.evalAsString()
    des_name = des_parm.evalAsString()
    proj_name = proj_parm.eval()
    seq_name = int(seq_parm.evalAsString())
    
    if not shot_name:
        hou.ui.displayMessage("Shot Name not found", severity=hou.severityType.Error)
    elif not proj_name:
        hou.ui.displayMessage("Project not found", severity=hou.severityType.Error) 
    elif not seq_name:
        hou.ui.displayMessage("Sequence not found", severity=hou.severityType.Error)
    else:        
        # --------------------------------------
        # Create a Shot with data
        # --------------------------------------
        data = {
            'project': {"type":"Project","id": proj_name}, # Project ID should be an integer
            'sg_sequence': {"type": "Sequence", "id": seq_name}, # Sequence ID should be an integer
            'code': shot_name, # Name of the shot
            'description': des_name, # Description of the shot
            'sg_status_list': 'ip' # 'ip' stands for In Progress
        }
        result = sg.create('Shot', data)
        print("The id of the {} is {}.".format(result['type'], result['id']))
        hou.ui.displayMessage(f"Shot '{shot_name}' created successfully in Flow Production.", severity=hou.severityType.Message) 
