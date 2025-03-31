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
    a "Courir, c'est ma bulle, loin de tout."
    window auto hide

    a "Allez, on garde le rythme !"

# Déclaration du personnage pour les dialogues (facultatif)
    define e = Character("Emily")

    e "Waouh, t'as la pêche ! T'as déjà connecté ta montre ?"
    a "Pas encore... Tu pourrais m'aider ?"
    e "Bien sûr ! Commence par ouvrir l'appli DATA SPORT."

label Data_Sport :
    $ renpy.scene(layer="screens")
    show screen Data_Sport
    e "Une fois lancée, connecte-toi."
    while True :
        empty ""

label consentement1 :
    $ renpy.scene(layer="screens")
    show screen consentement1
    a "Il va suivre mon rythme cardiaque. C'est précis comme info santé ?" # déf rythme cardiaque
    while True :
        empty ""

label consentement2 :
    $ renpy.scene(layer="screens")
    show screen consentement2
    a "Les données podométriques ? C'est juste mon nombre de pas ! Ils vont être fiers de moi chez OK Data."
    while True :
        empty ""

label consentement3 :
    $ renpy.scene(layer="screens")
    show screen consentement3
    a "Mon temps d'effort... fini les pauses discrètes à l'abri des regards !"
    while True :
        empty ""

label resultat :
    $ renpy.scene(layer="screens")

#if DS_points ==3:
    #action Jump "resultat_Data_Sport"
#else:
    e_nvl "Quand tu utilises ce genre d'application, garde à l'esprit que tes données de santé sont en jeu."
    call addPoints(DS_points,'point_sante') from _call_addPoints_21
    e_nvl "Si tu partages toutes tes infos, elles peuvent être utilisées sans que tu saches vraiment pourquoi." #e_nvl "Et même si vous donner juste une partie de celles-ci"
    e_nvl "C'est vrai que partager tes données permet de profiter à fond des fonctionnalités de ta  montre connectée."


    scene black
    with fade
    $ hubClickable["watch"]= 0


# Label de démarrage du mini-jeu
label game:
    show runwatch
    e "Garde le rythme et sois précise."
    e "Appuie quatre fois de suite sur le bouton rouge pour rester dans le tempo !"

    # Initialisation des variables du jeu
    $ bar_color = "yellow"  # Couleur initiale de la barre
    $ game_active = True  # Détermine si le mini-jeu est actif
    $ result_message = ""  # Message affiché après le clic
    $ correct_clicks = 0  # Compteur de clics corrects
    $ required_clicks = 4  # Nombre de clics requis pour gagner

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
                    result_message = "Excellent !"
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
     # Affiche le résultat après le mini-jeu
    e "Bien joué, t'es dans rythme !"
    jump resultat_final

    # Affiche le résultat après le clic

label resultat_final:
    $ renpy.scene(layer="screens")
    show screen resultat_Data_Sport  # Affiche l'écran contenant l'image du résultat
    e "Bien joué, t'es dans rythme !"
    e_nvl "Mais fais attention : ne donne pas ton consentement pour tout. Limite les autorisations à ce qui est vraiment utile, et utilise l'appli seulement quand tu en as besoin."
    e_nvl "Pense à fermer les applis après les avoir utilisées, et vérifie le potentiel de fuite des données avec des outils comme Exodus Privacy."
    hide screen resultat_Data_Sport

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
