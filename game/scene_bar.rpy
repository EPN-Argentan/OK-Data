label barOut:
    nvl clear
    #show screen phoneDown
    hide screen phoneDown

    syrielle_nvl "Salut frangine ! \nFaut qu’on s’organise pour la surprise 🎉 \ndu fréro. T’es dispo ?\nOn pourrait se\nretrouver au bar\nChez Thon Thon 🐟,\nrue du Port."
    syrielle_nvl "👍 Yes, t’as raison. On peut s’y retrouver maintenant."
    syrielle_nvl "Un coup\nde téléportation,\net j’y suis ! 😜"
    a "J’me souviens plus trop comment y aller, \non vérifie ça sur Data Maps."
    hide screen hubElements
    show screen dataMap
    #medBubble "Petite idée de Germain :\nÀ ce moment là, on pourrait peut être afficher une fenêtre proposant quatre choix sur l’utilisation de la localisation par DATA Maps :\n- « Autoriser uniquement si l’application est en cours d’utilisation » \n- « Toujours autoriser » \n-« Demander à chaque fois » \n- « Refuser »"

    window auto hide
    show screen phoneDown
    #window auto hide
    window hide
    empty ""
    while LocalisationState == False:
        empty ""
    hide screen dataMap
    scene black
    with dissolve

    #scene bar
    show barSister
    stop music fadeout 1.0
    play music "ambi_bar.mp3"
    transform offset_middle:
        xpos -250
    show clic at offset_middle
    #medBubble "Germain : J'ai ajouté une flèche clic car j'ai remarqué une attente de la part des joueurs."
    empty ""
    hide clic
    a "Wouhouuu ! Ça fait une éternité qu’on ne s’est pas vues,\nil faut l’anniversaire de Pierrot pour qu’on se croise !"
    s "Tu as raison, on va immortaliser ça."
    a "On se fait un petit {a=information: C’est un autoportrait photographique réalisé généralement avec un portable et destiné à être publié sur les réseaux sociaux. Le selfie est également considéré comme un reflet de notre personnalité. En prenant un selfie, on contrôle l’image qu’on souhaite donner de soi-même.}selfie ?{/a}  et je l’enverrai à maman,\nça lui fera plaisir de nous voir ensemble."
    show screen selfie
    with dissolve
    while True:
        empty ""

label barOutAfter:
    nvl clear
    hide screen selfie
    #check if selfie has been shared to be display or not on photo frame
    if LocalisationState :
        $ shareSelfie = True

    call addPoints(5,'point_localisation',LocalisationState, False, "En laissant la géolocalisation activée, l’endroit où tu te\ntrouves sera enregistré dans les {a=information: Les métadonnées sont des informations associées à un fichier, mais elles ne sont pas visibles directement. Pour une photo, cela peut être la date de prise de vue, le lieu, le modèle d’appareil ou les réglages utilisés…} métadonnées{/a} de ta photo.µSi tu partages cette photo, n’importe qui peut alors savoir où tu étais.", "Bravo !µIl est important de réduire au maximum\nles {a=information: Les métadonnées sont des informations associées à un fichier, mais elles ne sont pas visibles directement. Pour une photo, cela peut être la date de prise de vue, le lieu, le modèle d’appareil ou les réglages utilisés…} métadonnées{/a}\nd’une photo, surtout lorsqu’on prévoit\nde la diffuser sur\nles réseaux sociaux.") from _call_addPoints
    hide screen selfie
    $ set_hub_at_Start()

    a "De ton côté les préparatifs sont fait pour l'anniversaire surprise de Pierro ?"
    s "Oui, et pour toi ? Tu as un cadeau ?"
    a "Non, pas encore... j'ai la journée pour trouver un truc..."
    scene black
    with dissolve
    jump hub
