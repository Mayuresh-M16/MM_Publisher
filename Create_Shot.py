## --------------------------------------
## Imports
## --------------------------------------
import shotgun_api3
from pprint import pprint # useful for debugging
import hou
## --------------------------------------
## Function to run
## --------------------------------------
def menu(kwargs):
    hda = kwargs["node"]
    
    project_choice = hda.parm("proj_name_1").eval()
    
    ptg = hda.type().definition().parmTemplateGroup()
    sub_menu_template = ptg.find("sup_seq")

    
    menu_items = []
    menu_labels = []

    if project_choice == 2111:
        menu_items = ["10370","10371","10372","10373"]
        menu_labels = ["JWF", "MSM","WER","YUI"]
    elif project_choice == 2103:
        menu_items = ["10238"]
        menu_labels = ["Test"]
    else:
        menu_items = []
        menu_labels = []

    sub_menu_template.setMenuItems(menu_items)
    sub_menu_template.setMenuLabels(menu_labels)
  
    ptg.replace("sup_seq", sub_menu_template)
    hda.type().definition().setParmTemplateGroup(ptg)

#    sub_menu_parm = hda.parm("sup_seq")
    
    


# make sure to change this to match your Flow Production Tracking server and auth credentials.
SERVER_PATH = "https://bow-valley-college.shotgrid.autodesk.com"
SCRIPT_NAME = 'publisher'
SCRIPT_KEY = 'ocpg3tvungmhrUotovt*ollmx'
## --------------------------------------
## Function to run
## --------------------------------------    
def create_shot_in_shotgrid(kwargs):
    hda = kwargs["node"]
    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
    shot_parm = hda.parm("new_shot")
    des_parm = hda.parm("despcrip")
    proj_parm = hda.parm("proj_name_1")
    seq_parm = hda.parm("sup_seq")
    
    shot_name = shot_parm.evalAsString()
    des_name = des_parm.evalAsString()
    proj_name = proj_parm.eval()
    seq_name = int(seq_parm.evalAsString())
    
    # --------------------------------------
    # Create a Shot with data
    # --------------------------------------
    data = {
        'project': {"type":"Project","id": proj_name},
        'sg_sequence': {"type": "Sequence", "id": seq_name},
        'code': shot_name,
        'description': des_name,
        'sg_status_list': 'ip'
    }
    print('sg_sequence')
    result = sg.create('Shot', data)
    pprint(result)
    print("The id of the {} is {}.".format(result['type'], result['id']))
    
    
