label dataZon :
  nvl clear
  hide screen hubElements
  hide screen phoneDown
  show zoomPC
  show screen barre_de_vie
  a "allons voir mes mails"
  show screen desktopbutton
  a "allons-y !"



label mailx3 :
    $ renpy.scene(layer="screens")

    show screen mailx3
    a "hum... je lis quel mail"

    while True:
        empty ""


label brouillon :
    $ renpy.scene(layer="screens")
    show screen brouillon
    a "Ah mais oui mon mail d'hier soir... Je dois le finir."
    a "Bon je l'envoi à tous mes contacts. J'envoi en A ou en CCI ?"

    while True:
        empty ""

label Brouillon_phone_ok :
    $ renpy.scene(layer="screens")
    show screen brouillon
    call addPoints(2,'point_sociaux')
    e_nvl "Bravo, En effet rien ne sert de communiquer les mails de tes proches à tous"
    jump mailx3

label Brouillon_phone_No:
    $ renpy.scene(layer="screens")
    show screen brouillon
    call addPoints(-2,'point_sociaux')
    e_nvl "Il faut mieux éviter de placer tous tes contacts dans A car tu communiques les adresses à tous."
    jump mailx3

label mail_coli6mots :
    $ renpy.scene(layer="screens")
    show screen mail_coli6mots
    a "Hum un colis ?"

    while True:
        empty ""


label feed_coli6mots :
    $ renpy.scene(layer="screens")
    show screen feed_coli6mots
    a "Oh Zut !"

label Noformok :
    nvl clear
    e_nvl "Bravo, il ne faut pas en effet répondre à ce genre de mail. L'adresse mail était suspecte"
    jump mailx3

label phonestopcoli6mots :
    nvl clear
    $ renpy.scene(layer="screens")
    show screen feed_coli6mots_statique
    call addPoints(-2,'point_administrative')
    e_nvl "Zut, voici un mail du type phishing qui cherche à dérober des informations et à t'extorquer de l'argent."
    e_nvl "Penses à vérifier l'adresse de l'expéditeur avant de cliquer"
    jump mailx3


label superclerc:
    $ renpy.scene(layer="screens")
    show screen superclerc
    a "ok, mon ticket de course"
    jump mailx3

label mailsepharo :
    $ renpy.scene(layer="screens")
    show screen mailsepharo
    a "Oh ? Ah oui c'est vrai j'avais laissé ma géolocalisation activée"
    jump mailx3

#partie datazon#



screen desktopbutton:
    imagebutton:
        xalign 0.515
        yalign 0.43
        idle "UI/datazon/mailbutton_idle.png"
        hover "UI/datazon/mailbutton_hover.png"
        action Jump("brouillon")

screen brouillon :
    add "UI/datazon/brouillon.png" xalign 0.5 yalign 0.5
#bouton CCI
    imagebutton:
        xalign 0.515
        yalign 0.43
        idle "UI/datazon/zone_envoi_idle.jpg"
        hover "UI/datazon/zone_envoi_hover.jpg"
        action Jump("Brouillon_phone_ok")
#boutton A
    imagebutton:
        xalign 0.515
        yalign 0.39
        idle "UI/datazon/zone_envoi_idle.jpg"
        hover "UI/datazon/zone_envoi_hover.jpg"
        action Jump("Brouillon_phone_No")

screen mailx3 :
    add "UI/datazon/mailx3.jpg"
    imagebutton:
        xalign 0.546
        yalign 0.264
        idle "UI/datazon/mail1_idle.jpg"
        hover "UI/datazon/mail1_hover.jpg"
        action Jump("mail_coli6mots")

    imagebutton:
        xalign 0.546
        yalign 0.412
        idle "UI/datazon/mail2_idle.jpg"
        hover "UI/datazon/mail2_hover.jpg"
        action Jump("superclerc")

    imagebutton:
        xalign 0.546
        yalign 0.562
        idle "UI/datazon/mail3_idle.jpg"
        hover "UI/datazon/mail3_hover.jpg"
        action Jump("mailsepharo")


screen mail_coli6mots :
    add "UI/datazon/mail_coli6mots.jpeg" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.447
        yalign 0.667
        idle "UI/datazon/formbutton_idle.jpeg"
        hover "UI/datazon/formbutton_hover.jpeg"
        action Jump("feed_coli6mots")

    imagebutton:
        xalign 0.65
        yalign 0.667
        idle "UI/datazon/Noformbutton_idle.jpeg"
        hover "UI/datazon/Noformbutton_hover.jpeg"
        action Jump ("Noformok")

screen feed_coli6mots :
    add "UI/datazon/feedcoli6mots.jpeg" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "UI/datazon/feedcoli6mots.jpeg"
        hover "UI/datazon/feedcoli6mots.jpeg"
        action Jump ("phonestopcoli6mots")

screen feed_coli6mots_statique:
    add "UI/datazon/feedcoli6mots.jpeg" xalign 0.5 yalign 0.5

screen superclerc:
    add "UI/datazon/mailsuperclerc.png" xalign 0.5 yalign 0.5

screen mailsepharo:
    add "UI/datazon/mailsepharo.png" xalign 0.5 yalign 0.5
