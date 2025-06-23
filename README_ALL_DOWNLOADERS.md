# 🌟 Social Media Downloaders Collection

Complete set of downloaders for YouTube, Instagram, Twitter/X, and more social media platforms.

## 📁 Available Scripts

### 1. **`youtube_downloader.py`** 🎬
- YouTube videos and audio
- Playlist support
- Multiple quality options

### 2. **`instagram_downloader.py`** 📱  
- Instagram posts, reels, stories, IGTV
- User profile downloads
- Image and video support

### 3. **`twitter_downloader.py`** 🐦
- Twitter/X videos and images  
- User tweet downloads
- Twitter Spaces audio

### 4. **`social_media_downloader.py`** 🌟
- **Universal downloader** for all platforms
- Auto-detects platform from URL
- Supports 10+ platforms

## 🚀 Quick Setup

### Installation

```bash
# Install yt-dlp
pipx install yt-dlp

# Install FFmpeg
brew install ffmpeg
```

### Supported Platforms

✅ **YouTube** - Videos, playlists, channels  
✅ **Instagram** - Posts, reels, stories, user profiles  
✅ **Twitter/X** - Videos, images, user tweets, Spaces  
✅ **TikTok** - Videos and audio  
✅ **Facebook** - Videos and posts  
✅ **Reddit** - Videos and media  
✅ **Vimeo** - Videos  
✅ **Twitch** - Clips and VODs  
✅ **Dailymotion** - Videos  
✅ **And 1000+ more platforms!**

## 💡 Usage Examples

### Universal Downloader (Recommended)

```bash
# Interactive mode (easiest)
python3 social_media_downloader.py

# Any platform URL
python3 social_media_downloader.py "https://youtube.com/watch?v=VIDEO_ID"
python3 social_media_downloader.py "https://instagram.com/p/POST_ID"
python3 social_media_downloader.py "https://twitter.com/user/status/TWEET_ID"

# Audio only from any platform
python3 social_media_downloader.py -f audio "https://any-platform-url"

# Download playlist/channel
python3 social_media_downloader.py -p "https://youtube.com/playlist?list=PLAYLIST_ID"
```

### Platform-Specific Scripts

```bash
# YouTube
python3 youtube_downloader.py "https://youtube.com/watch?v=VIDEO_ID"
python3 youtube_downloader.py -f audio -q 720p "https://youtube.com/watch?v=VIDEO_ID"

# Instagram  
python3 instagram_downloader.py "https://instagram.com/p/POST_ID"
python3 instagram_downloader.py -u username -n 10  # Download user's recent posts

# Twitter/X
python3 twitter_downloader.py "https://twitter.com/user/status/TWEET_ID"
python3 twitter_downloader.py -u username -n 20    # Download user's recent tweets
```

## 🎯 Interactive Mode

All scripts support interactive mode - just run without arguments:

```bash
python3 social_media_downloader.py
```

The interactive mode will:
- 🔍 Auto-detect the platform
- 📋 Show media information  
- 🎯 Guide you through format selection
- 📊 Let you choose quality options
- 📁 Organize downloads by platform

## 📊 Command Line Options

### Universal Downloader

| Option | Description | Example |
|--------|-------------|---------|
| `url` | Social media URL | Required |
| `-f, --format` | `video` or `audio` | `-f audio` |
| `-q, --quality` | Video quality | `-q 720p` |
| `-o, --output` | Download directory | `-o ~/Downloads` |
| `-p, --playlist` | Download playlist | `-p` |
| `-n, --number` | Max playlist downloads | `-n 100` |
| `--info` | Show info without downloading | `--info` |

### Platform-Specific Options

**YouTube:**
- Quality: `best`, `1080p`, `720p`, `480p`, `360p`, `worst`
- Supports playlists and channels

**Instagram:**
- Format: `video`, `audio`, `image`
- User downloads: `-u username -n 10`
- Quality: `best`, `medium`, `worst`

**Twitter:**
- Supports Twitter Spaces: `-s`
- User tweets: `-u username -n 20`
- Format: `video`, `audio`, `image`

## 📁 Download Organization

Files are automatically organized:

```
downloads/
├── youtube/
│   └── ChannelName/
│       ├── Video1.mp4
│       └── Video2.mp4
├── instagram/  
│   └── username/
│       ├── post1.mp4
│       └── post2.jpg
├── twitter/
│   └── username/
│       ├── tweet1.mp4
│       └── spaces/
│           └── space_audio.mp3
└── tiktok/
    └── creator/
        └── video.mp4
```

## 🌟 Features

### All Scripts Include:
- ✅ **Progress tracking** during downloads
- ✅ **Metadata saving** (JSON info files)
- ✅ **Description files** for context
- ✅ **Subtitle download** (when available)
- ✅ **Error handling** and recovery
- ✅ **Platform detection** (universal script)
- ✅ **Quality selection** options
- ✅ **Batch downloads** support

### Smart Features:
- 🧠 **Auto-detects** playlists vs single videos
- 🔍 **Preview info** before downloading  
- 📱 **Platform-specific** optimizations
- 🚀 **Parallel processing** for multiple downloads
- 💾 **Resume capability** for interrupted downloads

## 📱 Platform-Specific Notes

### YouTube 🎬
- Full playlist and channel support
- Automatic subtitle download
- Age-restricted content support
- Live stream recording

### Instagram 📱
- Works with public profiles only
- Stories require recent posts
- High-quality image downloads
- IGTV and Reels support

### Twitter/X 🐦
- Video tweets and GIFs
- Thread image downloads
- Twitter Spaces audio
- Tweet metadata preservation

### TikTok 🎵
- No watermark downloads
- Audio extraction
- User profile videos
- Trending content

## 🔧 Troubleshooting

### Common Issues:

**"yt-dlp not found"**
```bash
pipx install yt-dlp
```

**FFmpeg errors**
```bash
brew install ffmpeg
```

**Private content errors**
- Content may be private or deleted
- Some platforms require login (not supported)
- Try different quality settings

**Slow downloads**
- Check internet connection
- Try lower quality settings
- Some platforms have rate limits

### Platform-Specific Issues:

**Instagram:**
- Only public profiles work
- Stories may be time-limited
- Some content requires login
- If you get "Requested format is not available" error, try:
  ```bash
  # Check available formats first
  yt-dlp --list-formats "INSTAGRAM_URL"
  
  # Use flexible format selection
  python3 social_media_downloader.py "INSTAGRAM_URL"
  ```

**Twitter:**
- Protected accounts not supported
- Deleted tweets can't be downloaded
- Spaces must be live or recently ended

**TikTok:**
- Regional restrictions may apply
- Some content may be age-restricted

## 🚀 Pro Tips

1. **Use the Universal Downloader** for most tasks - it's the most versatile
2. **Try interactive mode first** - it's user-friendly and guides you
3. **Use playlist mode** for bulk downloads from channels/profiles
4. **Check `--info` first** to preview content before downloading
5. **Organize downloads** with custom output directories (`-o`)
6. **Download audio only** to save space and bandwidth (`-f audio`)

## 📝 Examples by Use Case

### Music Collection
```bash
# Download playlist as MP3
python3 social_media_downloader.py -f audio -p "https://youtube.com/playlist?list=MUSIC_PLAYLIST"

# Download Instagram music posts
python3 instagram_downloader.py -f audio -u music_artist -n 20
```

### Video Archive
```bash
# Download channel videos
python3 youtube_downloader.py -p -q 720p "https://youtube.com/c/CHANNEL_NAME"

# Download user's TikToks  
python3 social_media_downloader.py -u tiktok_user -n 50
```

### News & Information
```bash
# Download Twitter thread videos
python3 twitter_downloader.py -u news_account -n 10

# Download Reddit videos
python3 social_media_downloader.py "https://reddit.com/r/videos/post_url"
```

## 🛡️ Legal Notice

**Important:** 
- This tool is for **personal use only**
- Respect platform **Terms of Service**
- Respect **copyright laws**
- Only download content you have **permission** to download
- **Do not redistribute** downloaded content without permission

## 🔗 Platform Terms of Service

Please review the terms of service for each platform:
- [YouTube ToS](https://www.youtube.com/static?template=terms)
- [Instagram ToS](https://help.instagram.com/581066165581870)
- [Twitter ToS](https://twitter.com/tos)

---

**Happy downloading! 🎉**

*Made with ❤️ using yt-dlp - supporting 1000+ platforms worldwide* 