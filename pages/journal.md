---
layout: page
title: Journal
permalink: /journal/
---

<p>Issues and editorials from the Entrepreneurship for Sustainability journal.</p>

<section class="section-block">
  <div class="section-title">Journal</div>
  <div class="post-grid">
    {% assign posts = site.categories["Journal"] %}
    {% for post in posts %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
</section>
