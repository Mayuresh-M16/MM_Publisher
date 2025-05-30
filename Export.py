import hou

def Exporting(kwargs):

    hda = kwargs['node']
    format_value = hda.parm("export").eval()
    fbx_node = hda.node("rop_fbx")
    vbd_node = hda.node("filecache")
    abc_node = hda.node("rop_alembic")

    if format_value == 0:
        execute_parm = fbx_node.parm("execute") 
        execute_parm.pressButton()

    elif format_value == 1:
        execute_parm = vbd_node.parm("execute")
        execute_parm.pressButton()  

    elif format_value == 2:
        execute_parm = abc_node.parm("execute")
        execute_parm.pressButton()
