"use client";

import Link from "next/link";
import { FormEvent } from "react";

export default function LoginPage() {
  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
  }

  return (
    <div className="page login-page">
      <div className="login-panel reveal-up">
        <p className="eyebrow">Private area</p>
        <h1>Welcome <em>back.</em></h1>
        <p className="login-copy">Sign in to access saved notes and unfinished ideas.</p>
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">Email address</label>
          <input id="email" type="email" placeholder="you@example.com" required />
          <label htmlFor="password">Password</label>
          <input id="password" type="password" placeholder="••••••••" required />
          <button className="button button-dark login-button" type="submit">Continue <span>→</span></button>
        </form>
        <p className="login-footer">New here? <Link href="/">Return to the profile</Link></p>
      </div>
      <div className="login-aside"><span className="aside-mark">A</span><p>Ideas are<br /><em>worth keeping.</em></p></div>
    </div>
  );
}