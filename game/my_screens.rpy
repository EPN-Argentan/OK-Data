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
                    idle "appphoto.png"
                    hover "appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A2:
                    idle "appphoto.png"
                    hover "appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A3:
                    idle "appphoto.png"
                    hover "appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B1:
                    idle "appphoto.png"
                    hover "appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B2:
                    idle "appphoto.png"
                    hover "appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B3   :
                    idle "appphoto.png"
                    hover "appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "appphotoout.png"


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
        xalign 0.5
        yalign 0.5
        idle "selfie.png"
    imagebutton:
        xalign 0.5
        yalign 0.72
        idle "share-icon.png"
