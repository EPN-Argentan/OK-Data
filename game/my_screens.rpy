screen hubElements:
    imagebutton:
        xpos 1258
        ypos 70
        idle At('UI/imagebuttons/sources.png', outline_transform(6, "#ffffff", 4.0))
        hover "UI/imagebuttons/sources.png"
        hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Sources"))]
        action ShowMenu("sources")
    if hubClickable["dog"] == 1:
        imagebutton:
            xpos 1467
            ypos 827
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
            xpos 665
            ypos 540
            idle At('UI/imagebuttons/forest.png', outline_transform(6, "#ffffff", 4.0))
            hover "UI/imagebuttons/forest.png"
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

#Smartphone home screen
#Each argument is one application icon that can be avaible or not
transform greyscale():
    matrixcolor SaturationMatrix(0)

default nameAppSize = 18

screen appsPhone(A1=True,A2=True,A3=True,B1=True,B2=True,B3=True,C1=True,posY=0.5) :
    imagebutton:
        xalign posY
        ypos 150
        idle "smartphone.png"

    frame:
        background None
        xalign posY
        yalign 0.5
        xmaximum 360
        ymaximum 700
        grid 3 3:
            spacing 12
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if A1:
                        idle At("UI/applications/Icons/appGallery.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appGallery.png"
                        action [Hide("appsPhone"),Jump("searchInGallery")]
                    else:
                        idle "UI/applications/Icons/appGallery.png" at greyscale()
                text "{color=#555}Photos{/color}" xalign 0.5 size nameAppSize
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if A2:
                        idle At("UI/applications/Icons/appCloud.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appCloud.png"
                        action Jump("openDataCloud")
                    else:
                        idle "UI/applications/Icons/appCloud.png" at greyscale()
                text "{color=#555}Data Book{/color}" xalign 0.5 size nameAppSize
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if A3:
                        idle At("UI/applications/Icons/appDataBook.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appDataBook.png"
                        action Jump("searchInDataBookDate")
                    else:
                        idle "UI/applications/Icons/appDataBook.png" at greyscale()
                text "{color=#555}DataBook{/color}" xalign 0.5 size nameAppSize
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if B1:
                        idle At("UI/applications/Icons/appMail.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appMail.png"
                        action Jump("searchInGallery")
                    else:
                        idle "UI/applications/Icons/appMail.png" at greyscale()
                text "{color=#555}Mail{/color}" xalign 0.5 size nameAppSize
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if B2:
                        idle At("UI/applications/Icons/appLocalisation.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appLocalisation.png"
                        action Jump("searchInGallery")
                    else:
                        idle "UI/applications/Icons/appLocalisation.png" at greyscale()
                text "{color=#555}Carte{/color}" xalign 0.5 size nameAppSize
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if B3   :
                        idle At("UI/applications/Icons/appNoCo.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appNoCo.png"
                        action Jump("searchInGallery")
                    else:
                        idle "UI/applications/Icons/appNoCo.png" at greyscale()
                text "{color=#555}Normandie{/color}" xalign 0.5 size nameAppSize
            vbox:
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    if C1   :
                        idle At("UI/applications/Icons/appSettings.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                        hover "UI/applications/Icons/appSettings.png"
                        action Jump("searchInGallery")
                    else:
                        idle "UI/applications/Icons/appSettings.png" at greyscale()
                text "{color=#555}Paramètres{/color}" xalign 0.5 size nameAppSize


    hbox:
        xalign posY-0.01
        yalign 0.2
        spacing 20
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
                    idle At("UI/browser/eventBirtdhay.png", outline_transform(0, "#8080804f", 4.0, offset=(5, 5)))
                    hover "UI/browser/eventBirtdhay.png"
                    action Jump("insideEventPage")
                imagebutton:
                    idle "UI/browser/alarmArticle.png"
                    action Call("addPoints",-1,'point_conviction',"","","Des liens vers des articles peuvent vous emmener vers des sites frauduleuxµ Attention aux articles racoleurs","",'')
                imagebutton:
                    idle "UI/browser/chickenArticle.jpg"
                    action Call("addPoints",-1,'point_conviction',"","","Des liens vers des articles peuvent vous emmener vers des sites frauduleuxµ Attention aux articles racoleurs","",'')
                imagebutton:
                    idle "UI/browser/burgerArticle.jpg"
                    action Call("addPoints",-1,'point_conviction',"","","Des liens vers des articles peuvent vous emmener vers des sites frauduleuxµ Attention aux articles racoleurs","",'')
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
                action [Show("browserWindowSubscribeTrue"),Call("addPoints",-5,"point_sociaux","","","Evites de donner trop d’informations ou de vraies informations. Les champs obligatoires (indiquées par un astérisque) sont suffisants.µCela contribue à divulguer vos données personnelles d’identité. µDes grandes Sociétés comme ici DATABOOK récoltent ces données et les revendent ensuite, µsoit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses. ","","browserLabelFeed")]
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
        action NullAction()


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

screen countdown: 
    text "[points[listePoints[0]][0]]"
    timer 1.0 repeat True action SetDict(points, listePoints[0], [points[listePoints[0]][0] - 1, points[listePoints[0]][1]])