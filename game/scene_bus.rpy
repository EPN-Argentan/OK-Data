default whereYouStart = [False,False,False] #track wich application player has launched [Gallery,Cloud]
default findYearPic = False

label bus:
$ freeWifiActivate = False
$ WifiState = False
$ DataState = False

hide screen hubElements
stop music fadeout 1.0

#display photo without sister selie or with it depending of previous events (see bar scene)
nvl clear
if shareSelfie == False:
    show frame_slideshow_noselfie with moveinbottom
    a "oh là là, ça date ça..."
else:
    show frame_slideshow_withselfie with moveinbottom
    a "oh non pourvu que personne d'autre ne voit cette photo..."

winted_nvl "Vous avez reçu un colis Winted, pensez à le récupérer à temps"
a "Oh mince, j'avais complétement zappé !"
a "Allez !  je vais le chercher tout de suite sinon il va encore repartir"
$ renpy.scene(layer = "screens")
scene busAdFreeze
show busAdReveal
window auto hide
$ renpy.pause(3.0, hard=True)
a "mais...mais..."
a "C'est la photo de Pierre mon frère!"
a "Mais comment c'est possible, c'est ma photo en plus ! "
a "Elle doit même encore être sur mon téléphone"
a "Il faut que je la retrouve !"
a "Mais elle a été prise {b}où{/b} et {b}quand{/b} cette photo ?"

label homeScreen:
    hide screen dataBookSearch
    scene busAdOnBus
    window auto hide
    play music "The World's Fair - Godmode.mp3"
    show screen appsPhone(True,True,True,False,False,False,False,0.7)
    if whereYouStart[2] == False:
        a "Je devrais pouvoir trouver ces infos dans ma galerie photos ou alors sur mon cloud..."
    else:
        a "Je devrais trouver la date et la localisation de la photo ailleurs"
    while True:
        empty ""

label searchInGallery:
    hide screen dataCloudSearching
    show screen galeryOpening
    a "Allons voir dans la galerie"
    show screen galeryNoFilter
    hide screen galeryOpening
    if whereYouStart[0] == False and whereYouStart[1] == False: #Player launch gallery at first
        a "Commençons par ici"
        a "Il faut vraiment que je fasse le tri !"
    elif whereYouStart[0] == False and whereYouStart[1] == True: #Player launched cloud at first
        a "Il faut vraiment que je fasse le tri !"
    elif whereYouStart[0] == True and whereYouStart[1] == True: #Player launched both applications
        a "J'ai du louper une info, peut être la date..."
    $ whereYouStart[0] = True
    while True:
        empty ""

label openDataCloud:
    nvl clear
    hide screen galeryNoFilter
    if whereYouStart[0] == True and whereYouStart[1] == False: #Player launch gallery at first
        a "Allons voir sur Datacloud"
    elif whereYouStart[0] == False and whereYouStart[1] == False: #Player launched cloud at first
        a "Allons voir sur Datacloud"
    elif whereYouStart[0] == True and whereYouStart[1] == True: #Player launched both applications
        a "Je devrais au moins pouvoir retrouver le lieu ici"
    $ whereYouStart[1] = True
    if freeWifiActivate == False :
        $ freeWifiActivate = True
        hide screen appsPhone
        show screen freeWifi
        a "il me reste encore un peu de forfait"
        while True:
            empty ""
    else:
        show screen dataCloudOpening
        window auto hide
        $ renpy.pause(1.0, hard=True)
        #show screen dataCloudSearching
        hide screen dataCloudOpening
        jump searchInDataCloud
    while True:
        empty ""


label searchInDataCloud:
    show screen cloudNoFilter
    while True:
        empty ""

label searchInDataBookDate:
    $ whereYouStart[2] = True
    hide screen cloudNoFilter
    show screen dataBookOpening
    window auto hide
    $ renpy.pause(1.0, hard=True)
    show screen dataBookSearch
    hide screen dataBookOpening
    $ dateInput = renpy.input("Entrez la date", "1990", length = 12)   
    $ birthdayYear = str(year-3)
    if dateInput == birthdayYear :
        a "Oui c'était l'année de ses 30 ans"
        a "Mais c'était où ?"
        jump searchInDataBookLocalisation
    else:
        jump searchInDataBookDate

label searchInDataBookLocalisation:
    window auto hide
    $ renpy.pause(1.0, hard=True)
    show screen dataBookSearch
    hide screen dataBookOpening
    $ localisationInput = renpy.input("Entrez la localisation", "Paris", length = 12)
    if localisationInput == "Barcelone" or dateInput =="barcelone" or dateInput == "barcelon" or dateInput == "Barcelon":
            jump foundInDataBook
            hide screen dataBookSearch
    else:
        jump searchInDataBookLocalisation

label foundInDataBook:
    hide screen dataBookSearch
    show screen dataBookFound
    a "Voilà, c'est celle là"
    a "Mais comment ils ont fait ?!"
    a "Ils n'ont pas le droit"
    e_nvl "Malheureusement si."
    e_nvl "Quand tu partages une photo sur un réseau social, celle-ci ne t'appartient plus."
    e_nvl "Tu peux savoir connaître les endroits où elles sont utilisées  grâce à des outils de recherche inversée comme {a=https://lens.google/intl/fr/}google lens{/a}."
    window auto hide
    $ renpy.pause(1.0, hard=True)
    hide screen dataBookFound
    show screen outOfBattery
    hide screen appsPhone
    a "Mince !"
    a "Et en plus j'ai oublié mon chargeur"
    hide screen outOfBattery

label travelToStore:
    hide busAdFreeze
    hide screen galeryFilter
    stop music fadeout 1.0
    show getInsideBus
    window auto hide
    $ renpy.pause(3.0, hard=True)
    #empty ""
    show insideBus
    window auto hide
    $ renpy.pause(3.0, hard=True)
    #empty ""
    show exitBus
    window auto hide
    $ renpy.pause(3.0, hard=True)

label insideStore:
    show getInStore
    window auto hide
    $ renpy.pause(3.0, hard=True)
    show askStore
    window auto hide
    $ renpy.pause(3.0, hard=True)
    show receiveStore
    window auto hide
    $ renpy.pause(3.0, hard=True)
    show freezeReceive
    vendeuse "Voilà votre colis"
    a "Merci"
    vendeuse "N'hésitez pas à profiter de notre promotion sur l'impression sur mug"
    a "C'est vrai, on peut faire ça ici ?"
    a "Je pourrais en profiter pour customiser une tasse pour mon frère!"
    show computerStore
    window auto hide
    $ renpy.pause(3.0, hard=True)
    show zoomComputerStore
    show screen storeCustomPage
    a "Bon, alors qu'est ce que je pourrai mettre dessus ?"
    while True:
        empty ""

label outStore:
    show screen storeCustomPage
    a "Ce sera du plus bel effet !"
    window auto hide
    $ hubClickable["photoFrame"]= 0
    menu:
        "Récupérer votre mug":
            call addPoints(-5,'point_sociaux',"","","Il vaut mieux toujours prendre l'habitude de se déconnecter de n'importe quelle sessionµ Un ordinateur resté connecté est une porte ouverte pour n'importe qui", "","hub") from _call_addPoints_1
        "Rester sur la session":
            a "J'ai du oublier quelquechose"
    while True:
        empty ""
    jump hub


#####################################################################SCREEN#####################################################################
#All scenes elements used in this label
image emptyPhone:
    "smartphone.png"
image frame_slideshow_noselfie:
   "/UI/Cadre/slideshowFrame_001.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_002.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_003.png"
   pause 2.5
   repeat

image frame_slideshow_withselfie:
   "/UI/Cadre/slideshowFrame_015.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_002.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_003.png"
   pause 2.5
   repeat


screen galeryOpening:
    add "UI/applications/loadingScreen.png" xalign 0.6955 yalign 0.5
    add "UI/applications/Icons/appGallery.png" xalign 0.675 yalign 0.5 zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

screen galeryNoFilter:
    add "UI/applications/galeryNoFilter.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5
    hbox:
            xalign 0.74
            yalign 0.22
            imagebutton:
                idle "UI/applications/Exit.png"
                hover "UI/applications/Exit.png"
                action Jump("homeScreen")
    side "c b r":
         area (0.575, 0.3, 330, 500)

         viewport id "vp":
            draggable True
            vbox:
                spacing 20
                text "[year]"  color "#000000"
                grid 2 1:
                    spacing 20
                    add "UI/applications/galery/dog001.jpg"
                    add "UI/applications/galery/dog002.jpg"
                text "[year-1]" color "#000000"
                grid 2 3:
                    spacing 20
                    add "UI/applications/galery/motherSister.png"
                    add "UI/applications/galery/sisterBeach.png"
                    add "UI/applications/galery/brotherInParis001.png"
                    add "UI/applications/galery/brotherSelfie.png"
                    add "UI/applications/galery/003.jpeg"
                text "[year-2]"  color "#000000"
                grid 2 2:
                    spacing 20
                    add "UI/applications/galery/motherBarcelona001.png"
                    add "UI/applications/galery/brotherInBarcelona001.png"
                    add "UI/applications/galery/in_barcelone_en_mode_winner.png"
                    add "UI/applications/galery/brotherInBarcelona002.png"


         bar value XScrollValue("vp")
         vbar value YScrollValue("vp")

screen cloudNoFilter:
    add "UI/applications/cloudNoFilter.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

    side "c b r":
         area (0.57, 0.3, 330, 550)

         viewport id "vp":
            draggable True
            vbox:
                spacing 20
                grid 2 5:
                    spacing 20
                    imagebutton:
                        idle At('UI/applications/galery/barcelona001.jpg', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/barcelona001.jpg"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002358_01")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/jump_with_sister_in_the_street.png', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/jump_with_sister_in_the_street.png"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002555_12")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/barcelona002.jpg', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/barcelona002.jpg"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002355_17")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/motherBarcelona001.png', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/motherBarcelona001.png"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002455_05")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/Sagrada3.jpg', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/Sagrada3.jpg"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002300_01")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/brotherInBarcelona001.png', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/brotherInBarcelona001.png"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n003055_01")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/brotherInBarcelona002.png', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/brotherInBarcelona002.png"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002355_01")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/sisterBeach.png', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/sisterBeach.png"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002355_01")
                        unhovered Hide("metaData")
                        action NullAction()
                    imagebutton:
                        idle At('UI/applications/galery/in_barcelone_en_mode_winner.png', outline_transform(6, "#ff0000", 4.0))
                        hover "UI/applications/galery/in_barcelone_en_mode_winner.png"
                        hovered Show("metaData",None,"Métadonnées : \nBarcelone \n002355_01")
                        unhovered Hide("metaData")
                        action NullAction()
         bar value XScrollValue("vp")
         vbar value YScrollValue("vp")
         
    hbox:
        xalign 0.74
        yalign 0.22
        imagebutton:
            idle "UI/applications/Exit.png"
            hover "UI/applications/Exit.png"
            action Jump("homeScreen")

screen metaData(text):
     frame:
         xpadding 10
         ypadding 10
         xalign 0.5
         yalign 0.8
         has hbox
         text "[text]"

screen dataCloudOpening:
    add "UI/applications/loadingScreen.png" xalign 0.6955 yalign 0.5
    add "UI/applications/Icons/appCloud.png" xalign 0.6955 yalign 0.5 zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

screen birthdayPicture:
    add "UI/Cadre/frameBirthday.png" xalign 0.5 yalign 0.5

screen notificationWinted:
    add "UI/Cadre/notificationWinted.png" xalign 0.75 yalign 0.8


screen freeWifi:
    add "smartphone.png" xalign 0.7 yalign 0.5
    add "UI/applications/FreeWifi.png" xalign 0.6955 yalign 0.5
    hbox:
        spacing 20
        xalign 0.69
        yalign 0.22
        imagebutton:
            if WifiState == True:
                idle "UI/settingsIcons/WifiON.png"
                hover "UI/settingsIcons/WifiOFF.png"
            else:
                idle "UI/settingsIcons/WifiOFF.png"
                hover "UI/settingsIcons/WifiON.png"
            action [SetVariable("WifiState", not WifiState),Call("addPoints",-5,"point_localisation","","","Évites les réseaux wifi publics, ils sont dangereux ","","openDataCloud")]
        imagebutton:
            if DataState == True:
                idle "UI/settingsIcons/DataON.png"
                hover "UI/settingsIcons/DataOFF.png"
            else:
                idle "UI/settingsIcons/DataOFF.png"
                hover "UI/settingsIcons/DataON.png"
            action [SetVariable("DataState", not DataState),Call("addPoints",+5,"point_localisation","",""," ","Tu as bien fait d'éviter le wifi public, c'est le maaaaal","openDataCloud")]
        imagebutton:
            if LocalisationState == True:
                idle "UI/settingsIcons/LocalisationON.png"
                hover "UI/settingsIcons/LocalisationOFF.png"
            else:
                idle "UI/settingsIcons/LocalisationOFF.png"
                hover "UI/settingsIcons/LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)
    # frame:
    #     area (1100,500,350,350)
    #     background Frame(
    #         Text( "\u25A2", #### <--- this is a small rounded rectangle character
    #               background="#ffffff",  
    #               color="#ffffff", 
    #               font="DejaVuSans.ttf", 
    #               size=72), 
    #         32, 32, 
    #         tile=True)

    #     text "{color=#000}Afin d’accéder à votre Data Cloud, veuillez vous connecter à un réseau via vos données mobiles ou un réseau wifi public.{/color}"

    frame:
        background "#fff"
        pos (1100,400)
        padding (12, 8)
        xysize (325, 300)

        has vbox:
            align (0.5, 0.5)
            text "{color=#000}Afin d’accéder à votre Data Cloud, veuillez vous connecter à un réseau via vos données mobiles ou un réseau wifi public.{/color}"
        
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

screen cloudPhotos:
    add "smartphone.png" xalign 0.7 yalign 0.5

screen dataBookOpening:
    add "UI/applications/loadingScreen.png" xalign 0.6955 yalign 0.5
    add "UI/applications/Icons/appDataBook.png" xalign 0.67 yalign 0.5  zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

screen dataBookSearch:
    add "UI/applications/dataBookSearch.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5
    hbox:
        xalign 0.74
        yalign 0.22
        imagebutton:
            idle "UI/applications/Exit.png"
            hover "UI/applications/Exit.png"
            action Jump("homeScreen")


screen dataBookFound:
    add "UI/applications/dataBookInFeed.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

screen outOfBattery:

    add "UI/applications/outBattery.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

default profilPic = False

screen storeCustomPage:
    add "UI/store/hobbyFabCustompage.png" xalign 0.44 yalign 0.42
    if profilPic == False:
        imagebutton:
            idle At("UI/store/importPicture.png", outline_transform(0, "#8080804f", 4.0, offset=(3, 3)))
            hover "UI/store/importPicture.png"
            xalign 0.72
            yalign 0.8
            action Show("logViaPopup")
        imagebutton:
            idle "UI/store/profilPicLogOut.png"
            hover "UI/store/profilPicLogOut.png"
            xalign 0.77
            yalign 0.15
            action NullAction()
    else:
        add "UI/store/customMugShot.png" xalign 0.33 yalign 0.71
        imagebutton:
            idle At("UI/store/printBtn.png", outline_transform(0, "#8080804f", 4.0, offset=(3, 3)))
            hover "UI/store/printBtn.png"
            xalign 0.70
            yalign 0.8
            action Call("outStore")
        imagebutton:
            idle At("UI/store/profilPicLogIn.png", outline_transform(0, "#8080804f", 4.0, offset=(3, 3)))
            hover "UI/store/profilPicLogIn.png"
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Déconnexion"))]
            xalign 0.77
            yalign 0.15
            action [Call("addPoints",5,'point_sociaux',"","","","Vous avez raison, il vaut mieux toujours prendre l'habitude de se déconnecter de n'importe quelle sessionµ Un ordinateur resté connecté est une porte ouverte pour n'importe qui",'hub')]

screen logViaPopup:
    add "UI/store/logVia.png" xalign 0.5 yalign 0.5
    imagebutton:
        idle At("UI/store/logViaOK.png", outline_transform(0, "#8080804f", 4.0, offset=(3, 3)))
        hover "UI/store/logViaOK.png"
        xalign 0.5
        yalign 0.51
        action [SetVariable("profilPic","True"),Hide("logViaPopup"),Call("addPoints",-2,'point_sociaux',"","","Il vaut mieux éviter la connexion via un service tiers (SSO)µ Ce système donne accès à ces services à de nombreuses informations personnelles relatives au site parcouruµ Vous ne voudriez pas que votre boite mail connaisse vos goûts en matière de consommation ou de lecture politique","",'')]
    imagebutton:
        idle "UI/store/logViaMail.png"
        hover "UI/store/logViaMail.png"
        xalign 0.5
        yalign 0.6
        action [SetVariable("profilPic","True"),Hide("logViaPopup"),Call("addPoints",2,'point_sociaux',"","","","Il vaut mieux éviter la connexion via un service tiers (SSO)µ Ce système donne accès à ces services à de nombreuses informations personnelles relatives au site parcouruµ Vous ne voudriez pas que votre boite mail connaisse vos goûts en matière de consommation ou de lecture politique",'')]
