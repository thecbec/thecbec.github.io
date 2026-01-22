---
layout: "page"
title: "Our Story: Told Through the Lens"
permalink: "/gallery/"
body_class: "gallery-page"
---
<div class="gallery-grid gallery-grid--uniform">
  {% for item in site.data.gallery %}
  <figure class="gallery-tile{% if item.size %} gallery-tile--{{ item.size }}{% endif %}">
    <a class="gallery-link" href="{{ item.src }}">
      <img src="{{ item.src }}" alt="{{ item.alt | default: '' }}" loading="lazy" />
    </a>
  </figure>
  {% endfor %}
</div>

<div class="gallery-lightbox" aria-hidden="true">
  <div class="gallery-lightbox__backdrop" data-gallery-close></div>
  <figure class="gallery-lightbox__content" role="dialog" aria-modal="true" aria-label="Image preview">
    <button class="gallery-lightbox__close" type="button" aria-label="Close image" data-gallery-close>X</button>
    <img class="gallery-lightbox__image" src="" alt="" />
  </figure>
</div>
<script>
(function() {
  var lightbox = document.querySelector('.gallery-lightbox');
  if (!lightbox) {
    return;
  }
  var image = lightbox.querySelector('.gallery-lightbox__image');
  var links = document.querySelectorAll('.gallery-page .gallery-link');
  var closeButtons = lightbox.querySelectorAll('[data-gallery-close]');

  function openLightbox(src) {
    image.src = src;
    lightbox.classList.add('is-open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.classList.add('lightbox-open');
  }

  function closeLightbox() {
    lightbox.classList.remove('is-open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lightbox-open');
    image.src = '';
  }

  links.forEach(function(link) {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      var src = link.getAttribute('href');
      if (src) {
        openLightbox(src);
      }
    });
  });

  closeButtons.forEach(function(button) {
    button.addEventListener('click', closeLightbox);
  });

  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && lightbox.classList.contains('is-open')) {
      closeLightbox();
    }
  });
})();
</script>

