(function() {
    'use strict';
    const form = document.getElementById('form');

    function request(url) {
        return fetch(url).then(response => response.json());
    }

    function change_list_content(list, element) {
        const li = list.reduce((elements, value) => {
            return elements + `<li>${value}</li>`;
        }, "");
        element.innerHTML = li;
    }

    function change_explication_content(neighbors) {
        //const explication_text = document.getElementById('explication_text');
        const neighbors_element = document.getElementById('users');
        const explication = "Você recebeu essas recomendações de filmes de acordo "
                        + "com a nota que outros usuários que tem perfis "
                        + "similares a seu atribuiram a filme. "
                        + "Os filmes recomendados são os que possuem as maiores notas "
                        + "atribuidas por estes usuários. "
                        + "Os 5 usuários com perfis mais similares estão listados abaixo:";
        
        explication_text.innerText = explication;
        change_list_content(neighbors, neighbors_element);
    }

    function get_results() {
        const movies = document.getElementById('movies');
        const user = document.getElementById('user');
        //const rmse = document.getElementById('rmse');
        
        request(`/api/results?uid=${form.User.value}`).then(data => {
            change_list_content(data.movies, movies);
            //change_list_content(data.users, users);
            //rmse_knn.innerText = `RMSE: ${data.rmse.rmse_knn}`;
            //rmse_svd.innerText = `RMSE: ${data.rmse.rmse_svd}`;
            change_explication_content(data.users);
        });
        return false;
    }


    (function main() {
        form.onsubmit = get_results;
    })();
})();