export default function JourneyPage() {
  return (
    <div className="page timeline-page">
      <section className="journey-section" aria-labelledby="journey-title">
        <div className="timeline-heading">
          <p className="eyebrow">Bab / Journey</p>
          <h1 id="journey-title">Our little<br /><em>timeline.</em></h1>
        </div>
        <div className="timeline-list journey-list">
          <article className="timeline-item"><time>Chapter 01</time><div><h2>The beginning</h2><p>Add a date or place</p><span>A template for the first memory, first conversation, or first moment worth keeping.</span></div></article>
          <article className="timeline-item"><time>Chapter 02</time><div><h2>A favorite memory</h2><p>Add a date or place</p><span>Use this space for a small story, an inside joke, or a day you want to remember.</span></div></article>
          <article className="timeline-item"><time>Chapter 03</time><div><h2>What&apos;s next</h2><p>Still being written</p><span>The next part is intentionally open.</span></div></article>
        </div>
      </section>
    </div>
  );
}
