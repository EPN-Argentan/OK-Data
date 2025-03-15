label browserLabel:
    $ hubClickable["phoneCall"]= 0
    scene hub
    hide screen hubElements
    hide screen phoneDown
    stop music fadeout 1.0
    #show Player_Sitting
    show screen callPhoneIncoming
    while True:
        empty ""

label browserLabelCall:
    show screen callPhoneAnswer
    a "Ouiiiii maman !"
    m "Coucou, ma grande..."
    m "Je suis désolé de te solliciter encore une fois pour un problème d'ordinateur, mais j'ai vraiment besoin de ton aide. C'est pour l'anniversaire de ton frère..."
    jump browserLabelAfterCall
    while True:
        empty ""

label browserLabelAfterCall:
    hide screen callPhoneIncoming
    hide screen callPhoneAnswer
    #scene lounge with fade
    show loungeIdle with fade
    show screen phoneDown
    a "C'est quoi le problème ?"
    m "Eh bien, un ami de ton frère m'a demandé de lui envoyer des photos sur Databook, mais je ne sais pas comment faire !"
    a "La première chose, c'est de te créer un compte Databook."
    m "Ah bon, j'ai bien peur de ne pas savoir faire ça. Ça ne te dérangerait pas de le faire à ma place ? Je te laisse mes papiers d'identité si besoin."
    hide screen phoneDown
    show loungeZoom
    $ renpy.pause(2.5, hard=True) #Wait zoom animation has been finished before to show laptop screen on
    show screen browserWindowSubscribe
    show loungeHandIn onlayer overlay
    $ renpy.pause(1.5, hard=True) #Wait for hand in animation stop
    hide loungeIdle
    while True:
        show handInFixed onlayer overlay
        empty ""

label browserLabelFeed:
    #call addPoints(5,'point_sociaux',GoodState,True,"Tu perds des points ! µEvitez de donner trop d’informations. Les champs obligatoires *(indiquées par un astérisque) sont suffisants. µTrop de précision sur ton identité peut entraîner la divulgation de données un peu trop personnellesµDes grandes Société comme ici DATABOOK récoltent ces données et les revendent ensuite µ cela à des fins de marketing ou à d’autres sociétés parfois peu scrupuleuses. ", "Bravo ! µ\n Il est parfois bon de ne pas trop en dire.µLes champs obligatoires *(indiquées par un astérisque) sont suffisants. µTrop de précision sur votre identité peut entraîner la divulgation de données un peu trop personnellesµ Des grandes Société comme ici DATABOOK récoltent ces données et les revendent ensuite \n soit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses.") from _call_addPoints_1
    show loungeZoomFix
    show screen browserWindowFeed
    hide screen browserWindowSubscribe
    hide screen browserWindowSubscribeFake
    hide screen browserWindowSubscribeTrue
    show screen barre_de_vie
    a "C’est bon maman, ton compte est activé. On va pouvoir consulter l’événement créé pour l’anniversaire de Pierre."
    while True:
        empty ""

label insideEventPage:
    hide screen browserWindowFeed
    show screen insideEvent
    show screen barre_de_vie
    a "Regarde, tu descends un peu dans l’événement et tu trouveras un bouton pour partager des photos."
    while True:
        empty ""

#Screens used in scene_browser

screen insideEvent:
    add "UI/browser/frameDataBook.png" xpos 42 ypos 97
    side "c b r":
        area (358, 160, 775, 800)
        viewport id "vp":
            draggable True
            vbox:
                spacing 20
                imagebutton:
                    idle "UI/browser/EventPage.png"
                hbox:
                    ypos -195
                    xalign 1.0
                    spacing 5
                    imagebutton:
                        idle At("UI/browser/sendPhotosDatabook.png", outline_transform(0, "#8080805f", 4.0, offset=(5, 5)))
                        hover "UI/browser/sendPhotosDatabook.png"
                        action Call("addPoints",-2,'point_administrative',"","","Il est préférable de partager ses photos par e-mail. µEn publiant tes photos, tu accordes souvent au réseau social une licence d'utilisation {a=information: Les Conditions Générales d'Utilisation (CGU) sont les règles d'utilisation auxquelles tu as donné ton accord lors de la création de ton compte. Elles t'informent de ce que tu peux ou pas faire et de ce que le réseau social peut faire avec tes données, comme par exemple avec le contenu de tes publications.}(CGU){/a} µqui leur donne le libre choix de les afficher, de les partager, et parfois même de les utiliser à des fins commerciales.","",'hub')
                    imagebutton:
                        idle At("UI/browser/sendPhotosMail.png", outline_transform(0, "#8080805f", 4.0, offset=(5, 5)))
                        hover "UI/browser/sendPhotosMail.png"
                        action Call("addPoints",2,'point_administrative',"","","","Tu as bien fait ! µCar en publiant tes photos, tu accordes souvent au réseau social une licence d’utilisation {a=information: Les Conditions Générales d'Utilisation (CGU) sont les règles d'utilisation auxquelles tu as donné ton accord lors de la création de ton compte. Elles t'informent de ce que tu peux ou pas faire et de ce que le réseau social peut faire avec tes données, comme par exemple avec le contenu de tes publications.}(CGU){/a} µqui leur donne le libre choix de les afficher, de les partager, et parfois même de les utiliser à des fins commerciales.",'hub')
        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")
