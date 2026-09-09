export default function ExperiencePage() {
  return (
    <div className="page timeline-page">
      <section className="timeline-section" aria-labelledby="experience-title">
        <div className="timeline-heading">
          <p className="eyebrow">Portfolio / Experience</p>
          <h1 id="experience-title">
            Things I&apos;ve<br /><em>worked on.</em>
          </h1>

          <a
            className="section-link experience-resume-link"
            href="/documents/anton-joseph-cruz-resume.pdf"
            target="_blank"
            rel="noreferrer"
          >
            View resume <span>↗</span>
          </a>
        </div>

        <div className="experience-timeline">

          {/* Work Experience */}
          <div className="timeline-category">
            <div className="timeline-category-heading">
              <p className="eyebrow">Work Experience</p>
            </div>

            <div className="timeline-list">
              <article className="timeline-item">
                <time>2026 — Present</time>
                <div>
                  <h2>Technology Development Program Associate</h2>
                  <p>Optum / Cebu City</p>
                  <span>
                    Part of Optum&apos;s Technology Development Program,
                    beginning with a one-month bootcamp followed by a full year
                    of real-world project experience. Currently in my first
                    rotation in mobile development, with my current task
                    focused on automation.
                  </span>
                </div>
              </article>

              <article className="timeline-item">
                <time>2025 — 2026</time>
                <div>
                  <h2>Associate Software Engineer</h2>
                  <p>Accenture / Cebu City</p>
                  <span>
                    Completed a PeopleSoft bootcamp and contributed to project
                    deployment, technical support, incident analysis, automation,
                    and instructor support.
                  </span>
                </div>
              </article>
            </div>
          </div>

          {/* School Experience */}
          <div className="timeline-category school-experience">
            <div className="timeline-category-heading">
              <p className="eyebrow">School Experience</p>
            </div>

            <div className="timeline-list">
              <article className="timeline-item">
                <time>2025</time>
                <div>
                  <h2>On-the-Job Training Intern</h2>
                  <p>Department of Education — Cebu Province</p>
                  <span>
                    Worked as a project manager, full-stack developer, UI/UX
                    designer, and deployment lead, helping manage the project
                    throughout its development and implementation.
                  </span>
                </div>
              </article>

              <article className="timeline-item">
                <time>2024 — 2025</time>
                <div>
                  <h2>Capstone and Research 1 &amp; 2</h2>
                  <p>Cebu Institute of Technology - University</p>
                  <span>
                    Served as a leader, full-stack developer, and UI/UX
                    designer, working through the complete development and
                    research process from planning and design to implementation
                    and deployment.
                  </span>
                </div>
              </article>

              <article className="timeline-item">
                <time>2021 — 2025</time>
                <div>
                  <h2>Bachelor of Science in Information Technology</h2>
                  <p>Cebu Institute of Technology - University</p>
                  <span>
                    Built a strong foundation in software development, web
                    development, databases, UI/UX design, systems analysis,
                    project development, and information technology research.
                  </span>
                </div>
              </article>

              <article className="timeline-item">
                <time>2019 — 2021</time>
                <div>
                  <h2>
                    Technical-Vocational-Livelihood (TVL) -
                    Information and Communication Technology
                  </h2>
                  <p>Asian College of Technology - IEF</p>
                  <span>
                    Completed the Information and Communication Technology
                    strand with Honors and earned NC II certification in
                    Animation.
                  </span>
                </div>
              </article>
            </div>
          </div>

        </div>
      </section>
    </div>
  );
}