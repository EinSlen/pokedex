// Fichier app.js
document.addEventListener('DOMContentLoaded', function () {
    var shineyButton = document.getElementById('shiny-button');
    var pokemonImage = document.querySelector('.pokemon-image');

    shineyButton.addEventListener('click', function () {
        // Changez l'attribut 'src' de l'image en fonction du bouton
        if (pokemonImage.getAttribute('src') === regularImage) {
            pokemonImage.setAttribute('src', shinyImage);
        } else {
            pokemonImage.setAttribute('src', regularImage);
        }
    });
});
