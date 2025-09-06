const dropdown = document.getElementById('entity_selector');
const navigateToSelectedEntity = (e) => {
  window.location.href = '/evil/showcreature/' + e.target.value;
};

dropdown.onchange = (e) => navigateToSelectedEntity(e);
