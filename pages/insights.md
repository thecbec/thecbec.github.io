---
layout: page
title: Insights
permalink: /insights/
---

<p>Analysis, research insights, and field observations across cross-border e-commerce.</p>

<section class="section-block">
  <div class="section-title">Insights</div>
  <div class="post-grid">
    {% assign posts = site.categories["Insights"] %}
    {% for post in posts %}
      {% include post-card.html post=post class="post-card--grid" show_excerpt=false %}
    {% endfor %}
  </div>
</section>
