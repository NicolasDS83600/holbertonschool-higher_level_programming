const update = document.querySelector ("#update_header");

update.addEventListener ("click", () => {
    const header = document.querySelector ("header");
    header.textContent = "New Header!!!";
});