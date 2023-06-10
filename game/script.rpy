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

# Le jeu commence ici
label start:

    $ BluetoothState = True
    $ LocalisationState = True
    $ DataState = True

    scene bar
    show Player at Position (xpos = 1100, ypos = 1000)
    show Mary at Position (xpos = 820, ypos = 1000)
    show screen barre_de_vie

    $ point_interet = 5
    $ point_sante = 5
    $ point_conviction = 5
    $ point_localisation = 5
    $ point_sociaux = 5
    $ point_administrative = 5
    
    m "ça fait vraiment longtemps en effet, je suis contente de pouvoir te voir de passage par ici."
    m "Tu veux pas qu'on fasse un selfie ? Et tu l'envois à notre frêre après ?"
    e_nvl "Bienvenue sur Ok Data"
    n_nvl "Let's go"


    label lPhoneDown :
        call screen phoneDown

    label telplay:
        call screen telephoneplayer

    label selfie:
        if LocalisationState:
            $ point_interet -= 5
        else:
            $ point_interet += 5
        call screen selfie
        with dissolve
    return
