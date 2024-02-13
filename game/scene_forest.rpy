label forest :
  nvl clear
  hide screen hubElements
  show walkInForest
  show screen barre_de_vie
  a "Oh c'est tellement bien d'être en forêt loin des réseaux, je me sens ressourcée"
  call addPoints(2,'point_localisation') from _call_addPoints_2
  a "Je récupère des points de vie privée (localisation)"
  call addPoints(2,'point_sociaux') from _call_addPoints_3
  a "Je récupère des points de vie privée (sociaux)"
  call addPoints(2,'point_sante') from _call_addPoints_4
  a "Je récupère des points de vie privée (santé)"
  call addPoints(2,'point_administrative') from _call_addPoints_5
  a "Je récupère des points de vie privée (administrative)"
  call addPoints(2,'point_interet') from _call_addPoints_6
  a "Je récupère des points de vie privée (interet)"
  call addPoints(2,'point_conviction') from _call_addPoints_7
  a "Je récupère des points de vie privée (conviction)"
  a "Je suis trop content"
  $ hubClickable["forest"]= 0
  jump hub
