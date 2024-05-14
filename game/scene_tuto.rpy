label tuto:
    $ posY = 175
    scene hub
    show hubDogCouch
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
    medBubble "Au contraire, des points vous seront attribués dans les cas suivants : \nEn faisant les bons choix, \nEn regardant les contenus supplémentaires,\nEn allant vous promener!" 
    jump hub
