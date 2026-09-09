import MusicPlayer from "../components/music-player";

export default function VibePage() {
  return (
    <div className="page vibe-page">
      <section className="vibe-card reveal-up" aria-labelledby="vibe-title">
        <div className="vibe-content">
          <p className="eyebrow">Vibe <span aria-hidden="true">♡</span></p>
          <h1 id="vibe-title">Always</h1>
          <MusicPlayer />
        </div>
      </section>
    </div>
  );
}