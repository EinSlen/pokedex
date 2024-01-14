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


        // Fonction pour obtenir les favoris depuis le stockage local
        function getFavoritesFromLocalStorage() {
            var favorites = localStorage.getItem('favorites');
            return favorites ? JSON.parse(favorites) : [];
        }

        // Fonction pour mettre à jour les favoris dans le stockage local
        function updateFavoritesInLocalStorage(favorites) {
            localStorage.setItem('favorites', JSON.stringify(favorites));
        }

        function addToFavorites(pokemonName) {
            var favoritesList = document.getElementById('favorites-list');
            var listItem = document.createElement('li');
            listItem.appendChild(document.createTextNode(pokemonName));
            favoritesList.appendChild(listItem);

            var addButton = document.getElementById('add-to-favorites-btn');
            if (addButton) {
                addButton.innerHTML = '<i class="fas fa-star"></i>';
                addButton.id = 'remove-from-favorites-btn';
                addButton.onclick = function () {
                    removeFromFavorites(pokemonName);
                };

                // Mettre à jour les favoris dans le stockage local
                var favorites = getFavoritesFromLocalStorage();
                favorites.push(pokemonName);
                updateFavoritesInLocalStorage(favorites);
            }
        }

        function removeFromFavorites(pokemonName) {
            var favoritesList = document.getElementById('favorites-list');
            var listItems = favoritesList.getElementsByTagName('li');

            for (var i = 0; i < listItems.length; i++) {
                if (listItems[i].textContent === pokemonName) {
                    favoritesList.removeChild(listItems[i]);
                    break;
                }
            }

            var removeButton = document.getElementById('remove-from-favorites-btn');
            if (removeButton) {
                removeButton.innerHTML = '<i class="fas fa-star"></i>';
                removeButton.id = 'add-to-favorites-btn';
                removeButton.onclick = function () {
                    addToFavorites(pokemonName);
                };

                // Mettre à jour les favoris dans le stockage local
                var favorites = getFavoritesFromLocalStorage();
                var index = favorites.indexOf(pokemonName);
                if (index !== -1) {
                    favorites.splice(index, 1);
                    updateFavoritesInLocalStorage(favorites);
                }
            }
        }

        // Charger les favoris au chargement de la page
        window.onload = function () {
            var favorites = getFavoritesFromLocalStorage();
            var favoritesList = document.getElementById('favorites-list');

            for (var i = 0; i < favorites.length; i++) {
                var listItem = document.createElement('li');
                listItem.appendChild(document.createTextNode(favorites[i]));
                favoritesList.appendChild(listItem);
            }
        };

        function resetFavorites() {
            var favoritesList = document.getElementById('favorites-list');
            favoritesList.innerHTML = ''; // Efface tous les éléments de la liste

            // Réinitialiser le stockage local à un tableau vide
            updateFavoritesInLocalStorage([]);

            var addButton = document.getElementById('add-to-favorites-btn');
            if (addButton) {
                addButton.innerHTML = '<i class="fas fa-star"></i>';
                addButton.id = 'add-from-favorites-btn';
                addButton.onclick = function () {
                    var pokemonName = document.querySelector('input[name="name"]').value;
                    addToFavorites(pokemonName);
                };
            }
        }