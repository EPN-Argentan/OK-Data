label browserLabel:
    scene hub
    hide screen hubElements
    hide screen phoneDown
    show Player_Sitting
    show screen callPhoneIncoming
    while True:
        empty ""

label browserLabelCall:
    s "Alors Maman, qu’est-ce que tu veux que je te montre ? "
    m "Eh bien c’est pour envoyer une photo sur Databook, je ne sais pas comment ça marche … "
    m "Monique m'as invité à l'anniversaire de Franck mais il me faut un compte Databook"
    while True:
        empty ""

label browserLabelAfterCall:
    hide screen callPhoneIncoming
    hide screen callPhoneAnswer
    scene lounge
    show loungeIdle
    show screen phoneDown
    s "Alors Maman, qu’est-ce que tu veux que je te montre ?"
    m "Eh bien c’est pour envoyer une photo sur Databook, je ne sais pas comment ça marche … "
    s "Mais tu n’as pas de compte Databook !? il va falloir t’en créer un."
    m "Oh je préfère que tu le créé toi, tu es super à la pointe dans ces choses-là !Tiens voila mes papiers d’identité si tu en as besoin."
    hide screen phoneDown
    show loungeZoom
    empty ""
    show screen browserWindowSubscribe
    show loungeHandIn onlayer overlay
    hide loungeIdle
    while True:
        empty ""

label browserLabelFeed:
    call addPoints(5,'point_sociaux',GoodState,True,"Vous perdez des points ! µ Evitez de donner trop d’informations ou de vraies informations. Les champs obligatoires (indiquées par un astérisque) sont suffisants. µ Cela contribue à divulguer vos données personnelles d’identité. Des grandes Société comme ici DATABOOK récoltent ces données et les revendent ensuite, soit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses. ", "Bravo ! µ Il est parfois bon de ne pas trop en dire.µLes champs obligatoires (indiquées par un astérisque) sont suffisants. Trop de précision sur votre identité contribue à divulguer vos données personnelles d’identité. µ Des grandes Société comme ici DATABOOK récoltent ces données et les revendent ensuite, soit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses.") from _call_addPoints_1
    show loungeZoomFix
    show screen browserWindowFeed
    hide screen browserWindowSubscribe
    hide screen browserWindowSubscribeFake
    hide screen browserWindowSubscribeTrue
    show screen barre_de_vie
    s "T'es complétement chtarbée"
