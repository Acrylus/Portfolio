export default function ExperiencePage() {
  return (
    <div className="page timeline-page">
      <section className="timeline-section" aria-labelledby="experience-title">
        <div className="timeline-heading">
          <p className="eyebrow">Portfolio / Experience</p>
          <h1 id="experience-title">Things I&apos;ve<br /><em>worked on.</em></h1>
        </div>
        <div className="timeline-list">
          <article className="timeline-item"><time>2026 — Present</time><div><h2>Your next chapter</h2><p>Role or project title</p><span>Add a short description of the work, the problem, and what you learned.</span></div></article>
          <article className="timeline-item"><time>2024 — 2026</time><div><h2>Previous experience</h2><p>Company or independent work</p><span>Replace this template with a meaningful project, role, or milestone.</span></div></article>
          <article className="timeline-item"><time>Earlier</time><div><h2>Where it began</h2><p>First experiments</p><span>A place for the beginning of your story and the ideas that shaped it.</span></div></article>
        </div>
      </section>
    </div>
  );
}
