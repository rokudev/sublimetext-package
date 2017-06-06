#############################################
#   Roku Deploy Plugin for Sublime Text 3   #
#############################################

------------------------
I. Editor Installation:
------------------------
    1. Download Sublime Text 3 (Windows, OSX, Linux):
        http://www.sublimetext.com/3
    2. Install Sublime Text 3.

------------------------
II. Package Instalation:
------------------------
    1. Get the package: RokuPlugin.sublime-package
    2. Launch SublimeText3 and go to menu "Preferences" -> "Browse Packages..."
    3. Put RokuPlugin.sublime-package file to this directory.
    3.1. If not working, put file to "Installed Packages" directory (at the same level as "Packages")
    4. Restart Sublime Text 3.

------------------------
III. Deployment:
------------------------
    1. Check network connection beetween workstation and Roku box.
    2. Launch SublimeText3 and go to menu "File" -> "Open Folder..."
    3. Open your channale source code directory, for example: ..\apps\simple_channel\dev
    4. Click on any file at to open it in a view/edit mode, for example: ..\source\main.brs
    5. Press "ctrl+alt+e" on Windows (configurable from menu) and observe the console "ctrl+`" (view/show console) 
    6. If everything is ok channel will be deployed on the box.

------------------------
IV. Configuration:
------------------------
    1. You can change key bindings for Deploy:
        - please check: "Preferense/package Settings/Roku Plugin/Key Bindings - Default"
        - override your setting in: "Preferense/package Settings/Roku Plugin/Key Bindings - User"
        [
            { "keys": ["ctrl+alt+e"], "command": "roku_deploy" }
        ]

    2. Also you can configure plugin:
        - please check: "Preferense/package Settings/Roku Plugin/Settings - Default"
        - override your setting in: "Preferense/package Settings/Roku Plugin/Settings - User"
        - for example, change Roku Box IP:
            {
                "rokuIp"            : "192.168.1.254",
                "rokuDevUsername"   : "rokudev",
                "rokuDevPass"       : "test",
            }

------------------------
V. Additional Packages:
------------------------
1. Autocomplete+ provider for XML via XSD: [download exalt](https://packagecontrol.io/packages/Exalt)

 >The XSD file follows the W3C standard. The XML file to autocomplete ask for validation.
 > That is, the root element must looks like: 
 
 ```<component name="SomeComponentName..." xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" extends="Scene" xsi:noNamespaceSchemaLocation="http://rokudev.roku.com/rokudev/schema/RokuSceneGraph.xsd">```

