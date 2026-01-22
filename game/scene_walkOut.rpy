label walkOut :
    scene hub
    hide screen hubElements
    play sound "TutoAdmin.mp3"
    e_nvl "Hey ! Moi c’est ton {a=information: Le médiateur numérique est un super-héros du monde digital ! Il a pour mission d’accompagner les publics vers une autonomie des usages du numérique.}médiateur numérique{/a}, prêt à t’accompagner, te guider et te filer quelques bons tuyaux."
    e_nvl "D'ailleurs, il serait grand temps de sortir promener ton chien."
    e_nvl "On y vaaa !"
    nvl clear
    window hide
    hide screen hubElements
    scene street
    show walkInfinite
    stop music fadeout 1.0
    $ renpy.pause(2.0, hard=True)
    show walkZoom
    $ renpy.pause(1.0, hard=False)
    show walkFix
    show clic
    #show screen phoneDown
    empty ""
    #hide screen phoneDown
    hide clic
    sepharo_nvl "Ça fait longtemps que vous n'êtes pas venu nous voir !"

    sepharo_nvl "En ce moment pour l'achat d'un parfum, vous avez le deuxième à moitié prix !"
    hide screen skipTuto
    call addPoints(5,'point_localisation',LocalisationState, False, "En laissant activée ta {a=information: La géolocalisation, c’est la capacité de repérer ta position sur une carte en temps réel, grâce aux satellites, au Wi-Fi ou aux réseaux mobiles. En gros, ton téléphone sait où tu es… et ça permet de trouver ton chemin, recevoir la météo locale, retrouver ton resto préféré… mais aussi pour OK DATA de savoir ce que tu fais.}géolocalisation{/a}, tu peux être localisé par OK DATA, qui revendra cette information à ses partenaires, comme SEPHARO.", "Bien joué, t’as eu le bon réflexe en désactivant ta localisation !") from _call_addPoints_8
    show screen phoneDown
    medBubble "Dès que ton téléphone est visible, tu peux activer ou désactiver une fonction en touchant l’icône dédiée."
    show screen bubbleTuto("", -500,-500)
    #wait until localisation setting is desactivate
    while LocalisationState == True:
        empty ""
    #give back point if you lost them before
    if points['point_localisation'][0] == -5:
        call addPoints(5,'point_localisation',LocalisationState, False, "En laissant activée la géolocalisation, tu peux être localisé par OK DATA, qui revendra cette information à ses partenaires.", "Tu as bien désactivé la localisation") from _call_addPoints_9
    nvl clear
    scene hub with fade
    hide screen hubElements
    e_nvl "Maintenant, tu es prêt pour la grande aventure des données personnelles."
    e_nvl "À toi de jouer !"

    $ dogInBasket = False
    ##Set hub elements clickable
    $ set_hub_at_Start()

    jump hub
