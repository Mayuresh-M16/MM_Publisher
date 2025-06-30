import hou
# This script is used to export geometry in different formats based on user selection in Houdini.
# It supports FBX, VDB, and Alembic formats.
# The user can specify the file name and path, and the script will execute the appropriate export node.
# The script is designed to be used within a Houdini Digital Asset (HDA) context.

def Exporting(kwargs):
    hda = kwargs["node"]
    filename = hda.parm("file_name").evalAsString()
    filepath = hda.parm("file_path").evalAsString()
    format_value = hda.parm("export").eval()
    fbx_node = hda.node("rop_fbx")
    vbd_node = hda.node("filecache")
    abc_node = hda.node("rop_alembic")

    if  not filename:
        hou.ui.displayMessage("File Name not found", severity=hou.severityType.Error)
    elif not filepath:
        hou.ui.displayMessage("File Path not found", severity=hou.severityType.Error)
    else:
        if format_value == 0:
            execute_parm = fbx_node.parm("execute")

        elif format_value == 1:
            execute_parm = vbd_node.parm("execute")

        elif format_value == 2:
            execute_parm = abc_node.parm("execute")
            

        execute_parm.pressButton()
        hou.ui.displayMessage(f"{filename}_V00{version} : rendered successfully.", severity=hou.severityType.Message)

    
    
    