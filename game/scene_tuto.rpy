label tuto:
    $ posY = 175
    scene hub
    show loungeHubDogInBasket
    show screen barre_de_vie
    show screen skipTuto

    show clic
    play sound "TutoBonjour.mp3"
    medBubble "Bonjour Alexia, bienvenue dans ton salon !"
    play sound "TutoClic.mp3"
    medBubble "Pour progresser, il te suffira de cliquer sur l’écran."
    hide clic
    play sound "TutoCategories.mp3"
    medBubble "Nous avons classé tes {a=information: C'est une information qui permet d’identifier directement ou indirectement une personne.}données personnelles{/a} en six catégories distinctes."
    play sound "TutoInteret.mp3"
    medBubble "Les données de centre d’intérêt"
    play sound "TutoSante.mp3"
    medBubble "Les données de santé"
    play sound "TutoConvictions.mp3"
    medBubble "Les données de convictions"
    play sound "TutoLocalisation.mp3"
    medBubble "Les données de localisation"
    play sound "TutoReseaux.mp3"
    medBubble "Les données de réseaux sociaux"
    play sound "TutoAdmin.mp3"
    medBubble "Les données administratives"
    play sound "TutoPoints.mp3"
    medBubble "Au-dessus de chaque icône est indiqué le nombre de points restants."
    call addPoints(-5,'point_administrative') from _call_addPoints_19
    play sound "TutoPerdre.mp3"
    medBubble "Tu perds des points si tu ne prêtes pas attention à préserver ta vie privée."

    call addPoints(5,'point_administrative') from _call_addPoints_20
    play sound "TutoGagner.mp3"
    medBubble "Au contraire, tu gagneras des points : \n- En faisant les bons choix, \n- En regardant les contenus supplémentaires,\n- En allant te promener !"
    jump hub


screen skipTuto:
    imagebutton :
        idle At("UI/imagebuttons/skipTuto.png", outline_transform(6, "#ffffff", 4.0))
        hover "UI/imagebuttons/skipTuto.png"
        #at bounce
        action [Hide("skipTuto"),Jump("hub")]
        xalign 0.9
        yalign 0.05
        xpadding 20
        ypadding 20


screen clic:
    add "UI/applications/Icons/clic.png"xalign 0.65 yalign 0.4
