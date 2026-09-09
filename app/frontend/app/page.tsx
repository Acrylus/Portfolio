import Link from "next/link";

export default function ProfilePage() {
  return (
    <div className="page profile-page">
      <section className="profile-hero" id="profile" aria-labelledby="profile-title">
        <div className="portrait-wrap reveal-up">
          <div className="portrait" role="img" aria-label="Portrait of Anton Joseph Cruz" />
        </div>
        <div className="profile-copy reveal-up">
          <p className="eyebrow">Profile</p>
          <h1 id="profile-title">Anton Joseph<br /><span>Cruz</span></h1>
          <h2>Software Engineer</h2>
          <p className="hero-intro">Software engineer building thoughtful digital experiences and exploring the world of technology.</p>
          <div className="profile-links">
            <div><p className="profile-label">Social media</p><div className="social-links"><a href="#" aria-label="Facebook">fb</a><a href="#" aria-label="Instagram">ig</a><a href="#" aria-label="GitHub">gh</a><a href="#" aria-label="LinkedIn">in</a></div></div>
          </div>
        </div>
      </section>
      <section className="portfolio-section" id="portfolio" aria-labelledby="portfolio-title">
        <div className="portfolio-overlay">
          <p className="eyebrow">Portfolio</p>
          <h2 id="portfolio-title">Selected work and notes.</h2>
          <Link className="section-link" href="/blog">Open blog <span>↗</span></Link>
        </div>
      </section>
    </div>
  );
}