label barOut:
    nvl clear
    show screen phoneDown
    syrielle_nvl "Salut frangine ! \n On se retrouve au \n {u}Bar chez Thon Thon \n rue du port{/u}"
    hide screen hubElements
    show screen dataMap
    empty ""
    while LocalisationState == False:
        empty ""
    hide screen dataMap
    scene bar
    show barSister
    empty ""
    s "Ça fait longtemps, je suis heureuse de te revoir ! "
    s "Aller, on se fait un {a=information: C’est un autoportrait photographique réalisé généralement avec un portable et destiné à être publié sur les réseaux sociaux. Le selfie est également considéré comme un reflet de notre personnalité. En prenant un selfie, on contrôle l’image qu’on souhaite donner de soi-même.}Selfie{/a} et on l’envoie à Pierrot, il sera content de revoir ses sœurettes ! "
    s "Mais attention ! pas de gaffes sur son anniversaire surprise ! "
    a "OK, je prends mon téléphone."
    show screen selfie
    with dissolve
    while True:
        empty ""

label barOutAfter:
    nvl clear
    
    #check if selfie has been shared to be display or not on photo frame
    $ shareSelfie = False
    if LocalisationState :
        $ shareSelfie = True

    call addPoints(5,'point_localisation',LocalisationState, False, "Raté ! \n En laissant ta géolocalisation activée, ta localisation sera présente dans les métadonnées de ta photo.µ N’importe qui peut ainsi savoir où tu étais.", "Bravo  ! \n Tu gagnes des points de géolocalisation, en pensant à la désactiver.µ De cette façon, ta photo ne contient pas d'information de localisation.") from _call_addPoints
    hide screen selfie
    $ hubClickable["phone"]= 0
    $ hubClickable["phoneCall"]= 1
    jump hub
