# Here's the code for the phone!

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "Nighten" ##The name of the main character, used to place them on the screen
define Syrielle = "Syrielle"
define Sepharo = "Sepharo"
define Winted = "Winted"

init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")
    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 0.5 yoffset 0

transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0


transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):
    tag example
    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        if len(dialogue) == 0:
            $ PhoneState = False
        viewport:
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 30
                use nvl_phonetext(dialogue)
                null height 100
        hbox:
            spacing 20
            xalign 0.5
            yalign -0.15 #top margin for settings buttons
            imagebutton:
                if WifiState == True:
                    idle "UI/settingsIcons/WifiON.png"
                    hover "UI/settingsIcons/WifiOFF.png"
                else:
                    idle "UI/settingsIcons/WifiOFF.png"
                    hover "UI/settingsIcons/WifiON.png"
                action SetVariable("WifiState", not WifiState)
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

screen nvl_phonetext(dialogue):
    style_prefix None
    #Buttons settings, bluetooth, localisation...
    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos .0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == MC_Name:
                $ message_frame = "UI/conversation/phone_send_frame.png"
            else:
                $ message_frame = "UI/conversation/phone_received_frame.png"

            hbox:
                spacing 10
                if d.who == MC_Name:
                    box_reverse True

                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == MC_Name:
                        $ message_icon = "UI/conversation/mediateur_phone_icon.png"
                    elif d.who == Syrielle:
                        $ message_icon = "UI/conversation/sister_phone_icon.png"
                    elif d.who == Sepharo:
                        $ message_icon = "UI/conversation/sepharo_phone_icon.png"
                    elif d.who == Winted:
                        $ message_icon = "UI/conversation/winted_phone_icon.png"
                    else:
                        $ message_icon = "UI/conversation/mediateur_phone_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()

                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != MC_Name and previous_d_who != d.who:
                        text d.who

                    frame:
                        #layout message text bubble
                        padding (20,20)


                        background Frame(message_frame, 23,23,23,23)
                        xsize 350

                        if d.current:
                            if d.who == MC_Name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)
                            xsize 350
                            slow_cps False


                            if d.who == MC_Name :
                                color "#FFF"
                                text_align 1.0
                                xpos -580
                            else:
                                color "#000"


                            id d.what_id
        $ previous_d_who = d.who

style phoneFrame is default

style phoneFrame_frame:
    background Transform("smartphone.png", xcenter=0.5,yalign=0.5)
    #foreground Transform("phone_foreground.png", xcenter=0.5,yalign=0.5)

    ysize 550
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset 50 #margin-top phone dialogue frame

style phoneFrame_vbox:
    spacing 15 #spacing between dialogue box from same conversation
    xfill True
