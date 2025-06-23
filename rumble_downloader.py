#!/usr/bin/env python3
"""
Rumble Video Downloader
Downloads videos from Rumble.com using yt-dlp
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class RumbleDownloader:
    def __init__(self, download_path="./downloads/rumble"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def get_video_info(self, url):
        """Get Rumble video information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Unknown'),
                'description': info.get('description', ''),
                'uploader': info.get('uploader', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'thumbnail': info.get('thumbnail', '')
            }
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None

    def download_video(self, url, quality='best'):
        """Download Rumble video"""
        
        # Quality mapping for Rumble
        quality_mapping = {
            '1080p': 'best[height<=1080]',
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
            '--write-thumbnail',
            '--progress',
            url
        ]

        try:
            print(f"🎯 Starting Rumble download...")
            print(f"📊 Quality: {quality}")
            
            # Get video info first
            info = self.get_video_info(url)
            if info:
                print(f"📹 Title: {info['title']}")
                print(f"👤 Uploader: {info['uploader']}")
                print(f"⏱️  Duration: {info['duration']} seconds")
                print(f"👀 Views: {info['view_count']:,}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ Rumble download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_channel(self, url, max_downloads=50):
        """Download videos from Rumble channel"""
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--progress',
            url
        ]
        
        try:
            print(f"📋 Downloading Rumble channel...")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ Channel download completed!")
        except Exception as e:
            print(f"❌ Channel download failed: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rumble_downloader.py <rumble_url> [quality]")
        print("Quality options: best, 1080p, 720p, 480p, 360p, audio")
        sys.exit(1)
    
    url = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else 'best'
    
    downloader = RumbleDownloader()
    
    print("🎯 Rumble Video Downloader")
    print("=" * 30)
    
    if '/c/' in url or '/user/' in url:
        # Channel URL
        max_downloads = int(input("Max downloads [50]: ") or 50)
        downloader.download_channel(url, max_downloads)
    else:
        # Single video
        downloader.download_video(url, quality)


if __name__ == "__main__":
    main() 