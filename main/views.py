from django.shortcuts import render

def homepage(request):
    """This function will display the main.html template, will render the
    homepage for this website"""
    DICTIO = {
        "title":"Du gras, oui, mais de qualité",
        "help_substitute":"Trouvez un produit de substitution pour ceux que \
vous consommez tous les jours.",
        "name":"Colette et Remy",
        "history":"Remy et Colette sont amoureux de la gastronomie \
française.Travaillant quotidiennement avec les meilleurs produits du \
terroir, ils affectionnent particulièrement la bonne chaire et aiment \
partager leur passion. Pour y parvenir, ils décidèrent de lancer une \
plateforme web en ce sens. Voici le résultat !",
        "contact":"Contactez-nous!",
        "catchphrase":"Pour nous contacter ou faire une réservation, veuillez \
utiliser les informations ci-dessous.",
        "number":"+(33) 1 47 43 57 512",
        "mail":"purbeurre@gmail.com",
    }

    return render(request, 'main/main.html', DICTIO)

def copyright(request):
    """This function will display copyrights of this website"""
    DICTIO = {
        "title":"Mentions légales",
        "h2_1":"Le site web PurBeurre est la propriété de Colette et Remy",
        "p1_1":"Siège Social : Restaurant de Montmartre",
        "p1_2":"Téléphone:+(33) 1 47 43 57 512",
        "p1_3":"Email : purbeurre@gmail.com",
        "h2_2":"Créateur et hébergement du site :",
        "p2_1":"La société OC, société par actions simplifiée est en activité depuis 11 ans \
D au chiffre d'affaires de 7 137 700,00 € immatriculée au RCS le 28-11-2008 n° de \
Siret : 49386136300064.",
        "p2_2":"Adresse :7 CITE DE PARADIS - 75010 PARIS",
        "p2_3":"Tel :+33 (0) 1 80 88 80 30",
        "h2_3":"Modifications",
        "p3_1":"En accédant et en naviguant sur ce site, l'utilisateur est informé de ses \
droits et obligations et accepte pleinement de se conformer aux \
présentes conditions d'utilisations du site. L'éditeur du site se \
réserve la possibilité de modifier ces conditions. Il appartient à \
l'utilisateur de vérifier périodiquement le contenu des documents \
concernés. L'éditeur se réserve la possibilité de supprimer ou de \
modifier en tout ou partie le « site ».",
        "h2_4":"Collecte de données et Loi Informatiques et Libertés",
        "p4_1":"Conformément à la loi n° 78-17 du 6 janvier 1978, l'utilisateur peut à tout \
moment accéder aux informations personnelles le concernant détenues par \
Colette et Remy, demander leur modification ou leur suppression. Ainsi, \
selon les articles 36, 39 et 40 de la loi Informatique et Libertés, \
l’utilisateur peut demander que soient rectifiées, complétées, \
clarifiées, mises à jour ou effacées les informations le concernant qui \
sont inexactes, incomplètes, équivoques, périmées ou dont la collecte \
ou l'utilisation, la communication ou la conservation sont \
interdites.",
        "p4_2":"Si vous souhaitez exercer ce droit et obtenir communication des \
informations vous concernant,",
        "p4_3":"veuillez-vous adresser par email à : purbeurre@gmail.com",
        "name":"Copyrights",
        "icons_copy":"Icons used in this website are owned by FontAwesome©. \
Do not reproduce.",
        "photo_copy":"Main page image is owned by Ubon Ratchathani©. Do not \
reproduce.",
    }

    return render(request, 'main/copyright.html', DICTIO)
