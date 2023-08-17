screen hub:
    imagebutton:
        xpos 1400
        ypos 797
        idle "UI/imagebuttons/dog_idle.png"
        hover "UI/imagebuttons/dog_hover.png"
        if hubClickable["dog"] == 1:
            action Null
        else:
            action Jump("browserScene")
    #add list of hub clickable elements here

#Screen when head phone is just visible with settings icons
screen phoneDown :
    imagebutton:
        xalign 0.5
        yalign 3.0
        idle "smartphone.png"
        action Jump("telplay")
    hbox:
        spacing 20
        xalign 0.5
        yalign 0.95
        imagebutton:
            if BluetoothState == True:
                idle "UI/settingsIcons/BluetoothON.png"
                hover "UI/settingsIcons/BluetoothOFF.png"
            else:
                idle "UI/settingsIcons/BluetoothOFF.png"
                hover "UI/settingsIcons/BluetoothON.png"
            action SetVariable("BluetoothState", not BluetoothState)
        imagebutton:
            if DataState == True:
                idle "UI/settingsIcons/DataON.png"
                hover "UI/settingsIcons/DataOFF.png"
            else:
                idle "UI/settingsIcons/DataOFF.png"
                hover "UI/settingsIcons/DataON.png"
            action SetVariable("DataState", not DataState)
        imagebutton:
            if LocalisationState == True:
                idle "UI/settingsIcons/LocalisationON.png"
                hover "UI/settingsIcons/LocalisationOFF.png"
            else:
                idle "UI/settingsIcons/LocalisationOFF.png"
                hover "UI/settingsIcons/LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)


#Smartphone home screen
#Each argument is one application icon that can be avaible or not
screen telephoneplayer(A1=True,A2=True,A3=True,B1=True,B2=True,B3=True) :
    imagebutton:
        xalign 0.5
        ypos 150
        idle "smartphone.png"

    imagebutton:
        xalign 0.5
        yalign 0.95
        idle "masquetelephone.png"
        hover "masquetelhiver.png"
        action Hide("telephoneplayer"), Jump("lPhoneDown")

    frame:
        background None
        xalign 0.5
        yalign 0.4
        xmaximum 360
        ymaximum 700
        grid 3 2:
            spacing 20
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A1:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A2:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A3:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B1:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B2:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B3   :
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"


    hbox:
        xalign 0.5
        yalign 0.2
        spacing 20
        imagebutton:
            if BluetoothState == True:
                idle "UI/settingsIcons/BluetoothON.png"
                hover "UI/settingsIcons/BluetoothOFF.png"
            else:
                idle "UI/settingsIcons/BluetoothOFF.png"
                hover "UI/settingsIcons/BluetoothON.png"
            action SetVariable("BluetoothState", not BluetoothState)
        imagebutton:
            if DataState == True:
                idle "UI/settingsIcons/DataON.png"
                hover "UI/settingsIcons/DataOFF.png"
            else:
                idle "UI/settingsIcons/DataOFF.png"
                hover "UI/settingsIcons/DataON.png"
            action SetVariable("DataState", not DataState)
        imagebutton:
            if LocalisationState == True:
                idle "UI/settingsIcons/LocalisationON.png"
                hover "UI/settingsIcons/LocalisationOFF.png"
            else:
                idle "UI/settingsIcons/LocalisationOFF.png"
                hover "UI/settingsIcons/LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)



#Screen phone when selfie photo is display
screen selfie :
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "selfie.png"
    imagebutton:
        xalign 0.5
        yalign 0.72
        idle "share-icon.png"
        action Jump("walkOut")

label walkOut :
    scene desert
    show Player_Walking
    m "Oh non, qu'est ce que j'ai fais ?"
