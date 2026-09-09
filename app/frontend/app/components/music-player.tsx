"use client";

import { useEffect, useRef, useState } from "react";

export default function MusicPlayer() {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    audio.volume = 0.55;
    audio.play().then(() => setIsPlaying(true)).catch(() => setIsPlaying(false));
    const updateProgress = () => setProgress(audio.duration ? (audio.currentTime / audio.duration) * 100 : 0);
    audio.addEventListener("timeupdate", updateProgress);
    audio.addEventListener("loadedmetadata", updateProgress);
    return () => {
      audio.removeEventListener("timeupdate", updateProgress);
      audio.removeEventListener("loadedmetadata", updateProgress);
    };
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

  function seek(event: React.MouseEvent<HTMLDivElement>) {
    const audio = audioRef.current;
    if (!audio || !audio.duration) return;
    const bounds = event.currentTarget.getBoundingClientRect();
    audio.currentTime = ((event.clientX - bounds.left) / bounds.width) * audio.duration;
  }

  return (
    <div className="music-player">
      <audio ref={audioRef} loop onEnded={() => setIsPlaying(false)} src="/music/always-atlanticstarr.mp3" />
      <div className="record-art" aria-hidden="true"><img src="/bab.jpg" alt="" /><span>♡</span></div>
      <div className="track-details">
        <h2>Always</h2>
        <p>Atlantic Starr</p>
        <a className="spotify-link" href="https://open.spotify.com/search/Always%20Atlantic%20Starr" target="_blank" rel="noreferrer"><img src="/code/always.svg" alt="Open Always on Spotify" /></a>
        <div className="track-progress" onClick={seek} role="slider" aria-label="Track progress" aria-valuemin={0} aria-valuemax={100} aria-valuenow={Math.round(progress)} tabIndex={0}><span style={{ width: `${progress}%` }} /></div>
        <div className="player-controls"><button type="button" aria-label="Previous track">|◀</button><button className="play-button" type="button" onClick={togglePlayback} aria-label={isPlaying ? "Pause Always" : "Play Always"}>{isPlaying ? "Ⅱ" : "▶"}</button><button type="button" aria-label="Next track">▶|</button></div>
      </div>
    </div>
  );
}