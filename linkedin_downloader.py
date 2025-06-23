#!/usr/bin/env python3
"""
LinkedIn Content Downloader
Downloads videos and content from LinkedIn using yt-dlp
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class LinkedInDownloader:
    def __init__(self, download_path="./downloads/linkedin"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def get_post_info(self, url):
        """Get LinkedIn post information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'LinkedIn Post'),
                'description': info.get('description', ''),
                'uploader': info.get('uploader', 'Unknown'),
                'upload_date': info.get('upload_date', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0)
            }
        except Exception as e:
            print(f"Error getting post info: {e}")
            return None

    def download_post(self, url, quality='best'):
        """Download LinkedIn post content"""
        
        # Quality mapping for LinkedIn
        quality_mapping = {
            '720p': 'best[height<=720]',
            '480p': 'best[height<=480]',
            '360p': 'best[height<=360]',
            'best': 'best',
            'audio': 'bestaudio'
        }
        
        format_selector = quality_mapping.get(quality, 'best')
        
        cmd = [
            'yt-dlp',
            '-f', format_selector,
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]

        try:
            print(f"💼 Starting LinkedIn download...")
            print(f"📊 Quality: {quality}")
            
            # Get post info first
            info = self.get_post_info(url)
            if info:
                print(f"📋 Title: {info['title']}")
                print(f"👤 Author: {info['uploader']}")
                if info['duration']:
                    print(f"⏱️  Duration: {info['duration']} seconds")
                print(f"📅 Upload Date: {info['upload_date']}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ LinkedIn download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 LinkedIn content often requires authentication")
            print("   Try using --cookies or logging in via browser")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_with_cookies(self, url, cookies_file, quality='best'):
        """Download LinkedIn content with cookies for authentication"""
        
        quality_mapping = {
            '720p': 'best[height<=720]',
            '480p': 'best[height<=480]',
            '360p': 'best[height<=360]',
            'best': 'best'
        }
        
        format_selector = quality_mapping.get(quality, 'best')
        
        cmd = [
            'yt-dlp',
            '-f', format_selector,
            '--cookies', cookies_file,
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]

        try:
            print(f"💼 Starting authenticated LinkedIn download...")
            print(f"🍪 Using cookies: {cookies_file}")
            
            result = subprocess.run(cmd, check=True)
            print("✅ Authenticated LinkedIn download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def extract_info_only(self, url):
        """Extract LinkedIn post information without downloading"""
        info = self.get_post_info(url)
        if info:
            print("\n💼 LinkedIn Post Information:")
            print("=" * 40)
            for key, value in info.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print("❌ Could not extract post information")


def main():
    print("💼 LinkedIn Content Downloader")
    print("=" * 35)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Basic: python3 linkedin_downloader.py <linkedin_url>")
        print("2. With cookies: python3 linkedin_downloader.py <linkedin_url> --cookies <cookies_file>")
        print("3. Info only: python3 linkedin_downloader.py <linkedin_url> --info")
        print("\nExamples:")
        print("python3 linkedin_downloader.py 'https://linkedin.com/posts/...'")
        print("python3 linkedin_downloader.py 'https://linkedin.com/posts/...' --cookies cookies.txt")
        print("\n💡 Note: LinkedIn often requires authentication for content access")
        sys.exit(1)
    
    downloader = LinkedInDownloader()
    url = sys.argv[1]
    
    # Check for flags
    if '--info' in sys.argv:
        downloader.extract_info_only(url)
    elif '--cookies' in sys.argv:
        try:
            cookies_index = sys.argv.index('--cookies')
            cookies_file = sys.argv[cookies_index + 1]
            quality = input("Quality (best/720p/480p/360p) [best]: ").strip() or 'best'
            downloader.download_with_cookies(url, cookies_file, quality)
        except (IndexError, ValueError):
            print("❌ Error: Please provide cookies file after --cookies flag")
    else:
        # Basic download
        quality = input("Quality (best/720p/480p/360p/audio) [best]: ").strip() or 'best'
        downloader.download_post(url, quality)


if __name__ == "__main__":
    main() 