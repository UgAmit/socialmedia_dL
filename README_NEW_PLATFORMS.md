# 🚀 New Platform Downloaders

## 📋 Overview

मैंने आपके लिए **8 नए platform downloaders** बनाए हैं! अब आप इन सभी platforms से content download कर सकते हैं:

## 🆕 New Downloaders

| Platform | Downloader | Features |
|----------|------------|----------|
| 🎯 Rumble | `rumble_downloader.py` | Videos, Channels, Quality options |
| 📌 Pinterest | `pinterest_downloader.py` | Pins, Boards, User content |
| 💼 LinkedIn | `linkedin_downloader.py` | Professional videos, Cookie auth |
| 🎵 Triller | `triller_downloader.py` | Music videos, User content |
| ❤️ Likee | `likee_downloader.py` | Short videos, Hashtags, Users |
| 🌐 PeerTube | `peertube_downloader.py` | Decentralized videos, Instances |
| 👻 Snapchat | `snapchat_downloader.py` | Spotlight content (limited) |
| 🎮 Discord | `discord_downloader.py` | Attachments, Media files |

## 🔧 Installation

```bash
# Install Python dependencies
pip install requests

# yt-dlp should already be installed
# If not: pipx install yt-dlp
```

## 📱 Usage Examples

### 🎯 Rumble
```bash
# Single video
python3 rumble_downloader.py "https://rumble.com/v..."

# Channel videos  
python3 rumble_downloader.py "https://rumble.com/c/channel" channel
```

### 📌 Pinterest
```bash
# Single pin
python3 pinterest_downloader.py "https://pinterest.com/pin/..."

# Board download
python3 pinterest_downloader.py "https://pinterest.com/user/board/" board

# User pins
python3 pinterest_downloader.py "username" user
```

### 💼 LinkedIn
```bash
# Basic download
python3 linkedin_downloader.py "https://linkedin.com/posts/..."

# With authentication
python3 linkedin_downloader.py "URL" --cookies cookies.txt

# Info only
python3 linkedin_downloader.py "URL" --info
```

### 🎵 Triller
```bash
# Video download
python3 triller_downloader.py "https://triller.co/v/..."

# User videos
python3 triller_downloader.py "username" user
```

### ❤️ Likee
```bash
# Single video
python3 likee_downloader.py "https://likee.video/v/..."

# User videos
python3 likee_downloader.py "username" user

# Hashtag videos
python3 likee_downloader.py "dance" hashtag
```

### 🌐 PeerTube
```bash
# Single video
python3 peertube_downloader.py "https://framapiaf.org/videos/watch/..."

# Channel download
python3 peertube_downloader.py "https://peertube.tv/c/channel/" channel

# List popular instances
python3 peertube_downloader.py --list-instances
```

### 👻 Snapchat
```bash
# Spotlight content
python3 snapchat_downloader.py "https://snapchat.com/spotlight/..."

# Show limitations
python3 snapchat_downloader.py --limitations
```

### 🎮 Discord
```bash
# Single attachment
python3 discord_downloader.py "https://cdn.discordapp.com/..."

# Bulk download
python3 discord_downloader.py "urls.txt" bulk

# Show info
python3 discord_downloader.py --info
```

## 🎛️ Quality Options

| Platform | Available Qualities |
|----------|-------------------|
| Rumble | best, 1080p, 720p, 480p, 360p, audio |
| Pinterest | best, image, video |
| LinkedIn | best, 720p, 480p, 360p, audio |
| Triller | best, 1080p, 720p, 480p, 360p, audio |
| Likee | best, 720p, 480p, 360p, audio |
| PeerTube | best, 1080p, 720p, 480p, 360p, audio |
| Snapchat | best, 720p, 480p, 360p |
| Discord | Original file quality |

## 📁 Download Structure

```
downloads/
├── rumble/
│   └── uploader/video.mp4
├── pinterest/
│   └── user/pin.jpg
├── linkedin/
│   └── author/post.mp4
├── triller/
│   └── creator/music_video.mp4
├── likee/
│   └── user/short_video.mp4
├── peertube/
│   └── instance/uploader/video.mp4
├── snapchat/
│   ├── spotlight/
│   └── stories/
└── discord/
    └── attachment.mp4
```

## ⚠️ Important Notes

### 🔒 Authentication Required
- **LinkedIn**: Often needs cookies for access
- **Pinterest**: Some content may be private
- **Snapchat**: Limited to public/spotlight content
- **Discord**: Need access permissions

### 🌐 Platform Limitations
- **Snapchat**: Private snaps/stories not accessible
- **Discord**: Only direct attachment links work
- **LinkedIn**: Professional content may be restricted
- **Pinterest**: Board access depends on privacy settings

### 📋 yt-dlp Support Status
| Platform | yt-dlp Support | Notes |
|----------|---------------|-------|
| ✅ Rumble | Full | Native extractor |
| ⚠️ Pinterest | Limited | Some content supported |
| ⚠️ LinkedIn | Limited | Authentication often required |
| ❓ Triller | Experimental | May require workarounds |
| ❓ Likee | Experimental | Limited support |
| ✅ PeerTube | Full | Native extractor |
| ❌ Snapchat | Minimal | Very limited access |
| ❌ Discord | None | Direct download only |

## 🔧 Troubleshooting

### Common Issues:

1. **"Extractor not found"**
   - Platform may not be supported by yt-dlp
   - Try direct download methods

2. **Authentication errors**
   - Use `--cookies` flag for LinkedIn
   - Login to platform in browser first

3. **Private content**
   - Ensure you have access permissions
   - Content may be region-restricted

4. **Download failures**
   - Check if content is still available
   - Platform may have changed API

## 🆕 Updates from GitHub

ये downloaders [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp) के latest extractors पर based हैं।

## 🤝 Contributing

अगर आपको कोई bugs मिलते हैं या improvements चाहिए:
1. Issues report करें
2. नए features suggest करें  
3. Platform-specific improvements

---

## 🎉 Summary

**अब आपके पास total 15+ platform downloaders हैं:**

**Original**: YouTube, Instagram, Twitter, TikTok, Facebook, Reddit, Dailymotion, Vimeo, Twitch

**New**: Rumble, Pinterest, LinkedIn, Triller, Likee, PeerTube, Snapchat, Discord + Vimeo (enhanced)

**🚀 Happy Downloading!** 🎬📱💾 