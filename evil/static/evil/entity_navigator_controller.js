const dropdown = document.getElementById('entity_selector');
const navigateToSelectedEntity = (e) => {
  console.log(e);
  window.location.href = '/evil/showcreature/' + e.target.value;
};

dropdown.onchange = (e) => navigateToSelectedEntity(e);
