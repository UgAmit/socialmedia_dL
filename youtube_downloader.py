#!/usr/bin/env python3
"""
YouTube Video + Audio Downloader
A simple script to download YouTube videos and audio using yt-dlp
"""

import os
import sys
import argparse
import subprocess
import json
from pathlib import Path


class YouTubeDownloader:
    def __init__(self, download_path="./downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed or not found in PATH")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)
        
    def get_video_info(self, url):
        """Get video information without downloading"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Parse the first line of JSON output
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', 'Unknown'),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown')
            }
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None

    def download_video(self, url, quality='best', format_type='video'):
        """Download video or audio from YouTube URL"""
        
        cmd = ['yt-dlp']
        
        # Configure download options based on format type
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '192K',
                '--format', 'bestaudio/best'
            ])
        else:
            # Video download options
            if quality == 'best':
                format_selector = 'best[height<=1080]'
            elif quality == 'worst':
                format_selector = 'worst'
            elif quality == '720p':
                format_selector = 'best[height<=720]'
            elif quality == '480p':
                format_selector = 'best[height<=480]'
            elif quality == '360p':
                format_selector = 'best[height<=360]'
            else:
                format_selector = 'best'
                
            cmd.extend(['--format', format_selector, '--merge-output-format', 'mp4'])

        # Add output template and other options
        cmd.extend([
            '--output', str(self.download_path / '%(title)s.%(ext)s'),
            '--progress',
            url
        ])

        try:
            print(f"Starting download from: {url}")
            
            # Get video info first
            info = self.get_video_info(url)
            if info:
                print(f"Title: {info['title']}")
                print(f"Uploader: {info['uploader']}")
                print(f"Duration: {info['duration']} seconds")
                print("-" * 50)
            
            # Run the download command
            result = subprocess.run(cmd, check=True)
            print("✅ Download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_playlist(self, url, quality='best', format_type='video'):
        """Download entire playlist"""
        cmd = ['yt-dlp']
        
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '192K',
                '--format', 'bestaudio/best'
            ])
        else:
            if quality == 'best':
                format_selector = 'best[height<=1080]'
            elif quality == '720p':
                format_selector = 'best[height<=720]'
            elif quality == '480p':
                format_selector = 'best[height<=480]'
            else:
                format_selector = 'best'
            cmd.extend(['--format', format_selector])

        cmd.extend([
            '--output', str(self.download_path / '%(playlist_title)s/%(title)s.%(ext)s'),
            '--ignore-errors',
            '--progress',
            url
        ])

        try:
            result = subprocess.run(cmd, check=True)
            print("✅ Playlist download completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Playlist download failed with exit code {e.returncode}")
        except Exception as e:
            print(f"❌ Playlist download failed: {e}")


def main():
    parser = argparse.ArgumentParser(description='YouTube Video + Audio Downloader')
    parser.add_argument('url', help='YouTube URL to download')
    parser.add_argument('-f', '--format', choices=['video', 'audio'], default='video',
                        help='Download format: video or audio only (default: video)')
    parser.add_argument('-q', '--quality', choices=['best', '1080p', '720p', '480p', '360p', 'worst'],
                        default='best', help='Video quality (default: best)')
    parser.add_argument('-o', '--output', default='./downloads',
                        help='Output directory (default: ./downloads)')
    parser.add_argument('-p', '--playlist', action='store_true',
                        help='Download entire playlist')
    parser.add_argument('--info', action='store_true',
                        help='Show video information without downloading')
    
    args = parser.parse_args()
    
    # Create downloader instance
    downloader = YouTubeDownloader(args.output)
    
    if args.info:
        # Just show video info
        info = downloader.get_video_info(args.url)
        if info:
            print("📹 Video Information:")
            print(f"Title: {info['title']}")
            print(f"Uploader: {info['uploader']}")
            print(f"Duration: {info['duration']} seconds")
            print(f"Views: {info['view_count']:,}")
            print(f"Upload Date: {info['upload_date']}")
        return
    
    print("🎬 YouTube Downloader Started")
    print(f"📁 Download directory: {args.output}")
    print(f"🎯 Format: {args.format}")
    if args.format == 'video':
        print(f"📊 Quality: {args.quality}")
    print("-" * 50)
    
    if args.playlist:
        print("📋 Downloading playlist...")
        downloader.download_playlist(args.url, args.quality, args.format)
    else:
        print("📹 Downloading single video...")
        downloader.download_video(args.url, args.quality, args.format)


def interactive_mode():
    """Interactive mode for easier usage"""
    print("🎬 YouTube Video + Audio Downloader")
    print("=" * 40)
    
    while True:
        try:
            url = input("\n📎 Enter YouTube URL (or 'quit' to exit): ").strip()
            if url.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not url:
                continue
                
            # Download path
            download_path = input("📁 Download directory (press Enter for ./downloads): ").strip()
            if not download_path:
                download_path = "./downloads"
                
            downloader = YouTubeDownloader(download_path)
            
            # Show video info first
            print("\n🔍 Getting video information...")
            info = downloader.get_video_info(url)
            if not info:
                print("❌ Could not retrieve video information. Please check the URL.")
                continue
                
            print(f"\n📹 Video: {info['title']}")
            print(f"👤 Uploader: {info['uploader']}")
            print(f"⏱️  Duration: {info['duration']} seconds")
            
            # Format selection
            print("\n🎯 Select download format:")
            print("1. Video (MP4)")
            print("2. Audio only (MP3)")
            
            format_choice = input("Enter choice (1-2): ").strip()
            format_type = 'audio' if format_choice == '2' else 'video'
            
            # Quality selection for video
            quality = 'best'
            if format_type == 'video':
                print("\n📊 Select video quality:")
                print("1. Best available")
                print("2. 1080p")
                print("3. 720p")
                print("4. 480p")
                print("5. 360p")
                
                quality_choice = input("Enter choice (1-5): ").strip()
                quality_map = {'1': 'best', '2': '1080p', '3': '720p', '4': '480p', '5': '360p'}
                quality = quality_map.get(quality_choice, 'best')
            
            # Check if it's a playlist
            is_playlist = 'playlist' in url or 'list=' in url
            if is_playlist:
                playlist_choice = input("\n📋 This appears to be a playlist. Download entire playlist? (y/n): ").strip().lower()
                if playlist_choice == 'y':
                    downloader.download_playlist(url, quality, format_type)
                else:
                    downloader.download_video(url, quality, format_type)
            else:
                downloader.download_video(url, quality, format_type)
                
        except KeyboardInterrupt:
            print("\n\n👋 Download interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, run in interactive mode
        interactive_mode()
    else:
        # Command line arguments provided
        main() 