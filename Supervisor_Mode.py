def Supervisor(kwargs):
    hda = kwargs["node"]
    super = hda.parm("supervisor_mode").eval()
    correct_username = "test"
    correct_password = "test123"

    if super == 1:
        username_input = hou.ui.readInput("Supervisor Login", title="Supervisor Mode")
        username = username_input[1]

        if username == correct_username:
            password_input = hou.ui.readInput("Password", title="Supervisor Mode")
            password = password_input[1]

            if password == correct_password:
                hou.ui.displayMessage("Working")

            else:
                hou.ui.displayMessage(
                    "Password is incorrect", severity=hou.severityType.Error
                )

        else:
            hou.ui.displayMessage(
                "Username is incorrect", severity=hou.severityType.Error
            )
