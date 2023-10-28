var startTime = localStorage.getItem('startTime');

startTime = new Date().getTime();
localStorage.setItem('startTime', startTime);
startTime = parseInt(startTime);

function updateTimer() {
  var currentTime = new Date().getTime();
  var elapsedTime = currentTime - startTime;

  var hours = Math.floor(elapsedTime / 3600000);
  var minutes = Math.floor((elapsedTime % 3600000) / 60000);
  var seconds = Math.floor((elapsedTime % 60000) / 1000);

  var timerDisplay = hours.toString().padStart(2, '0') + ":" + minutes.toString().padStart(2, '0') + ":" + seconds.toString().padStart(2, '0');
  document.getElementById('timer').textContent = timerDisplay;

  setTimeout(updateTimer, 1000); // Update the timer every second
}

// Start the timer when the page loads
window.addEventListener('load', function() {
  updateTimer();
});