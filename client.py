import subprocess

############################# GUI #########################################################
# TODO: Create Protoype for Client Gui (Runs on MainThread)
#     - Connect to server
#     - Send get command from user
#     - Send to engine function
############################# After Engine #########################################################
#     - Receive output from engine function

############################# ENGINE #########################################################
# TODO: Create engine for client function (Runs on new thread)
#     - Receive command from gui
#     - Send command to server (Using global socket has been initialized in main thread (GUI))
#     - Receive output from server
#     - Send command to run sys command
#     - Send output to gui


def engine(cmd):
    pass