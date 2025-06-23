#!/usr/bin/env python3
"""
Snapchat Content Downloader
Downloads public Snapchat content using yt-dlp
Note: Limited to public/spotlight content due to platform restrictions
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class SnapchatDownloader:
    def __init__(self, download_path="./downloads/snapchat"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def get_content_info(self, url):
        """Get Snapchat content information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Snapchat Content'),
                'description': info.get('description', ''),
                'uploader': info.get('uploader', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'thumbnail': info.get('thumbnail', '')
            }
        except Exception as e:
            print(f"Error getting content info: {e}")
            return None

    def download_spotlight(self, url, quality='best'):
        """Download Snapchat Spotlight content"""
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(self.download_path / 'spotlight/%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--write-thumbnail',
            '--progress',
            url
        ]

        try:
            print(f"👻 Starting Snapchat Spotlight download...")
            print(f"📊 Quality: {quality}")
            
            # Get content info first
            info = self.get_content_info(url)
            if info:
                print(f"📹 Title: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                print(f"⏱️  Duration: {info['duration']} seconds")
                print(f"👀 Views: {info['view_count']:,}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ Snapchat download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Snapchat has limited public content available")
            print("   Only Spotlight and some public content can be downloaded")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_public_story(self, url):
        """Download public Snapchat story (if available)"""
        
        cmd = [
            'yt-dlp',
            '--output', str(self.download_path / 'stories/%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]

        try:
            print(f"👻 Starting public story download...")
            result = subprocess.run(cmd, check=True)
            print("✅ Story download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Most Snapchat stories are private and cannot be downloaded")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def show_limitations(self):
        """Show Snapchat download limitations"""
        print("\n⚠️  Snapchat Download Limitations:")
        print("=" * 40)
        print("🔒 Private snaps: Not accessible")
        print("🔒 Private stories: Not accessible") 
        print("🔒 Direct messages: Not accessible")
        print("✅ Spotlight content: May be accessible")
        print("✅ Some public content: May be accessible")
        print("\n💡 Legal Note:")
        print("   Only download content you have permission to download")
        print("   Respect privacy and terms of service")

    def extract_info_only(self, url):
        """Extract information without downloading"""
        info = self.get_content_info(url)
        if info:
            print("\n👻 Snapchat Content Information:")
            print("=" * 40)
            for key, value in info.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print("❌ Could not extract content information")


def main():
    print("👻 Snapchat Content Downloader")
    print("=" * 35)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Spotlight: python3 snapchat_downloader.py <spotlight_url>")
        print("2. Public story: python3 snapchat_downloader.py <story_url> story")
        print("3. Info only: python3 snapchat_downloader.py <url> --info")
        print("4. Show limitations: python3 snapchat_downloader.py --limitations")
        print("\nExamples:")
        print("python3 snapchat_downloader.py 'https://snapchat.com/spotlight/...'")
        print("python3 snapchat_downloader.py 'https://story.snapchat.com/...' story")
        print("\n⚠️  Note: Limited to public/spotlight content only")
        sys.exit(1)
    
    downloader = SnapchatDownloader()
    
    if sys.argv[1] == '--limitations':
        downloader.show_limitations()
        return
    
    url = sys.argv[1]
    
    # Check for flags
    if '--info' in sys.argv:
        downloader.extract_info_only(url)
    elif len(sys.argv) >= 3 and sys.argv[2] == 'story':
        downloader.download_public_story(url)
    else:
        # Spotlight download
        quality = input("Quality (best/720p/480p/360p) [best]: ").strip() or 'best'
        downloader.download_spotlight(url, quality)


if __name__ == "__main__":
    main() 