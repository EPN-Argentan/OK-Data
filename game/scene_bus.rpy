label bus:
$ freeWifiActivate = False
hide screen hubElements
show screen birthdayPicture with moveinbottom
a "oh là là, ça date ça..."
e_nvl "Vous avez reçu un colis Winted, pensez à le récupérer à temps"
a "Oh mince, j'avais complétement zappé !"
a "Allez !  je vais le chercher tout de suite sinon il va encore repartir"
$ renpy.scene(layer = "screens")
scene busAdFreeze
show busAdReveal
$ renpy.pause(3.0, hard=True)
a "mais...mais..."
a "C'est la photo de Pierre mon frère!"
a "Mais comment c'est possible, c'est ma photo en plus ! "
a "Elle doit même encore être sur mon téléphone"
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
    a "alors..."
    if freeWifiActivate == False :
        $ freeWifiActivate = True
        show screen freeWifi
        a "il me reste encore un peu de forfait"
        while True:
            empty ""
    else:
        show screen dataCloudOpening
        $ renpy.pause(1.0, hard=True)
        show screen dataCloudSearching
        a "Alors, quelle est la date..."
        jump inputDate
    while True:
        empty ""

label inputDate:
    $ dateInput = renpy.input("Entrez la date recherchée", "1900", length = 4)
    if dateInput == "2014":
        jump searchInDataCloud
    else:        
        jump inputDate

label searchInDataCloud:
    show screen cloudNoFilter
    a "je fais ma recherche" 
    $ renpy.pause(1.0)
    a "bon, toujours rien"

label travelToStore:
    hide busAdFreeze
    hide screen galeryFilter
    show getInsideBus
    $ renpy.pause(3.0, hard=True)
    a "mais comment ils ont obtenu cette photo..."
    $ renpy.pause(3.0, hard=True)
    show exitBus
    $ renpy.pause(3.0, hard=True)
    show getInStore
    $ renpy.pause(3.0, hard=True)
    show homeStore


#All scenes elements used in this label
screen galeryOpening:
    add "UI/applications/galeryOpening.png" xalign 0.5 yalign 0.5
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
                text "2024"  color "#000000"
                grid 2 4:
                    spacing 20  
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                    add "UI/applications/galery/004.jpeg"
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                text "2023"  color "#000000"
                grid 2 4:
                    spacing 20  
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/001.jpeg"
                    add "UI/applications/galery/002.jpeg"
                    add "UI/applications/galery/003.jpeg"
                text "2022"  color "#000000"
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
         area (0.42, 0.3, 330, 500)

         viewport id "vp":
            draggable True
            vbox:
                spacing 20
                text "2014"  color "#000000"
                grid 2 4:
                    spacing 20  
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
    add "UI/applications/cloudOpening.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5


screen dataCloudSearching:
    add "UI/applications/cloudOpening.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

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
            action Call("addPoints",5,"point_sociaux","","Bravo","Faites attention, sur des réseaux publics vous n'êtes pas protégé ! ","openDataCloud")

    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen cloudPhotos:
    add "smartphone.png" xalign 0.5 yalign 0.5
