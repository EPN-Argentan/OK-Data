label barOut:
    nvl clear
    #show screen phoneDown
    hide screen phoneDown

    syrielle_nvl "Salut frangine ! \n On se retrouve au \n {u}Bar chez Thon Thon \n rue du port.{/u}"
    hide screen hubElements
    show screen dataMap
    window auto hide
    show screen phoneDown
    #window auto hide
    window hide
    empty ""
    while LocalisationState == False:
        empty ""
    hide screen dataMap
    scene bar
    show barSister
    stop music fadeout 1.0
    play music "ambi_bar.mp3"
    empty ""
    s "Ça fait longtemps, je suis heureuse de te revoir ! Ce texte devrait être super long pour que je teste la longueur de la bulle mon gars, yeah. Encore plus de texte pour avoir beaucoup, beaucoup de longueur "
    s "Allez, on se fait un {a=information: C’est un autoportrait photographique réalisé généralement avec un portable et destiné à être publié sur les réseaux sociaux. Le selfie est également considéré comme un reflet de notre personnalité. En prenant un selfie, on contrôle l’image qu’on souhaite donner de soi-même.}Selfie{/a} et on l’envoie à Pierrot, ça l’amusera de revoir ses sœurettes ! "
    s "Mais attention ! Pas de gaffes sur son anniversaire surprise ! "
    a "OK, je prends mon téléphone."
    show screen selfie
    with dissolve
    while True:
        empty ""

label barOutAfter:
    nvl clear

    #check if selfie has been shared to be display or not on photo frame
    if LocalisationState :
        $ shareSelfie = True

    call addPoints(5,'point_localisation',LocalisationState, False, "En laissant ta géolocalisation activée, ta localisation sera présente dans les {a=information: C'est comme les petites étiquettes sur les boîtes de conserve. Pour une photo, elles peuvent inclure la date de prise de vue, le lieu, et le type d’appareil utilisé.} métadonnées{/a} de ta photo.µ N’importe qui peut ainsi savoir où tu étais.", "Bravo  ! \n Tu gagnes des points de géolocalisation, en pensant à la désactiver.µDe cette façon, ta photo ne contient pas d'information de localisation.") from _call_addPoints
    hide screen selfie
    $ hubClickable["phone"]= 0
    $ hubClickable["phoneCall"]= 1
    jump hub
