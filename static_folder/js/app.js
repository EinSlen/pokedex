// Fichier app.js
document.addEventListener('DOMContentLoaded', function () {
    var shineyButton = document.getElementById('shiny-button');
    var pokemonImage = document.querySelector('.pokemon-image');

    shineyButton.addEventListener('click', function () {
        if (pokemonImage.getAttribute('src') === regularImage) {
            pokemonImage.setAttribute('src', shinyImage);
            shineyButton.textContent = "⚫";
        } else {
            pokemonImage.setAttribute('src', regularImage);
             shineyButton.textContent = "✨";
        }
    });
});

