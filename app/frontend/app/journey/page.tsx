export default function JourneyPage() {
  return (
    <div className="page timeline-page">
      <section className="journey-section" aria-labelledby="journey-title">
        <div className="timeline-heading">
          <p className="eyebrow">Bab / Journey</p>
          <h1 id="journey-title">
            Our little<br /><em>timeline.</em>
          </h1>
        </div>

        <div className="timeline-list journey-list">
          <article className="timeline-item">
            <time>18 July 2026</time>
            <div>
              <h2>The first hello</h2>
              <p>Where our story quietly began</p>
              <span>
                It started with a simple “Hello.” I replied to her PopUp
                status asking about age and location, saying, “24, Cebu.”
                She replied, “24, Banawa,” and then asked, “ikaw asa ka
                dapita sa Cebu?” It was just a small conversation at the
                time, but it would become the beginning of something much
                more meaningful.
              </span>
            </div>
          </article>

          <article className="timeline-item">
            <time>08 August 2026</time>
            <div>
              <h2>Infinity, made official</h2>
              <p>The day we became us</p>
              <span>
                On August 8, we officially became a couple. The date felt
                meant to be—the number 8 resembles infinity, and January 8
                is also her birthday. She answered me with a poem, making
                the day even more special and giving our new chapter a
                beautiful beginning.
              </span>
            </div>
          </article>

          <article className="timeline-item">
            <time>08 September 2026</time>
            <div>
              <h2>Our first monthsary</h2>
              <p>A month worth remembering</p>
              <span>
                We celebrated our first monthsary by giving gifts to each
                other and looking back on the story we had started only a
                month before. She also made a video about our story
                together—a little piece of our memories that we can keep
                and look back on someday.
              </span>
            </div>
          </article>
        </div>
      </section>
    </div>
  );
}