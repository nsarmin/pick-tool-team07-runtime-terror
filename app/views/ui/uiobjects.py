import os 
ui_dir = os.path.dirname(os.path.abspath(__file__))

from PyQt5 import uic

# For all .ui files please follow the structure of creating 
# the Form and QtBase object as shown bellow

# Main Window UI objects
Ui_MainWindow, _ = uic.loadUiType(ui_dir+r'/PICK_App.ui')

# Lead View Prompt UI objects
Ui_TeamConfig, _ = uic.loadUiType(ui_dir+r'/PICK_TeamConfig.ui')

# Event Config View and Vector Dialog UI Objects
Ui_EventConfig,_ = uic.loadUiType(ui_dir+r'/PICK_ECWidget.ui') 
Ui_CreateVector, _ = uic.loadUiType(ui_dir+r'/PICK_CreateVectorWidget.ui')

# Directory Config View
Ui_DirectoryConfig, _ = uic.loadUi(ui_dir+r'/PICK_DirectoryConfig.ui')