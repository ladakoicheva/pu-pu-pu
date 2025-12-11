const button = document.querySelector(".btn ");

button.addEventListener('click', () => {
  const div = document.createElement('div');//<div></div>
  div.classList.add('img');//<div class="img"></div>
  document.body.appendChild(div);//добавили в боди
  const img = document.createElement('img');//<img>
  img.setAttribute('src', "/img/cat_or_dog_1.jpg");//<img src="/img/cat_or_dog_1.jpg">

  div.appendChild(img);//добавили в див

})

