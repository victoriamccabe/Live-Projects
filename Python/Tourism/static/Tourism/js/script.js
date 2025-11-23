

document.addEventListener('DOMContentLoaded', function () {
  const input = document.getElementById('search-input');
  const suggestionsBox = document.getElementById('suggestions');

  if (!input || !suggestionsBox) {
    // Elements not found, do nothing to avoid errors
    return;
  }

  input.addEventListener('input', function () {
    const query = input.value;

    if (query.length === 0) {
      suggestionsBox.innerHTML = '';
      return;
    }

    fetch(`/live-search/?q=${encodeURIComponent(query)}`)
      .then(response => response.json())
      .then(data => {
        console.log('Results:', data);  // Debug
        suggestionsBox.innerHTML = '';
        data.forEach(item => {
          const div = document.createElement('div');
          div.textContent = item.place_name;
          div.classList.add('suggestion-item');
          div.addEventListener('click', function () {
            input.value = item.place_name;
            suggestionsBox.innerHTML = '';
          });
          suggestionsBox.appendChild(div);
        });
      })
      .catch(error => console.error('Fetch error:', error));
  });
});


// Loading spinner
