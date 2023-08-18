# NVL characters are used for the phone texting
define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.2)

define m = Character('Mary', color="#c8ffc8")
image Mary :
    "sister"
    zoom 0.55

define P = Character('Player', color="#209792")
image Player :
    "player_sit"
    zoom 0.55


# Initialisation du jeu
label start:

    $ BluetoothState = True
    $ LocalisationState = True
    $ DataState = True

    #points store all point score and y position (to be able to shake this value later)
    $ points = {
        'point_interet': [5,0],
        'point_sante': [5,0],
        'point_conviction': [5,0],
        'point_localisation': [5,0],
        'point_sociaux': [5,0],
        'point_administrative': [5,0]
    }

    #dynamic list of elements clickable in hub
    #if value == 0, the element can't be clicked
    $ hubClickable = {
        'dog': 1,
        'laptop': 0,
        'photoFrame': 0,
        'watch': 0,
        'tablet': 0,
        'homeAssistant': 0
    }

#Lancement du Hub
label hub:
    scene hub
    show Player_Sitting
    show screen barre_de_vie
    show screen hubElements

    m "je crois que quelque chose vient de se passer"

    #Boucle infinie dans le hub
    jump hub

    #call addPoints(-5,'point_conviction','','bravo, tu n\'as rien compris','Bravo tu as bien compris !')

    #label telplay:
    #    call screen telephoneplayer(False,True,False,True,True,True)

    return
