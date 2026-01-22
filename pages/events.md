---
layout: page
title: Events
permalink: /events/
---

<p>Workshops, forums, and collaborative events across the CBEC network.</p>

<section class="section-block">
  <div class="section-title">Events</div>
  <div class="post-grid">
    {% assign posts = site.categories["Events"] %}
    {% for post in posts %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
</section>
