#!/usr/bin/env python3
"""
Twitter/X Media Downloader
A simple script to download Twitter/X videos, images, and GIFs using yt-dlp
"""

import os
import sys
import argparse
import subprocess
import json
from pathlib import Path


class TwitterDownloader:
    def __init__(self, download_path="./twitter_downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed or not found in PATH")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)
        
    def get_tweet_info(self, url):
        """Get Twitter/X media information without downloading"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Parse the first line of JSON output
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Twitter Media'),
                'description': info.get('description', 'No description'),
                'uploader': info.get('uploader', 'Unknown'),
                'uploader_id': info.get('uploader_id', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'like_count': info.get('like_count', 0),
                'repost_count': info.get('repost_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'formats': len(info.get('formats', []))
            }
        except Exception as e:
            print(f"Error getting tweet info: {e}")
            return None

    def download_media(self, url, quality='best', format_type='video'):
        """Download Twitter/X media"""
        
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
            # For Twitter images/photos
            cmd.extend([
                '--write-thumbnail',
                '--skip-download',  # Only download thumbnails for images
                '--format', 'best'
            ])
        else:
            # Video download options
            if quality == 'best':
                format_selector = 'best'
            elif quality == 'worst':
                format_selector = 'worst'
            elif quality == 'medium':
                format_selector = 'best[height<=720]'
            else:
                format_selector = 'best'
                
            cmd.extend(['--format', format_selector])

        # Add Twitter-specific options
        cmd.extend([
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ])

        try:
            print(f"Starting download from: {url}")
            
            # Get tweet info first
            info = self.get_tweet_info(url)
            if info:
                print(f"🐦 Tweet: {info['title']}")
                print(f"👤 User: @{info['uploader_id']} ({info['uploader']})")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                if info['like_count']:
                    print(f"❤️  Likes: {info['like_count']:,}")
                if info['repost_count']:
                    print(f"🔄 Retweets: {info['repost_count']:,}")
                print("-" * 50)
            
            # Run the download command
            result = subprocess.run(cmd, check=True)
            print("✅ Download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Note: Some Twitter content may be private or deleted")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_user_tweets(self, username, max_downloads=20):
        """Download recent media tweets from a user (public profiles only)"""
        profile_url = f"https://twitter.com/{username}"
        
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
            print(f"Downloading recent media tweets from @{username}...")
            result = subprocess.run(cmd, check=True)
            print("✅ User tweets download completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Note: User profile might be private, protected, or not exist")
        except Exception as e:
            print(f"❌ Download failed: {e}")

    def download_twitter_space(self, url):
        """Download Twitter Space audio"""
        cmd = [
            'yt-dlp',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--output', str(self.download_path / 'spaces/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]

        try:
            print(f"Downloading Twitter Space from: {url}")
            result = subprocess.run(cmd, check=True)
            print("✅ Twitter Space download completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Note: Twitter Space might be ended or private")
        except Exception as e:
            print(f"❌ Download failed: {e}")


def main():
    parser = argparse.ArgumentParser(description='Twitter/X Media Downloader')
    parser.add_argument('url', nargs='?', help='Twitter/X URL to download')
    parser.add_argument('-f', '--format', choices=['video', 'audio', 'image'], default='video',
                        help='Download format (default: video)')
    parser.add_argument('-q', '--quality', choices=['best', 'medium', 'worst'],
                        default='best', help='Media quality (default: best)')
    parser.add_argument('-o', '--output', default='./twitter_downloads',
                        help='Output directory (default: ./twitter_downloads)')
    parser.add_argument('-u', '--user', help='Download recent media tweets from username')
    parser.add_argument('-n', '--number', type=int, default=20,
                        help='Number of tweets to download from user (default: 20)')
    parser.add_argument('-s', '--space', action='store_true',
                        help='Download Twitter Space audio')
    parser.add_argument('--info', action='store_true',
                        help='Show tweet information without downloading')
    
    args = parser.parse_args()
    
    # Create downloader instance
    downloader = TwitterDownloader(args.output)
    
    if args.user:
        # Download user tweets
        print("🐦 Twitter User Media Downloader")
        print(f"👤 Username: @{args.user}")
        print(f"📊 Max tweets: {args.number}")
        print("-" * 50)
        downloader.download_user_tweets(args.user, args.number)
        return
    
    if not args.url:
        print("❌ Error: Please provide either a URL or username")
        parser.print_help()
        return
    
    if args.space:
        # Download Twitter Space
        downloader.download_twitter_space(args.url)
        return
    
    if args.info:
        # Just show tweet info
        info = downloader.get_tweet_info(args.url)
        if info:
            print("🐦 Twitter Media Information:")
            print(f"Title: {info['title']}")
            print(f"User: @{info['uploader_id']} ({info['uploader']})")
            print(f"Description: {info['description'][:100]}...")
            if info['duration']:
                print(f"Duration: {info['duration']} seconds")
            if info['like_count']:
                print(f"Likes: {info['like_count']:,}")
            if info['repost_count']:
                print(f"Retweets: {info['repost_count']:,}")
            print(f"Upload Date: {info['upload_date']}")
        return
    
    print("🐦 Twitter/X Media Downloader Started")
    print(f"📁 Download directory: {args.output}")
    print(f"🎯 Format: {args.format}")
    print(f"📊 Quality: {args.quality}")
    print("-" * 50)
    
    downloader.download_media(args.url, args.quality, args.format)


def interactive_mode():
    """Interactive mode for easier usage"""
    print("🐦 Twitter/X Media Downloader")
    print("=" * 40)
    
    while True:
        try:
            print("\n🎯 Select download type:")
            print("1. Single tweet URL")
            print("2. User's recent media tweets")
            print("3. Twitter Space audio")
            print("4. Exit")
            
            choice = input("Enter choice (1-4): ").strip()
            
            if choice == '4':
                print("👋 Goodbye!")
                break
            elif choice == '2':
                username = input("👤 Enter Twitter username (without @): ").strip()
                if not username:
                    continue
                    
                try:
                    max_tweets = int(input("📊 Number of recent tweets to download (default 20): ").strip() or "20")
                except ValueError:
                    max_tweets = 20
                
                download_path = input("📁 Download directory (press Enter for ./twitter_downloads): ").strip()
                if not download_path:
                    download_path = "./twitter_downloads"
                    
                downloader = TwitterDownloader(download_path)
                downloader.download_user_tweets(username, max_tweets)
                
            elif choice == '3':
                url = input("📎 Enter Twitter Space URL: ").strip()
                if not url:
                    continue
                    
                download_path = input("📁 Download directory (press Enter for ./twitter_downloads): ").strip()
                if not download_path:
                    download_path = "./twitter_downloads"
                    
                downloader = TwitterDownloader(download_path)
                downloader.download_twitter_space(url)
                
            elif choice == '1':
                url = input("📎 Enter Twitter/X URL: ").strip()
                if not url:
                    continue
                    
                # Download path
                download_path = input("📁 Download directory (press Enter for ./twitter_downloads): ").strip()
                if not download_path:
                    download_path = "./twitter_downloads"
                    
                downloader = TwitterDownloader(download_path)
                
                # Show tweet info first
                print("\n🔍 Getting tweet information...")
                info = downloader.get_tweet_info(url)
                if not info:
                    print("❌ Could not retrieve tweet information. Please check the URL.")
                    continue
                    
                print(f"\n🐦 Tweet: {info['title']}")
                print(f"👤 User: @{info['uploader_id']}")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                
                # Format selection
                print("\n🎯 Select download format:")
                print("1. Video")
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