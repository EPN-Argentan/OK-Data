default visitedForest = False
label forest :
  nvl clear
  $ visitedForest = True
  hide screen hubElements
  show walkInForest
  show screen barre_de_vie
  stop music fadeout 1.0
  play music "To Ponder - Godmode.mp3"
  a "Au cœur de la forêt, là où les arbres murmurent leurs secrets au vent, il est un endroit où le temps se suspend."
  a "C’est là que l’âme se ressource, loin des écrans lumineux et des bruits assourdissants."
  call addPoints(2,'point_localisation') from _call_addPoints_13
  a "Je récupère des points de vie privée (localisation)"
  call addPoints(2,'point_sociaux') from _call_addPoints_14
  a "Je récupère des points de vie privée (sociaux)"
  call addPoints(2,'point_sante') from _call_addPoints_15
  a "Je récupère des points de vie privée (santé)"
  call addPoints(2,'point_administrative') from _call_addPoints_16
  a "Je récupère des points de vie privée (administrative)"
  call addPoints(2,'point_interet') from _call_addPoints_17
  a "Je récupère des points de vie privée (interet)"
  call addPoints(2,'point_conviction') from _call_addPoints_18
  a "Je récupère des points de vie privée (conviction)"
  a "Je suis trop content"
  $ hubClickable["forest"]= 0
  jump hub
