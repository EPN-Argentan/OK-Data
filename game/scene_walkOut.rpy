label walkOut :
    scene hub
    hide screen hubElements
    e_nvl "Votre chien veut sortir"
    e_nvl "C'est parti pour la promenade"
    nvl clear
    hide screen hubElements
    scene street
    show Player_Walking
    show screen phoneDown
    a "Je marche seule !"
    hide screen phoneDown
    sepharo_nvl "Vous passez devant Sepharo !"
    sepharo_nvl "Venez profiter de notre offre du moment : Un parfum acheté le deuxième offert !"
    call addPoints(5,'point_localisation',LocalisationState, False, "Tu as perdu 5 points de vie Privée !", "Tu as bien désactiver la localisation")
    e_nvl "En laissant activée la géolocalisation sur ton téléphone, tu peux être visible par les réseaux, d’où la réception de message de publicité."
    e_nvl "Tu as la possibilité d’activer ou non cette fonction en touchant l’icône en haut du téléphone. Penses-y à l’avenir et essaye dès maintenant."
    show screen phoneDown
    show screen bubbleTuto("Dés que le téléphone est visible, tu peux à tout moment désactiver un des paramètres",300,700)
    empty ""
    show screen bubbleTuto("", -500,-500)
    while LocalisationState == True:
        empty ""
    $ hubClickable["dog"]= 0
    $ hubClickable["phone"]= 1
    jump hub
