screen hubElements:

    if hubClickable["dog"] == 1:
        imagebutton:
            xpos 1400
            ypos 797
            idle At('UI/imagebuttons/dog.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/dog.png"
            action Jump("walkOut")

    if hubClickable["phone"] == 1:
        imagebutton:
            xpos 1175
            ypos 607
            idle At('UI/imagebuttons/phone.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/phone.png"
            action Jump("barOut")

    if hubClickable["phoneCall"] == 1:
        imagebutton:
            xpos 1175
            ypos 607
            idle At('UI/imagebuttons/phone.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/phone.png"
            action Jump("browserLabel")

    if hubClickable["watch"] == 1:
        imagebutton:
            xpos 230
            ypos 838
            idle At('UI/imagebuttons/watch.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/watch.png"
            action OpenURL("http://reddit.com/")
            #action Jump("browserLabel")dataZon
    
    if hubClickable["forest"] == 1:
        imagebutton:
            xpos 1400
            ypos 797
            idle At('UI/imagebuttons/dog.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/dog.png"
            action Jump("forest")

    if hubClickable["laptop"] == 1:
        imagebutton:
            xpos 199
            ypos 410
            idle At('UI/imagebuttons/PC.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/PC.png"
            action Jump("dataZon")

    if hubClickable["tablet"] == 1:
        imagebutton:
            xpos 275
            ypos 765
            idle At('UI/imagebuttons/tablet.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/tablet.png"
            action Jump("algorithmGame")
    
    if hubClickable["photoFrame"] == 1:
        imagebutton:
            xpos 435
            ypos 145
            idle At('UI/imagebuttons/photoFrame.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/photoFrame.png"
            action Jump("bus")

    #...
    #add list of hub clickable elements here

#Screen when head phone is just visible with settings icons
screen phoneDown :
    imagebutton:
        xalign 0.9
        yalign 3.0
        idle "smartphone.png"
        action NullAction()
    hbox:
        spacing 20
        xalign 0.87
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
screen appsPhone(A1=True,A2=True,A3=True,B1=True,B2=True,B3=True) :
    imagebutton:
        xalign 0.5
        ypos 150
        idle "smartphone.png"

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
                    idle "UI/applications/Icons/appOKDATA.png"
                    hover "UI/applications/Icons/appOKDATA_hover.png"
                    action Jump("searchInGallery")
                else:
                    idle "UI/applications/Icons/appOKDATA_out.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A2:
                    idle "UI/applications/Icons/appOKDATA.png"
                    hover "UI/applications/Icons/appOKDATA_hover.png"
                    action Jump("openDataCloud")
                else:
                    idle "UI/applications/Icons/appOKDATA_out.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A3:
                    idle "UI/applications/Icons/appphoto.png"
                    hover "UI/applications/Icons/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/Icons/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B1:
                    idle "UI/applications/Icons/appphoto.png"
                    hover "UI/applications/Icons/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/Icons/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B2:
                    idle "UI/applications/Icons/appphoto.png"
                    hover "UI/applications/Icons/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/Icons/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B3   :
                    idle "UI/applications/Icons/appphoto.png"
                    hover "UI/applications/Icons/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/Icons/appphotoout.png"


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


screen browserWindowFeed:
    add "UI/browser/frameDataBook.png" xpos 42 ypos 97
    side "c b r":
        area (358, 160, 675, 800)

        viewport id "vp":
            draggable True
            vbox:
                spacing 30
                imagebutton:
                    idle "UI/browser/eventBanner.png"
                imagebutton:
                    idle "UI/browser/eventBirtdhay.png"
                    action Jump("insideEventPage")
                imagebutton:
                    idle "UI/browser/alarmArticle.png"
                imagebutton:
                    idle "UI/browser/chickenArticle.jpg"
                imagebutton:
                    idle "UI/browser/burgerArticle.jpg"
            #add "UI/browser/feedDataBook.png"

        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")

screen browserWindowSubscribe:
    add "UI/browser/DataBookToSubscribe.png" xpos 42 ypos 97
    vbox:
        spacing 30
        hbox:
            spacing 15
            xpos 380
            ypos 805
            imagebutton:
                idle "UI/browser/fakeInformation_idle.png"
                hover "UI/browser/fakeInformation_hover.png"
                action [Show("browserWindowSubscribeFake"),Call("addPoints",5,"point_sociaux","","","","Bravo ! µ Il est parfois bon de ne pas trop en dire.µLes champs obligatoires (indiquées par un astérisque) sont suffisants. µTrop de précision sur votre identité contribue à divulguer vos données personnelles d’identité.µ Des grandes Sociétés comme ici DATABOOK récoltent ces données et les revendent ensuite, µsoit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses.","browserLabelFeed")]
            imagebutton:
                idle "UI/browser/trueInformation_idle.png"
                hover "UI/browser/trueInformation_hover.png"
                action [Show("browserWindowSubscribeTrue"),Call("addPoints",-5,"point_sociaux","","","Vous perdez des points ! µEvitez de donner trop d’informations ou de vraies informations. Les champs obligatoires (indiquées par un astérisque) sont suffisants.µCela contribue à divulguer vos données personnelles d’identité. µDes grandes Sociétés comme ici DATABOOK récoltent ces données et les revendent ensuite, µsoit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses. ","","browserLabelFeed")]
        #add "UI/browser/feedDataBook.png"

screen browserWindowSubscribeTrue:
    add "UI/browser/DataBookTrueInformation.png" xpos 42 ypos 97

screen browserWindowSubscribeFake:
    add "UI/browser/DataBookFakeInformation.png" xpos 42 ypos 97

#Phone call incoming
screen callPhoneIncoming:
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5
    add "UI/call/incoming_call_mother.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.69
        idle "UI/call/answer_idle.png"
        hover "UI/call/answer_hover.png"
        action [Show("callPhoneAnswer"),Jump("browserLabelCall")]

screen callPhoneAnswer:
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5
    add "UI/call/call_mother.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.69
        idle "UI/call/hangup_hover.png"
        hover "UI/call/hangup_idle.png"
        action Jump("browserLabelAfterCall")


style bubble_tuto:
    background "#e226c0"
    xpadding 30
    ypadding 30

screen bubbleTuto(value="mon texte", posX=0, posY=0):
    add "UI/bubbletuto/bubbletop.png" xpos posX ypos posY
    frame:
        style "bubble_tuto"
        xpos posX
        ypos posY+20
        text value xalign 0.5 yalign 0.5

screen dataMap:
    add "smartphone.png" xalign 0.5 yalign 0.5
    add "UI/applications/dataMap.png" xalign 0.5 yalign 0.5
    frame:
        background "#ffffff"
        xalign 0.5
        yalign 0.65
        text "{color=#000000}{size=-10}Veuillez activer la \ngéolocalisation pour \nconnaitre l'itinéraire{/size}{/color}" xalign 0.5 yalign 0.5

screen phoneCall:
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5


#Screen phone when selfie photo is display
screen selfie :
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5
    add "UI/applications/selfie.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.8
        idle "UI/applications/Icons/send_idle.png"
        hover "UI/applications/Icons/send_hover.png"
        action Jump("barOutAfter")
