"use client";

import { useEffect, useState } from "react";

type Theme = "system" | "dark" | "light";

export default function ThemeSwitcher() {
  const [theme, setTheme] = useState<Theme>("system");

  useEffect(() => {
    const savedTheme = window.localStorage.getItem("theme") as Theme | null;
    if (savedTheme === "dark" || savedTheme === "light" || savedTheme === "system") {
      setTheme(savedTheme);
      applyTheme(savedTheme);
    }
  }, []);

  function chooseTheme(nextTheme: Theme) {
    setTheme(nextTheme);
    window.localStorage.setItem("theme", nextTheme);
    applyTheme(nextTheme);
  }

  return (
    <div className="theme-switcher" aria-label="Color theme">
      {(["system", "dark", "light"] as Theme[]).map((option) => (
        <button className={theme === option ? "active" : ""} key={option} onClick={() => chooseTheme(option)} type="button">
          {option}
        </button>
      ))}
    </div>
  );
}

function applyTheme(theme: Theme) {
  if (theme === "system") document.documentElement.removeAttribute("data-theme");
  else document.documentElement.dataset.theme = theme;
}