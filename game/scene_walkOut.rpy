label walkOut :
    scene hub
    hide screen hubElements
    e_nvl "Bonjour, je suis le {a=information: Le médiateur numérique est un super-héros du monde digital ! Il a pour mission d’accompagner les publics vers une autonomie des usages du numérique.}médiateur numérique{/a}, et je vais vous guider et vous conseiller tout au long du jeu."
    e_nvl "D'ailleurs, il serait bon d'aller promener votre chien."
    e_nvl "C'est parti !"
    nvl clear
    hide screen hubElements
    scene street
    show Player_Walking
    show screen phoneDown
    empty ""
    hide screen phoneDown
    sepharo_nvl "Ça fait longtemps que vous n'êtes pas venu nous voir !"
    sepharo_nvl "En ce moment pour l'achat d'un parfum, vous avez le deuxième à moitié prix !"
    call addPoints(5,'point_localisation',LocalisationState, False, "En laissant activée la géolocalisation sur ton portable, tu peux être localisé par OK DATA, qui revendra les données à ses partenaires.", "Tu as bien désactivé la localisation") from _call_addPoints_8
    e_nvl "Tu as la possibilité d’activer ou non cette fonction en touchant l’icône en haut du téléphone. Penses-y à l’avenir et essaye dès maintenant."
    show screen phoneDown
    medBubble "Dés que le téléphone est visible, tu peux à tout moment désactiver un des paramètres"
    show screen bubbleTuto("", -500,-500)
    while LocalisationState == True:
        empty ""
 
    ##Set hub elements clickable
    $ hubClickable["dog"]= 0
    $ hubClickable["phone"]= 1
    $ hubClickable["tablet"]= 0
    $ hubClickable["laptop"]= 1
    $ hubClickable["walkout"]= 1
    $ hubClickable["forest"]= 1
    $ hubClickable["photoFrame"]= 1
    
    jump hub
