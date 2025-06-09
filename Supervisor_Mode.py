import hou

def Supervisor(kwargs):
    hda = kwargs["node"]
    supervisor = hda.parm("supervisor_mode").eval()
    correct_username = "test"
    correct_password = "test123"
    folder_seq = hda.parm("create")
    
    if supervisor == 1:
        username_input = hou.ui.readInput(
            "Enter Supervisor Username:",
            buttons=("OK", "Cancel"),
            initial_contents="",
            title="Supervisor Login"
        )
        
        # Check if Cancel was clicked for username input
        if username_input[0] == 1:
            hou.ui.displayMessage("Process cancelled.",severity=hou.severityType.Fatal)
            hda.parm("supervisor_mode").set(0)
            return
        
        username = username_input[1]

        # Check if username is empty
        if username == "": 
            hou.ui.displayMessage("Username cannot be empty. Please enter a username.", severity=hou.severityType.Error)
            hda.parm("supervisor_mode").set(0)
            return

        if username == correct_username:
            password_input_result = hou.ui.readInput(
                "Password",
                buttons=("OK", "Cancel"),
                title="Supervisor Mode",

            )
            
            # Check if Cancel was clicked for password input
            # Important: This should be 'password_input_result', not 'password_input'
            if password_input_result[0] == 1:
                hou.ui.displayMessage("Process cancelled.", severity=hou.severityType.Important)
                hda.parm("supervisor_mode").set(0)
                return
            
            password = password_input_result[1]
            
            if password == "": 
                hou.ui.displayMessage("Password cannot be empty. Please enter a username.", severity=hou.severityType.Error)
                hda.parm("supervisor_mode").set(0)
                return
            
            if password == correct_password:
                hou.ui.displayMessage("Working")
                folder_seq.set(1)
            else:
                hou.ui.displayMessage("Password is incorrect", severity=hou.severityType.Error)
                hda.parm("supervisor_mode").set(0)
                
        else: # This 'else' belongs to 'if username == correct_username'
            hou.ui.displayMessage("Username is incorrect", severity=hou.severityType.Error)
            hda.parm("supervisor_mode").set(0)