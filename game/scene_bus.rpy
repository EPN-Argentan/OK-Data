default whereYouStart = [False,False,False] #track wich application player has launched [Gallery,Cloud]
default findYearPic = False
default birthdayYear = year-2

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
    a "Ouah, c’est vieux ça !"
else:
    show frame_slideshow_withselfie with moveinbottom
    a "Mais qu’est-ce que cette photo fait là ? Pourvu que personne ne tombe dessus !"
    e_nvl "Quand tu prends une photo avec ton téléphone, si celui-ci est connecté à ton cloud, la photo peut être automatiquement sauvegardée en ligne."
    e_nvl "Et là… toute personne ou appareil ayant accès à ce cloud peut aussi y jeter un œil."
    e_nvl "Pratique pour retrouver tes souvenirs, mais mieux vaut garder un œil sur les paramètres de partage !"
winted_nvl "Rappel : Votre colis Winsted vous attend ! Pensez à venir le récupérer à temps."
a "Oh mince, j’avais complètement oublié !"
a "Bon, j’y vais tout de suite."
$ renpy.scene(layer = "screens")
scene busAdFreeze
show busAdReveal
window auto hide
$ renpy.pause(3.0, hard=True)
a "Ben ! Pierre, il joue les modèles maintenant ? "
a "Comment mon frère a-t-il pu se retrouver sur cette pub !?"
a "C'est moi qui ai pris cette photo en plus ! "
a "Je devrais pouvoir la retrouver sur mon téléphone."
a "Mais je l'ai prise {b}où{/b} et {b}quand{/b} cette photo ?"

label homeScreen:
    hide screen dataBookSearch
    hide screen searchInGallery
    hide screen dataCloudSearching
    hide screen cloudNoFilter
    scene busAdOnBus
    window auto hide
    play music "The World's Fair - Godmode.mp3"
    show screen appsPhone(True,True,True,False,False,False,False,0.7)
    if whereYouStart[0] == False and whereYouStart[1] == False: #Player launch gallery at first
        a "En cherchant sur mes photos ou mon {a=information: Au lieu de garder tes données ou tes photos sur ton ordinateur, ou ton téléphone, tu les envoies dans le Cloud. Ainsi, quand tu en as besoin, tu peux les récupérer de n'importe où, tant que tu as une connection internet. }cloud{/a}, je devrais retrouver la date et le lieu de prise de vue."
    elif whereYouStart[0] == False and whereYouStart[1] == True: #Player launched cloud at first
        a "je dois chercher dans la galerie"
    elif whereYouStart[0] == True and whereYouStart[1] == False: #Player launched cloud at first
        a "je dois chercher dans le cloud"
    elif whereYouStart[0] == True and whereYouStart[1] == True: #Player launched both applications
        a "J’ai la date et le lieu, mais je n’ai pas encore retrouvé la photo. Elle devrait être sur un {a=information: Un post, c’est un petit bout de vie qu’on partage sur les réseaux sociaux — une pensée, une image, une vidéo… bref, c’est un petit instant qu’on choisit de rendre public ou de partager avec ses amis.}post{/a} Databook, allons vérifier !"
    while True:
        empty ""

label searchInGallery:
    $ whereYouStart[0] = True
    hide screen dataBookSearch
    hide screen dataCloudSearching
    hide screen cloudNoFilter
    show screen galeryOpening
    a "Commençons par les photos enregistrées directement sur le téléphone"
    show screen galeryNoFilter
    hide screen galeryOpening
    if whereYouStart[0] == False and whereYouStart[1] == False: #Player launch gallery at first
        a "Il faut vraiment que je fasse le tri !"
    elif whereYouStart[0] == False and whereYouStart[1] == True: #Player launched cloud at first
        a "Il faut vraiment que je fasse le tri !"
    elif whereYouStart[0] == True and whereYouStart[1] == True: #Player launched both applications
        a "J'ai du louper une info, peut être la date..."
    while True:
        empty ""

label openDataCloud:
    nvl clear
    $ whereYouStart[1] = True
    hide screen galeryNoFilter
    show screen dataCloudOpening
    if whereYouStart[0] == True and whereYouStart[1] == False: #Player launch gallery at first
        a "Allons voir sur Datacloud"
    elif whereYouStart[0] == False and whereYouStart[1] == False: #Player launched cloud at first
        a "Allons voir sur Datacloud"
    elif whereYouStart[0] == True and whereYouStart[1] == True: #Player launched both applications
        a "Je devrais au moins pouvoir retrouver le lieu ici"
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
    hide screen dataBookSearch
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
    $ birthdayYear = year-2
    $ dateInput = int(dateInput)
    if dateInput == birthdayYear :
        a "Oui c'était l'année de ses 30 ans"
        a "Mais c'était où ?"
        jump searchInDataBookLocalisation
    else:
        a "Non ce n'est pas ça...je devrais peut être retourné dans ma galerie photos"
        jump searchInDataBookDate

label searchInDataBookLocalisation:
    window auto hide
    $ renpy.pause(1.0, hard=True)
    show screen dataBookSearch
    hide screen dataBookOpening
    $ localisationInput = renpy.input("Entrez la localisation", "Paris", length = 12)
    if localisationInput == "Barcelone" or localisationInput =="barcelone" or localisationInput == "barcelon" or localisationInput == "Barcelon" or localisationInput == "BARCELONE":
            jump foundInDataBook
            hide screen dataBookSearch
    else:
        jump searchInDataBookLocalisation

label foundInDataBook:
    hide screen dataBookSearch
    show screen dataBookFound
    a "Voilà, c'est celle là."
    a "Mais comment ils ont fait ?!"
    a "Ils n'ont pas le droit !"
    e_nvl "Malheureusement si."
    e_nvl "Quand tu publies une photo sur un réseau social, tu acceptes que la plateforme ait certains droits dessus, selon leurs conditions."
    e_nvl "Il est toujours possible de vérifier si une photo a été utilisée en effectuant une {a=information: Une recherche inversée d’image revient à demander à Internet : Où cette photo a-t-elle déjà été vue ? L’outil analyse alors le web pour repérer des pages contenant la même image ou des versions similaires.}recherche inversée.{/a}"
    window auto hide
    $ renpy.pause(1.0, hard=True)
    hide screen dataBookFound
    show screen outOfBattery
    hide screen appsPhone
    a "Ah, la poisse ! Plus de batterie…"
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
    show freezeReceive
    a "Bonjour ! Je viens pour récupérer un colis."
    vendeuse "Bonjour ! C’est à quel nom, s’il vous plaît ?"
    a "Mme Alexia."
    vendeuse "Parfait, je vous le prépare…"
    show receiveStore
    window auto hide
    $ renpy.pause(3.0, hard=True)
    show freezeReceive
    vendeuse "Aujourd’hui, on a une petite offre sympa sur l'impression de photos sur des mugs !"
    a "Oh chouette ! Justement, c’est l’anniversaire de mon frère."
    vendeuse "Il suffit de choisir une photo et de la glisser sur le mug.\n On a des ordis juste là."
    show computerStore
    window auto hide
    $ renpy.pause(3.0, hard=True)
    show zoomComputerStore
    $ renpy.pause(3.0, hard=True)
    show screen storeCustomPage
    a "Top, J’ai sûrement une photo rigolote sur mon téléphone…"
    a "Ah mince, bien sûr… plus de batterie."
    a "Heureusement, je peux me connecter à mon cloud direct depuis l’ordi."
    while True:
        empty ""

label outStore:
    show screen storeCustomPage
    a "Ça va faire son petit effet !"
    window auto hide
    $ hubClickable["photoFrame"]= 0
    menu:
        "Récupérer votre mug":
            call addPoints(-5,'point_sociaux',"","","Toujours se déconnecter, c’est une bonne habitude !µUn ordi laissé connecté, c’est comme laisser sa porte ouverte : niveau sécurité, c’est moyen...", "","hub") from _call_addPoints_1
        "Un petit truc en plus !":
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
            action [SetVariable("WifiState", not WifiState),Call("addPoints",-5,"point_localisation","","","Se connecter à un Wi-Fi public peut sembler pratique, mais c’est un vrai terrain de jeu pour les pirates.","","openDataCloud")]
        imagebutton:
            if DataState == True:
                idle "UI/settingsIcons/DataON.png"
                hover "UI/settingsIcons/DataOFF.png"
            else:
                idle "UI/settingsIcons/DataOFF.png"
                hover "UI/settingsIcons/DataON.png"
            action [SetVariable("DataState", not DataState),Call("addPoints",+5,"point_localisation","",""," ","Tu as bien fait d’éviter le Wi-Fi public, car il présente de nombreux risques de sécurité.","openDataCloud")]
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
            action [Call("addPoints",5,'point_sociaux',"","","","Toujours se déconnecter, c’est une bonne habitude !",'hub')]

screen logViaPopup:
    add "UI/store/logVia.png" xalign 0.5 yalign 0.5
    imagebutton:
        idle At("UI/store/logViaOK.png", outline_transform(0, "#8080804f", 4.0, offset=(3, 3)))
        hover "UI/store/logViaOK.png"
        xalign 0.5
        yalign 0.51
        action [SetVariable("profilPic","True"),Hide("logViaPopup"),Call("addPoints",-2,'point_sociaux',"","","Il vaut mieux éviter la connexion via un {a=information: ou Single Sign-On, est un système qui permet à un utilisateur d'accéder à plusieurs applications ou services avec un seul jeu d'identifiants (nom d'utilisateur et mot de passe). L'utilisateur s'authentifie auprès d'un seul service et peut accéder à d'autres services sans avoir besoin de se reconnecter à chaque fois.}SSO{/a}.µLa simplification de la connexion à une série de services tels que la recherche, les e-mails, la cartographie, les photos et le stockage en ligne µpermet à ces entreprises de regrouper un vaste ensemble de données personnelles collectées à partir des différents services proposés.","",'')]
    imagebutton:
        idle At("UI/store/logViaMail.png", outline_transform(0, "#8080804f", 4.0, offset=(3, 3)))
        hover "UI/store/logViaMail.png"
        xalign 0.5
        yalign 0.6
        action [SetVariable("profilPic","True"),Hide("logViaPopup"),Call("addPoints",2,'point_sociaux',"","","","Bravo, en évitant la connexion via un {a=information: ou Single Sign-On, est un système qui permet à un utilisateur d'accéder à plusieurs applications ou services avec un seul jeu d'identifiants (nom d'utilisateur et mot de passe). L'utilisateur s'authentifie auprès d'un seul service et peut accéder à d'autres services sans avoir besoin de se reconnecter à chaque fois.}SSO{/a},µtu limites la diffusion des données personnelles aux autres services proposés par un SSO.",'')]
