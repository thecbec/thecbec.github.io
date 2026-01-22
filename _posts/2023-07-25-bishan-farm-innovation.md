---

layout: "post"
title: "Innovative Digital Solutions for a Smart Farm in Rural China (Video)"
date: "2023-07-25 00:00:00 +0000"
featured_image: "/wp-content/uploads/2023/07/bishan-farm.jpg"
permalink: "/2023/07/25/bishan-farm-innovation/"
categories:
  - "Insights"
  - "Stories"
tags:
  - "agricultural technology"
  - "agriIno challenge"
  - "AgTech"
  - "Asian agriculture"
  - "blockchain"
  - "China agriculture"
  - "connecting farmers and consumers"
  - "digital agriculture"
  - "ecommerce"
  - "FAO"
  - "farm to fork"
  - "food traceability"
  - "IoT farming"
  - "revitalizing rural communities"
  - "rural development"
  - "smallholder farmers"
  - "smart farming"
redirect_from:
  - "/2023/07/26/bishan-farm-innovation/"
---
<p>Bishan Farm, located in Hubei Province, China, was founded by Professor Zhou Deyi of Huazhong Agricultural University as a training and research base. The farm raises free-range animals and collects local products for sale to urban consumers.</p>



<div class="video-embed">
  <button class="video-embed__trigger" type="button" data-video-src="/wp-content/uploads/2023/07/bishan-farm-innovation-china.mp4" aria-label="Play Bishan Farm video">
    <img src="/wp-content/uploads/2023/07/bishan-farm.jpg" alt="Bishan Farm innovation video cover" loading="lazy" />
    <span class="video-embed__play" aria-hidden="true">▶</span>
  </button>
  <p class="video-embed__caption">Innovation for Rural Revitalization: Bishan Farm's Tech-Driven Proposal</p>
</div>

<div class="video-lightbox" aria-hidden="true">
  <div class="video-lightbox__backdrop" data-video-close></div>
  <figure class="video-lightbox__content" role="dialog" aria-modal="true" aria-label="Video preview">
    <button class="video-lightbox__close" type="button" aria-label="Close video" data-video-close>×</button>
    <video class="video-lightbox__media" controls playsinline preload="metadata"></video>
  </figure>
</div>

<script>
(function() {
  var trigger = document.querySelector('.video-embed__trigger');
  var lightbox = document.querySelector('.video-lightbox');
  if (!trigger || !lightbox) return;

  var video = lightbox.querySelector('.video-lightbox__media');
  var closeButtons = lightbox.querySelectorAll('[data-video-close]');

  function openVideo(src) {
    if (!src) return;
    video.src = src;
    lightbox.classList.add('is-open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.classList.add('lightbox-open');
    video.play().catch(function() {});
  }

  function closeVideo() {
    lightbox.classList.remove('is-open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lightbox-open');
    video.pause();
    video.removeAttribute('src');
    video.load();
  }

  trigger.addEventListener('click', function() {
    openVideo(trigger.getAttribute('data-video-src'));
  });

  closeButtons.forEach(function(button) {
    button.addEventListener('click', closeVideo);
  });

  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && lightbox.classList.contains('is-open')) {
      closeVideo();
    }
  });
})();
</script>



<p>However, high labor requirements in animal production and lack of trust in product genuineness are challenges. As a result, farmland is underutilized, causing environmental issues, and many rural residents lack job opportunities.</p>



<p>To address these issues, the Bishan Farm team aims to implement the following innovative digital solutions:</p>



<ul>
<li>GPS locators and e-fences to prevent free-range animals from wandering</li>



<li>Automatic gates to open/close animal enclosures</li>



<li>Webcams for remote animal monitoring and rural-urban communication</li>



<li>Automatic mosquito control systems</li>



<li>Automated feeding machines and drinking troughs</li>



<li>Remote broadcast system to call animals back for daily feeding</li>



<li>Blockchain-based traceability system to record product origins and ensure genuineness</li>



<li>Group e-commerce system to facilitate transactions between rural producers and urban consumers</li>
</ul>



<p>The project was submitted to the UN FAO's Global AgriInno Challenge 2021 competition to showcase innovative digital solutions for agriculture. By expanding production and sales, the project intends to:</p>



<ul>
<li>Reduce labor costs and increase productivity</li>



<li>Provide job opportunities for rural women and elders</li>



<li>Use rice straw for feed instead of burning it</li>



<li>Produce healthier food for citizens</li>



<li>Provide internships for local and international youth</li>
</ul>



<p>In closing, the Bishan Farm project aims to benefit rural communities through innovative technology integration, ensuring sustainable and safe food production while connecting smallholder farmers to urban markets.</p>



<p>If you are interested in discussing innovative solutions relevant to Bishan Farm or the International Innovative Farm School Alliance, please contact us. We welcome collaborations and knowledge exchange to further empower rural communities through technology. To get in touch, email us or explore our website for more details on our projects and vision. Together, we can create positive change for smallholder farmers and revitalize rural economies.</p>
