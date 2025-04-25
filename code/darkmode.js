let darkmode = localStorage.getItem("darkmode");
const themeSwitch = document.getElementById("theme-switch");

// Ativar o darkmode
const enableDarkmode = () => {
  document.documentElement.classList.add("darkmode");
  localStorage.setItem("darkmode", "active");
};

// Desativar o darkmode
const disableDarkmode = () => {
  document.documentElement.classList.remove("darkmode");
  localStorage.setItem("darkmode", null);
};

// Se darkmode estava ativo antes, manter
if (darkmode === "active") enableDarkmode();

// Evento de clique no botão
themeSwitch.addEventListener("click", () => {
  darkmode = localStorage.getItem("darkmode");
  darkmode !== "active" ? enableDarkmode() : disableDarkmode();
});
