label tuto:
    $ posY = 175
    scene hub
    show loungeHubDogInBasket
    show screen barre_de_vie
    show screen skipTuto

    show clic
    play sound "DogGPT/DogGPT_Bienvenue.mp3"
    medBubble "Bienvenue sur OKDATA… et avant tout, retiens qu’il faut cliquer pour avancer."
    hide clic
    play sound "DogGPT/DogGPT_MotEnBleu.mp3"
    medBubble "Et si tu vois un mot en {a=information: Bleu (n. m.) : Couleur souvent évoquée dans les livres, parfois aperçue sur les cartes postales, mais considérée comme espèce protégée en Normandie.}bleu,{/a} tu peux cliquer dessus pour avoir une définition."
    play sound "DogGPT/DogGPT_Topo.mp3"
    medBubble "Moi, c’est DogGPT, le chien qui parle. Mon job, c’est de te faire un petit topo du jeu."
    play sound "DogGPT/DogGPT_MaMaitresse.mp3"
    medBubble "Là, sur le canapé, c’est Alexia, ma maîtresse. Elle est sympa, mais elle ne fait pas super attention à ses données. Du coup, on va essayer de l’aider un peu."
    play sound "DogGPT/DogGPT_Cookies.mp3"
    medBubble "Faut savoir que, sans t’en rendre compte, à chaque connexion tu laisses des petites traces… et les cookies, ils adorent ça."
    play sound "DogGPT/DogGPT_Limiter.mp3"
    medBubble "Ton rôle, va t'être de limiter au maximum ces petites traces, tout en profitant des avantages du numérique."
    play sound "DogGPT/DogGPT_SIX.mp3"
    medBubble "On a classé les {a=information: Les données personnelles, c’est ton double numérique : ton prénom, ton âge, ton adresse, ou encore tes goûts et préférences. Ce sont des infos qui permettent de te définir en profondeur. Elles sont précieuses, comme un journal intime. Il faut les protéger, comme on protège un trésor : avec attention, discernement, et une bonne dose de prudence.}données personnelles{/a} en six catégories."
    play sound "DogGPT/DogGPT_Interet.mp3"
    medBubble "Les données de centre d’intérêt"
    play sound "DogGPT/DogGPT_Sante.mp3"
    medBubble "Les données de santé"
    play sound "DogGPT/DogGPT_Conviction.mp3"
    medBubble "Les données de conviction"
    play sound "DogGPT/DogGPT_Localisation.mp3"
    medBubble "Les données de localisation"
    play sound "DogGPT/DogGPT_Reseaux.mp3"
    medBubble "Les données de réseaux sociaux"
    play sound "DogGPT/DogGPT_Admi.mp3"
    medBubble "Les données administratives"
    play sound "DogGPT/DogGPT_Score.mp3"
    medBubble "Au-dessus de chacune d’elles, tu verras ton score."
    call addPoints(-5,'point_administrative') from _call_addPoints_19
    play sound "DogGPT/DogGPT_Perdre.mp3"
    medBubble "Évidemment, tu perds des points si tu ne protèges pas ta vie privée."

    call addPoints(5,'point_administrative') from _call_addPoints_20
    play sound "DogGPT/DogGPT_Gagner.mp3"
    medBubble "Mais tu y gagnes si tu restes discret, si tu vas piocher dans les ressources… et si tu m’emmènes me promener loin des réseaux."
    window hide
    jump hub


screen skipTuto:
    imagebutton :
        idle At("UI/imagebuttons/skipTuto.png", outline_transform(6, "#ffffff", 4.0))
        hover "UI/imagebuttons/skipTuto.png"
        #at bounce
        action [Function(set_hub_afterWAlkout),Hide("skipTuto"),Jump("hub")]
        xalign 0.9
        yalign 0.05
        xpadding 20
        ypadding 20


screen clic:
    add "UI/applications/Icons/clic.png"xalign 0.65 yalign 0.4
