function verif1(){
    let num = document.getElementById("numPermis");
    let num1 = num.substring(0, 3);
    let num_symbol = num.substring(3);
    let num2 = num.substring(4, num.length);

    if (num_symbol != "/" || !("01" <= num1<= "99") || !("0001"<=  num2 <= "9999")){
        alert("Une chaîne de 8 caractères respectant le format suivant : xx/xxxxx  (où chaque x représente un chiffre).");
        return false;
    } 
    let Nom = document.getElementById("nom");
    if (!(3 <= Nom.length <= 20)){
        alert("Une chaîne alphabétique ayant une longueur comprise entre 3 et 20.");
        return false;
    }
    let Prenom = document.getElementById("prenom");
    if (!(3 <= Prenom.length <= 20)){
        alert("Une chaîne alphabétique ayant une longueur comprise entre 3 et 20.");
        return false;
    }
    let genre = document.querySelector('input[name="genre"]:checked');
    if (!(genre)){
        alert("La sélection d’un genre est obligatoire.  ");
        return false;
    }
    return true;
}

function verif2(){
    let num = document.getElementById("numPermis");
    let num1 = num.substring(0, 3);
    let num_symbol = num.substring(3);
    let num2 = num.substring(4, num.length);

    if (num_symbol != "/" || !("01" <= num1<= "99") || !("0001"<=  num2 <= "9999")){
        alert("Une chaîne de 8 caractères respectant le format suivant : xx/xxxxx  (où chaque x représente un chiffre).");
        return false;
    }
    let modele = document.getElementById("idModele")
    if (modele == ""){
        alert("La sélection d’un modèle est obligatoire.")
        return false
    }
    let securite = document.getElementById("securite")
    if (!(1<= securite <= 5)){
        alert("Un entier entre 1 et 5.")
        return false
    }
    let conduite = document.getElementById("conduite")
    if (!(1<= conduite <= 5)){
        alert("Un entier entre 1 et 5.")
        return false
    } 
    let confort = document.getElementById("confort")
    if (!(1<= confort <= 5)){
        alert("Un entier entre 1 et 5.")
        return false
    } 
}