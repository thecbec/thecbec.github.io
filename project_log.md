# Project Log

## 2026-01-14 03:55
- Jekyll preflight rule: run `where.exe ruby`, `ruby -v`, `where.exe bundle`, `bundle -v` before Jekyll commands.
- If missing, set session PATH: `C:\Ruby34-x64\bin;C:\Ruby34-x64\lib\ruby\gems\3.4.0\bin`.
- If gem is not resolvable, run `C:\Ruby34-x64\bin\gem.cmd -v` explicitly.
- Project folder: `F:\cbec_fresh`.
- Next ops checklist: `bundle install --jobs 1 --retry 3`, `bundle exec jekyll serve --port 4001`, `bundle exec jekyll build`, confirm `._site\index.html`.
- GitHub Pages prep: keep `_site` ignored (unless static deploy), add `README.md` deploy steps, optional `.github/workflows/pages.yml` for Jekyll build/deploy.
- Do not fetch media from WordPress.com; use local `wp-content/uploads`.

## 2026-01-14 04:10
- Redesigned the global layout with a newspaper-style masthead, section rules, and updated typography.
- Added the homepage hero with CTA buttons and sectioned layout.
- Built category landing pages for Stories, Insights, Forums, Journal, Events, and Publications.
- Updated post and page templates to surface categories/tags and improve readability.
- Refreshed archive styling and added minimal styling for WordPress block content.

## 2026-01-14 04:30
- Added `featured_image` to posts by mapping WordPress featured images from `_source/thecbec.xml`.
- Rebuilt home + section listings to show featured images using a shared post-card include.
- Tightened the visual system toward a newspaper layout with rectangular cards and simplified styling.
- Improved WordPress block styling (galleries, columns, slideshows) for consistent rectangular images.

## 2026-01-14 04:50
- Removed the placeholder test post and refined the Latest grid to avoid empty space under the lead story.
- Added a people-page body class and styled profile images as circular portraits.
- Centered the site header, added the italic farm worker spirit tagline, and removed the redundant home sections block.
- Added the CBEC logo asset under `assets/images` and integrated it into the masthead.
- Tuned mobile header spacing/centering and unified gallery image sizing on mobile.

## 2026-01-14 05:20
- Standardized mobile gallery tile heights across gallery block types.
- Filled the first gallery grid with a new image and wired it in `pages/gallery.md` and `_site/gallery/index.html`.
- Moved the new gallery photo into `wp-content/uploads/2023/07/cbec-forum-bangladesh-2024.jpg`.
- Hid the homepage hero section on all screen sizes and swapped the hero image to a people photo for when it is re-enabled.
- Relaxed people portrait crop with a 180px circular frame and adjusted `object-position` for better headroom.

## 2026-01-14 05:50
- Added the 8th CBEC Forum post (`_posts/2025-09-21-8th-cbec-forum-kunming.md`) with embedded images and excerpt.
- Moved `8thcbec-1.png`, `8thcbec-2.png`, and `8thcbec-3.png` into `wp-content/uploads/2025/09/` (and `_site`).
- Updated the CBEC Forums Journey timeline to 2018-2025 with the new 2025 entry.
- Added Events category/tag to the 8th CBEC Forum post.

## 2026-01-14 06:10
- Added a "View All Posts" link below the Trending block on the homepage, pointing to `/blog/`.

## 2026-01-14 06:20
- Replaced the Zhou Deyi portrait with `wp-content/uploads/2023/07/zhou-deyi.png` (new source image).

## 2026-01-14 07:00
- Fixed mobile gallery tile width inconsistency by normalizing all gallery block types (wp-block-gallery, wp-block-jetpack-slideshow, wp-block-jetpack-tiled-gallery) to full-width on mobile.
- Added comprehensive tiled gallery styling with grid layout and consistent aspect ratios.
- Made hero banner thinner with max-width constraint (960px), reduced height (240-280px), and more compact padding.
- Improved typography with new font stack: Playfair Display (display), Source Serif 4 (body), Inter (UI).
- Made post cards more compact: reduced padding, tighter gaps, smaller font sizes, added subtle hover effects.
- Refined section titles, buttons, and footer for a cleaner look with reduced letter-spacing.
- Comprehensive mobile optimization: adjusted all spacing, font sizes, and layouts for 700px and below.
- Updated Google Fonts include to load new font families.

## 2026-01-14 07:30
- Fixed gallery mobile tile width issue with `!important` overrides to force inline `flex-basis` styles to 100% on mobile.
- Changed gallery containers to `display: block` on mobile with proper spacing between tiles.
- Added `alignfull` and `alignwide` resets on mobile to prevent width inconsistencies.
- Removed excerpts from all category listing pages (Stories, Insights, Forums, Journal, Events, Publications) and the Blog archive for a cleaner, more uniform card appearance.

## 2026-01-14 08:00
- Added two new gallery images (`img_8390.jpg`, `pr4_8445.jpg`) into `wp-content/uploads/2023/07/` and `_site`.
- Filled the top and bottom grid gaps by inserting the new tiles into the custom gallery grid order.
- Updated the gallery tiles to link to the original image files with a zoom-in cursor, opening full size on click.

## TODO

## Notes: Project origin and build approach
This repository is a static site rebuild of the CBEC website originally hosted on WordPress.com. The source content was exported from WordPress.com using the standard WXR/XML export (`thecbec.xml`) and preserved under `_source/` for traceability and possible re-import.

Because WordPress.com exports reference media by URL rather than bundling binaries in the XML, the media library was exported separately. The media archive was extracted into `wp-content/uploads/` to mirror the canonical WordPress uploads path and keep content-to-asset references consistent.

The site is rebuilt as a Jekyll project. Posts and pages are represented as Markdown with YAML front matter, rendered via Jekyll layouts/includes plus a site-specific stylesheet under `assets/`. Build output is generated into `_site/` via `bundle exec jekyll build`, and local preview is provided via `bundle exec jekyll serve`.

The delivery target is GitHub Pages. The repository is structured to support a repeatable build and publish workflow, where the Jekyll source is versioned in Git and the rendered static site is deployed through GitHub Pages (either via the built-in Pages pipeline or a GitHub Actions workflow).

## 2026-01-14 08:20
- Added an in-page lightbox for gallery tiles with click-to-zoom, close button, and ESC support on desktop and mobile.
- Updated gallery tiles to use in-page links (no new tab) and added lightbox styling in `assets/css/site.css` and `_site/assets/css/site.css`.

## 2026-01-14 08:40
- Implemented a diversity-first Trending selection: excludes Latest posts, picks most recent posts by category priority (Stories, Insights, CBEC Forums, Events, Journal, Publications), then fills to 10 with newest remaining posts.
- Updated the built homepage trending grid to render 10 posts using the new selection logic.

## 2026-01-14 09:00
- Added a beginner-friendly `README.md` with local preview and GitHub Pages publishing steps.

## 2026-01-14 09:10
- Added Ruby/Bundler troubleshooting steps to `README.md` for new sessions where PATH is missing.

## 2026-01-14 09:20
- Added phone preview instructions to `README.md` using `--host 0.0.0.0` and local IP.

## 2026-01-15 01:43
- Moved the gallery to a data-driven list in `_data/gallery.yml` and updated `pages/gallery.md` to loop it while keeping the lightbox markup.
- Added `scripts/update_gallery.py` to append new images found in `wp-content/uploads/gallery/` without changing the existing order.
- Switched the gallery grid to a uniform layout via a `gallery-grid--uniform` class and added a 5-column layout on wide screens.
- Created `wp-content/uploads/gallery/` with a `.gitkeep` placeholder for future gallery drops.

## 2026-01-15 01:55
- Appended `IMG_8385.JPG` from `wp-content/uploads/gallery/` into `_data/gallery.yml` using the update script.

## 2026-01-15 02:05
- Updated `scripts/update_gallery.py` to remove missing entries that point to `wp-content/uploads/gallery/` so deleted files no longer leave empty tiles.

## 2026-01-15 02:10
- Added `scripts/serve.ps1` and `scripts/build.ps1` to auto-run the gallery update before serving or building.
- Updated `README.md` to use the new scripts so gallery changes are picked up automatically.

## 2026-01-15 02:22
- Added `scripts/serve.cmd` and `scripts/build.cmd` so Windows can run the workflow without PowerShell execution policy errors.
- Updated `README.md` to use the `.cmd` wrappers.

## 2026-01-15 02:27
- Clarified in `README.md` that `scripts/build.cmd` is only needed to refresh the local `_site/` output and GitHub Pages handles builds.

## 2026-01-15 02:35
- Adjusted People page bio text alignment to justify on desktop and left-align on mobile for better readability.

## 2026-01-15 02:40
- Tightened People page bios with a narrower text column and slightly smaller font, keeping names/roles centered and bios left-aligned on mobile.

## 2026-01-15 02:48
- Hid post tag chips visually while keeping them in the HTML for crawlers by applying a visually hidden tag list style.

## 2026-01-15 03:09
- Added `tools/post-builder.html`, a browser-based form that generates new post Markdown with front matter, tags, categories, images, and content blocks.
- Documented the post builder in `README.md`.

## 2026-01-15 03:29
- Fixed the post builder to normalize image paths to web-friendly `/wp-content/...` URLs and insert real newlines in image blocks.
- Cleaned the test post image paths and markup so Jekyll can parse the front matter.

## 2026-01-15 03:58
- Rebuilt `tools/post-builder.html` with a block-based UI, file-name helpers for images, auto-suggested upload folders, and draft auto-save.

## 2026-01-15 04:31
- Refined the post builder with clearer guidance for pasted HTML, an advanced-only upload folder field, and better folder previews.
- Added `Post_Builder_README.md` and referenced it from `README.md`.

## 2026-01-15 04:32
- Tweaked post builder image helper text to clarify the file picker and path preview behavior.

## 2026-01-15 05:39
- Rebuilt `tools/post-builder.html` as Post Builder v2 with Markdown/HTML modes, live preview, drag-drop images, and optional save-to-_posts support.
- Updated `Post_Builder_README.md` to explain the new workflow and browser support.

## 2026-01-15 05:41
- Added an in-app note in the post builder about pasting HTML from Word/ChatGPT starting at H2.
