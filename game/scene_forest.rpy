label forest :
  nvl clear
  show walkInForest
  show screen barre_de_vie
  a "Oh c'est tellement bien d'être en forêt loin des réseaux, je me sens ressourcée"
  call addPoints(2,'point_localisation')
  a "Je récupère des points de vie privée (localisation)"
  call addPoints(2,'point_sociaux')
  a "Je récupère des points de vie privée (sociaux)"
  call addPoints(2,'point_sante')
  a "Je récupère des points de vie privée (santé)"
  call addPoints(2,'point_administrative')
  a "Je récupère des points de vie privée (administrative)"
  call addPoints(2,'point_interet')
  a "Je récupère des points de vie privée (interet)"
  call addPoints(2,'point_conviction')
  a "Je récupère des points de vie privée (conviction)"
  jump hub
