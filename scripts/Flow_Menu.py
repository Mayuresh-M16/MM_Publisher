import hou
import shotgun_api3
# This script dynamically updates the 'seq_name' (Sequence) and 'shot_name' (Shot)
# parameters in the HDA based on the selected Project and Sequence from ShotGrid.   
# It retrieves the sequences and shots from ShotGrid and populates the corresponding menus in the HDA.
# It also handles the case where the sequence ID is invalid, clearing the shot menu if necessary.
def flow_menu(kwargs):

    hda = kwargs["node"]
    
    # Get the selected project ID from the HDA parameter
    project = hda.parm("proj_name").eval()
    supervisor = hda.parm("supervisor_mode").eval()

    ptg = hda.type().definition().parmTemplateGroup()
    sub_menu_template = ptg.find("seq_name")

    menu_items = []
    menu_labels = []

    if project == 0000:  # Project ID for "Flow Production Tracking"
        menu_items = ["1234","5678","9101","1121"]  # Replace with actual sequence IDs
        menu_labels = ["Sequence A", "Sequence B", "Sequence C", "Sequence D"] # Replace with actual sequence names
    elif project == 0000:  # Project ID for "Flow Production Tracking 2"
        menu_items = ["10234","10400","10401","10402"] # Replace with actual sequence IDs
        menu_labels = ["Sequence X", "Sequence Y", "Sequence Z", "Sequence W"] # Replace with actual sequence names
    else:
        menu_items = [] # If no valid project is selected, clear the menu
        menu_labels = [] 

    sub_menu_template.setMenuItems(menu_items)   # Set the menu items for the sequence parameter
    sub_menu_template.setMenuLabels(menu_labels) # Set the menu labels for the sequence parameter

    ptg.replace("seq_name", sub_menu_template) # Replace the existing 'seq_name' parameter template with the updated one
    hda.type().definition().setParmTemplateGroup(ptg)  # Update the HDA definition with the new parameter template group

    # make sure to change this to match your Flow Production Tracking server and auth credentials.
    SERVER_PATH = "https://my-site.shotgrid.autodesk.com" # Replace with your ShotGrid site URL
    SCRIPT_NAME = 'my_script' # Replace with your ShotGrid script name
    SCRIPT_KEY = '27b65d7063f46b82e670fe807bd2b6f3fd1676c1' # Replace with your ShotGrid script key


    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    # Get the selected sequence ID from the HDA parameter
    sequence_parm = hda.parm("seq_name")
    sequence_id_str = sequence_parm.evalAsString()
    
    try:
        # Attempt to convert the string to an integer
        sequence_id = int(sequence_id_str)
    except ValueError:
        # If conversion fails (e.g., sequence_id_str is "none", "", or "abc")
        print(f"Warning: Invalid sequence ID '{sequence_id_str}' obtained. Expected an integer.")
        print("Clearing shot menu as sequence ID is invalid.")
    
        ptg = hda.type().definition().parmTemplateGroup()
        sub_menu_template = ptg.find("shot_name")
        sub_menu_template.setMenuItems([])
        sub_menu_template.setMenuLabels([])
        ptg.replace("shot_name", sub_menu_template)
        hda.type().definition().setParmTemplateGroup(ptg)
        return

    shot_filters =[['sg_sequence', 'is', {'type': 'Sequence', 'id': sequence_id}]]
    shot_fields = ['code', 'sg_status_list']

    all_shots = sg.find('Shot', shot_filters, shot_fields)

    menu_items = []
    menu_labels = []

    if all_shots:
        shot_data = []
        for shot in all_shots:
            shot_name = shot.get('code')
            shot_id = shot.get('id')
            if shot_name and shot_id is not None:
                shot_data.append((shot_name, str(shot_id))) # Store as string for menu_items


        for shot_name, shot_id_str in shot_data:
            menu_labels.append(shot_name)
            menu_items.append(shot_id_str) # Add the string ID to menu_items

    else:
        if supervisor == 0:
            hou.ui.displayMessage("Warning: No shots found in the selected sequence.", severity=hou.severityType.ImportantMessage)
        menu_items = []
        menu_labels = []

    ptg = hda.type().definition().parmTemplateGroup()
    sub_menu_template = ptg.find("shot_name")

    sub_menu_template.setMenuItems(menu_items)
    sub_menu_template.setMenuLabels(menu_labels)

    ptg.replace("shot_name", sub_menu_template)
    hda.type().definition().setParmTemplateGroup(ptg)
