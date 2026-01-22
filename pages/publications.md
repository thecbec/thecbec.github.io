---
layout: page
title: Publications
permalink: /publications/
---

<p>Reports, books, and published resources from the CBEC community.</p>

<section class="section-block">
  <div class="section-title">Publications</div>
  <div class="post-grid">
    {% assign posts = site.categories["Publications"] %}
    {% for post in posts %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
</section>
