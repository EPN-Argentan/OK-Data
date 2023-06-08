screen hub:
    imagebutton:
        xpos 1400
        ypos 797
        idle "dog_idle.png"
        hover "dog_hover.png"
        action Null

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
                idle "BluetoothON.png"
                hover "BluetoothOFF.png"
            else:
                idle "BluetoothOFF.png"
                hover "BluetoothON.png"
            action SetVariable("BluetoothState", not BluetoothState)
        imagebutton:
            if DataState == True:
                idle "DataON.png"
                hover "DataOFF.png"
            else:
                idle "DataOFF.png"
                hover "DataON.png"
            action SetVariable("DataState", not DataState)
        imagebutton:
            if LocalisationState == True:
                idle "LocalisationON.png"
                hover "LocalisationOFF.png"
            else:
                idle "LocalisationOFF.png"
                hover "LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)


screen telephoneplayer :
    imagebutton:
        xalign 0.5
        ypos 150
        idle "smartphone.png"

    imagebutton:
        xalign 0.5
        yalign 0.85
        idle "masquetelephone.png"
        hover "masquetelhiver.png"
        action Hide("telephoneplayer"), Jump("lPhoneDown")

    imagebutton:
        xpos 800
        ypos 300
        idle "appphoto.png"
        hover "appphotohover.png"
        action Jump("selfie")

    hbox:
        xalign 0.5
        yalign 0.2
        spacing 20
        imagebutton:
            if BluetoothState == True:
                idle "BluetoothON.png"
                hover "BluetoothOFF.png"
            else:
                idle "BluetoothOFF.png"
                hover "BluetoothON.png"
            action SetVariable("BluetoothState", not BluetoothState)
        imagebutton:
            if DataState == True:
                idle "DataON.png"
                hover "DataOFF.png"
            else:
                idle "DataOFF.png"
                hover "DataON.png"
            action SetVariable("DataState", not DataState)
        imagebutton:
            if LocalisationState == True:
                idle "LocalisationON.png"
                hover "LocalisationOFF.png"
            else:
                idle "LocalisationOFF.png"
                hover "LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)



#Screen phone when selfie photo is display
screen selfie :
    imagebutton:
        xpos 700
        ypos 150
        idle "selfie.png"
