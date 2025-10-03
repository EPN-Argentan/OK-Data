label tuto:
    $ posY = 175
    scene hub
    show loungeHubDogInBasket
    show screen barre_de_vie
    show screen skipTuto

    show clic
    play sound "PetitMomentEnsemble.mp3"
    medBubble "Salut Alexia, prête pour un petit moment ensemble ? car on va t'aider à protéger tes données !"
    play sound "SimpleClic.mp3"
    medBubble "un simple clic te fait progresser dans le jeu."
    hide clic
    play sound "TutoBleu&Categories.mp3"
    medBubble "Nous avons classé tes {a=information: C'est une information qui permet d’identifier directement ou indirectement une personne.}données personnelles{/a} en six catégories."
    play sound "TutoInteret.mp3"
    medBubble "Les données de centre d’intérêt"
    play sound "TutoSante.mp3"
    medBubble "Les données de santé"
    play sound "TutoConviction.mp3"
    medBubble "Les données de conviction"
    play sound "TutoLocalisation.mp3"
    medBubble "Les données de localisation"
    play sound "TutoReseaux.mp3"
    medBubble "Les données de réseaux sociaux"
    play sound "TutoAdmin.mp3"
    medBubble "Les données administratives"
    play sound "TutoPoints.mp3"
    medBubble "Au-dessus de chaque catégorie est indiqué ton nombre de points."
    call addPoints(-5,'point_administrative') from _call_addPoints_19
    play sound "TutoPerdre.mp3"
    medBubble "Tu perds des points si tu ne protèges pas ta vie privée."

    call addPoints(5,'point_administrative') from _call_addPoints_20
    play sound "TutoGagner.mp3"
    medBubble "Et tu gagneras des points en te divulguant le moins possible, en consultant les ressources ou tout simplement en allant te promener loin des réseaux."
    window hide
    jump hub


screen skipTuto:
    imagebutton :
        idle At("UI/imagebuttons/skipTuto.png", outline_transform(6, "#ffffff", 4.0))
        hover "UI/imagebuttons/skipTuto.png"
        #at bounce
        action [Function(set_hub_at_Start),Hide("skipTuto"),Jump("hub")]
        xalign 0.9
        yalign 0.05
        xpadding 20
        ypadding 20


screen clic:
    add "UI/applications/Icons/clic.png"xalign 0.65 yalign 0.4
