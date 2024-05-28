window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector);
      if (element) element.innerText = text;
    };
  
    for (const dependency of ['chrome', 'node', 'electron']) {
      replaceText(`${dependency}-version`, `${dependency}-version`+ process.versions[dependency]);
    }
  });

// Adding the event listener to the input field when the DOM content is loaded
window.addEventListener('DOMContentLoaded', () => {
  document.getElementById('userInput').addEventListener('input', function(event) {
    console.log(event.target.value);
  });
});
  