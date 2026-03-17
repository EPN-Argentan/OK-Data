#Photo frame display in front of player
label photoFrameCheck:
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
    # a "Mais qu’est-ce que cette photo fait là ? Pourvu que personne ne tombe dessus !"
    # e_nvl "Quand tu prends une photo avec ton téléphone, si celui-ci est connecté à ton cloud, la photo peut être automatiquement sauvegardée en ligne."
    # e_nvl "Et là… toute personne ou appareil ayant accès à ce cloud peut aussi y jeter un œil."
    # e_nvl "Pratique pour retrouver tes souvenirs, mais mieux vaut garder un œil sur les paramètres de partage !"

a "Ah oui c'est vrai, j'avais oublié cette histoire !"
a "On avait bien rit...Tiens ça ferait un super cadeau souvenir ça"
a "Elle doit être sur mon cloud !"

#Alexa open his phone to find funny brother's picture
label searchBrotherPicInPhone:
    show screen galeryOpeningLogo
    a "Je dois l'avoir quelquepart..."
    show screen galery
    hide screen galeryOpeningLogo
    a "Voilà, il n'y a plus qu'à chercher"
    window auto hide
    $ renpy.pause(2.0, hard=False)
    show screen popUpAI
    while True:
        empty ""

#####################################################################SCREEN#####################################################################
#All scenes elements used in this label

#Photo Frame Galery
image frame_slideshow_noselfie:
   "/UI/Cadre/frameFunnyPhoto.png"
   pause 2.5
   "/UI/Cadre/slideshowFrame_001.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_002.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_003.png"
   pause 2.5
   repeat

image frame_slideshow_withselfie:
   "/UI/Cadre/frameFunnyPhoto.png"
   pause 2.5
   "/UI/Cadre/slideshowFrame_015.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_002.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_003.png"
   pause 2.5
   repeat

#Browsing in phone gallery
screen galeryOpeningLogo:
    add "UI/applications/loadingScreen.png" xalign 0.6955 yalign 0.5
    add "UI/applications/Icons/appGallery.png" xalign 0.675 yalign 0.5 zoom 1.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5

screen galery:
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

screen popUpAI:
    hbox:
        xalign 0.6955
        yalign 0.2
        imagebutton:
            idle "UI/Cadre/popUpAI.png"
            action Jump("homeScreen")