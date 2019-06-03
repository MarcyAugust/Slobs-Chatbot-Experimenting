# Import Libraries
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

# Import your Settings class
from Settings_Module import MySettings

# Script information
ScriptName = "SFXBan"
Website = "https://github.com/MarcyAugust/Slobs-Chatbot-Experimenting"
Description = "Bans a user while playing a sound effect!"
Creator = "ToransuShojo"
Version = "1.0"

# Define Global Variables
global SettingsFile
SettingsFile = ""
global ScriptSettings
ScriptSettings = MySettings()

# Initialize Data
def Init():

    # Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    ScriptSettings = MySettings(SettingsFile)
    ScriptSettings.Response = "SFXBan settings overwritten!"
    return

    # Create SFX Directory
    sfxdirectory = os.path.join(os.path.dirname(__file__), "SFX")
    if not os.path.exists(sfxdirectory):
        os.makedirs(sfxdirectory)

# Execute data
def Execute(data):


    #   Check if the proper command is used and the user has permission to use the command
    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and Parent.HasPermission(data.User,ScriptSettings.Permission,ScriptSettings.Info):
        if data.GetParamCount() == 2:
            Parent.SendStreamMessage("/ban " + data.GetParam(1))    # Bans the user
            Parent.SendStreamMessage(data.GetParam(1) + " was banned for " + ScriptSettings.Reason) # Posts the ban in chat
            sfxdirectory = os.path.join(os.path.dirname(__file__), "SFX")
            Parent.PlaySound(sfxdirectory + "/" + ScriptSettings.File, ScriptSettings.Volume)   # Plays the SFX
        else:
            Parent.SendStreamMessage("You didn't specify a user to ban!")


    return

# Tick method
def Tick():
    return

# Parse method
def Parse():
    return

# Settings reload
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

# Unload method
def Unload():
    return

# Script toggle method
def ScriptToggled(state):
    return

# Open SFX directory method
def OpenSFXDir():
    sfxdir = os.path.join(os.path.dirname(__file__), "SFX")
    os.startfile(sfxdir)
    return
