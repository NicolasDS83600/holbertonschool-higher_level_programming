const red_class = document.querySelector("#red_header");

red_class.addEventListener ("click", () => {
    const header = document.querySelector("header");
    header.classList.add("red");
});