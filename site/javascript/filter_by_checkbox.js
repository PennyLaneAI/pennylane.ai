// inspired by https://codepen.io/piotrek/pen/mXpRmQ

var allCheckboxes = document.querySelectorAll('input[type=checkbox]');
var allPlayers = Array.from(document.querySelectorAll('.device'));
var checked = {};

getChecked('plugin');
getChecked('model');
getChecked('mode');

Array.prototype.forEach.call(allCheckboxes, function (el) {
  el.addEventListener('change', toggleCheckbox);
});

function toggleCheckbox(e) {
  getChecked(e.target.name);
  setVisibility();
}

function getChecked(name) {
  checked[name] = Array.from(document.querySelectorAll('input[name=' + name + ']:checked')).map(function (el) {
    return el.value;
  });
}

function setVisibility() {
  allPlayers.map(function (el) {
    var plugin = checked.plugin.length ? _.intersection(Array.from(el.classList), checked.plugin).length : true;
    var model = checked.model.length ? _.intersection(Array.from(el.classList), checked.model).length : true;
    var mode = checked.mode.length ? _.intersection(Array.from(el.classList), checked.mode).length : true;
    if (plugin && model && mode) {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
  });
}
