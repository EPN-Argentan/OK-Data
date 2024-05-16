label forest :
  nvl clear
  hide screen hubElements
  show walkInForest
  show screen barre_de_vie
  a "Au cœur de la forêt, là où les arbres murmurent leurs secrets au vent, il est un endroit où le temps se suspend."
  a "C’est là que l’âme se ressource, loin des écrans lumineux et des bruits assourdissants."
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
  a "Je suis trop content"
  $ hubClickable["forest"]= 0
  jump hub
