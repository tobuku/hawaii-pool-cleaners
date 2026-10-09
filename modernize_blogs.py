"""
Modernize WordPress blog posts to match the site's modern template.
Extracts article content from old WP HTML, wraps in clean modern design.
"""
import os, re, glob, html

BLOG_POSTS = [
    "the-benefits-of-having-a-clean-pool-for-your-health",
    "the-dangers-of-neglecting-regular-pool-maintenance",
    "securing-your-pool-saves-lives",
    "the-cost-savings-of-a-well-maintained-pool",
    "how-to-find-a-quality-pool-maintenance-company",
    "the-importance-of-cleaning-pool-surfaces-to-prevent-algae-growth",
    "the-role-of-pool-maintenance-in-preserving-the-aesthetic-of-your-pool",
    "the-impact-of-pool-maintenance-on-the-lifespan-of-pool-equipment",
    "vinyl-pools-in-hawaii",
    "your-trusted-pool-cleaning-service-hawaii",
]

# Also handle the huge filtration-system post
LONG_SLUG = "numerous-health-and-environmental-benefits-of-proper-upkeep-and-maintenance-of-your-residential-or-commercial-pool-filtration-system"
if os.path.exists(f"{LONG_SLUG}/index.html"):
    BLOG_POSTS.append(LONG_SLUG)


def extract_meta(content):
    """Extract title, description, canonical, image, and date from WP HTML."""
    title_m = re.search(r"<title>(.*?)</title>", content)
    title = title_m.group(1).replace(" - Hawaii Pool Cleaners", "").strip() if title_m else "Blog Post"

    desc_m = re.search(r'<meta name="description" content="(.*?)"', content)
    desc = desc_m.group(1) if desc_m else ""

    canon_m = re.search(r'<link rel="canonical" href="(.*?)"', content)
    canonical = canon_m.group(1) if canon_m else ""

    # Get OG image (may be relative)
    img_m = re.search(r'<meta property="og:image" content="(.*?)"', content)
    og_image = img_m.group(1) if img_m else ""
    if og_image and not og_image.startswith("http"):
        og_image = "https://hawaiipoolcleaners.com" + og_image

    # Get featured image from post content
    feat_m = re.search(r'post-thumb-img-content.*?src="(.*?)"', content, re.DOTALL)
    feat_image = feat_m.group(1) if feat_m else ""

    # Get date
    date_m = re.search(r'datePublished.*?>\s*(\w+ \d+, \d{4})', content)
    pub_date = date_m.group(1).strip() if date_m else ""

    # Get ISO date
    iso_m = re.search(r'article:published_time" content="(.*?)"', content)
    iso_date = iso_m.group(1) if iso_m else ""

    return title, desc, canonical, og_image, feat_image, pub_date, iso_date


def extract_body(content):
    """Extract article body content from WordPress HTML."""
    # Find entry-content div
    body_m = re.search(
        r'<div class="entry-content clear"[^>]*>(.*?)(?:</div><!-- \.entry-content|<div class="hpc-post-cta">)',
        content, re.DOTALL
    )
    if not body_m:
        # Fallback: try to find content between entry-content and the CTA
        body_m = re.search(r'itemprop="text">(.*?)<div class="hpc-post-cta">', content, re.DOTALL)
    if not body_m:
        return "<p>Content not found.</p>"

    body = body_m.group(1).strip()

    # Clean up whitespace
    body = re.sub(r'\n\s*\n\s*\n', '\n\n', body)
    body = body.strip()

    return body


def build_modern_page(slug, title, desc, canonical, og_image, feat_image, pub_date, iso_date, body):
    """Build a modern blog post page matching site design."""
    # Use feat_image or fallback
    hero_img = feat_image if feat_image else "/wp-content/uploads/2025/04/pexels-photo-261152.jpeg"

    # Make sure canonical is absolute
    if canonical and not canonical.startswith("http"):
        canonical = "https://hawaiipoolcleaners.com" + canonical

    # OG image fallback
    if not og_image:
        og_image = "https://hawaiipoolcleaners.com/wp-content/uploads/2024/06/Hawaii-Pool-Cleaners-Logo.jpg"

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8JJP16T6L4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-8JJP16T6L4');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} | Hawaii Pool Cleaners</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)} | Hawaii Pool Cleaners">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)} | Hawaii Pool Cleaners">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{og_image}">
<link rel="canonical" href="{canonical}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{html.escape(title)}","description":"{html.escape(desc)}","url":"{canonical}","image":"{og_image}","datePublished":"{iso_date}","author":{{"@type":"Organization","name":"Hawaii Pool Cleaners","url":"https://hawaiipoolcleaners.com"}},"publisher":{{"@type":"Organization","name":"Hawaii Pool Cleaners","url":"https://hawaiipoolcleaners.com","logo":{{"@type":"ImageObject","url":"https://hawaiipoolcleaners.com/wp-content/uploads/2024/06/Hawaii-Pool-Cleaners-Logo.jpg"}}}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://hawaiipoolcleaners.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://hawaiipoolcleaners.com/blog/"}},{{"@type":"ListItem","position":3,"name":"{html.escape(title)}"}}]}}
</script>
<link rel="icon" href="/wp-content/uploads/2024/06/cropped-Hawaii-Pool-Cleaners-Logo-192x192.jpg" sizes="192x192">
<link rel="apple-touch-icon" href="/wp-content/uploads/2024/06/cropped-Hawaii-Pool-Cleaners-Logo-192x192.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>
:root{{--teal:#00D082;--navy:#0a1628;--mid:#1a3a5c;--lteal:#7adcb4;--white:#ffffff;--lgray:#f8fafc;--muted:#4a6080;--shadow:0 8px 40px rgba(0,0,0,.12)}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;font-size:16px}}
body{{font-family:'Libre Franklin',sans-serif;font-weight:400;line-height:1.65;color:var(--navy);background:var(--white);overflow-x:hidden;cursor:default}}
a,button{{cursor:pointer}}
.nav{{position:fixed;top:0;left:0;right:0;z-index:1000;padding:20px 48px;display:flex;align-items:center;justify-content:space-between;transition:all .4s ease;background:rgba(10,22,40,.92);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid rgba(0,208,130,.12)}}
.nav-logo{{display:flex;align-items:center;gap:12px;text-decoration:none}}
.nav-logo img{{height:52px;width:52px;object-fit:contain;border-radius:4px}}
.nav-logo-text{{font-size:1rem;font-weight:700;color:#fff;line-height:1.2;letter-spacing:-.02em}}
.nav-logo-text span{{display:block;font-size:.62rem;font-weight:400;color:var(--lteal);letter-spacing:.14em;text-transform:uppercase}}
.nav-links{{display:flex;align-items:center;gap:32px;list-style:none}}
.nav-links a{{color:rgba(255,255,255,.82);text-decoration:none;font-size:.82rem;font-weight:500;letter-spacing:.06em;text-transform:uppercase;position:relative;transition:color .3s}}
.nav-links a::after{{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--teal);transition:width .3s}}
.nav-links a:hover{{color:var(--teal)}}
.nav-links a:hover::after{{width:100%}}
.nav-cta{{white-space:nowrap!important;background:var(--teal)!important;color:var(--navy)!important;padding:10px 26px!important;border-radius:50px!important;font-weight:700!important;transition:background .3s,transform .3s,box-shadow .3s!important}}
.nav-cta::after{{display:none!important}}
.nav-cta:hover{{background:var(--lteal)!important;transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(0,208,130,.4)!important}}
.nav-toggle{{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;padding:6px;cursor:pointer;z-index:1002;flex-shrink:0}}
.nav-toggle span{{display:block;width:24px;height:2px;background:#fff;border-radius:2px;transition:transform .3s,opacity .3s}}
.nav-toggle.open span:nth-child(1){{transform:translateY(7px) rotate(45deg)}}
.nav-toggle.open span:nth-child(2){{opacity:0}}
.nav-toggle.open span:nth-child(3){{transform:translateY(-7px) rotate(-45deg)}}
.nav-mobile{{position:fixed;inset:0;background:rgba(10,22,40,.97);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);z-index:1001;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:translateX(100%);transition:transform .4s cubic-bezier(.77,0,.18,1);pointer-events:none}}
.nav-mobile.open{{transform:translateX(0);pointer-events:all}}
.nav-mobile-links{{list-style:none;display:flex;flex-direction:column;align-items:center;gap:0;width:100%;padding:0 24px;margin-bottom:36px}}
.nav-mobile-links li{{width:100%;text-align:center;border-bottom:1px solid rgba(255,255,255,.07)}}
.nav-mobile-links li:first-child{{border-top:1px solid rgba(255,255,255,.07)}}
.nav-mobile-links a{{display:block;padding:22px 16px;color:rgba(255,255,255,.85);text-decoration:none;font-size:1rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;transition:color .2s}}
.nav-mobile-links a:hover{{color:var(--teal)}}
.mobile-cta-btn{{display:inline-block;background:var(--teal);color:var(--navy)!important;text-decoration:none;font-weight:800;font-size:.88rem;letter-spacing:.1em;text-transform:uppercase;padding:16px 44px;border-radius:50px;transition:background .3s}}
.mobile-cta-btn:hover{{background:var(--lteal)}}

/* PAGE HERO */
.page-hero{{padding:140px 40px 80px;background:linear-gradient(135deg,var(--navy) 0%,#0d2245 60%,#0e2a1e 100%);text-align:center;position:relative;overflow:hidden}}
.page-hero::before{{content:'';position:absolute;top:-80px;right:-80px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(0,208,130,.07),transparent 70%);pointer-events:none}}
.eyebrow{{font-size:.7rem;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--teal);margin-bottom:14px;display:block}}
.page-hero h1{{font-size:clamp(1.6rem,3.5vw,2.6rem);font-weight:800;color:#fff;letter-spacing:-.035em;line-height:1.15;margin-bottom:18px;max-width:720px;margin-left:auto;margin-right:auto}}
.page-hero .date{{font-size:.85rem;color:rgba(255,255,255,.45);margin-top:8px}}

/* ARTICLE */
.article-section{{padding:80px 40px;background:#fff}}
.article-wrap{{max-width:760px;margin:0 auto}}
.article-hero-img{{width:100%;max-height:440px;object-fit:cover;border-radius:20px;display:block;margin-bottom:48px}}
.article-wrap h2{{font-size:1.5rem;font-weight:800;color:var(--navy);margin:40px 0 16px;letter-spacing:-.02em;line-height:1.2}}
.article-wrap h3{{font-size:1.2rem;font-weight:700;color:var(--navy);margin:32px 0 12px;letter-spacing:-.02em;line-height:1.25}}
.article-wrap p{{font-size:1rem;color:var(--muted);line-height:1.85;margin-bottom:20px}}
.article-wrap ol,.article-wrap ul{{margin:0 0 20px 24px;color:var(--muted);line-height:1.85}}
.article-wrap li{{margin-bottom:8px}}
.article-wrap li strong{{color:var(--navy)}}
.article-wrap img{{max-width:100%;height:auto;border-radius:12px;margin:24px 0}}
.article-wrap a{{color:var(--teal);text-decoration:underline;text-underline-offset:3px}}
.article-wrap a:hover{{color:var(--lteal)}}
.article-wrap blockquote{{border-left:4px solid var(--teal);padding:16px 24px;margin:28px 0;background:var(--lgray);border-radius:0 12px 12px 0}}
.article-wrap blockquote p{{color:var(--navy);font-style:italic;margin-bottom:0}}

/* CTA */
.post-cta{{background:linear-gradient(135deg,var(--navy),var(--mid));border-radius:24px;padding:48px 44px;margin:56px 0 0;text-align:center}}
.post-cta h3{{font-size:1.4rem;font-weight:800;color:#fff;margin-bottom:12px;letter-spacing:-.02em}}
.post-cta p{{font-size:.95rem;color:rgba(255,255,255,.6);line-height:1.76;margin-bottom:28px}}
.post-cta .cta-btns{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:20px}}
.btn-teal{{display:inline-block;background:var(--teal);color:var(--navy);text-decoration:none;font-weight:800;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;padding:14px 36px;border-radius:50px;transition:background .3s,transform .3s}}
.btn-teal:hover{{background:var(--lteal);transform:translateY(-2px)}}
.btn-outline{{display:inline-block;border:2px solid rgba(255,255,255,.2);color:rgba(255,255,255,.7);text-decoration:none;font-weight:600;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;padding:12px 32px;border-radius:50px;transition:border-color .3s,color .3s}}
.btn-outline:hover{{border-color:var(--teal);color:var(--teal)}}
.post-cta .areas{{font-size:.8rem;color:rgba(255,255,255,.38);margin-top:8px}}
.post-cta .areas a{{color:rgba(255,255,255,.5);text-decoration:none;transition:color .2s}}
.post-cta .areas a:hover{{color:var(--teal)}}
.back-link{{display:inline-flex;align-items:center;gap:8px;margin-top:36px;font-size:.82rem;font-weight:600;color:var(--teal);text-decoration:none;letter-spacing:.08em;text-transform:uppercase;transition:gap .3s}}
.back-link:hover{{gap:14px}}

/* FOOTER */
footer{{background:#050e1a;padding:64px 40px 36px;border-top:1px solid rgba(255,255,255,.06)}}
.footer-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:48px;margin-bottom:56px}}
.footer-brand img{{height:60px;width:60px;object-fit:contain;border-radius:4px;margin-bottom:16px;display:block}}
.footer-brand-name{{font-size:1.05rem;font-weight:700;color:#fff;margin-bottom:12px;letter-spacing:-.02em}}
.footer-brand-desc{{font-size:.85rem;color:rgba(255,255,255,.4);line-height:1.76;max-width:300px}}
.footer-col-title{{font-size:.68rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin-bottom:20px}}
.footer-links{{list-style:none;display:flex;flex-direction:column;gap:11px}}
.footer-links a{{font-size:.85rem;color:rgba(255,255,255,.45);text-decoration:none;transition:color .3s}}
.footer-links a:hover{{color:var(--teal)}}
.footer-bottom{{max-width:1200px;margin:0 auto;padding-top:26px;border-top:1px solid rgba(255,255,255,.06);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}}
.footer-copy{{font-size:.8rem;color:rgba(255,255,255,.28)}}
.footer-line{{width:56px;height:2px;background:linear-gradient(90deg,var(--teal),transparent);border-radius:2px}}
@media(max-width:768px){{
  .nav{{padding:14px 20px}}
  .nav-toggle{{display:flex}}
  .nav-links{{display:none!important}}
  .page-hero{{padding:120px 20px 60px}}
  .article-section{{padding:48px 20px}}
  .post-cta{{padding:36px 24px}}
  .footer-inner{{grid-template-columns:1fr;gap:32px}}
}}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <a href="/" class="nav-logo">
    <img src="/img/beaudoins-hawaii-pool-cleaners-logo.png" alt="Hawaii Pool Cleaners">
    <div class="nav-logo-text">Hawaii Pool Cleaners<span>Island Pool Experts</span></div>
  </a>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="/offerings/">Offerings</a></li>
    <li><a href="/areas/">Service Areas</a></li>
    <li><a href="/blog/">Blog</a></li>
    <li><a href="/contact/" class="nav-cta">Free Liner Quote</a></li>
  </ul>
  <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="nav-mobile" id="navMobile" aria-hidden="true">
  <ul class="nav-mobile-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="/offerings/">Offerings</a></li>
    <li><a href="/areas/">Service Areas</a></li>
    <li><a href="/blog/">Blog</a></li>
  </ul>
  <a href="/contact/" class="mobile-cta-btn">Free Liner Quote</a>
</div>

<!-- HERO -->
<section class="page-hero">
  <span class="eyebrow">Pool Care Tips</span>
  <h1>{html.escape(title)}</h1>
  <div class="date">{pub_date}</div>
</section>

<!-- ARTICLE -->
<section class="article-section">
  <article class="article-wrap">
    <img class="article-hero-img" src="{hero_img}" alt="{html.escape(title)}" loading="lazy">
    {body}
    <div class="post-cta">
      <h3>Hawaii Pool Cleaners &mdash; Serving All of Oahu</h3>
      <p>Need professional pool cleaning, maintenance, or vinyl liner work? Our team serves homeowners and commercial properties across the island.</p>
      <div class="cta-btns">
        <a href="/offerings/" class="btn-teal">Our Services</a>
        <a href="/contact/" class="btn-outline">Get a Free Quote</a>
      </div>
      <p class="areas">Serving: <a href="/areas/honolulu/">Honolulu</a> &bull; <a href="/areas/kailua/">Kailua</a> &bull; <a href="/areas/kaneohe/">Kaneohe</a> &bull; <a href="/areas/kapolei/">Kapolei</a> &bull; <a href="/areas/pearl-city/">Pearl City</a> &bull; <a href="/areas/mililani/">Mililani</a> &bull; <a href="/areas/">View all 53 areas &rarr;</a></p>
    </div>
    <a href="/blog/" class="back-link">&larr; Back to Blog</a>
  </article>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="/img/beaudoins-hawaii-pool-cleaners-logo.png" alt="Hawaii Pool Cleaners">
      <div class="footer-brand-name">Hawaii Pool Cleaners</div>
      <p class="footer-brand-desc">Oahu's trusted vinyl pool liner specialists. Expert installation, repair, and pool maintenance across the island.</p>
    </div>
    <div>
      <div class="footer-col-title">Services</div>
      <ul class="footer-links">
        <li><a href="/offerings/">Vinyl Liner Installation</a></li>
        <li><a href="/offerings/">Pool Repair</a></li>
        <li><a href="/offerings/">Pool Cleaning</a></li>
        <li><a href="/offerings/">Chemical Balancing</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Company</div>
      <ul class="footer-links">
        <li><a href="/about/">About Us</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/areas/">Service Areas</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Contact</div>
      <ul class="footer-links">
        <li><a href="tel:808-864-3605">808-864-3605</a></li>
        <li><a href="/contact/">Free Quote</a></li>
        <li>Serving All of Oahu</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span class="footer-copy">&copy; 2026 Hawaii Pool Cleaners. All rights reserved.</span>
    <span class="footer-line"></span>
  </div>
</footer>

<script>
var navToggle=document.getElementById('navToggle'),navMobile=document.getElementById('navMobile');
if(navToggle&&navMobile){{navToggle.addEventListener('click',function(){{var o=navMobile.classList.toggle('open');navToggle.classList.toggle('open',o);navToggle.setAttribute('aria-expanded',String(o));navMobile.setAttribute('aria-hidden',String(!o));document.body.style.overflow=o?'hidden':''}});navMobile.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{navMobile.classList.remove('open');navToggle.classList.remove('open');navToggle.setAttribute('aria-expanded','false');navMobile.setAttribute('aria-hidden','true');document.body.style.overflow=''}})}})}}
</script>
</body>
</html>'''


def process_post(slug):
    fpath = f"{slug}/index.html"
    if not os.path.exists(fpath):
        print(f"SKIP (not found): {fpath}")
        return False

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    title, desc, canonical, og_image, feat_image, pub_date, iso_date = extract_meta(content)
    body = extract_body(content)

    # Remove the old CTA block and back-to-blog link from body (we add our own)
    body = re.sub(r'<div class="hpc-post-cta">.*?</div>\s*', '', body, flags=re.DOTALL)
    body = re.sub(r'<a href="/blog/"[^>]*>.*?</a>\s*', '', body, flags=re.DOTALL)
    body = body.strip()

    modern = build_modern_page(slug, title, desc, canonical, og_image, feat_image, pub_date, iso_date, body)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(modern)

    print(f"OK: {title[:60]}")
    return True


if __name__ == "__main__":
    count = 0
    for slug in BLOG_POSTS:
        if process_post(slug):
            count += 1
    print(f"\nDone: {count} posts modernized")
