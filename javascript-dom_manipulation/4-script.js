const add_item = document.querySelector ("#add_item");

add_item.addEventListener ("click", () =>{
    const list = document.createElement("li");
    list.textContent = "Item";

    const parent = document.querySelector(".my_list"); 
    parent.appendChild(list);
});