---
layout: page
title: Forums
permalink: /forums/
---

<p>Highlights, timelines, and reflections from the CBEC Forum series around the region.</p>

<section class="section-block">
  <div class="section-title">CBEC Forums</div>
  <div class="post-grid">
    {% assign posts = site.categories["CBEC Forums"] %}
    {% for post in posts %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
</section>
