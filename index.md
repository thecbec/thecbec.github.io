---
layout: default
title: Home
---

<section class="hero">
  <div class="hero-media">
    <img src="{{ "/wp-content/uploads/2023/07/main-banner.png" | relative_url }}" alt="CBEC forum banner">
    <div class="hero-overlay"></div>
    <div class="hero-caption">
      <span>CBEC Forum Series</span>
      <span>Building cross-border e-commerce bridges since 2018.</span>
    </div>
  </div>
  <div class="hero-content">
    <p class="hero-kicker">Cross-Border E-Commerce</p>
    <h1 class="hero-title">CBEC for Development</h1>
    <p class="hero-summary">Farm Worker Spirit. A living archive of forum milestones, field research, and partnerships across the Belt and Road.</p>
    <div class="cta">
      <a class="btn-primary" href="{{ "/stories/" | relative_url }}">Explore Stories</a>
      <a class="btn-secondary" href="{{ "/forums/" | relative_url }}">Forum Journey</a>
    </div>
  </div>
</section>

<section class="section-block">
  <div class="section-title">Latest</div>
  <div class="latest-grid">
    {% assign lead_post = site.posts | first %}
    {% if lead_post %}
      {% include post-card.html post=lead_post class="post-card--lead" show_excerpt=true excerpt=220 %}
    {% endif %}
    {% for post in site.posts offset: 1 limit: 4 %}
      {% include post-card.html post=post class="post-card--compact" show_excerpt=false %}
    {% endfor %}
  </div>
</section>

<section class="section-block">
  <div class="section-title">Trending</div>
  <div class="post-grid">
    {% assign latest_posts = site.posts | slice: 0, 5 %}
    {% assign latest_urls = "" | split: "" %}
    {% for post in latest_posts %}
      {% assign latest_urls = latest_urls | push: post.url %}
    {% endfor %}

    {% assign trending_posts = "" | split: "" %}
    {% assign trending_urls = "" | split: "" %}
    {% assign category_order = "Stories,Insights,CBEC Forums,Events,Journal,Publications" | split: "," %}

    {% for category in category_order %}
      {% assign category_posts = site.categories[category] %}
      {% if category_posts %}
        {% for post in category_posts %}
          {% unless latest_urls contains post.url or trending_urls contains post.url %}
            {% assign trending_posts = trending_posts | push: post %}
            {% assign trending_urls = trending_urls | push: post.url %}
            {% break %}
          {% endunless %}
        {% endfor %}
      {% endif %}
    {% endfor %}

    {% assign remaining = 10 | minus: trending_posts.size %}
    {% if remaining > 0 %}
      {% for post in site.posts %}
        {% if remaining == 0 %}
          {% break %}
        {% endif %}
        {% unless latest_urls contains post.url or trending_urls contains post.url %}
          {% assign trending_posts = trending_posts | push: post %}
          {% assign trending_urls = trending_urls | push: post.url %}
          {% assign remaining = remaining | minus: 1 %}
        {% endunless %}
      {% endfor %}
    {% endif %}

    {% for post in trending_posts limit: 10 %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
  <div class="section-action">
    <a class="view-all" href="{{ "/blog/" | relative_url }}">View All Posts</a>
  </div>
</section>
