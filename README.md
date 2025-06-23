# YouTube Video + Audio Downloader

A Python script to download YouTube videos and audio using yt-dlp with support for various quality options and formats.

## Features

- ✅ Download videos in multiple quality options (1080p, 720p, 480p, 360p)
- ✅ Download audio-only files (MP3 format)
- ✅ Support for playlist downloads
- ✅ Interactive mode for easy usage
- ✅ Command-line interface with arguments
- ✅ Progress tracking during downloads
- ✅ Video information preview
- ✅ Error handling and recovery

## Installation

1. **Install yt-dlp using pipx:**
   ```bash
   pipx install yt-dlp
   ```

2. **Install FFmpeg (required for audio conversion):**
   
   **macOS (using Homebrew):**
   ```bash
   brew install ffmpeg
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **Windows:**
   - Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   - Add FFmpeg to your system PATH

## Usage

### Interactive Mode (Recommended for beginners)

Simply run the script without any arguments:

```bash
python youtube_downloader.py
```

The script will guide you through:
- Entering the YouTube URL
- Choosing download directory
- Selecting format (video or audio)
- Choosing video quality
- Handling playlists

### Command Line Interface

**Basic video download:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download audio only:**
```bash
python youtube_downloader.py -f audio "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download specific quality:**
```bash
python youtube_downloader.py -q 720p "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download to specific directory:**
```bash
python youtube_downloader.py -o "/path/to/downloads" "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download entire playlist:**
```bash
python youtube_downloader.py -p "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

**Get video information only:**
```bash
python youtube_downloader.py --info "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-f, --format` | Download format: `video` or `audio` | `video` |
| `-q, --quality` | Video quality: `best`, `1080p`, `720p`, `480p`, `360p`, `worst` | `best` |
| `-o, --output` | Output directory | `./downloads` |
| `-p, --playlist` | Download entire playlist | False |
| `--info` | Show video information without downloading | False |

## Examples

**Download a video in 720p quality:**
```bash
python youtube_downloader.py -q 720p "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Download playlist as audio files:**
```bash
python youtube_downloader.py -f audio -p "https://www.youtube.com/playlist?list=PLExample"
```

**Download to Music folder:**
```bash
python youtube_downloader.py -f audio -o "~/Music" "https://www.youtube.com/watch?v=VIDEO_ID"
```

## File Structure

After downloading, your files will be organized as:

```
downloads/
├── Single Video.mp4
├── Audio File.mp3
└── Playlist Name/
    ├── Video 1.mp4
    ├── Video 2.mp4
    └── Video 3.mp4
```

## Troubleshooting

**"FFmpeg not found" error:**
- Make sure FFmpeg is installed and accessible in your system PATH
- For audio downloads, FFmpeg is required for format conversion

**"Unable to extract video info" error:**
- Check if the YouTube URL is valid and accessible
- Some videos may be region-restricted or private
- Try updating yt-dlp: `pip install --upgrade yt-dlp`

**Slow download speeds:**
- Try using a different quality setting
- Check your internet connection
- Some videos may have bandwidth limitations

**Permission errors:**
- Make sure you have write permissions to the download directory
- Try running with elevated permissions if necessary

## Legal Notice

This tool is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content that you have permission to download.

## Dependencies

- `yt-dlp`: Modern YouTube downloader (fork of youtube-dl) - installed via pipx
- `FFmpeg`: Required for audio conversion and video processing

## Notes

This script uses the command-line version of `yt-dlp` installed via `pipx`, which provides better isolation and avoids Python environment conflicts on macOS and other systems with externally managed Python environments.

## License

This project is for educational purposes. Use responsibly and in accordance with YouTube's Terms of Service. 