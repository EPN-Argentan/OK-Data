#image backgroundSpeaker = "images/UI/homeAssistant/homeAssistant.jpeg"
default switchOnHomeAssistant = False

label homeAssistant:
    nvl clear
    hide screen hubElements
    hide screen phoneDown
    stop music fadeout 1.0
    show home_assistant
    show screen barre_de_vie


    define d = Character("DATASSISTANTE")
    #First time you click on home assistant
    if switchOnHomeAssistant == False :
        $ switchOnHomeAssistant = True
        $ printit()
        a "Dis DATASSISANTE, peux-tu me rappeler les événements de la journée ?"
        d "Bonjour Alexia, oui, pas de problème, je suis là pour toi."
        d "Aujourd'hui, vous avez l'anniversaire de votre frère, vous aviez noté qu'il fallait lui touver un cadeau"
        d "Vous avez aussi demandé que je vous rappel que votre maman compte sur vous pour trouver le cadeau qu'elle doit lui offrir"
        d "Puis-continuer à vous aider ?"
        jump hub
    else :
    #Second time you click on home assistant
        $ switchOnHomeAssistant = False
        show screen homeAssistantButton # Display interface home assistant button
        #show zoomEnceinte
        while True:
            empty ""
nvl clear

screen homeAssistantButton:
    add "images/sprites/home_assistant/lastFrameImage_zoom_enceinte.png"
    imagebutton:
        xalign 0.63
        yalign 0.46
        idle At("images/UI/homeAssistant/homeAssistantBtn.png", outline_transform(6, "#ffffff", 4.0))
        hover "images/UI/homeAssistant/homeAssistantBtn.png"
        action [SetVariable("speakerState", "False"),Jump("endHomeAssitant")]

label endHomeAssitant:
    hide screen homeAssistantButton
    $ hubClickable["homeAssistant"]= 0
    e_nvl "Les enceintes connectées, comme la plupart des objets connectés, sont sources de récolte de données les plus intimes et intrusives"
    jump hub

init python:
    import threading


    current_category = 0

    def printit():
        global current_category  # Utiliser la variable globale
        if speakerState==True:
            # Décrémenter le premier élément de la liste de la catégorie actuelle
            points[list(points.keys())[current_category]][0] -= 1
            # Incrémenter l'index de la catégorie actuelle
            current_category = (current_category + 1) % len(points)
            print("Homme assistant activé")
            renpy.restart_interaction() #Refresh screen to show variable modification
            renpy.redraw("barre_de_vie",0)
            threading.Timer(10.0, printit).start()
            renpy.play("audio/pop.mp3")
        else:
            print("Home assistant désactivé")
