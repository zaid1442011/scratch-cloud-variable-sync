#Import modules
import scratchattach as scratch3
from dotenv import load_dotenv
import os

#Load the .env file(s)
load_dotenv('app.env')

#Set variables to the environment variables
username=os.getenv('username')
sessionID=os.getenv('sessionID')
scratch_project=os.getenv('scratch_project')
server=os.getenv('cloud_host')
contact_info=os.getenv('contact')
egress=os.getenv("egress")

if sessionID == "" and egress == (""):
    print("This is a test branch for 2-way communication, if you won't use 2-way communication, don't use this branch.")
    exit()

try:
    scratch_session = scratch3.Session(sessionID, username=username)
    scratch_conn = scratch_session.connect_cloud(scratch_project)
except:
    print("Failed to connect to Scratch. Closing.")
    exit()

#Connect to Turbowarp's cloud server or another cloud server
try:
    turbo_conn = scratch3.TwCloudConnection(project_id=scratch_project, username=username, cloud_host=server, purpose="A bot that syncs Scratch variables to another cloud server", contact=contact_info)
except:
    print("Couldn't connect to the cloud server. Closing the program.")
    exit()

set_vars = None
while True:
    for var in egress:
        turbo_variable = scratch3.get_tw_var(project_id=scratch_project, variable=var, purpose="A bot that syncs Scratch variables to another cloud server", contact=contact_info, cloud_host=server)
        scratch_conn.set_var(variable=var, value=turbo_variable)
    if variables == {} or variables == None:
        print("Something went wrong while retrieving the cloud variable list or there are no cloud variables in the project. Closing.")
        exit()
    #Get a dictionary of the cloud variables on Scratch
    variables = scratch3.get_cloud(scratch_project)
    #Sets these variables in Turbowarp
    if set_vars == variables: continue
    for var in variables:
        turbo_conn.set_var(var, variables[var])
    set_vars = variables.copy()