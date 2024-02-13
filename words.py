import nltk
from nltk.corpus import stopwords

import json

nltk.download('wordnet')
nltk.download('stopwords')


##Politics
political_words_list = ['Biden', 'Trump', 'Macron', 'Merkel', 'Putin', 'Johnson', 'Castex', 'Hollande', 'Sarkozy', 'Chirac', 'Mitterrand', 'De Gaulle', 'Roosevelt', 'Churchill',
                        'Bolsonaro', 'Xi Jinping', 'Modi', 'Trudeau', 'Abe', 'Erdogan', 'Netanyahu', 'Orban', 'Merkel', 'Macron', 'Putin', 'Johnson', 'Castex', 'Hollande', 'Sarkozy', 'Chirac', 'Mitterrand', 'De Gaulle', 'Roosevelt', 'Churchill',
                        'leftist', 'rightist', 'conservative', 'tory', 'labour', 'Democrats', 'Republicans', 'Green Party', 'Politics', 'politics', 'politic', 'president', 'President',
                        'MAGA', 'Brexit', 'EU', 'European Union', 'United Nations', 'UN', 'NATO', 'G7', 'G20', 'G8']
additional_words = ['présidentielle', 'député', 'députée', 'politique', 'gouvernement', 'élections', 'démocratie', 'parti', 'vote',
                            'assemblée', 'sénat', 'président', 'ministre', 'réforme', 'loi', 'décret',
                            'opposition', 'majorité', 'droite', 'gauche', 'centre', 'libéral', 'conservateur',
                            'socialiste', 'républicain', 'député', 'sénateur', 'campagne', 'scrutin',
                            'politicien', 'mandat', 'législation', 'constitution', 'référendum', 'parlement',
                            'congrès', 'électeur', 'candidat', 'coalition', 'idéologie', 'débat', 'discours',
                            'diplomatie', 'négociation', 'traité', 'sommet', 'alliance', 'conflit',
                             'révolution', 'manifestation', 'grève', 'répression', 'censure',
                            'autorité', 'liberté', 'droits', 'justice', 'égalité', 'citoyen', 'nation',
                            'patriotisme', 'souveraineté', 'état', 'gouvernance', 'administration', 'budget',
                            'fiscalité', 'impôt', 'économie', 'social', 'UMP', 'PS', 'RN', 'LREM', 'FI', 'EELV', 'PCF', 'LR', 'NPA', 'LFI', 'Modem',
                            'PRG', 'UDI', 'FN', 'RPR', 'Les Verts', 'MRC', 'DLF', 'LO', 'PP', 'Rassemblement',
                            'Gauche', 'Droite', 'Centriste', 'Socialiste', 'Républicain', 'Démocrate', 'Libéral',
                            'Conservateur', 'Progressiste', 'Nationaliste', 'Ecologiste', 'Communiste',
                            'Indépendantiste', 'Populiste', 'Patriote', 'Réformiste', 'Radical', 'Royaliste',
                            'Monarchiste', 'Fédéraliste', 'Unioniste', 'Souverainiste', 'Autonomiste',
                            'Libertaire', 'Anarchiste', 'Marxiste', 'Léniniste', 'Trotskyiste', 'Maoïste',
                            'Gaulliste', 'Mitterrandiste', 'Chiraquien', 'Sarkozyste', 'Hollandais',
                            'Juppéiste', 'Filloniste', 'Vallsiste', 'Macroniste', 'Mélenchoniste', 'Le Pen',
                            'Sarkozy', 'Hollande', 'Macron', 'Mélenchon', 'Royal', 'Valls', 'Fillon', 'Juppé',
                            'Bayrou', 'Dupont-Aignan', 'Poutou', 'Arthaud', 'Lagarde', 'Borloo', 'Besancenot',
                            'Cheminade', 'Asselineau', 'Philippe', 'Hidalgo', 'Taubira', 'Collomb', 'Baroin',
                            'Ciotti', 'Ruffin', 'Quatennens', 'Corbière', 'Autain', 'Boutin', 'De Villiers',
                            'Bergé', 'Faure', 'Bartolone', 'Retailleau', 'Jacob', 'Wauquiez', 'Pécresse',
                            'Bertrand', 'Le Maire', 'Darmanin', 'Castaner', 'Ferrand', 'Le Foll', 'Montebourg',
                            'Hamon', 'Royal', 'Aubry', 'Borloo', 'Baylet', 'Cosse', 'Placé', 'De Rugy', 'Jadot',
                            'Piolle', 'Rivasi', 'Bové', 'Duflot', 'Mamère', 'Cohn-Bendit', 'Cazeneuve', 'Vidal',
                            'Borne', 'Le Drian', 'Parly', 'Goulard', 'Lemoyne', 'Lecornu', 'Fesneau', 'Attal',
                            'Ndiaye', 'Schyns', 'Moreau', 'Buzyn', 'Bachelot', 'Touraine', 'Rossignol', 'El Khomri',
                            'Schiappa', 'Belloubet', 'Dupond-Moretti', 'Pompili', 'Rugy', 'Flessel',
                            'Girardin', 'Nyssen', 'Franco', 'Pénicaud', 'Mounir', 'Mahjoubi', 'Griveaux',
                            'Philippe', 'Lemaire', 'Denormandie', 'Pannier-Runacher', 'Guérini', 
                            'Ferracci', 'Villani', 'Taché', 'Avia', 'Taquet', 'Bergé',
                            'Gosselin', 'Abad', 'Ciotti', 'Larrivé', 'Woerth', 'Buffet', 'Guaino', 'Debré',
                            'Lamassoure', 'Karoutchi', 'Retailleau', 'Peltier', 'Mariani', 'Patriat', 'Guérini',
                            'Fasquelle', 'Lecornu', 'Darrieussecq', 'Bussereau', 'Dussopt', 'Fesneau', 'Girardin',
                            'Gourault', 'Lecornu', 'Lemoyne', 'Morin']


political_words_list += additional_words
political_words_pairs = [[word, 'politique'] for word in political_words_list]

##Climate
climate_words_list = [ 'vert', 'climat', 'environnement', 'écologie', 'durabilité',
                    'émissions de carbone', 'réchauffement global', 'effet de serre',
                    'changement climatique', 'crise climatique', 'urgence climatique',
                    'action pour le climat', 'carbone', 'gaz à effet de serre', 'combustibles fossiles',
                    'énergie renouvelable', 'énergie solaire', 'énergie éolienne', 'déforestation',
                    'biodiversité', 'extinction', 'pollution', 'plastique', 'recyclage', 'océan',
                    'mer', 'forêt', 'faune', 'animal', 'plante', 'terre', 'planète', 'durable',
                    'développement durable', 'changement climatique', 'réchauffement global',
                    'empreinte carbone', 'gaz à effet de serre', 'combustibles fossiles',
                    'énergie renouvelable', 'énergie solaire', 'énergie éolienne', 'hydroélectrique',
                    'biomasse', 'durabilité', 'conservation', 'biodiversité', 'déforestation',
                    'reforestation', 'pollution', "qualité de l'air", 'acidification des océans',
                    'fonte des glaciers', 'élévation du niveau de la mer', 'extinction', 'espèces en danger', 
                    "perte d'habitat", 'écosystèmes', 'recyclage', 'compostage', 'zéro déchet',
                    'politique environnementale', 'Protocole de Kyoto', 'Accord de Paris', 'CCNUCC',
                    'COP26', 'écologique', 'développement durable', 'neutre en carbone', 'compensation carbone',
                    'géo-ingénierie', 'adaptation climatique', 
                    'marché des émissions', 'taxe carbone', 'technologie verte', 'énergie propre',
                    'efficacité énergétique', 'véhicules électriques', 'transports publics', 'vélo',
                    'marche', 'urbanisme', 'espaces verts', 'foresterie urbaine', 'permaculture',
                    'agriculture biologique', 'agroécologie', 'kilomètres alimentaires', 'pêche durable', 'réserves marines', 'récifs coralliens',
                    'écolos', 'verts', 'écologistes', 'climatologues',  'activistes']
list(set(climate_words_list))
#climate_words_list = get_words(climate_start_terms,2)
climate_words_pairs = [[word, 'climat'] for word in climate_words_list]

##Sport
sport_word_list = ['sport', 'athlète', 'compétition', 'tournoi', 'match', 'partie', 'victoire', 'défaite', 'record', 'exploit',
                    'médaille', 'podium', 'champion', 'championnat', 'ligue', 'équipe', 'joueur', 'entraîneur', 'manager', 'stade',
                    'piste', 'terrain', 'balle', 'balle', 'raquette', 'golf', 'tennis', 'football', 'basket-ball', 'rugby', 'volley-ball',
                    'handball', 'baseball', 'hockey', 'natation', 'athlétisme', 'cyclisme', 'boxe', 'marathon', 'triathlon', 'escalade',
                    'ski', 'snowboard', 'patinage', 'plongée', 'gymnastique', 'haltérophilie', 'lutte', 'culturophysique', 'karaté', 'judo',
                    'taekwondo', 'lutte', 'tennis de table', 'badminton', 'squash', 'billard', 'échecs', 'olympique', 'paralympique',
                    'jeux', 'fédération', 'athlétisme', 'confédération', 'sportif', 'coupe', 'grand', 'chelem', 'maîtres', 'dopage',
                    'antidopage', 'disqualification', 'arbitre', 'arbitrage', 'carte', 'pénalité', 'hors-jeu', 'but', 'essai', 'panier',
                    'athlétisme', 'Real Madrid', 'Barcelone', 'PSG', 'Marseille', 'Lyon', 'Lille', 'Monaco', 'Girondins', 'Liverpool',
                    'Super Bowl', 'NFL','victoire', 'Super Bowl', 'Bowl', 'CAN']
   
sport_words_pairs = [[word, 'sport'] for word in sport_word_list]

##Culture 
culture_words = ['culture', 'art', 'musique', 'cinéma', 'théâtre', 'danse', 'opéra', 'photographie', 'peinture', 'sculpture', 'architecture', 'design', 'mode', 'littérature', 'poésie', 'roman', 'essai', 'critique', 'festival', 'exposition', 'galerie', 'musée', 'patrimoine', 'tradition', 'folklore', 'identité', 'diversité', 'créativité', 'inspiration', 'innovation', 'avant-garde', 'mouvement', 'artistique', 'éducation', 'histoire', 'esthétique', 'anthropologie', 'sociologie', 'philosophie', 'expression', 'interprétation', 'beauté', 'émotion', 'sensibilité', 'perception', 'réception', 'contemplation', 'théorie', 'cinématographie', 'dramaturgie', 'performance', 'spectateur', 'public', 'scénographie', 'réalisation', 'acteur', 'actrice', 'réalisateur', 'chorégraphe', 'chanteur', 'compositeur', 'musicien', 'interprète', 'représentation', 'documentaire', 'animation', 'réalisme', 'symbolisme', 'impressionnisme', 'expressionnisme', 'cubisme', 'surréalisme', 'baroque', 'renaissance', 'minimalisme', 'néoclassicisme', 'modernisme', 'postmodernisme', 'romantisme', 'classicisme', 'contemporain', 'théâtral', 'mise en scène', 'dramaturge', 'répertoire théâtral', 'acte', 'scène', 'comédie', 'tragédie', 'drame', 'farce', 'ballet', 'classique', 'jazz', 'hip-hop', 'folklorique', 'traditionnel', 'musical', 'orchestre', 'concert', 'symphonie', 'sonate', 'rock', 'pop', 'blues', 'rap', 'électronique', 'expérimental', 'world', 'reggae', 'funk', 'indie', 'alternatif', 'techno', 'performance', 'installation', "chef-d'œuvre", 'exposition', 'rétrospective', 'international', 'national', 'local', 'représentation', 'théâtrale', 'musicale', 'chorégraphique', 'artistique', 'événement', 'populaire', 'culturel', 'saison', 'semaine culturelle', 'journée culturelle', 'musée', 'visite guidée', 'interactive', 'immersif', 'virtuel', 'activité familiale', 'performance culturelle', 'concert culturel', 'projection culturelle', 'débat', 'conférence', 'séminaire', 'forum', 'atelier', 'masterclass', 'rencontre artistique', 'littéraire', 'cinématographique', 'thématique', 'interculturel', 'professionnel', 'artiste', 'auteur', 'cinéaste', 'choregraphe', 'musicien', 'comédien',
                 'Taylor Swift', 'Swift', 'Kanye West', 'Rihanna', 'Beyonce', 'pop', 'rap', 'song', 'album']
culture_words_pairs = [[word, 'culture'] for word in culture_words] 


##Numérique
digital_words_list = [ 'digital', 'numérique', 'internet', 'web', 'site', 'site web', 'site internet', 'réseau', 'réseau social', 'réseaux sociaux', 'réseaux', 'social', 'média', 'médias sociaux', 'réseau social', 'réseaux sociaux', 'réseau', 'réseaux', 'digitalisation', 'digitalisation',
                      'facebook', 'twitter', 'instagram', 'linkedin', 'tiktok', 'snapchat', 'whatsapp', 'messenger', 'youtube', 'google', 'amazon', 'apple', 'microsoft', 'netflix', 'spotify', 'deezer', 'twitch', 'discord', 'reddit', 'tumblr', 'pinterest', 'flickr', 'vimeo', 'dailymotion', 
                    'technologie', 'innovation', 'cyber', 'cyberespace', 'cybersécurité', 'commerce électronique',
                    'startups', 'applications', 'logiciel', 'programmation', 'développement', 'code',
                    'robotique', 'appareils connectés', 'IoT', 'intelligence collective', 'révolution numérique',
                    'disruption numérique', 'science des données', 'analyse de données', 'cryptomonnaies',
                    'blockchain', 'cryptomonnaie', 'fintech', 'paiement en ligne', 'e-learning',
                    'apprentissage en ligne', 'cloud', 'mobilité', 'télétravail', 'télécommunications',
                    'réalité virtuelle', 'réalité augmentée', 'chatbots', 'assistant virtuel',
                    'automatisation', 'apprentissage automatique', 'IA', 'algorithmes', "systèmes d'information",
                    'design', 'UX', 'UI', 'ergonomie', 'partage de données', 'open data',
                    'protection des données', 'vie privée', 'sécurité des données', 'piratage', 'piratage', 'censure',
                    'filtrage', 'gouvernance', 'communautés en ligne', 'natives du numérique', 'géants du web',
                    'médias sociaux', 'blogs', 'vlogs', 'podcasts', 'streaming', 'contenu en ligne',
                    'commerce numérique', 'publicité en ligne', 'marketing numérique', 'stratégie numérique',
                    'cyberculture', 'cybercriminalité', 'fausses nouvelles', 'désinformation', 'économie numérique',
                    'société numérique', 'politique numérique', 'droit numérique', 'éthique numérique',               
                    'neutralité du net', 'détox numérique', 'responsabilité numérique', 'informatique verte'
                    ]
digital_pairs = [[word, 'technologie'] for word in digital_words_list]

##France
france_words = ['Macron']
france_words_pairs = [[word, 'france'] for word in france_words]

##Economy
economy_words = ['économie', 'économique', 'finance', 'financier', 'marché', 'bourse', 'bourse', 'commerce', 'commerce', 'affaires', 'entreprise', 'société', 'corporation', 'industrie', 'secteur', 'croissance', 'récession', 'crise', 'reprise', 'plan de relance', 'fonds de relance', 'stratégie de relance', 'mesures de relance', 'politique de relance', 'programme de relance', 'initiative de relance', 'action de relance', 'effort de relance', 'processus de relance', 'opération de relance', 'Wall Street', 'Dow Jones', 'Nasdaq', 'CAC 40', 'DAX', 'FTSE 100', 'Nikkei', 'Hang Seng', 'Shanghai Composite', 'Sensex', 'Bovespa', 'TSX', 'S&P 500', 'DAX 30', 'FTSE MIB', 'IBEX 35', 'SMI', 'AEX', 'BEL 20', 'ATX', 'unemployment', 'employment', 'job', 'jobless', 'joblessness', 'job loss', 'job cuts', 'jobless rate', 'minimum wage', 'businesses','business', 'company', 'corporation', 'industry', 'sector', 'growth', 'recession', 'crisis', 'recovery', 'recovery plan', 'recovery fund', 'recovery strategy', 'recovery measures', 'recovery policy', 'recovery program', 'recovery initiative', 'recovery action', 'recovery effort', 'recovery process', 'recovery operation', 'Wall street', 'Dow Jones', 'Nasdaq', 'CAC 40', 'DAX', 'FTSE 100', 'Nikkei', 'Hang Seng', 'Shanghai Composite', 'Sensex', 'Bovespa', 'TSX', 'S&P 500', 'DAX 30', 'FTSE MIB', 'IBEX 35', 'SMI', 'AEX', 'BEL 20', 'ATX', 'unemployment', 'employment', 'job', 'jobless', 'joblessness', 'job loss', 'job cuts', 'jobless rate', 'minimum wage']
economy_words_pairs = [[word, 'economie'] for word in economy_words]

## Catastrophe naturelles
catastrophe_words = ['catastrophe', 'catastrophe naturelle', 'désastre', 'inondation', 'inondations', 'inondé', 'inondation', 'eaux de crue', 'plaine inondable', 'zone inondable', 'barrages anti-inondation', 'éruption volcanique', 'éruption', 'tornade', 'tremblement de terre', 'ouragan', 'typhon', 'cyclone', 'tsunami', 'glissement de terrain', 'avalanche', 'sécheresse', 'incendie de forêt', 'feu de forêt', 'incendie']
catastrophe_words_pairs = [[word, 'catastrophe'] for word in catastrophe_words]

## Santé
health_words = ['santé', 'santé', 'soins de santé', 'soin', 'médical', 'médecine', 'médicament', 'médicament', 'médicaments', 'médicaments', 'pharmacie', 'pharmaceutique', 'produits pharmaceutiques', 'cancer', 'diabète', 'maladie cardiaque', 'obésité', 'santé mentale', 'maladie mentale', 'dépression', 'anxiété', 'stress', 'addiction', 'alcoolisme', 'toxicomanie', 'abus de substances', 'tabagisme', 'tabac', 'virus', 'bactéries', 'infection', 'infections', 'infectieux', 'pandémie', 'épidémie', 'épidémie', 'contagion', 'covid', 'covid-19', 'coronavirus', 'vaccin', 'vaccination', 'vaccins', 'vaccinations', 'vacciné', 'vaccination', 'vacciner', 'vaccinés', 'médecin', 'médecin', 'infirmière', 'hôpital', 'clinique', 'urgence', 'ambulance', 'paramédic', 'ambulanciers', 'premiers secours', 'premier intervenant', 'premiers intervenants', 'assurance maladie', 
                'bactérie', 'virus', 'covid-19']
health_words_pairs = [[word, 'sante'] for word in health_words]

##Stopwords
stop_words = list(set(stopwords.words('french')))
stop_words2 = ['a', 'afin', 'ai', 'aie', 'aient', 'aies', 'ait', 'alors', 'as', 'au', 'aucun', 'aura', 'aurai', 'auraient', 'aurais', 'aurait', 'auras', 'aurez', 'auriez', 'aurions', 'aurons', 'auront', 'aussi', 'autre', 'aux', 'avaient', 'avais', 'avait', 'avant', 'avec', 'avez', 'aviez', 'avions', 'avoir', 'avons', 'ayant', 'ayez', 'ayons', 'bon', 'car', 'ce', 'ceci', 'cela', 'ces', 'cet', 'cette', 'ceux', 'chaque', 'ci', 'comme', 'comment', 'd', 'dans', 'de', 'dedans', 'dehors', 'depuis', 'des', 'deux', 'devrait', 'doit', 'donc', 'dos', 'droite', 'du', 'dès', 'début', 'elle', 'elles', 'en', 'encore', 'essai', 'est', 'et', 'eu', 'eue', 'eues', 'eurent', 'eus', 'eusse', 'eussent', 'eusses', 'eussiez', 'eussions', 'eut', 'eux', 'eûmes', 'eût', 'eûtes', 'fait', 'faites', 'fois', 'font', 'force', 'furent', 'fus', 'fusse', 'fussent', 'fusses', 'fussiez', 'fussions', 'fut', 'fûmes', 'fût', 'fûtes', 'haut', 'hors', 'ici', 'il', 'ils', 'j', 'je', 'juste', 'l', 'la', 'le', 'les', 'leur', 'leurs', 'lui', 'là', 'm', 'ma', 'maintenant', 'mais', 'me', 'mes', 'moi', 'moins', 'mon', 'mot', 'même', 'n', 'ne', 'ni', 
    "Le", "La", "Un", "Les", "En", "Le", 
   "sans", "Pour", "c’est", "C’est", "ans", "plus", "après",
    "trois", "contre", "fin", "être", "près", "face", "d’une",  
    "faire", "d’un", "notion", "partant",
    "vécues", "Premium",
    "remettre", "ouvrage", "tente", "?", ":", "«", "»", "!", "»"
]
stop_words.extend(stop_words2)
stop_words_pairs = [[word, 'stopword'] for word in stop_words]


## Faits divers
divers_words = [ 'meurtre', 'tué', 'enlèvement', 'disparition', 'disparu', 'assassiné', 
                'assassinat', 'kidnapping', 'kidnappé', 'kidnappée', 'kidnappés', 'kidnappées',
                'meurtrier', 'meurtrière', 'meurtriers', 'cambriolage', 'cambriolé', 'cambriolés',
                'braquage', 'corps', 'cadavre', 'cadavres', 'criminel', 'criminels', 'criminelle', 'criminelles',
                'enlèvement', 'défiguré', 'dispute', 'lynchage', 'rixe', 'deal', 'dealer', 'Affaire', 'affaire' ]
divers_words_pairs = [[word, 'divers'] for word in divers_words]
## VSS
vss_words = [ 'viol', 'viols', 'tuée', 'assassinée', 'féminicide', 'sexuel', 'sexuelles', 'sexuels', 
             'violée', 'violées', 'violé', 'violés', 'inceste', 'pédophilie', 'pédophile', 'pédophiles',
                'harcèlement', 'harcèlements', 'harcèlement sexuel', 'vss']
vss_words_pairs = [[word, 'vss'] for word in vss_words]

## Immigration
immigration_words = ['droit du sol', 'immigration', 'migrants', 'réfugiés', 'asile', 'intégration',
                     'frontière', "demandeurs d'asile", 'sans-papiers', 'expulsions', 'régularisation',
                     'OQTF', 'naturalisation']
immigration_words_pairs = [[word, 'immigration'] for word in immigration_words]

#Export to json
words_json = []
for word in political_words_pairs:
    word_dict = {
        "word": word[0],
        "category": word[1]
    }
    words_json.append(word_dict)
for words in climate_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in sport_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in culture_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in france_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in stop_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in digital_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in economy_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in catastrophe_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in health_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in divers_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in vss_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)
for words in immigration_words_pairs:
    word_dict = {
        "word": words[0],
        "category": words[1]
    }
    words_json.append(word_dict)

with open('json/mots.json', 'w') as f:
    json.dump(words_json, f, indent=4)
    print(f"Nombre de mots enregistrés : {len(words_json)}")