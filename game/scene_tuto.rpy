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
    $ points['point_administrative'][0] -= 5
    medBubble "Vous perdrez des points si vous ne prêtez pas attentions aux réglages permettant de préserver votre vie privée."
    $ points['point_administrative'][0] += 5
    medBubble "Au contraire, des points vous seront attribués dans les cas suivants : \nEn suivant les tutoriels d’explication, \nEn faisant les bons choix, \nEn regardant les contenus supplémentaires"

    jump hub
