label bus:
$ freeWifiActivate = False
hide screen hubElements

#display photo without sister selie or with it depending of previous events (see bar scene)
if shareSelfie == False:
    show frame_slideshow_noselfie with moveinbottom
    a "oh là là, ça date ça..."
else:
    show frame_slideshow_withselfie with moveinbottom
    a "oh non pourvu que personne d'autre ne voit cette photo..."

e_nvl "Vous avez reçu un colis Winted, pensez à le récupérer à temps"
a "Oh mince, j'avais complétement zappé !"
a "Allez !  je vais le chercher tout de suite sinon il va encore repartir"
$ renpy.scene(layer = "screens")
scene busAdFreeze
show busAdReveal
window auto hide
$ renpy.pause(3.0, hard=True)
a "mais...mais..."
a "C'est la photo des 30 ans de Pierre mon frère!"
a "Mais comment c'est possible, c'est ma photo en plus ! "
a "Elle doit même encore être sur mon téléphone"

label homeScreen:
    show screen appsPhone(True,True,False,False,False,False)
    while True:
        empty ""

label searchInGallery:
    show screen galeryOpening
    a "..."
    show screen galeryNoFilter
    hide screen galeryOpening
    a "Cherchons"
    a "Il faut que je fasse le tri !"
    while True:
        empty ""

label openDataCloud:
    a "mince, elle doit dater d'avant 2022"
    if freeWifiActivate == False :
        $ freeWifiActivate = True
        show screen freeWifi
        a "il me reste encore un peu de forfait"
        while True:
            empty ""
    else:
        show screen dataCloudOpening
        window auto hide
        $ renpy.pause(1.0, hard=True)
        show screen dataCloudSearching
        hide screen dataCloudOpening
        a "mais de quand date-t-elle ?..."
        jump inputDate
    while True:
        empty ""

label inputDate:
    $ dateInput = renpy.input("Entrez la date recherchée", "2000", length = 4)
    $ birthdayYear = str(year-5)
    if dateInput == birthdayYear:
        hide screen dataCloudSearching
        jump searchInDataCloud
    else:
        jump inputDate

label searchInDataCloud:
    show screen cloudNoFilter
    a "je fais ma recherche"
    window auto hide
    $ renpy.pause(3.0)
    a "bon, toujours rien"
    a "j'ai peut-être vu cette photo sur Databook !"
    window auto hide
    $ renpy.pause(1.0)

label searchInDataBook:
    hide screen cloudNoFilter
    show screen dataBookOpening
    window auto hide
    $ renpy.pause(1.0, hard=True)
    show screen dataBookSearch
    hide screen dataBookOpening
    $ dateInput = renpy.input("Entrez la localisation", "Paris", length = 12)
    if dateInput == "Barcelone":
        jump foundInDataBook
        hide screen dataBookSearch
    else:
        jump searchInDataBook

label foundInDataBook:
    hide screen dataBookSearch
    show screen dataBookFound
    a "Mais non !"
    e_nvl "quand vous partagez une photo sur un réseau social, celle-ci ne vous appartient plus."
    window auto hide
    $ renpy.pause(3.0, hard=True)
    hide screen dataBookFound
    show screen outOfBattery
    a "mince !"
    a "et en plus j'ai oublié mon chargeur"
    hide screen outOfBattery

label travelToStore:
    hide busAdFreeze
    hide screen galeryFilter
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
    a "Mais oui, je pourrai en profiter pour customiser une tasse !"
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
    menu:
        "Récupérer votre mug":
            call addPoints(-5,'point_sociaux',"","","Il vaut mieux toujours prendre l'habitude de se déconnecter de n'importe quelle sessionµ Un ordinateur resté connecté est une porte ouverte pour n'importe qui", "","hub")
        "Rester sur la session":
            a "J'ai du oublier quelquechose"
    while True:
        empty ""
    jump hub


#####################################################################SCREEN#####################################################################
#All scenes elements used in this label

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
    add "UI/applications/loadingScreen.png" xalign 0.5 yalign 0.5
    add "UI/applications/Icons/appGallery.png" xalign 0.5 yalign 0.5 zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen galeryNoFilter:
    add "UI/applications/galeryNoFilter.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

    side "c b r":
         area (0.42, 0.3, 330, 500)

         viewport id "vp":
            draggable True
            vbox:
                spacing 20
                text "[year]"  color "#000000"
                grid 2 4:
                    spacing 20
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                    add "UI/applications/galery/004.jpeg"
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                text "[year-1]" color "#000000"
                grid 2 4:
                    spacing 20
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                text "[year-2]"  color "#000000"
                grid 2 4:
                    spacing 20
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                textbutton "Retrouvez vos anciennes photos sur Datacloud" action Jump("openDataCloud")


         bar value XScrollValue("vp")
         vbar value YScrollValue("vp")

screen cloudNoFilter:
    add "UI/applications/cloudNoFilter.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

    side "c b r":
         area (0.42, 0.3, 330, 550)

         viewport id "vp":
            draggable True
            vbox:
                spacing 20
                text "[year-5]"  color "#000000"
                grid 2 4:
                    spacing 10
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                    add "UI/applications/galery/004.jpeg"
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
         bar value XScrollValue("vp")
         vbar value YScrollValue("vp")

screen dataCloudOpening:
    add "UI/applications/loadingScreen.png" xalign 0.5 yalign 0.5
    add "UI/applications/Icons/appCloud.png" xalign 0.5 yalign 0.5 zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen dataCloudSearching:
    add "UI/applications/cloudDateInput.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.58
        yalign 0.22
        imagebutton:
            idle "UI/applications/Exit.png"
            hover "UI/applications/Exit.png"
            action Jump("homeScreen")

screen birthdayPicture:
    add "UI/Cadre/frameBirthday.png" xalign 0.5 yalign 0.5

screen notificationWinted:
    add "UI/Cadre/notificationWinted.png" xalign 0.75 yalign 0.8

screen freeWifi:
    add "smartphone.png" xalign 0.5 yalign 0.5
    add "UI/applications/FreeWifi.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.65
        spacing 10
        imagebutton:
            idle "UI/applications/yes_idle.png"
            hover "UI/applications/yes_hover.png"
            action Call("addPoints",-5,"point_sociaux","","","Faites attention, sur des réseaux publics vous n'êtes pas protégé ! ","","openDataCloud")
        imagebutton:
            idle "UI/applications/no_idle.png"
            hover "UI/applications/no_hover.png"
            action Call("addPoints",5,"point_sociaux","","Bravo","Faites attention, sur des réseaux publics vous n'êtes pas protégé ! ","Dans la mesure du possible, évitez les réseaux wifi publics","openDataCloud")

    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen cloudPhotos:
    add "smartphone.png" xalign 0.5 yalign 0.5

screen dataBookOpening:
    add "UI/applications/loadingScreen.png" xalign 0.5 yalign 0.5
    add "UI/applications/Icons/appDataBook.png" xalign 0.5 yalign 0.5  zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen dataBookSearch:
    add "UI/applications/dataBookSearch.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.58
        yalign 0.22
        imagebutton:
            idle "UI/applications/Exit.png"
            hover "UI/applications/Exit.png"
            action Jump("searchInDataCloud")


screen dataBookFound:
    add "UI/applications/dataBookFound.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen outOfBattery:
    add "UI/applications/outBattery.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

default profilPic = False

screen storeCustomPage:
    add "UI/store/hobbyFabCustompage.png" xalign 0.44 yalign 0.42
    if profilPic == False:
        imagebutton:
            idle At("UI/store/importPicture.png", outline_transform(6, "#A27ABB", 4.0))
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
            idle At("UI/store/printBtn.png", outline_transform(6, "#A27ABB", 4.0))
            hover "UI/store/printBtn.png"
            xalign 0.70
            yalign 0.8
            action Call("outStore")
        imagebutton:
            idle At("UI/store/profilPicLogIn.png", outline_transform(6, "#A27ABB", 4.0))
            hover "UI/store/profilPicLogIn.png"
            xalign 0.77
            yalign 0.15
            action [Call("addPoints",5,'point_sociaux',"","","","Vous avez raison, il vaut mieux toujours prendre l'habitude de se déconnecter de n'importe quelle sessionµ Un ordinateur resté connecté est une porte ouverte pour n'importe qui",'hub')]

screen logViaPopup:
    add "UI/store/logVia.png" xalign 0.5 yalign 0.5
    imagebutton:
        idle At("UI/store/logViaOK.png", outline_transform(6, "#A27ABB", 4.0))
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

