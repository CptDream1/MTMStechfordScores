const form = document.getElementById('scoreForm');
const scoreList = document.getElementById('scoreList');
const allScores = [];

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('studentName').value.trim();
  const counts = {
    purple: parseInt(document.getElementById('purple').value) || 0,
    orange: parseInt(document.getElementById('orange').value) || 0,
    green: parseInt(document.getElementById('green').value) || 0,
    blue: parseInt(document.getElementById('blue').value) || 0,
    pink: parseInt(document.getElementById('pink').value) || 0,
    gold: parseInt(document.getElementById('gold').value) || 0,
  };

  const score = (counts.purple * 3) +
                (counts.orange * 4) +
                (counts.green * 5) +
                (counts.blue * 1) +
                (counts.pink * 2) +
                (counts.gold * 10);

  allScores.push({ name, score });
  updateScoreList();

  form.reset();
});

function updateScoreList() {
  scoreList.innerHTML = '';
  allScores.forEach(student => {
    const li = document.createElement('li');
    li.textContent = `${student.name}: ${student.score}`;
    scoreList.appendChild(li);
  });
}