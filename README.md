# CBEC Site - How to Update and Publish

This site is built with Jekyll. You edit the source files (NOT the `_site/` folder) and then preview locally. GitHub Pages will build and publish the site for you.

## 1) Where to edit

- Posts: `_posts/*.md`
- Pages: `pages/*.md`
- Homepage: `index.md`
- CSS: `assets/css/site.css`
- Images: `wp-content/uploads/...`

Do **not** edit `_site/` directly. `_site/` is generated and will be overwritten.

## 1a) Easier post creation (no coding)

Open `tools/post-builder.html` in your browser. Fill the form and click "Generate Markdown". Then save the file into `_posts/`.
For a step-by-step walkthrough, see `Post_Builder_README.md`.

## 2) Preview locally (recommended)

Open PowerShell in the project folder and run:

```powershell
scripts\serve.cmd 4001
```

Then open:

```
http://localhost:4001
```

Stop the server with `Ctrl + C` when done.

## 2a) Preview on your phone (same Wi‑Fi)

Run the server so it listens on your network:

```powershell
scripts\serve.cmd 4001 0.0.0.0
```

Then open this on your phone (replace with your PC’s local IP):

```
http://YOUR-PC-IP:4001
```

If you don’t know your PC IP, run:

```powershell
ipconfig
```

Look for the IPv4 Address under your active network adapter.

## 3) Publish (GitHub Pages builds Jekyll)

You only push the source files (NOT `_site/`).

Basic flow:
1. Save your changes.
2. Commit with a short message.
3. Push to GitHub.

GitHub Pages will build and publish the site automatically.

## 3a) GitHub login/auth (switching accounts)

If you use multiple GitHub accounts on this PC, Git may cache the "wrong" user.
When that happens, clear the cached credentials and log in again.

### Option A: Browser login (Git Credential Manager)

This is the simplest login method.

```powershell
git config --global credential.helper manager-core
git push
```

A browser window will open. Sign in as the correct account.

### Option B: Personal Access Token (works even if GCM fails)

Create a token:
1. GitHub (web) -> Settings -> Developer settings
2. Personal access tokens -> Tokens (classic)
3. Generate new token (classic)
4. Scopes: check `repo`
5. Copy the token (you will see it only once)

Use it when pushing:

```powershell
git -c credential.helper= push
```

When prompted:
- Username: your GitHub username (e.g. `thecbec`)
- Password: paste the token

Note: the password prompt shows nothing as you type. Right-click to paste, then press Enter.

### Clear cached GitHub credentials (if push uses the wrong account)

```powershell
cmdkey /list
cmdkey /delete:git:https://github.com
cmdkey /delete:github.com
```

Then push again using Option A or Option B.

## 4) If you want to rebuild manually

This is optional. You usually do not need this because GitHub Pages builds the site for you. Use it only if you want to refresh the local `_site/` folder.

```powershell
scripts\build.cmd
```

This updates `_site/` for local viewing, but you still should not push `_site/` if GitHub Pages is building the site.

## 5) Common reminders

- If a new post should appear in a category page, add that **category** in the post front matter.
- If a post card needs an image, make sure `featured_image` is set.
- The gallery page uses a custom grid. Drop new images into `wp-content/uploads/gallery/` and run `scripts\serve.cmd` or `scripts\build.cmd` so it refreshes automatically.

## 6) If `bundle` fails (Ruby/Jekyll troubleshooting)

Sometimes PowerShell doesn’t have Ruby/Bundler on the PATH in a new session. You do **not** need to reinstall—just re‑set the PATH for the current session:

```powershell
where.exe ruby
ruby -v
where.exe bundle
bundle -v
```

If any of those fail, set PATH for the session:

```powershell
$env:PATH = 'C:\Ruby34-x64\bin;C:\Ruby34-x64\lib\ruby\gems\3.4.0\bin;' + $env:PATH
```

If `bundle` still fails, run:

```powershell
C:\Ruby34-x64\bin\gem.cmd -v
```

---
If anything is confusing, ask and I will walk you through it.
