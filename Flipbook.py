def Flip(kwargs):
    hda = kwargs["node"]

    relative_ropopengl_top_node_path = "topnet1/ropopengl"
    relative_ffmpeg_path = "topnet1/ffmpegencodevideo"

    ropopengl_top_node = hda.node(relative_ropopengl_top_node_path)
    ffmpeg_node = hda.node(relative_ffmpeg_path)
    
    hou.hipFile.save()
    print("File is saved")
    
    print("image sequence process started")
    ropopengl_top_node.cook()
    
    ropopengl_top_node.cookWorkItems(block=True)
    print("image sequence process completed")
    
    print("video generation process started")
    ffmpeg_node.cook()
    
    ffmpeg_node.cookWorkItems(block=True)
    print("video generation process completed")
