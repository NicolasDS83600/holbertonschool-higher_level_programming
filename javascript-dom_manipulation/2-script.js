const redClass = document.querySelector('#red_header');

redClass.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.classList.add('red');
});
