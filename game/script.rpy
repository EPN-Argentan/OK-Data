# NVL characters are used for the phone texting
define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Médiateur", kind=nvl, callback=Phone_ReceiveSound)
define syrielle_nvl = Character("Syrielle", kind=nvl, callback=Phone_ReceiveSound)
define sepharo_nvl = Character("Sepharo", kind=nvl, callback=Phone_ReceiveSound)
define winted_nvl = Character("Winted", kind=nvl, callback=Phone_ReceiveSound)

define info = Character(None, image="info", kind=bubble)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.2)

define s = Character('Syrielle', color="#ae3f5b")

define a = Character('Alexia', color="#7A1EBB")

define m = Character('Maman', color="#5833ae")

define med = Character('Mediateur', color="#209792")

define vendeuse = Character('Vendeuse', color="#DE843A")

define medBubble = Character(None, image="lucy", kind=bubble)   #Lucy

#Empty character display nothing
define empty = Character(None,color="#00000000", window_background="gui/empty_textbox.png")



# Initialisation du jeu
label start:

#Lancement du Tuto
#jump tuto #To reactivate
#jump browserLabel
#jump dataZon
jump tuto

#Lancement du Hub
label hub:
    if totalPoints() < 30 and visitedForest == False:
        $ hubClickable["forest"]= 1
    hide screen phoneDown
    hide screen mailx3
    scene hub
    show hubDogCouch
    show screen barre_de_vie
    show screen hubElements
    stop music fadeout 1.0
    play music "Spring Field - Godmode.mp3"
    empty ""

    #Boucle infinie dans le hub
    jump hub

    #call addPoints(-5,'point_conviction','','bravo, tu n\'as rien compris','Bravo tu as bien compris !')

    #label telplay:
    #    call screen telephoneplayer(False,True,False,True,True,True)

    return
