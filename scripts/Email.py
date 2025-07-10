import hou

# This script defines a function 'email' that sends an email notification.
# It then constructs a subject and body for the email and sets these values on a child 'sendemail' node
# within the HDA, finally cooking that node to send the email.

def email(kwargs):
    hda = kwargs['node']
    proj_parm = hda.parm('proj_name')
    seq_parm = hda.parm('seq_name')
    shot_parm = hda.parm('shot_name')
    version = hda.parm('flip_name').eval()
    
    # --- Fetch Project Name ---
    selected_proj_value = str(proj_parm.eval())
    all_proj_items = proj_parm.menuItems()
    all_proj_labels = proj_parm.menuLabels()

    project = ""
    if selected_proj_value in all_proj_items:
        index = all_proj_items.index(selected_proj_value)
        project = all_proj_labels[index]
    print(f"Project: {project}")
         
    relative_email_path = "topnet1/sendemail"
    email_node = hda.node(relative_email_path)
    
    subject = f" Subject- {project} - {version}" # Replace with your personalized subject
    message_body = f"Body"  # Replace with your personalized message

    # Set message body
    email_body_parm = email_node.parm('email_body')
    if email_body_parm is not None:
        email_body_parm.set(message_body)
    else:
        raise AttributeError("Parameter 'email_body' not found on the HDA.")
    
    # Set subject (if applicable)
    email_subject_parm = email_node.parm('email_subject')
    if email_subject_parm is not None:
        email_subject_parm.set(subject)
    else:
        print("Warning: Parameter 'email_subject' not found. Skipping subject set.")
        
    email_node.cook()
    email_node.cookWorkItems(block=True)
        
