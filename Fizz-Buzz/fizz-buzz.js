function fizzBuzz() {
    const n = document.querySelector('.js-number-input').value;
    const outputDiv = document.querySelector('.js-output');
    outputDiv.innerHTML = '';

    if (n === '' || isNaN(n) || n <= 0) {
      outputDiv.innerHTML = '<p>Please enter a positive number.</p>';
      return;
    }

    for (let i = 1; i <= n; i++) {
      if (i % 5 === 0 && i % 3 === 0) {
        outputDiv.innerHTML += '<p>FizzBuzz</p>';
      } else if (i % 3 === 0) {
        outputDiv.innerHTML += '<p>Fizz</p>';
      } else if (i % 5 === 0) {
        outputDiv.innerHTML += '<p>Buzz</p>';
      } else {
        outputDiv.innerHTML += `<p>${i}</p>`;
      }
    }
}