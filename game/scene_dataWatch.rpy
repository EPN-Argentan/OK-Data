# Déclaration des variables initiales
label dataWatch:
    nvl clear
    $ default_clicks = 0
    default DS_points = 0
    hide screen hubElements
    hide screen phoneDown
    stop music fadeout 1.0
    show runwatch
    show screen barre_de_vie
    a "ouh ouh ouh"
    window auto hide

    a "allons-y !"

# Déclaration du personnage pour les dialogues (facultatif)
define e = Character("Emily")

# Label de démarrage du mini-jeu
label game:
    show runwatch
    e "Alexia, pour courir de façon régulière il faut être précis."
    e "Clique 8 fois d'affilée sur le rouge pour réussir !"

    # Initialisation des variables du jeu
    $ bar_color = "yellow"  # Couleur initiale de la barre
    $ game_active = True  # Détermine si le mini-jeu est actif
    $ result_message = ""  # Message affiché après le clic
    $ correct_clicks = 0  # Compteur de clics corrects
    $ required_clicks = 8  # Nombre de clics requis pour gagner

    # Interface utilisateur pour afficher la barre colorée
    screen color_bar_game():
        if game_active:
            frame:
                align (0.34, 0.5)
                xsize 600
                ysize 100
                background (
                    "images/yellow_bar.png" if bar_color == "yellow" else
                    "images/orange_bar.png" if bar_color == "orange" else
                    "images/red_bar.png"  # Utilise l'image correspondant à la couleur
                )
                text "Clique ici !" align (0.9, 0.5) size 30

                # Détecte le clic sur la barre
                button:
                    action Function(check_click)  # Vérifie la couleur au clic
                    background None
                    xsize 600
                    ysize 100

            # Ajout d'un timer pour changer la couleur toutes les secondes
            timer 0.5 action Function(update_bar_color) repeat True

            # Affiche le nombre de clics corrects
            text "Clics corrects : [correct_clicks]/[required_clicks]" align (0.5, 0.6) size 25
        else:
            frame:
                align (0.5, 0.5)
                xsize 600
                ysize 100
                text result_message align (0.5, 0.5) size 30

    # Fonction pour gérer les clics
    python:
        def check_click():
            global bar_color, game_active, result_message, correct_clicks, required_clicks
            if bar_color == "red":
                correct_clicks += 1
                if correct_clicks >= required_clicks:
                    result_message = "Super !"
                    game_active = False
            else:
                correct_clicks = 0  # Réinitialise le compteur si clic incorrect
                result_message = "Clic incorrect ! Recommence !"

    # Fonction pour changer la couleur de la barre
    python:
        def update_bar_color():
            global bar_color
            if bar_color == "yellow":
                bar_color = "orange"  # Change l'état vers "orange"
            elif bar_color == "orange":
                bar_color = "red"  # Change l'état vers "rouge"
            elif bar_color == "red":
                bar_color = "yellow"  # Change l'état vers "jaune"

    # Affiche l'écran du mini-jeu
    show screen color_bar_game

    # Attends que le mini-jeu se termine
    while game_active:
        $ renpy.pause(0.1)

    # Affiche le résultat après le clic
    e "[result_message]"



    e "waouhh tu gères, tu veux voir ton score ?"
    a "C'est possible ça ?"
    e "Mais oui regarde dans l'application qui gère ta montre connecté"
    a "Je pense jamais à la regarder... ok"

label Data_Sport :
    $ renpy.scene(layer="screens")
    show screen Data_Sport
    a "Ah oui Data Sport... je me connecte"
    while True :
        empty ""

label consentement1 :
    $ renpy.scene(layer="screens")
    show screen consentement1
    "mon rythme cardiaque ?"
    while True :
        empty ""

label consentement2 :
    $ renpy.scene(layer="screens")
    show screen consentement2
    "mes données podométrique ? C'est le nombre de pas en fait ! Ils ont du vocabulaire chez OK Data."
    while True :
        empty ""

label consentement3 :
    $ renpy.scene(layer="screens")
    show screen consentement3
    "Et mon temps d'effort maintenant..."
    while True :
        empty ""

label resultat :
    $ renpy.scene(layer="screens")

#if DS_points ==3:
    #action Jump "resultat_Data_Sport"
#else:
    e_nvl "Lorsque l'on utilise ce type d'application il faut avoir conscience que vos données de santé son en jeux"
    call addPoints(DS_points,'point_sante')
    e_nvl "Si vous scéder toutes les informations, celles-ci peuvent être utiliser sans que vous sachiez à quelle fin"
    e_nvl "Et même si vous donner juste une partie de celles-ci"
    e_nvl "Donner vos informations permet il est vrai d'utiliser pleinement les fonctions de l'application et des montres connectées"
    e_nvl "C'est à vous de décidez ce que vous voulez dire ou ne pas dire."
    
    scene black
    with fade
    $ hubClickable["watch"]= 0
    jump hub

#label resultat_Data_Sport :
#    show screen resultat_Data_Sport


screen Data_Sport:
    add "sprites/run&watch/Data_Sport.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.500
        yalign 0.245
        idle "sprites/run&watch/data_sport_connect_hidle.jpg"
        hover "sprites/run&watch/data_sport_connect_hover.jpg"
        action Jump ("consentement1")

screen consentement1 :
    add "sprites/run&watch/consentement1.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.450
        yalign 0.600
        idle "sprites/run&watch/yesbutton_hidle.png"
        hover "sprites/run&watch/yesbutton_hover.png"
        action [SetVariable("DS_points", DS_points -1), Jump ("consentement2")]
    imagebutton :
        xalign 0.550
        yalign 0.600
        idle "sprites/run&watch/nobutton_hidle.png"
        hover "sprites/run&watch/nobutton_hover.png"
        action [SetVariable("DS_points", DS_points +1), Jump ("consentement2")]


screen consentement2 :
    add "sprites/run&watch/consentement2.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.450
        yalign 0.600
        idle "sprites/run&watch/yesbutton_hidle.png"
        hover "sprites/run&watch/yesbutton_hover.png"
        action [SetVariable("DS_points", DS_points -1), Jump ("consentement3")]
    imagebutton :
        xalign 0.550
        yalign 0.600
        idle "sprites/run&watch/nobutton_hidle.png"
        hover "sprites/run&watch/nobutton_hover.png"
        action [SetVariable("DS_points", DS_points +1), Jump ("consentement3")]

screen consentement3 :
    add "sprites/run&watch/consentement3.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.450
        yalign 0.600
        idle "sprites/run&watch/yesbutton_hidle.png"
        hover "sprites/run&watch/yesbutton_hover.png"
        action [SetVariable("DS_points", DS_points -1), Jump ("resultat")]
    imagebutton :
        xalign 0.550
        yalign 0.600
        idle "sprites/run&watch/nobutton_hidle.png"
        hover "sprites/run&watch/nobutton_hover.png"
        action [SetVariable("DS_points", DS_points +1), Jump ("resultat")]

screen resultat_Data_Sport :
    add "sprites/run&watch/resultat.png" xalign 0.5 yalign 0.5



    #choisir ce qui est partagé - rythme cardiaque / nombre de pas / durée de l'épreuve
