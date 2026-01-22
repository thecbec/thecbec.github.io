---
layout: page
title: Stories
permalink: /stories/
---

<p>Field narratives, travel logs, and on-the-ground collaboration stories from the CBEC network.</p>

<section class="section-block">
  <div class="section-title">Stories</div>
  <div class="post-grid">
    {% assign posts = site.categories["Stories"] %}
    {% for post in posts %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
</section>
