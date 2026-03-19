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
    hide frame_slideshow_noselfie with moveoutbottom
    hide frame_slideshow_withselfie with moveoutbottom
    show screen galery
    hide screen galeryOpeningLogo
    a "Voilà, il n'y a plus qu'à chercher"
    window auto hide
    $ renpy.pause(2.0, hard=False)
    show screen popUpAI
    while True:
        empty ""

label consent:
    hide screen galery
    show screen consentScreen
    while True:
        empty ""

label IAsearch:
    hide screen consentScreen
    show screen IASearch
    show screen blankPrompt
    a "Comment décrire cette image ?"
    hide screen blankPrompt
    show screen miniGamePrompt
    a "Bon, de quoi je me souviens ?"
    while True:
        empty ""

label endPrompt:
    hide screen IASearch
    hide screen miniGamePrompt
    a "Oui c'est ça !"
    show screen brotherPictureDisplay
    a "Voilà, c'est celle là"
    nvl clear
    e_nvl "Les IAs, c'est pas bien"
    a "MercIA"
    $ hubClickable["photoFrame"]= 0
    hide screen brotherPictureDisplay
    jump hub

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
        xalign 0.685
        yalign 0.2
        imagebutton:
            idle At("UI/Cadre/popUpAI.png", outline_transform(6, "#d44343", 4.0))
            hover "UI/Cadre/popUpAI.png"
            action Jump("consent")

screen consentScreen:
    add "UI/applications/loadingScreen.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5
    vbox :
        xalign 0.690
        yalign 0.45
        spacing 8
        imagebutton:
            idle "UI/Cadre/Consent.png"
        imagebutton:
            idle At('UI/Cadre/FullConsent.png', outline_transform(6, "#ffffff86", 4.0))
            hover "UI/Cadre/FullConsent.png"
            action [Call("addPoints",-5,'point_sociaux',"","","Il est important de toujours de demander si les permissions demandées sont cohérentes avec les fonctionnalités de l'app demandeuse","",'IAsearch')]
        imagebutton:
            idle At('UI/Cadre/PartialConsent.png', outline_transform(6, "#ffffff86", 4.0))
            hover "UI/Cadre/PartialConsent.png"
            action [Call("addPoints",5,'point_sociaux',"","","","Il est important de toujours de demander si les permissions demandées sont cohérentes avec les fonctionnalités de l'app demandeuse",'IAsearch')]
        imagebutton:
            idle At('UI/Cadre/Deny.png', outline_transform(6, "#ffffff86", 4.0))
            hover "UI/Cadre/Deny.png"
            action [Call("addPoints",5,'point_sociaux',"","","","Il est important de toujours de demander si les permissions demandées sont cohérentes avec les fonctionnalités de l'app demandeuse",'IAsearch')]

screen IASearch:
    add "UI/Cadre/IAHomePage.png" xalign 0.6955 yalign 0.5
    text "{color=#000}Bonjour, comment puis-je vous aider ? Vous cherchez une photo ?{/color}" xalign 0.5 yalign 0.4

style textButton_arrowIA:
    size 125


default keywordList1 = ["neige","skis","chien","voiture rouge","sapin"] #Change goodKeyCode1 combinaison to specify wich answers are good
default keywordList2 = ["neige","skis","frere","vache","sourire"] #Change goodKeyCode2 combinaison to specify wich answers are good
default keywordList3 = ["montagne","Pyréenneés"] #Change goodKeyCode3 combinaison to specify wich answers are good
default keyword1Value = 0
default keyword2Value = 0
default keyword3Value = 0
default keyword1 = keywordList1[keyword1Value]
default keyword2 = keywordList2[keyword2Value]
default keyword3 = keywordList3[keyword3Value]
default goodKeyCode1 = [1,3]
default goodKeyCode2 = [0]
default goodKeyCode3 = [0]

style promptStyle_text is text:
    color "#000000"

style promptKey_text is text :
    color "#5996E0"


screen blankPrompt:
    frame:
        background Frame("UI/conversation/phone_received_frame.png", 23,23,23,23)
        xalign 0.5
        yalign 0.55
        padding (50,50)
        text "🔎 {color=#999}Je cherche une image où on voit{/color}" yalign 0.5 style_prefix "promptStyle"

#Game where player has to choose between keyword in prompt
screen miniGamePrompt:
    imagebutton:
        xalign 0.9
        yalign 0.9
        idle At("UI/applications/sendIA.png", outline_transform(6, "#5996E0", 4.0))
        hover "UI/applications/sendIA.png"
        action Call("promptChecker",keyword1Value,keyword2Value,keyword3Value)
    frame:
        background Frame("UI/conversation/phone_received_frame.png", 23,23,23,23)
        xalign 0.5
        yalign 0.55
        padding (50,0)
        hbox:
            text "🔎 Je cherche une image où on voit  " yalign 0.5 style_prefix "promptStyle"
            vbox:
                textbutton "↑":
                    style_prefix "promptStyle"
                    action [SetScreenVariable("keyword1Value", min(len(keywordList1)-1, keyword1Value+1)), Function(renpy.restart_interaction)]
                    xalign 0.5
                text "[keywordList1[keyword1Value]]" style_prefix "promptKey"
                textbutton "↓":
                    style_prefix "promptStyle"
                    action SetScreenVariable("keyword1Value",max(0, keyword1Value - 1))
                    xalign 0.5
            text " avec " yalign 0.5 style_prefix "promptStyle"
            vbox:
                textbutton "↑":
                    style_prefix "promptStyle"
                    action [SetScreenVariable("keyword2Value", min(len(keywordList2)-1, keyword2Value+1)), Function(renpy.restart_interaction)]
                    xalign 0.5
                text "[keywordList2[keyword2Value]]" style_prefix "promptKey"
                textbutton "↓":
                    style_prefix "promptStyle"
                    action SetScreenVariable("keyword2Value",max(0, keyword2Value - 1))
                    xalign 0.5
            text " la scène se passe " yalign 0.5 style_prefix "promptStyle"
            vbox:
                textbutton "↑":
                    style_prefix "promptStyle"
                    action [SetScreenVariable("keyword3Value", min(len(keywordList3)-1, keyword3Value+1)), Function(renpy.restart_interaction)]
                    xalign 0.5
                text "[keywordList3[keyword3Value]]" style_prefix "promptKey"
                textbutton "↓":
                    style_prefix "promptStyle"
                    action SetScreenVariable("keyword3Value",max(0, keyword3Value - 1))
                    xalign 0.5

label promptChecker(key1=0,key2=0,key3=0):
    $ isCorrect = True

    if key1 not in goodKeyCode1:
        $ isCorrect = False

    if key2 not in goodKeyCode2:
        $ isCorrect = False

    if key3 not in goodKeyCode3:
        $ isCorrect = False

    if isCorrect:
        jump endPrompt
        # Tu peux ajouter score, suite du jeu, etc.
    else:
        a "Je ne me souviens pas de ça..."

    return

screen brotherPictureDisplay:
    add "ui/Cadre/brotherDisplayPhone.png" xalign 0.6955 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.7 yalign 0.5