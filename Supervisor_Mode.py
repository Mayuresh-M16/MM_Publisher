def Supervisor(kwargs):
    """
    Handles supervisor mode login for an HDA.
    Prompts for username and password, and if correct, enables 'create' parameter.
    """
    hda = kwargs["node"]
    supervisor_mode_parm = hda.parm("supervisor_mode")
    folder_seq_parm = hda.parm("create")

    correct_username = "test"
    correct_password = "test123"

    # Only proceed if supervisor mode is enabled
    if supervisor_mode_parm.eval() == 1:
        # Prompt for username
        username_input_result = hou.ui.readInput(
            "Enter Supervisor Username:",
            buttons=("OK", "Cancel"),
            initial_contents="",
            title="Supervisor Login"
        )

        # Check if Cancel was clicked for username input (button index 1 is Cancel)
        if username_input_result[0] == 1:
            hou.ui.displayMessage("Supervisor login cancelled.", severity=hou.severityType.Warning)
            supervisor_mode_parm.set(0) # Disable supervisor mode
            return

        username = username_input_result[1]

        # Check if username is empty
        if not username: # This is a more Pythonic way to check for an empty string
            hou.ui.displayMessage("Username cannot be empty. Please enter a username.", severity=hou.severityType.Error)
            supervisor_mode_parm.set(0) # Disable supervisor mode
            return

        # Check if username is correct
        if username == correct_username:
            # Prompt for password, with masking enabled
            password_input_result = hou.ui.readInput(
                "Enter Password",
                buttons=("OK", "Cancel"),
                initial_contents="",
                title="Supervisor Mode",
                
            )

            # Check if Cancel was clicked for password input
            if password_input_result[0] == 1:
                hou.ui.displayMessage("Supervisor login cancelled.", severity=hou.severityType.Warning)
                supervisor_mode_parm.set(0) # Disable supervisor mode
                return

            password = password_input_result[1]

            # Check if password is empty
            if not password:
                hou.ui.displayMessage("Password cannot be empty. Please enter a password.", severity=hou.severityType.Error)
                supervisor_mode_parm.set(0) # Disable supervisor mode
                return

            # Check if password is correct
            if password == correct_password:
                hou.ui.displayMessage("Login Successful! Supervisor mode enabled.")
                folder_seq_parm.set(1) # Enable the 'create' parameter
            else:
                hou.ui.displayMessage("Incorrect Password.", severity=hou.severityType.Error)
                supervisor_mode_parm.set(0) # Disable supervisor mode
        else:
            hou.ui.displayMessage("Incorrect Username.", severity=hou.severityType.Error)
            supervisor_mode_parm.set(0) # Disable supervisor mode