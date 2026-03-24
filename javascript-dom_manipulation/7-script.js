const title = document.querySelector ("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(response => response.json())
.then(data => data.results.forEach(film => {
    const list = document.createElement ("li");

    list.textContent = film.title;
    title.appendChild(list);
}));