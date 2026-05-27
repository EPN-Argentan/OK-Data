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
        a "Dis, DATASSISTANTE, peux tu me dire quels sont les trucs à faire aujourd’hui ?"
        d "Bonjour Alexia, bien sûr. Je suis là pour t’aider à ne rien oublier."
        d "Aujourd’hui, tu dois t’occuper de l’organisation de l’anniversaire de ton frère Pierre, et il faut aussi lui trouver un cadeau."
        d "Je te rappelle également que ta maman compte sur toi pour envoyer des photos et trouver quelque chose pour ton frère, car elle n’a pas d’idées."
        d "As tu besoin d’autre chose ? Je reste attentive et à l’écoute de la moindre de tes demandes."
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
    e_nvl "Oui, tu as eu le bon réflexe. Les enceintes connectées, comme beaucoup d’objets connectés, collectent énormément d’informations sur notre vie quotidienne."
    e_nvl "Et parfois, ce sont des données très personnelles, voire intrusives."
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
