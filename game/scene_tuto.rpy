label tuto:
    $ posY = 175
    scene hub
    show loungeHubDogInBasket
    show screen barre_de_vie
    show screen skipTuto

    play sound "PetitMomentEnsemble.mp3"
    show clic
    play sound "Coucou.mp3"
    medBubble "Coucou ! Pour commencer, pense à cliquer pour progresser dans le jeu."
    hide clic
    play sound "Bleu.mp3"
    medBubble "Et si tu vois un mot en {a=information: Bleu (n. m.) : Couleur souvent évoquée dans les livres, parfois aperçue sur les cartes postales, mais considérée comme espèce protégée en Normandie.}bleu,{/a} tu peux cliquer dessus pour obtenir une définition."
    play sound "Topo.mp3"
    medBubble "Moi, c’est DogGPT, le chien qui parle. Mon job, c’est de te faire un petit topo du jeu."
    play sound "Alexia.mp3"
    medBubble "Là, sur le canapé, c’est Alexia, ma maîtresse. Elle est sympa, mais elle ne fait pas super attention à ses données. Du coup, on va essayer de l’aider un peu."
    play sound "Cookies.mp3"
    medBubble "Faut savoir que, sans t’en rendre compte, à chaque connexion tu laisses des petites traces… et les cookies adorent ça."
    play sound "Miettes.mp3"
    medBubble "Ton rôle, ça va être de limiter au maximum ces petites miettes, tout en profitant à fond des avantages du numérique."
    play sound "Donnees.mp3"
    medBubble "On a classé les {a=information: Les données personnelles, c’est ton double numérique : ton prénom, ton âge, ton adresse, ou encore tes goûts et préférences. Ce sont des infos qui permettent de te définir en profondeur. Elles sont précieuses, comme un journal intime. Il faut les protéger, comme on protège un trésor : avec attention, discernement, et une bonne dose de prudence.}données personnelles{/a} en six catégories."
    medBubble "Les données de centre d’intérêt"
    medBubble "Les données de santé"
    medBubble "Les données de conviction"
    medBubble "Les données de localisation"
    medBubble "Les données de réseaux sociaux"
    medBubble "Les données administratives"
    play sound "Score.mp3"
    medBubble "Au-dessus de chacune d’elles, tu verras ton score."
    call addPoints(-5,'point_administrative') from _call_addPoints_19
    play sound "Perdre.mp3"
    medBubble "Évidemment, tu perds des points si tu ne protèges pas ta vie privée."

    call addPoints(5,'point_administrative') from _call_addPoints_20
    play sound "Gagner.mp3"
    medBubble "Et tu en gagnes si tu restes discret, si tu vas piocher dans les ressources… ou même si tu vas te promener loin des réseaux."
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
