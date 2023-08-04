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

image Player_Walking :
    "0001"
    pause 0.1
    "0003"
    pause 0.1
    "0005"
    pause 0.1
    "0007"
    pause 0.1
    "0009"
    pause 0.1
    "0011"
    pause 0.1
    "0013"
    pause 0.1
    "0015"
    pause 0.1
    "0017"
    pause 0.1
    "0019"
    pause 0.1
    "0021"
    pause 0.1
    "0023"
    pause 0.1
    "0025"
    pause 0.1
    "0027"
    pause 0.1
    "0029"
    pause 0.1
    repeat



# Le jeu commence ici
label start:

    $ BluetoothState = True
    $ LocalisationState = True
    $ DataState = True

    scene bar
    show Player at Position (xpos = 1100, ypos = 1000)
    show Mary at Position (xpos = 820, ypos = 1000)
    show screen barre_de_vie

    #points store all point score and y position (to be able to shake this value later)
    $ points = {
        'point_interet': [5,0],
        'point_sante': [5,0],
        'point_conviction': [5,0],
        'point_localisation': [5,0],
        'point_sociaux': [5,0],
        'point_administrative': [5,0]
    }


    m "ça fait vraiment longtemps en effet, je suis contente de pouvoir te voir de passage par ici."
    show Player_Walking
    m "Tu veux pas qu'on fasse un selfie ? Et tu l'envois à notre frêre après ?"

    call addPoints(-5,'point_conviction','','bravo, tu n\'as rien compris','Bravo tu as bien compris !')

    m "je crois que quelque chose vient de se passer"
    e_nvl "Bienvenue sur Ok Data"
    n_nvl "Let's go"


    label lPhoneDown :
        call screen phoneDown

    label telplay:
        call screen telephoneplayer(False,True,False,True,True,True)

    label selfie:
        call screen selfie
        with dissolve

    return
