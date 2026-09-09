import Link from "next/link";

export default function ProfilePage() {
  return (
    <div className="page profile-page">
      <section className="profile-hero" aria-labelledby="profile-title">
        <div className="portrait-wrap reveal-up">
          <div className="portrait" role="img" aria-label="Portrait of Anton Joseph Cruz">
            <img src="/profile.jpg" alt="Anton Joseph Cruz" />
          </div>
        </div>
        <div className="profile-copy reveal-up">
          <p className="eyebrow">Portfolio / Profile</p>
          <h1 id="profile-title">Anton Joseph<br /><span>Cruz</span></h1>
          <h2>Software Engineer</h2>
          <p className="hero-intro">Passionate software engineer exploring the world of technology.</p>
          <div className="profile-links">
            <div><p className="profile-label">Social media</p><div className="social-links"><a href="#" aria-label="Facebook">fb</a><a href="#" aria-label="Instagram">ig</a><a href="#" aria-label="GitHub">gh</a><a href="#" aria-label="LinkedIn">in</a></div></div>
            <div><p className="profile-label">Resume</p><a className="resume-link" href="#" aria-label="Download resume">↓</a></div>
          </div>
        </div>
      </section>
      <Link className="profile-blog-link" href="/blog">Read the blog <span>↗</span></Link>
    </div>
  );
}