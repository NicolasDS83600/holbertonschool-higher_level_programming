const red = document.querySelector('#red_header');

red.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
