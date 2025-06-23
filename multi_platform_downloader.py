#!/usr/bin/env python3
"""
Multi-Platform Social Media Downloader
Supports: LinkedIn, Pinterest, Rumble, Peertube, Triller, Likee, Snapchat, Discord
"""

import os
import sys
import subprocess
import json
import argparse
from pathlib import Path
from urllib.parse import urlparse


class MultiPlatformDownloader:
    def __init__(self, download_path="./downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)
    
    def detect_platform(self, url):
        """Detect platform from URL and return platform info"""
        domain = urlparse(url).netloc.lower()
        
        # Platform detection with emojis and support status
        platforms = {
            'linkedin': {
                'domains': ['linkedin.com', 'lnkd.in'],
                'emoji': '💼',
                'supported': True,
                'extractor': 'linkedin',
                'info': 'Professional network videos'
            },
            'pinterest': {
                'domains': ['pinterest.com', 'pin.it'],
                'emoji': '📌',
                'supported': True,
                'extractor': 'pinterest',
                'info': 'Pin images and videos'
            },
            'rumble': {
                'domains': ['rumble.com'],
                'emoji': '🎯',
                'supported': True,
                'extractor': 'rumble',
                'info': 'Video platform'
            },
            'peertube': {
                'domains': ['peertube', 'tube.'],
                'emoji': '🌐',
                'supported': True,
                'extractor': 'peertube',
                'info': 'Decentralized video platform'
            },
            'triller': {
                'domains': ['triller.co'],
                'emoji': '🎵',
                'supported': True,
                'extractor': 'triller',
                'info': 'Music video platform'
            },
            'likee': {
                'domains': ['likee.video', 'likee.com'],
                'emoji': '❤️',
                'supported': True,
                'extractor': 'likee',
                'info': 'Short video platform'
            },
            'snapchat': {
                'domains': ['snapchat.com', 'snap.com'],
                'emoji': '👻',
                'supported': False,
                'extractor': 'snapchat',
                'info': 'Stories and Spotlight (Limited support)'
            },
            'discord': {
                'domains': ['discord.com', 'discord.gg'],
                'emoji': '🎮',
                'supported': False,
                'extractor': 'discord',
                'info': 'Chat platform (No video extractor)'
            }
        }
        
        for platform, config in platforms.items():
            if any(d in domain for d in config['domains']):
                return platform, config
        
        return 'unknown', {
            'emoji': '❓',
            'supported': False,
            'extractor': 'generic',
            'info': 'Unknown platform'
        }

    def get_media_info(self, url):
        """Get media information without downloading"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Unknown Media'),
                'description': info.get('description', 'No description'),
                'uploader': info.get('uploader', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'platform': info.get('extractor_key', 'Unknown')
            }
        except Exception as e:
            print(f"⚠️ Error getting media info: {e}")
            return None

    def download_media(self, url, quality='best', format_type='video'):
        """Download media from supported platforms"""
        
        platform, config = self.detect_platform(url)
        
        print(f"\n🌟 Platform: {platform.upper()} {config['emoji']}")
        print(f"📋 Info: {config['info']}")
        
        if not config['supported']:
            print(f"❌ Platform '{platform}' is not fully supported by yt-dlp")
            print("⚠️  Limited functionality or no support available")
            
            if platform == 'snapchat':
                print("💡 Suggestion: Use Snapchat's web interface for public stories")
            elif platform == 'discord':
                print("💡 Suggestion: Discord doesn't host public videos for download")
            
            return False
        
        # Create platform-specific output directory
        output_dir = self.download_path / platform
        output_dir.mkdir(exist_ok=True)
        
        cmd = ['yt-dlp']
        
        # Configure download options based on format type
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '192K'
            ])
        else:
            # Platform-specific quality settings
            if platform in ['pinterest', 'linkedin']:
                # These platforms may have limited quality options
                format_selector = 'best[height<=720]/best'
            elif platform == 'rumble':
                # Rumble usually has good quality options
                format_selector = f'best[height<={quality.replace("p", "")}]' if quality != 'best' else 'best'
            else:
                format_selector = 'best'
            
            cmd.extend(['--format', format_selector])
        
        # Add common options
        cmd.extend([
            '--output', str(output_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ])
        
        try:
            print(f"🚀 Starting download from {platform.upper()} {config['emoji']}")
            
            # Get media info first
            info = self.get_media_info(url)
            if info:
                print(f"📹 Title: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                print("-" * 50)
            
            # Run the download command
            result = subprocess.run(cmd, check=True)
            print("✅ Download successful!")
            return True
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Possible issues:")
            print("   - Content may be private or restricted")
            print("   - Platform may require authentication")
            print("   - Content may not be available for download")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False

    def download_playlist(self, url, max_downloads=20):
        """Download playlist or channel videos"""
        platform, config = self.detect_platform(url)
        
        if not config['supported']:
            print(f"❌ Platform '{platform}' not supported for playlist downloads")
            return False
        
        output_dir = self.download_path / platform
        
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(output_dir / '%(uploader)s/%(playlist_title)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--progress',
            url
        ]

        try:
            print(f"📋 Downloading playlist from {platform.upper()} {config['emoji']}")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ Playlist download completed!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Playlist download failed with exit code {e.returncode}")
            return False

    def list_supported_platforms(self):
        """List all supported platforms"""
        print("\n🌟 SUPPORTED PLATFORMS:")
        print("=" * 50)
        
        supported = [
            ('LinkedIn', '💼', 'Professional videos, posts'),
            ('Pinterest', '📌', 'Pin videos and images'),
            ('Rumble', '🎯', 'Video sharing platform'),
            ('PeerTube', '🌐', 'Decentralized video platform'),
            ('Triller', '🎵', 'Music videos and content'),
            ('Likee', '❤️', 'Short video sharing')
        ]
        
        for name, emoji, desc in supported:
            print(f"{emoji} {name:<12} - {desc}")
        
        print("\n⚠️  LIMITED SUPPORT:")
        print("👻 Snapchat      - Public stories only")
        print("🎮 Discord       - No direct video support")
        
        print("\n💡 USAGE EXAMPLES:")
        print("python3 multi_platform_downloader.py 'https://linkedin.com/posts/...'")
        print("python3 multi_platform_downloader.py 'https://rumble.com/v...' -q 720p")
        print("python3 multi_platform_downloader.py 'https://pinterest.com/pin/...' -f audio")


def main():
    parser = argparse.ArgumentParser(description='Multi-Platform Social Media Downloader')
    parser.add_argument('url', nargs='?', help='URL to download')
    parser.add_argument('-f', '--format', choices=['video', 'audio'], default='video',
                        help='Download format: video or audio (default: video)')
    parser.add_argument('-q', '--quality', choices=['best', '1080p', '720p', '480p', '360p'],
                        default='best', help='Video quality (default: best)')
    parser.add_argument('-o', '--output', default='./downloads',
                        help='Output directory (default: ./downloads)')
    parser.add_argument('-p', '--playlist', action='store_true',
                        help='Download playlist/channel')
    parser.add_argument('--max-downloads', type=int, default=20,
                        help='Maximum number of downloads for playlist (default: 20)')
    parser.add_argument('--list-platforms', action='store_true',
                        help='List all supported platforms')
    parser.add_argument('--info', action='store_true',
                        help='Show media information without downloading')
    
    args = parser.parse_args()
    
    # Create downloader instance
    downloader = MultiPlatformDownloader(args.output)
    
    if args.list_platforms:
        downloader.list_supported_platforms()
        return
    
    if not args.url:
        print("❌ Error: URL is required")
        print("Use --help for usage information or --list-platforms to see supported platforms")
        return
    
    if args.info:
        # Just show media info
        info = downloader.get_media_info(args.url)
        if info:
            print("📹 Media Information:")
            print(f"Title: {info['title']}")
            print(f"Creator: {info['uploader']}")
            print(f"Duration: {info['duration']} seconds")
            print(f"Views: {info['view_count']:,}")
            print(f"Upload Date: {info['upload_date']}")
            print(f"Platform: {info['platform']}")
        return
    
    print("🌟 Multi-Platform Social Media Downloader")
    print(f"📁 Download directory: {args.output}")
    print(f"🎯 Format: {args.format}")
    if args.format == 'video':
        print(f"📊 Quality: {args.quality}")
    print("-" * 50)
    
    if args.playlist:
        downloader.download_playlist(args.url, args.max_downloads)
    else:
        downloader.download_media(args.url, args.quality, args.format)


def interactive_mode():
    """Interactive mode for easier usage"""
    print("🌟 Multi-Platform Social Media Downloader")
    print("=" * 50)
    
    downloader = MultiPlatformDownloader()
    
    while True:
        try:
            print("\n📋 OPTIONS:")
            print("1. Download single video/media")
            print("2. Download playlist/channel")
            print("3. Get media information")
            print("4. List supported platforms")
            print("5. Exit")
            
            choice = input("\n🎯 Choose option (1-5): ").strip()
            
            if choice == '5':
                print("👋 Goodbye!")
                break
            elif choice == '4':
                downloader.list_supported_platforms()
                continue
            elif choice in ['1', '2', '3']:
                url = input("\n📎 Enter URL: ").strip()
                if not url:
                    print("❌ URL cannot be empty!")
                    continue
                
                if choice == '1':
                    quality = input("📊 Quality (best/1080p/720p/480p/360p) [best]: ").strip() or 'best'
                    format_type = input("🎥 Format (video/audio) [video]: ").strip() or 'video'
                    downloader.download_media(url, quality, format_type)
                elif choice == '2':
                    max_dl = input("🔢 Max downloads [20]: ").strip()
                    max_downloads = int(max_dl) if max_dl.isdigit() else 20
                    downloader.download_playlist(url, max_downloads)
                elif choice == '3':
                    info = downloader.get_media_info(url)
                    if info:
                        print("\n📹 Media Information:")
                        for key, value in info.items():
                            print(f"{key.replace('_', ' ').title()}: {value}")
            else:
                print("❌ Invalid option! Please choose 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, start interactive mode
        interactive_mode()
    else:
        main() 