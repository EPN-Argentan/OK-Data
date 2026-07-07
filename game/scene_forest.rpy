default visitedForest = False
label forest :
  nvl clear
  $ visitedForest = True
  hide screen hubElements
  show walkInForest
  show screen barre_de_vie
  stop music fadeout 1.0
  play music "To Ponder - Godmode.mp3"
  a "Au cœur de la forêt, là où les arbres murmurent leurs secrets au vent, il existe un sanctuaire suspendu."
  a "C’est là que l’on se ressource, loin des lueurs flottantes du monde connecté, dans une paix qui semble naître de la terre elle-même."
  call addPoints(2,'point_localisation') from _call_addPoints_13
  a "Oh… les jolis points de localisation, scintillant comme des lucioles dans l’ombre des sous bois."
  call addPoints(2,'point_sociaux') from _call_addPoints_14
  a "Je cueille quelques points de réseaux sociaux, pareils à des plumes tombées d’un oiseau bavard."
  call addPoints(2,'point_sante') from _call_addPoints_15
  a "Je glane quelques points santé, fragiles et doux comme des herbes médicinales."
  call addPoints(2,'point_administrative') from _call_addPoints_16
  a "Je récolte quelques points de données administratives, lourds de leur gravité."
  call addPoints(2,'point_interet') from _call_addPoints_17
  a "Je prélève des points de centres d’intérêt, éclats de curiosité qui vibrent comme une feuille au vent."
  call addPoints(2,'point_conviction') from _call_addPoints_18
  a "Je saisis des points de conviction, ardents comme des braises."
  a "Et je suis enfin riche de ces petites étoiles invisibles que j’ai piochées."
  $ hubClickable["forest"]= 0
  jump hub
