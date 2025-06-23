#!/usr/bin/env python3
"""
Pinterest Downloader
Downloads images and videos from Pinterest using yt-dlp
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class PinterestDownloader:
    def __init__(self, download_path="./downloads/pinterest"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def get_pin_info(self, url):
        """Get Pinterest pin information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Pinterest Pin'),
                'description': info.get('description', ''),
                'uploader': info.get('uploader', 'Unknown'),
                'upload_date': info.get('upload_date', 'Unknown'),
                'thumbnail': info.get('thumbnail', ''),
                'url': info.get('webpage_url', url)
            }
        except Exception as e:
            print(f"Error getting pin info: {e}")
            return None

    def download_pin(self, url, format_type='best'):
        """Download Pinterest pin (image or video)"""
        
        cmd = [
            'yt-dlp',
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        if format_type == 'image':
            # For images, just download the best quality
            cmd.extend(['--format', 'best'])
        elif format_type == 'video':
            # For videos, prefer mp4 format
            cmd.extend(['--format', 'best[ext=mp4]/best'])

        try:
            print(f"📌 Starting Pinterest download...")
            print(f"🎯 Format: {format_type}")
            
            # Get pin info first
            info = self.get_pin_info(url)
            if info:
                print(f"📋 Title: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                print(f"📅 Upload Date: {info['upload_date']}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ Pinterest download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Note: Some Pinterest content may require cookies for access")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_board(self, url, max_downloads=100):
        """Download Pinterest board"""
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(self.download_path / '%(uploader)s/%(playlist_title)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--progress',
            url
        ]
        
        try:
            print(f"📋 Downloading Pinterest board...")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ Board download completed!")
        except Exception as e:
            print(f"❌ Board download failed: {e}")
            print("💡 Note: Some boards may be private or require authentication")

    def download_user_pins(self, username, max_downloads=50):
        """Download all pins from a Pinterest user"""
        user_url = f"https://pinterest.com/{username}/"
        
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(self.download_path / f'{username}/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--progress',
            user_url
        ]
        
        try:
            print(f"👤 Downloading pins from user: {username}")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ User pins download completed!")
        except Exception as e:
            print(f"❌ User pins download failed: {e}")


def main():
    print("📌 Pinterest Downloader")
    print("=" * 30)
    
    if len(sys.argv) < 2:
        print("Usage options:")
        print("1. Single pin: python3 pinterest_downloader.py <pin_url>")
        print("2. Board: python3 pinterest_downloader.py <board_url> board")
        print("3. User pins: python3 pinterest_downloader.py <username> user")
        print("\nExamples:")
        print("python3 pinterest_downloader.py 'https://pinterest.com/pin/123456789/'")
        print("python3 pinterest_downloader.py 'https://pinterest.com/user/board-name/' board")
        print("python3 pinterest_downloader.py 'username' user")
        sys.exit(1)
    
    downloader = PinterestDownloader()
    
    if len(sys.argv) >= 3 and sys.argv[2] == 'board':
        # Board download
        board_url = sys.argv[1]
        max_downloads = int(input("Max downloads [100]: ") or 100)
        downloader.download_board(board_url, max_downloads)
    elif len(sys.argv) >= 3 and sys.argv[2] == 'user':
        # User pins download
        username = sys.argv[1]
        max_downloads = int(input("Max downloads [50]: ") or 50)
        downloader.download_user_pins(username, max_downloads)
    else:
        # Single pin download
        pin_url = sys.argv[1]
        format_type = input("Format (image/video/best) [best]: ").strip() or 'best'
        downloader.download_pin(pin_url, format_type)


if __name__ == "__main__":
    main() 