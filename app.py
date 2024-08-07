#Import modules
import scratchattach as scratch3
from dotenv import load_dotenv
import os

#Load the .env file(s)
load_dotenv('app.env')

#Set variables to the environment variables
username=os.getenv('username')
scratch_project=os.getenv('scratch_project')
server=os.getenv('cloud_host')
contact_info=os.getenv('contact')

#Connect to Turbowarp's cloud server or another cloud server
turbo_conn = scratch3.TwCloudConnection(project_id=scratch_project, username=username, cloud_host=server, purpose="A bot that syncs Scratch variables to another cloud server", contact=contact_info)

set_vars = None
while True:
    #Get a dictionary of the cloud variables on Scratch
    variables = scratch3.get_cloud(scratch_project)
    #Sets these variables in Turbowarp
    if set_vars == variables: continue
    for var in variables:
        turbo_conn.set_var(var, variables[var])
    set_vars = variables.copy()