#!/usr/bin/env python3
"""
Universal Social Media Downloader
Download from YouTube, Instagram, Twitter/X, TikTok, Facebook, and more using yt-dlp
"""

import os
import sys
import argparse
import subprocess
import json
import re
from pathlib import Path
from urllib.parse import urlparse


class SocialMediaDownloader:
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
    
    def detect_platform(self, url):
        """Detect which social media platform the URL belongs to"""
        domain = urlparse(url).netloc.lower()
        
        if any(x in domain for x in ['youtube.com', 'youtu.be']):
            return 'youtube', '🎬'
        elif any(x in domain for x in ['instagram.com', 'instagr.am']):
            return 'instagram', '📱'
        elif any(x in domain for x in ['twitter.com', 'x.com', 't.co']):
            return 'twitter', '🐦'
        elif 'tiktok.com' in domain:
            return 'tiktok', '🎵'
        elif 'facebook.com' in domain or 'fb.com' in domain:
            return 'facebook', '📘'
        elif 'reddit.com' in domain:
            return 'reddit', '🤖'
        elif 'dailymotion.com' in domain:
            return 'dailymotion', '📺'
        elif 'vimeo.com' in domain:
            return 'vimeo', '🎥'
        elif 'twitch.tv' in domain:
            return 'twitch', '🎮'
        else:
            return 'unknown', '🌐'
    
    def get_media_info(self, url):
        """Get media information without downloading"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Parse the first line of JSON output
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Unknown Media'),
                'description': info.get('description', 'No description'),
                'uploader': info.get('uploader', 'Unknown'),
                'uploader_id': info.get('uploader_id', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'like_count': info.get('like_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'formats': len(info.get('formats', [])),
                'platform': info.get('extractor_key', 'Unknown')
            }
        except Exception as e:
            print(f"Error getting media info: {e}")
            return None

    def download_media(self, url, quality='best', format_type='video'):
        """Download media from any supported platform"""
        
        platform, emoji = self.detect_platform(url)
        
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
            # Video download options - platform-specific handling
            if platform == 'instagram':
                # Instagram-specific format handling
                if quality == 'best':
                    format_selector = 'best[ext=mp4]/best'
                elif quality == 'worst':
                    format_selector = 'worst[ext=mp4]/worst'
                elif quality == '720p':
                    format_selector = 'best[height<=720][ext=mp4]/best[height<=720]/best'
                elif quality == '480p':
                    format_selector = 'best[height<=480][ext=mp4]/best[height<=480]/best'
                elif quality == '360p':
                    format_selector = 'best[height<=360][ext=mp4]/best[height<=360]/best'
                else:
                    format_selector = 'best[ext=mp4]/best'
            else:
                # Standard format handling for other platforms
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
                
            cmd.extend(['--format', format_selector])

        # Platform-specific output directory
        output_dir = self.download_path / platform
        output_dir.mkdir(exist_ok=True)
        
        # Add common options
        cmd.extend([
            '--output', str(output_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--embed-subs',
            '--write-auto-subs',
            '--progress',
            url
        ])

        try:
            print(f"Starting download from {platform.upper()} {emoji}")
            print(f"URL: {url}")
            
            # Get media info first
            info = self.get_media_info(url)
            if info:
                print(f"{emoji} Title: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                if info['view_count']:
                    print(f"👀 Views: {info['view_count']:,}")
                if info['like_count']:
                    print(f"❤️  Likes: {info['like_count']:,}")
                print("-" * 50)
            
            # Run the download command
            result = subprocess.run(cmd, check=True)
            print("✅ Download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Note: Content may be private, deleted, or platform-restricted")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_playlist_or_channel(self, url, max_downloads=50):
        """Download playlist or channel videos"""
        platform, emoji = self.detect_platform(url)
        
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(self.download_path / platform / '%(uploader)s/%(playlist_title)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--embed-subs',
            '--write-auto-subs',
            '--ignore-errors',
            '--progress',
            url
        ]

        try:
            print(f"Downloading playlist/channel from {platform.upper()} {emoji}")
            print(f"Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ Playlist/Channel download completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
        except Exception as e:
            print(f"❌ Download failed: {e}")


def main():
    parser = argparse.ArgumentParser(description='Universal Social Media Downloader')
    parser.add_argument('url', help='Social media URL to download')
    parser.add_argument('-f', '--format', choices=['video', 'audio'], default='video',
                        help='Download format (default: video)')
    parser.add_argument('-q', '--quality', choices=['best', '1080p', '720p', '480p', '360p', 'worst'],
                        default='best', help='Video quality (default: best)')
    parser.add_argument('-o', '--output', default='./downloads',
                        help='Output directory (default: ./downloads)')
    parser.add_argument('-p', '--playlist', action='store_true',
                        help='Download entire playlist/channel')
    parser.add_argument('-n', '--number', type=int, default=50,
                        help='Max number of videos to download from playlist (default: 50)')
    parser.add_argument('--info', action='store_true',
                        help='Show media information without downloading')
    
    args = parser.parse_args()
    
    # Create downloader instance
    downloader = SocialMediaDownloader(args.output)
    platform, emoji = downloader.detect_platform(args.url)
    
    if args.info:
        # Just show media info
        info = downloader.get_media_info(args.url)
        if info:
            print(f"{emoji} {platform.upper()} Media Information:")
            print(f"Title: {info['title']}")
            print(f"Creator: {info['uploader']}")
            print(f"Platform: {info['platform']}")
            print(f"Description: {info['description'][:100]}...")
            if info['duration']:
                print(f"Duration: {info['duration']} seconds")
            if info['view_count']:
                print(f"Views: {info['view_count']:,}")
            if info['like_count']:
                print(f"Likes: {info['like_count']:,}")
            print(f"Upload Date: {info['upload_date']}")
        return
    
    print(f"{emoji} {platform.upper()} Media Downloader Started")
    print(f"📁 Download directory: {args.output}")
    print(f"🎯 Format: {args.format}")
    if args.format == 'video':
        print(f"📊 Quality: {args.quality}")
    print("-" * 50)
    
    if args.playlist:
        print("📋 Downloading playlist/channel...")
        downloader.download_playlist_or_channel(args.url, args.number)
    else:
        print("📹 Downloading single media...")
        downloader.download_media(args.url, args.quality, args.format)


def interactive_mode():
    """Interactive mode for easier usage"""
    print("🌟 Universal Social Media Downloader")
    print("Supports: YouTube, Instagram, Twitter/X, TikTok, Facebook, Reddit, and more!")
    print("=" * 70)
    
    while True:
        try:
            url = input("\n📎 Enter social media URL (or 'quit' to exit): ").strip()
            if url.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not url:
                continue
            
            downloader = SocialMediaDownloader()
            platform, emoji = downloader.detect_platform(url)
            
            print(f"\n🔍 Detected Platform: {platform.upper()} {emoji}")
            
            # Download path
            download_path = input("📁 Download directory (press Enter for ./downloads): ").strip()
            if download_path:
                downloader = SocialMediaDownloader(download_path)
            
            # Show media info first
            print("\n🔍 Getting media information...")
            info = downloader.get_media_info(url)
            if not info:
                print("❌ Could not retrieve media information. Please check the URL.")
                continue
                
            print(f"\n{emoji} Title: {info['title']}")
            print(f"👤 Creator: {info['uploader']}")
            if info['duration']:
                print(f"⏱️  Duration: {info['duration']} seconds")
            if info['view_count']:
                print(f"👀 Views: {info['view_count']:,}")
            
            # Check if it's a playlist
            is_playlist = any(keyword in url.lower() for keyword in ['playlist', 'channel', 'user', 'list='])
            
            if is_playlist:
                playlist_choice = input(f"\n📋 This appears to be a playlist/channel. Download multiple videos? (y/n): ").strip().lower()
                if playlist_choice == 'y':
                    try:
                        max_downloads = int(input("📊 Max number of videos to download (default 50): ").strip() or "50")
                    except ValueError:
                        max_downloads = 50
                    downloader.download_playlist_or_channel(url, max_downloads)
                    continue
            
            # Format selection
            print("\n🎯 Select download format:")
            print("1. Video")
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
                print("6. Worst (smallest file)")
                
                quality_choice = input("Enter choice (1-6): ").strip()
                quality_map = {
                    '1': 'best', '2': '1080p', '3': '720p', 
                    '4': '480p', '5': '360p', '6': 'worst'
                }
                quality = quality_map.get(quality_choice, 'best')
            
            downloader.download_media(url, quality, format_type)
                
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