#!/usr/bin/env python3
"""
Instagram Media Downloader
A simple script to download Instagram posts, reels, stories, and IGTV using yt-dlp
"""

import os
import sys
import argparse
import subprocess
import json
from pathlib import Path


class InstagramDownloader:
    def __init__(self, download_path="./instagram_downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed or not found in PATH")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)
        
    def get_media_info(self, url):
        """Get Instagram media information without downloading"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Parse the first line of JSON output
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Instagram Media'),
                'description': info.get('description', 'No description'),
                'uploader': info.get('uploader', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'like_count': info.get('like_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'formats': len(info.get('formats', []))
            }
        except Exception as e:
            print(f"Error getting media info: {e}")
            return None

    def download_media(self, url, quality='best', format_type='video'):
        """Download Instagram media"""
        
        cmd = ['yt-dlp']
        
        # Configure download options based on format type
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '192K',
                '--format', 'bestaudio/best'
            ])
        elif format_type == 'image':
            # For Instagram photos/images
            cmd.extend([
                '--format', 'best',
                '--write-thumbnail',
                '--skip-download'  # Only download thumbnails for images
            ])
        else:
            # Video download options - Instagram specific format handling
            if quality == 'best':
                format_selector = 'best[ext=mp4]/best'
            elif quality == 'worst':
                format_selector = 'worst[ext=mp4]/worst'
            elif quality == 'medium':
                format_selector = 'best[height<=720][ext=mp4]/best[height<=720]/best'
            else:
                format_selector = 'best[ext=mp4]/best'
                
            cmd.extend(['--format', format_selector])

        # Add Instagram-specific options
        cmd.extend([
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ])

        try:
            print(f"Starting download from: {url}")
            
            # Get media info first
            info = self.get_media_info(url)
            if info:
                print(f"📱 Media: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                if info['like_count']:
                    print(f"❤️  Likes: {info['like_count']:,}")
                print("-" * 50)
            
            # Run the download command
            result = subprocess.run(cmd, check=True)
            print("✅ Download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Note: Some Instagram content may be private or require login")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_user_posts(self, username, max_downloads=10):
        """Download recent posts from a user (public profiles only)"""
        profile_url = f"https://www.instagram.com/{username}/"
        
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(self.download_path / f'{username}/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            profile_url
        ]

        try:
            print(f"Downloading recent posts from @{username}...")
            result = subprocess.run(cmd, check=True)
            print("✅ User posts download completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Note: User profile might be private or not exist")
        except Exception as e:
            print(f"❌ Download failed: {e}")


def main():
    parser = argparse.ArgumentParser(description='Instagram Media Downloader')
    parser.add_argument('url', nargs='?', help='Instagram URL to download')
    parser.add_argument('-f', '--format', choices=['video', 'audio', 'image'], default='video',
                        help='Download format (default: video)')
    parser.add_argument('-q', '--quality', choices=['best', 'medium', 'worst'],
                        default='best', help='Media quality (default: best)')
    parser.add_argument('-o', '--output', default='./instagram_downloads',
                        help='Output directory (default: ./instagram_downloads)')
    parser.add_argument('-u', '--user', help='Download recent posts from username')
    parser.add_argument('-n', '--number', type=int, default=10,
                        help='Number of posts to download from user (default: 10)')
    parser.add_argument('--info', action='store_true',
                        help='Show media information without downloading')
    
    args = parser.parse_args()
    
    # Create downloader instance
    downloader = InstagramDownloader(args.output)
    
    if args.user:
        # Download user posts
        print("📱 Instagram User Posts Downloader")
        print(f"👤 Username: @{args.user}")
        print(f"📊 Max posts: {args.number}")
        print("-" * 50)
        downloader.download_user_posts(args.user, args.number)
        return
    
    if not args.url:
        print("❌ Error: Please provide either a URL or username")
        parser.print_help()
        return
    
    if args.info:
        # Just show media info
        info = downloader.get_media_info(args.url)
        if info:
            print("📱 Instagram Media Information:")
            print(f"Title: {info['title']}")
            print(f"Creator: {info['uploader']}")
            print(f"Description: {info['description'][:100]}...")
            if info['duration']:
                print(f"Duration: {info['duration']} seconds")
            if info['like_count']:
                print(f"Likes: {info['like_count']:,}")
            print(f"Upload Date: {info['upload_date']}")
        return
    
    print("📱 Instagram Media Downloader Started")
    print(f"📁 Download directory: {args.output}")
    print(f"🎯 Format: {args.format}")
    print(f"📊 Quality: {args.quality}")
    print("-" * 50)
    
    downloader.download_media(args.url, args.quality, args.format)


def interactive_mode():
    """Interactive mode for easier usage"""
    print("📱 Instagram Media Downloader")
    print("=" * 40)
    
    while True:
        try:
            print("\n🎯 Select download type:")
            print("1. Single post/reel/story URL")
            print("2. User's recent posts (public profiles)")
            print("3. Exit")
            
            choice = input("Enter choice (1-3): ").strip()
            
            if choice == '3':
                print("👋 Goodbye!")
                break
            elif choice == '2':
                username = input("👤 Enter Instagram username (without @): ").strip()
                if not username:
                    continue
                    
                try:
                    max_posts = int(input("📊 Number of recent posts to download (default 10): ").strip() or "10")
                except ValueError:
                    max_posts = 10
                
                download_path = input("📁 Download directory (press Enter for ./instagram_downloads): ").strip()
                if not download_path:
                    download_path = "./instagram_downloads"
                    
                downloader = InstagramDownloader(download_path)
                downloader.download_user_posts(username, max_posts)
                
            elif choice == '1':
                url = input("📎 Enter Instagram URL: ").strip()
                if not url:
                    continue
                    
                # Download path
                download_path = input("📁 Download directory (press Enter for ./instagram_downloads): ").strip()
                if not download_path:
                    download_path = "./instagram_downloads"
                    
                downloader = InstagramDownloader(download_path)
                
                # Show media info first
                print("\n🔍 Getting media information...")
                info = downloader.get_media_info(url)
                if not info:
                    print("❌ Could not retrieve media information. Please check the URL.")
                    continue
                    
                print(f"\n📱 Media: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                
                # Format selection
                print("\n🎯 Select download format:")
                print("1. Video/Reel")
                print("2. Audio only")
                print("3. Image/Photo")
                
                format_choice = input("Enter choice (1-3): ").strip()
                format_map = {'1': 'video', '2': 'audio', '3': 'image'}
                format_type = format_map.get(format_choice, 'video')
                
                # Quality selection
                if format_type == 'video':
                    print("\n📊 Select quality:")
                    print("1. Best available")
                    print("2. Medium quality")
                    print("3. Lowest quality")
                    
                    quality_choice = input("Enter choice (1-3): ").strip()
                    quality_map = {'1': 'best', '2': 'medium', '3': 'worst'}
                    quality = quality_map.get(quality_choice, 'best')
                else:
                    quality = 'best'
                
                downloader.download_media(url, quality, format_type)
            else:
                print("❌ Invalid choice. Please try again.")
                
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