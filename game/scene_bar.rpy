label barOut:
    nvl clear
    #show screen phoneDown
    hide screen phoneDown

    syrielle_nvl "Salut frangine ! \n Ça va arriver vite, faut qu’on s’organise pour la surprise du fréro. T’es dispo ? On pourrait se retrouver au bar Chez Thon Thon, rue du Port."
    syrielle_nvl "Yes, t’as raison. On peut s’y retrouver maintenant."
    syrielle_nvl "Un coup de téléportation et j’arrive !"
    a "J’me souviens plus trop comment y aller, on check ça sur Data Maps."
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
    s "Wouhouuu ! Ça fait une éternité qu’on ne s’est pas vus, il faut l’anniversaire de Pierrot pour qu’on se retrouve !"
    s "Tu as raison, on va immortaliser ça. On se fait un petit {a=information: C’est un autoportrait photographique réalisé généralement avec un portable et destiné à être publié sur les réseaux sociaux. Le selfie est également considéré comme un reflet de notre personnalité. En prenant un selfie, on contrôle l’image qu’on souhaite donner de soi-même.}selfie{/a} ! J’enverrai la photo à maman, ça va lui faire plaisir de nous voir ensemble."
    show screen selfie
    with dissolve
    while True:
        empty ""

label barOutAfter:
    nvl clear

    #check if selfie has been shared to be display or not on photo frame
    if LocalisationState :
        $ shareSelfie = True

    call addPoints(5,'point_localisation',LocalisationState, False, "En laissant ta géolocalisation activée, ta localisation sera présente dans les {a=information: Ce sont les informations “en tout petit” sur les packagings. Pour une photo, elles peuvent inclure la date de prise de vue, le lieu, le type d’appareil utilisé…} métadonnées{/a} de ta photo.µ N’importe qui peut ainsi savoir où tu étais.", "Bravo  ! \n Tu gagnes des points de géolocalisation, en pensant à la désactiver.µDe cette façon, ta photo ne contient pas d'information de localisation.") from _call_addPoints
    hide screen selfie
    $ hubClickable["phone"]= 0
    $ hubClickable["phoneCall"]= 1
    jump hub
