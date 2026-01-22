# Post Builder v4 Guide

A WYSIWYG editor for creating CBEC posts. Works like Word - select text, then format.

## Quick Start

1. Open `tools/post-builder.html` in Chrome or Edge
2. Fill in Title and other details in the sidebar
3. Write in the editor - formatting shows as you type
4. Click **Download** or **Save to _posts**

## Formatting

### Floating Toolbar
Select text to see the toolbar appear above your selection:
- **↶/↷** - Undo/Redo
- **B** - Bold
- **I** - Italic
- **P** - Paragraph (convert back from heading)
- **H2/H3** - Headings
- **Link** - Add hyperlink
- **"** - Blockquote

### Keyboard Shortcuts
- `Ctrl+B` - Bold
- `Ctrl+I` - Italic
- `Ctrl+K` - Link
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo

### Slash Commands
Type `/` anywhere to see options:
- `/h2` - Heading
- `/h3` - Subheading
- `/p` - Paragraph
- `/ul` - Bullet list
- `/ol` - Numbered list
- `/quote` - Blockquote
- `/img` - Insert image
- `/hr` - Divider

Use arrow keys to navigate, Enter to select.

## Images

### Browse for Files
1. Type `/img` or use the slash menu
2. Click **Browse Files...** to select an image
3. See the thumbnail preview in the modal
4. Adjust folder/filename if needed, click **Insert**

### Paste from Clipboard
1. Copy an image or take a screenshot
2. Press `Ctrl+V` in the editor
3. Modal opens with preview - confirm the path and insert

### Drag and Drop
1. Drag an image file onto the editor
2. Modal opens with preview - confirm and insert

### Live Preview
- Images show as actual thumbnails in the editor (not placeholders)
- A yellow indicator shows: "Copy to: /wp-content/uploads/..."
- Reminder: copy your image files to that folder after saving

### Auto Folder
The **Auto** option in the folder dropdown generates paths like `/wp-content/uploads/2026/01/` based on your post's publish date.

Available folders: 2025/09, 2025/04, 2024/06, 2024/05, 2024/04, 2023/07, gallery

### Featured Image
In the sidebar under "Featured Image":
- Drop an image or click to select
- Choose folder (Auto or specific)
- Enter filename

## Saving

- **Copy** - Copy the markdown to clipboard
- **Download** - Download as .md file
- **Save to _posts** - Save directly (Chrome/Edge only, prompts for folder first time)

## Tips

- The editor outputs HTML with WordPress block classes, so posts render correctly
- Paste HTML from Word or ChatGPT - it preserves formatting
- Use the Preview tab to see how your post will look
- Posts are saved as `YYYY-MM-DD-slug.md` format
- Image blob previews automatically convert to server paths on export
