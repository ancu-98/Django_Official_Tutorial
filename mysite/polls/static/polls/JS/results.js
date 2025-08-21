// Calcular porcentajes y animar barras
document.addEventListener("DOMContentLoaded", function () {
  const results = document.querySelectorAll(".result-item");
  let totalVotes = 0;
  const votes = [];

  // Obtener total de votos
  results.forEach((item) => {
    const voteCount = parseInt(
      item.querySelector(".vote-progress").dataset.votes
    );
    votes.push(voteCount);
    totalVotes += voteCount;
  });

  // Calcular porcentajes y animar
  results.forEach((item, index) => {
    const voteCount = votes[index];
    const percentage =
      totalVotes > 0 ? Math.round((voteCount / totalVotes) * 100) : 0;

    const progressBar = item.querySelector(".vote-progress");
    const percentageSpan = item.querySelector(".vote-percentage");

    // Animar barra de progreso
    setTimeout(() => {
      progressBar.style.width = percentage + "%";
      percentageSpan.textContent = percentage + "%";
    }, index * 200);
  });
});
