import type { Metadata } from "next";
import Link from "next/link";
import ThemeSwitcher from "./components/theme-switcher";
import "./globals.scss";

export const metadata: Metadata = {
  title: "Acrylus | Creative technologist",
  description: "The personal portfolio and notebook of Acrylus.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>
        <aside className="site-sidebar">
          <Link className="wordmark" href="/" aria-label="Acrylus home">
            <span>acrylus</span>
            <span className="wordmark-email">Anton Joseph Cruz</span>
          </Link>
          <nav className="nav-links" aria-label="Main navigation">
            <div className="nav-group">
              <a href="/#portfolio">Portfolio</a>
              <Link href="/blog">Blog</Link>
              <Link href="/experience">Experience</Link>
            </div>
            <div className="nav-group">
              <a href="/vibe">Bab <span aria-hidden="true">♡</span></a>
              <Link href="/vibe">Vibe</Link>
              <Link href="/journey">Journey</Link>
            </div>
          </nav>
          <div className="sidebar-bottom">
            <p className="sidebar-name">antonjosephcruz@gmail.com</p>
            <ThemeSwitcher />
          </div>
        </aside>
        <main className="site-main">{children}</main>
      </body>
    </html>
  );
}