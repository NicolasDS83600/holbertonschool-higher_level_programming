const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', () => {
  const list = document.createElement('li');
  list.textContent = 'Item';

  const parent = document.querySelector('.my_list');
  parent.appendChild(list);
});
