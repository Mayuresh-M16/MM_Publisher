import hou
# --------------------------------------    
# Function to handle supervisor mode login
# --------------------------------------
def Supervisor(kwargs):
    """
    Handles supervisor mode login for an HDA.
    Prompts for username and password, and if correct, enables 'create' parameter.
    """
    hda = kwargs["node"]
    supervisor_mode_parm = hda.parm("supervisor_mode")
    folder_seq_parm = hda.parm("create")

    correct_username = "admin" # Replace with your actual username
    correct_password = "password"  # Replace with your actual password

    # Only proceed if supervisor mode is enabled
    if supervisor_mode_parm.eval() == 1:
        # Prompt for username
        input_result =hou.ui.readMultiInput(
        "Enter Username and Password",
        ("Username", "Password"),
        buttons=("OK", "Cancel"),
        initial_contents=("", ""),
        password_input_indices=([1]),
        )

        # Check if Cancel was clicked for username input (button index 1 is Cancel)
        if input_result[0] == 1:
            hou.ui.displayMessage("Supervisor authentication cancelled.", severity=hou.severityType.Warning)
            supervisor_mode_parm.set(0) # Disable supervisor mode
            return

        username = input_result[1][0]

        # Check if username is empty
        if not username: # This is a more Pythonic way to check for an empty string
            hou.ui.displayMessage("Username cannot be empty. Please enter a username.", severity=hou.severityType.Error)
            supervisor_mode_parm.set(0) # Disable supervisor mode
            return

        # Check if username is correct
        if username == correct_username:
            # Check if Cancel was clicked for password input
            if input_result[0] == 1:
                hou.ui.displayMessage("Supervisor login cancelled.", severity=hou.severityType.Warning)
                supervisor_mode_parm.set(0) # Disable supervisor mode
                return

            password = input_result[1][1]

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
