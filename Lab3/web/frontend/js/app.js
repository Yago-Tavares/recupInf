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
        const neighbors_element = document.getElementById('users');
        change_list_content(neighbors, neighbors_element);
    }

    function get_results() {
        const movies = document.getElementById('movies');
        const users = document.getElementById('users');
        const rmse = document.getElementById('rmse');
        
        request(`/api/results?uid=${form.User.value}`).then(data => {
            change_list_content(data.movies, movies);
            rmse.innerText = `RMSE: ${data.rmse}`;
            change_list_content(data.users, users);
        });
        return false;
    }


    (function main() {
        form.onsubmit = get_results;
    })();
})();