label med :
    scene hub
    hide screen hubElements
    e_nvl "Maintenant, tu es prêt pour la grande aventure, le but étant de garder le plus possible de données personnelles. \n À toi de jouer !"

    ##Set hub elements clickable
    $ hubClickable["dog"]= 0
    $ hubClickable["phone"]= 1
    $ hubClickable["tablet"]= 0
    $ hubClickable["laptop"]= 1
    $ hubClickable["walkout"]= 1
    $ hubClickable["forest"]= 1
    $ hubClickable["photoFrame"]= 1
    
    jump hub
