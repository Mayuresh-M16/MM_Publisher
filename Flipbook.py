import hou
# This script is used to generate a flipbook video from an image sequence in Houdini.   
# It cooks the ropopengl node to process the image sequence and then uses ffmpeg to generate the video.
# The script is designed to be used within a Houdini Digital Asset (HDA) context.
# --------------------------------------
# Function to handle flipbook video generation
# --------------------------------------

def Flip(kwargs)

    hda = kwargs["node"]

    # Evaluate the parameters to get their string values
    camera_path = hda.parm("cam").evalAsString()
    scene_path = hda.parm("scene").evalAsString()
    filename = hda.parm("flip_name").evalAsString()
    filepath = hda.parm("out_flip").evalAsString()

    if not filename:  # Check if filename is an empty string or None
        hou.ui.displayMessage("File Name not found", severity=hou.severityType.Error)
    elif not filepath:  # Check if filepath is an empty string or None
        hou.ui.displayMessage("File Path not found", severity=hou.severityType.Error)
    elif not camera_path:  # Check if camera_path is an empty string or None
        hou.ui.displayMessage("Camera not found", severity=hou.severityType.Error)
    elif not scene_path:  # Check if scene_path is an empty string or None
        hou.ui.displayMessage("Scene not found", severity=hou.severityType.Error)
    else:
        relative_ropopengl_top_node_path = "topnet1/ropopengl"
        relative_ffmpeg_path = "topnet1/ffmpegencodevideo"

        ropopengl_top_node = hda.node(relative_ropopengl_top_node_path)
        ffmpeg_node = hda.node(relative_ffmpeg_path)

        hou.hipFile.save() # Save the current Houdini file before processing
        print("File is saved")
        
        print("image sequence process started")
        ropopengl_top_node.cook() # Use cook() with block=True to wait for completion
        
        ropopengl_top_node.cookWorkItems(block=True) 
        print("image sequence process completed")
        
        print("video generation process started")
        ffmpeg_node.cook()
        
        ffmpeg_node.cookWorkItems(block=True)
        print("video generation process completed")

        hou.ui.displayMessage("Flipbook generated successfully.", severity=hou.severityType.Message)  
