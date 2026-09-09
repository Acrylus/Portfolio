"use client";

import { useEffect, useRef, useState } from "react";

export default function MusicPlayer() {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    audio.volume = 0.55;
    audio.play().then(() => setIsPlaying(true)).catch(() => setIsPlaying(false));
  }, []);

  async function togglePlayback() {
    const audio = audioRef.current;
    if (!audio) return;

    if (audio.paused) {
      await audio.play();
      setIsPlaying(true);
    } else {
      audio.pause();
      setIsPlaying(false);
    }
  }

  return (
    <div className="music-player">
      <audio ref={audioRef} loop onEnded={() => setIsPlaying(false)} src="/music/always-atlanticstarr.mp3" />
      <div className="record-art" aria-hidden="true"><img src="/bab.jpg" alt="" /><span>♡</span></div>
      <div className="track-details">
        <h2>Always</h2>
        <p>Atlantic Starr</p>
        <a className="spotify-link" href="https://open.spotify.com/search/Always%20Atlantic%20Starr" target="_blank" rel="noreferrer"><img src="/code/always.svg" alt="Open Always on Spotify" /></a>
        <div className="track-progress"><span /></div>
        <div className="player-controls"><button type="button" aria-label="Previous track">|◀</button><button className="play-button" type="button" onClick={togglePlayback} aria-label={isPlaying ? "Pause Always" : "Play Always"}>{isPlaying ? "Ⅱ" : "▶"}</button><button type="button" aria-label="Next track">▶|</button></div>
      </div>
    </div>
  );
}