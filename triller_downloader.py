#!/usr/bin/env python3
"""
Triller Music Video Downloader
Downloads music videos and content from Triller using yt-dlp
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class TrillerDownloader:
    def __init__(self, download_path="./downloads/triller"):
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
        """Get Triller video information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Triller Video'),
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

    def download_video(self, url, quality='best', format_type='video'):
        """Download Triller video"""
        
        cmd = ['yt-dlp']
        
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '192K'
            ])
        else:
            # Quality mapping for Triller
            quality_mapping = {
                '1080p': 'best[height<=1080]',
                '720p': 'best[height<=720]',
                '480p': 'best[height<=480]',
                '360p': 'best[height<=360]',
                'best': 'best'
            }
            
            format_selector = quality_mapping.get(quality, 'best')
            cmd.extend(['-f', format_selector])
        
        cmd.extend([
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--write-thumbnail',
            '--progress',
            url
        ])

        try:
            print(f"🎵 Starting Triller download...")
            print(f"🎯 Format: {format_type}")
            if format_type == 'video':
                print(f"📊 Quality: {quality}")
            
            # Get video info first
            info = self.get_video_info(url)
            if info:
                print(f"📹 Title: {info['title']}")
                print(f"👤 Creator: {info['uploader']}")
                print(f"⏱️  Duration: {info['duration']} seconds")
                print(f"👀 Views: {info['view_count']:,}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ Triller download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Some Triller content may be private or region-restricted")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_user_videos(self, username, max_downloads=30):
        """Download videos from Triller user"""
        user_url = f"https://triller.co/@{username}"
        
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
            print(f"👤 Downloading videos from user: {username}")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ User videos download completed!")
        except Exception as e:
            print(f"❌ User videos download failed: {e}")


def main():
    print("🎵 Triller Music Video Downloader")
    print("=" * 35)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Single video: python3 triller_downloader.py <triller_url>")
        print("2. User videos: python3 triller_downloader.py <username> user")
        print("\nExamples:")
        print("python3 triller_downloader.py 'https://triller.co/v/...'")
        print("python3 triller_downloader.py 'username' user")
        sys.exit(1)
    
    downloader = TrillerDownloader()
    
    if len(sys.argv) >= 3 and sys.argv[2] == 'user':
        # User videos download
        username = sys.argv[1]
        max_downloads = int(input("Max downloads [30]: ") or 30)
        downloader.download_user_videos(username, max_downloads)
    else:
        # Single video download
        url = sys.argv[1]
        format_type = input("Format (video/audio) [video]: ").strip() or 'video'
        
        if format_type == 'video':
            quality = input("Quality (best/1080p/720p/480p/360p) [best]: ").strip() or 'best'
            downloader.download_video(url, quality, format_type)
        else:
            downloader.download_video(url, format_type=format_type)


if __name__ == "__main__":
    main() 