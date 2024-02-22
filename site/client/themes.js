
let themes =
    [
        {
            "theme": "Politique",
            "subthemes": [["Education", "checkbox-eduction"],
            ["Immigration", "checkbox-immigration"],
            ["Emploi", "checkbox-emploi"],
            ["Services publics", "checkbox-services-publics"]]
        },
        {
            "theme": "Economie",
            "subthemes": [["Entreprises", "checkbox-entreprises"],
            ["Fiscalité", "checkbox-fiscalite"],
            ["Innovation", "checkbox-innovation"],
            ["Commerce", "checkbox-commerce"]]
        },
        {
            "theme": "Sante",
            "subthemes": [["Cancer", "checkbox-cancer"],
            ["Prevention", "checkbox-prevention"],
            ["Santé publique", "checkbox-sante-publique"],
            ["Recherche", "checkbox-recherche"]]
        },
        {
            "theme": "Climat",
            "subthemes": [["Energie", "checkbox-energie"],
            ["Transport", "checkbox-transport"],
            ["Agriculture", "checkbox-agriculture"],
            ["Pollution", "checkbox-pollution"]]
        },
        {
            "theme": "Culture",
            "subthemes": [["Blockbuster", "checkbox-blockbuster"],
            ["Cinéma Français", "checkbox-francais"],
            ["Littérature", "checkbox-litterature"],
            ["Théâtre", "checkbox-theatre"]]
        },
        {
            "theme": "Sport",
            "subthemes": [["Football", "checkbox-football"],
            ["Basketball", "checkbox-basketball"],
            ["Rugby", "checkbox-rugby"],
            ["Tennis", "checkbox-tennis"],
            ["Feminin", "checkbox-feminin"],
            ["Masculin", "checkbox-masculin"]]
        },
        {
            "theme": "VSS",
            "subthemes": [["Viols", "checkbox-viols"],
            ["Agressions sexuelles", "checkbox-agressions-sexuelles"],
            ["Féminicides", "checkbox-feminicides"],
            ["Violences conjugales", "checkbox-violences-conjugales"]]
        },
        {
            "theme": "flag",
            "subthemes": [["Titre coupé", "checkbox-cut"],
            ["Pas un titre d'article", "checkbox-notarticle"],
            ["Catégorie manquante", "checkbox-missingcategory"],
            ["Erreur d'affichage", "checkbox-displayerror"],
            ["Autre", "checkbox-autre"]]
        },
        {
            "theme": "divers",
            "subthemes": [["Description du meurtre", "checkbox-murderdescription"]]
        }


    ];



for (let value of themes) {
    let theme = value.theme.toLowerCase();
    let subThemesArray = value.subthemes; 
    let theme_checkbox = document.getElementById('checkbox-' + theme);
    if (theme_checkbox) {
        theme_checkbox.addEventListener('change', function () {
            let subthemesElement = document.getElementById('subthemes');  // Élément DOM pour les sous-thèmes
            if (this.checked) {
                for (let subTheme of subThemesArray) {  // Parcourir l'array des sous-thèmes
                    let button = document.createElement('label');
                    button.className = 'checkbox-as-button subtheme-button-' + theme;
                    let subtheme_id = subTheme[1];
                    button.innerHTML = '<input type="checkbox" name="' + subtheme_id.replace("checkbox-", '') + '" id="' + subtheme_id + '" ><span class="checkbox-button-top theme-color-' + theme + '">' + subTheme[0] + '</span>';
                    subthemesElement.appendChild(button);  // Ajouter au DOM
                }
            } else {
                let subthemeButtons = document.getElementsByClassName('subtheme-button-' + theme);
                while (subthemeButtons.length > 0) {
                    subthemesElement.removeChild(subthemeButtons[0]);
                }
            }
        });
    }
}
function loadSourceLogo() {
    let source = document.getElementById('article_source');
    let sourceLogo = document.getElementById('journal-logo');
    let src = source.value.toLowerCase().replace(" ", "")
    sourceLogo.src = "logos/" + src + ".png";
    sourceLogo.alt = source.value;
}

//<label class="checkbox-as-button subtheme-button-sport" id="checkbox-sport"><input type="checkbox" id="sport + subtheme_id + '" ><span class="checkbox-button-top theme-color-' + theme + '">' + subTheme[0] + '</span>';
/*
        <div class="article-place">
            <p class="secondary-heading">Titre ici
                
            </p>
            <p class="card-description">
                sous titre ici
            </p>
        </div>
*/
// Charge un article de la base de donnée pour l'afficher
/*
function loadAndDisplayArticle() {
    fetch('http://localhost:3000/api/articles')
        .then(response => response.json())
        .then(articles => {
            const articlesContainer = document.querySelector('.columns-article');
            articlesContainer.innerHTML = ''; // Efface les articles précédents avant d'afficher le nouveau
            if (articles.length > 0) {
                let article = articles[0]; // Affiche le premier article

                // Code pour créer et afficher l'articleElement omis pour la brièveté

                // Vérifier si le champ article_id existe déjà
                let articleIdInput = document.getElementById('article_id');
                if (!articleIdInput) {
                    articleIdInput = document.createElement('input');
                    articleIdInput.setAttribute('type', 'hidden');
                    articleIdInput.setAttribute('name', 'article_id');
                    articleIdInput.setAttribute('id', 'article_id');
                    const form = document.getElementById('themes-form');
                    form.appendChild(articleIdInput);
                }
                // Mettre à jour la valeur avec le nouvel article_id
                articleIdInput.setAttribute('value', article.id_article);
            }
        })
        .catch(error => console.error('Erreur lors de la récupération des articles:', error));
}
*/
function loadAndDisplayArticle() {
    fetch('http://localhost:3000/api/articles')
        .then(response => response.json())
        .then(articles => {
            const articlesContainer = document.querySelector('.columns-article');
            articlesContainer.innerHTML = ''; // Efface les articles précédents avant d'afficher le nouveau
            if (articles.length > 0) {
                let article = articles[0]; // Affiche le premier article
                let logoName = article.source.toLowerCase().replace(" ", "").replace("é", "e").replace("’", "");
                const articleElement = document.createElement('div');
                articleElement.classList.add('article-place');
                articleElement.innerHTML = `
                  <img src="http://localhost:3000/client/logos/${logoName}.png" alt="journal-logo" class="journal-logo">
                  <p class="secondary-heading">${article.titre}</p>
                  <p class="card-description">${article.sous_titre || 'Pas de sous-titre'}</p>
                `;

                articlesContainer.appendChild(articleElement);

                // Vérifier si le champ article_id existe déjà
                let articleIdInput = document.getElementById('article_id');
                if (!articleIdInput) {
                    articleIdInput = document.createElement('input');
                    articleIdInput.setAttribute('type', 'hidden');
                    articleIdInput.setAttribute('name', 'article_id');
                    articleIdInput.setAttribute('id', 'article_id');
                }
                articleIdInput.setAttribute('value', article.id_article);

                // Vérifier si le champ article_source existe déjà
                let articleSourceInput = document.getElementById('article_source');
                if (!articleSourceInput) {
                    articleSourceInput = document.createElement('input');
                    articleSourceInput.setAttribute('type', 'hidden');
                    articleSourceInput.setAttribute('name', 'article_source');
                    articleSourceInput.setAttribute('id', 'article_source');
                }
                articleSourceInput.setAttribute('value', article.source);

                const form = document.getElementById('themes-form');
                form.appendChild(articleIdInput);
                form.appendChild(articleSourceInput);
            }
        })
        .catch(error => console.error('Erreur lors de la récupération des articles:', error));
}



// Appeler la fonction au chargement de la page
document.addEventListener('DOMContentLoaded', loadAndDisplayArticle);




function verifySubmit() {
    let checkbox_sport = document.getElementById('checkbox-sport');
    // Sélectionnez les checkboxes par leurs identifiants
    let checkbox1 = document.getElementById('checkbox-feminin');
    let checkbox2 = document.getElementById('checkbox-masculin');
    if (checkbox_sport.checked) {
        // Vérifiez si au moins une des deux checkboxes est cochée
        if (!checkbox1.checked && !checkbox2.checked) {
            // Si aucune des deux n'est cochée, empêchez la soumission du formulaire
            alert('Vous devez sélectionner un genre : Féminin ou Masculin !');
            return false;
        }
        return true;
        // Si au moins une est cochée, le formulaire sera soumis normalement
    } else {
        return true;
    }
};




function slideDivOut() {
    let divToMove = document.querySelector('div.card');
    divToMove.style.transform = 'translateX(-100%)';
    divToMove.style.transition = 'transform 1s';
    setTimeout(() => {
        divToMove.style.display = 'none';
    }, 1000);

}

function slideDivIn() {
    let articleCard = '<div class="card columns-article columns" style="transform: translateX(100%); transition: transform 3s;"><img src="/logos/lemonde.png" alt="journal-logo" class="journal-logo"><p class="secondary-heading">« La violence est ordinaire et gratuite chez ces jeunes gangrénés par la misère»...Mayotte, une cage dorée pour les expatriés français.</p><p class="card-description"><br></p><div class="button-container"></div></div>';
    let tempDiv = document.createElement('div');
    tempDiv.innerHTML = articleCard;
    let divToMove = tempDiv.firstChild;
    divToMove.style.transform = 'translateX(0)';
    divToMove.style.transition = 'transform 3s';
    let topContainer = document.querySelector('.top-container');
    topContainer.appendChild(divToMove);

    // Mettez en place la transition pour le mouvement de glissement
    setTimeout(() => {
        divToMove.style.transform = 'translateX(0)';
    }, 100);

    // Affichez la div après un délai
    setTimeout(() => {
        divToMove.style.display = 'block';
    }, 2000);

}

function secureSubmit() {
    // Créer un objet pour stocker les données du formulaire
    let formData = {};


    let aricle_id = document.getElementById('article_id');
    formData['article_id'] = aricle_id.value;
    // Récupérer la valeur de la case cochée pour chaque thème
    for (let value of themes) {
        let theme = value.theme.toLowerCase()
        theme = theme.replace("é", "e");
        let checkbox = document.getElementById('checkbox-' + theme);

        if (checkbox.checked) {
            formData[theme] = true;

            // Récupération des sous thèmes
            for (let value2 of value.subthemes) {
                let subtheme = value2[1];

                let subthemeCheckbox = document.getElementById(subtheme);
                if (subthemeCheckbox && subthemeCheckbox.checked) {
                    formData[subtheme.replace("checkbox-", "")] = true;
                }
            }

        }
    }
    // Convertir l'objet en JSON
    let jsonData = JSON.stringify(formData);
    // Envoyer le JSON au serveur via une requête POST
    // Envoi au port 3000
    fetch('http://localhost:3000/submit-form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    }).then(response => {
        if (response.ok) {
            console.log('Formulaire soumis avec succès.');
            //slideDivOut();
            //slideDivIn();
        } else {
            console.error('Erreur lors de la soumission du formulaire :', response.status);
        }
    }).catch(error => {
        console.error('Erreur lors de la soumission du formulaire :', error);
    });

    // Empêcher la soumission normale du formulaire
    return false;
}

// Attacher un gestionnaire d'événements au bouton de soumission
document.getElementById("submit-form").addEventListener("click", function () {
    // Récupérer l'élément du formulaire
    let formulaire2 = document.getElementById("themes-form");
    // Soumettre le formulaire
    //test = verifySubmit();
    //if (test) {
    secureSubmit();
    loadAndDisplayArticle();


});






