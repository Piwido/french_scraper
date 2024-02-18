
var themes = 
[
    {
        "theme": "Politique",
        "subthemes": [["Education","checkbox-eduction"], 
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
        "theme": "Santé",
        "subthemes": [["Cancer", "checkbox-cancer"], 
                    ["Prévention", "checkbox-prevention"], 
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
                    ["Féminin", "checkbox-feminin"], 
                    ["Masculin", "checkbox-masculin"]]
    },
    {
        "theme": "VSS",
        "subthemes": [["Viols", "checkbox-viols"], 
                    ["Agressions sexuelles", "checkbox-agressions-sexuelles"], 
                    ["Féminicides", "checkbox-feminicides"], 
                    ["Violences conjugales", "checkbox-violences-conjugales"]]
    }
    
];


for (let value of themes) {
    let theme = value.theme.toLowerCase();
    let subThemesArray = value.subthemes;  // Utilisez un nom différent pour éviter la confusion
    let theme_checkbox = document.getElementById('checkbox-' + theme);
    if (theme_checkbox) {
        theme_checkbox.addEventListener('change', function() {
            let subthemesElement = document.getElementById('subthemes');  // Élément DOM pour les sous-thèmes
            if (this.checked) {
                for (let subTheme of subThemesArray) {  // Parcourir l'array des sous-thèmes
                    let button = document.createElement('label');
                    button.className = 'checkbox-as-button subtheme-button-' + theme;
                    let subtheme_id = subTheme[1];
                    button.innerHTML = '<input type="checkbox" id="'+ subtheme_id +'" ><span class="checkbox-button-top">' + subTheme[0] + '</span>';
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


function secureSubmit() {
        var checkbox_sport = document.getElementById('checkbox-sport');
        // Sélectionnez les checkboxes par leurs identifiants
        var checkbox1 = document.getElementById('checkbox-feminin');
        var checkbox2 = document.getElementById('checkbox-masculin');
    
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

    }};


  
// Attacher un gestionnaire d'événements au bouton de soumission
document.getElementById("submit-form").addEventListener("click", function() {
    // Récupérer l'élément du formulaire
    var formulaire2 = document.getElementById("themes-form");
    // Soumettre le formulaire
    test = secureSubmit();
    if (test) {
        formulaire2.submit();
        console.log("Formulaire soumis !")
    }
    else 
        event.preventDefault();
  });
  