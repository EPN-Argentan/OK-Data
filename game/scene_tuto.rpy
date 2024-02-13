label tuto:
    $ posY = 175
    scene hub
    show Player_Sitting
    show screen barre_de_vie
    medBubble "Vos points de données personnelles se trouvent ici"
    medBubble "Ils sont répartis en 6 catégories"
    medBubble "Les données de centre d’intérêt"
    medBubble "Les données de santé"
    medBubble "Les données de convictions"
    medBubble "Les données de localisation"
    medBubble "Les données de réseaux sociaux"
    medBubble "Les données administratives"
    medBubble "Pour chacune de ces catégories, un chiffre vous indiquera le nombre de points restants"
    call addPoints(-5,'point_administrative')
    medBubble "Vous perdrez des points si vous ne prêtez pas attentions aux réglages permettant de préserver votre vie privée."
    call addPoints(5,'point_administrative')
    medBubble "Au contraire, des points vous seront attribués dans les cas suivants : \nEn suivant les tutoriels d’explication, \nEn faisant les bons choix, \nEn regardant les contenus supplémentaires"

    #Old way to display tutorial bubble (before RP 8.1)
    #show screen bubbleTuto("Vos points de données personnelles se trouvent ici",100,posY+50)
    #empty ""
    #show screen bubbleTuto("Ils sont répartis en 6 catégories",100,posY+50)
    #empty ""
    #show screen bubbleTuto("Les données de centre d’intérêt",145,posY)
    #empty ""
    #show screen bubbleTuto("Les données de santé",300,posY)
    #empty ""
    #show screen bubbleTuto("Les données de convictions",455,posY)
    #empty ""
    #show screen bubbleTuto("Les données de localisation",610,posY)
    #empty ""
    #show screen bubbleTuto("Les données de réseaux sociaux",765,posY)
    #empty ""
    #show screen bubbleTuto("Les données administratives",920,posY)
    #empty ""
    #show screen bubbleTuto("Pour chacune de ces catégories, un chiffre vous indiquera le nombre de points restants",100,posY+50)
    #empty ""
    #show screen bubbleTuto("Vous perdrez des points si vous ne prêtez pas attentions aux réglages permettant de préserver votre vie privée.",100,posY+50)
    #empty ""
    #show screen bubbleTuto("Au contraire, des points vous seront attribués dans les cas suivants : \nEn suivant les tutoriels d’explication, \nEn faisant les bons choix, \nEn regardant les contenus supplémentaires",100,posY+50)
    #empty ""
    #show screen bubbleTuto("", -500,-500)
    jump hub
