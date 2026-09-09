import Link from "next/link";

const posts = [
  { date: "08 Sep 2026", type: "Field note", title: "Making room for the first draft", excerpt: "A small argument for shipping the version that teaches you something.", accent: "mint" },
  { date: "21 Aug 2026", type: "On building", title: "The shape of a good question", excerpt: "Before the roadmap, there is usually a better question hiding nearby.", accent: "coral" },
  { date: "03 Jul 2026", type: "Field note", title: "Interfaces with a pulse", excerpt: "Some thoughts on warmth, restraint, and making software feel human.", accent: "yellow" },
];

export default function BlogPage() {
  return (
    <div className="page blog-page">
      <section className="blog-heading reveal-up">
        <p className="eyebrow">The notebook / 001</p>
        <h1>Notes from<br /><em>the in-between.</em></h1>
        <p className="blog-deck">Ideas, experiments, and observations from a life spent making things for the web.</p>
        <img className="blog-cover" src="/bab.jpg" alt="Night street photographs and shadows" />
      </section>
      <section className="post-list" aria-label="Blog posts">
        {posts.map((post, index) => (
          <article className="post-row" key={post.title}>
            <div className={`post-number ${post.accent}`}>{String(index + 1).padStart(2, "0")}</div>
            <div className="post-meta"><span>{post.type}</span><time>{post.date}</time></div>
            <div className="post-content"><h2>{post.title}</h2><p>{post.excerpt}</p></div>
            <Link className="post-arrow" href="#" aria-label={`Read ${post.title}`}>↗</Link>
          </article>
        ))}
      </section>
    </div>
  );
}