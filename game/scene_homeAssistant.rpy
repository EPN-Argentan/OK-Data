image backgroundSpeaker = "images/UI/homeAssistant/homeAssistant.jpeg"

label homeAssistant:
    hide screen hubElements
    show screen barre_de_vie
    scene backgroundSpeaker
    show screen homeAssistantButton
    a "voilà mon enceinte"
    while True:
        empty ""
    nvl clear

screen homeAssistantButton:     
    imagebutton:
        xalign 0.46
        yalign 0.7
        idle At("images/UI/homeAssistant/homeAssistantBtn.png", outline_transform(6, "#ffffff", 4.0))
        hover "images/UI/homeAssistant/homeAssistantBtn.png"
        action SetLocalVariable("speakerState", "False")



init python:
    speakerState = True #does speaker is active
    current_category = 0 
    
    import threading

    def printit():
        global current_category  # Utiliser la variable globale
        if speakerState:
            threading.Timer(5.0, printit).start()
            # Décrémenter le premier élément de la liste de la catégorie actuelle
            points[list(points.keys())[current_category]][0] -= 1
            # Incrémenter l'index de la catégorie actuelle
            current_category = (current_category + 1) % len(points)
            print("Homme assistant activé")
            printit()
        else:
            print("Home assistant désactivé")
    