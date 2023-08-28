label barOut:
    nvl clear
    show screen phoneDown
    syrielle_nvl "Salut ! voilà l’adresse pour notre rendez-vous ! \n {u}Bar chez Thon Thon \n 16 rue de la sardine{/u}"
    hide screen hubElements
    show screen dataMap
    empty ""
    while LocalisationState == False:
        empty ""
    hide screen dataMap
    scene bar
    show barPlace
    empty ""
    s "Ça fait tellement longtemps en effet, je suis super contente de te voir de passage dans le coin !! "
    s  "On fait un Selfie et on l’envoi à Pierre, Il sera content de voir ses sœurs réunies ! "
    s "Mais pas de gaffe ! il ne doit pas savoir qu’on prépare son anniversaire ! "
    a "OK je prends mon téléphone."
    show screen selfie
    with dissolve
    while True:
        empty ""

label barOutAfter:
    nvl clear
    call addPoints(5,'point_localisation',LocalisationState, False, "Raté ! \n En laissant ta géolocalisation activée, les données de localisation seront présentent dans les méta données) de ta photo. N’importe qui peut ainsi savoir où tu étais à ce moment-là.", "Bravo  ! \n Tu gagnes des points de géolocalisation, les données de localisation en pensant a la désactiver. De cette façon, ta photo ne contient pas de données de Métadonnées de localisation.")
    hide screen selfie
    $ hubClickable["dog"]= 0
    $ hubClickable["phone"]= 0
    $ hubClickable["phoneCall"]= 1
    $ hubClickable["watch"]= 1
    jump hub
