#!/usr/bin/env python3
"""
Likee Short Video Downloader
Downloads short videos from Likee using yt-dlp
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class LikeeDownloader:
    def __init__(self, download_path="./downloads/likee"):
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
        """Get Likee video information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'Likee Video'),
                'description': info.get('description', ''),
                'uploader': info.get('uploader', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'like_count': info.get('like_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'thumbnail': info.get('thumbnail', '')
            }
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None

    def download_video(self, url, quality='best', format_type='video'):
        """Download Likee video"""
        
        cmd = ['yt-dlp']
        
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '128K'
            ])
        else:
            # Quality mapping for Likee (short videos usually have limited quality options)
            quality_mapping = {
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
            print(f"❤️ Starting Likee download...")
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
                print(f"❤️ Likes: {info['like_count']:,}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ Likee download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Some Likee content may be private or region-restricted")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_user_videos(self, username, max_downloads=50):
        """Download videos from Likee user"""
        user_url = f"https://likee.video/@{username}"
        
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

    def download_hashtag_videos(self, hashtag, max_downloads=20):
        """Download videos from Likee hashtag"""
        hashtag_url = f"https://likee.video/hashtag/{hashtag}"
        
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(self.download_path / f'hashtag_{hashtag}/%(uploader)s_%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--progress',
            hashtag_url
        ]
        
        try:
            print(f"#️⃣ Downloading videos from hashtag: #{hashtag}")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ Hashtag videos download completed!")
        except Exception as e:
            print(f"❌ Hashtag videos download failed: {e}")


def main():
    print("❤️ Likee Short Video Downloader")
    print("=" * 35)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Single video: python3 likee_downloader.py <likee_url>")
        print("2. User videos: python3 likee_downloader.py <username> user")
        print("3. Hashtag videos: python3 likee_downloader.py <hashtag> hashtag")
        print("\nExamples:")
        print("python3 likee_downloader.py 'https://likee.video/v/...'")
        print("python3 likee_downloader.py 'username' user")
        print("python3 likee_downloader.py 'dance' hashtag")
        sys.exit(1)
    
    downloader = LikeeDownloader()
    
    if len(sys.argv) >= 3 and sys.argv[2] == 'user':
        # User videos download
        username = sys.argv[1]
        max_downloads = int(input("Max downloads [50]: ") or 50)
        downloader.download_user_videos(username, max_downloads)
    elif len(sys.argv) >= 3 and sys.argv[2] == 'hashtag':
        # Hashtag videos download
        hashtag = sys.argv[1]
        max_downloads = int(input("Max downloads [20]: ") or 20)
        downloader.download_hashtag_videos(hashtag, max_downloads)
    else:
        # Single video download
        url = sys.argv[1]
        format_type = input("Format (video/audio) [video]: ").strip() or 'video'
        
        if format_type == 'video':
            quality = input("Quality (best/720p/480p/360p) [best]: ").strip() or 'best'
            downloader.download_video(url, quality, format_type)
        else:
            downloader.download_video(url, format_type=format_type)


if __name__ == "__main__":
    main() 