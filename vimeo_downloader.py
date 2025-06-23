#!/usr/bin/env python3
"""
Vimeo Video Downloader
Handles Vimeo-specific format issues and downloads
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class VimeoDownloader:
    def __init__(self, download_path="./downloads/vimeo"):
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
        """Get Vimeo video information"""
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
                'upload_date': info.get('upload_date', 'Unknown')
            }
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None

    def get_available_formats(self, url):
        """Get available formats for Vimeo video"""
        try:
            cmd = ['yt-dlp', '--list-formats', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            return result.stdout
        except Exception as e:
            print(f"Error getting formats: {e}")
            return None

    def download_video(self, url, quality='720p'):
        """Download Vimeo video with proper format handling"""
        
        # Quality format mapping for Vimeo
        quality_mapping = {
            '1080p': 'hls-fastly_skyfire-1926+hls-fastly_skyfire-audio-high-English',
            '720p': 'hls-fastly_skyfire-1926+hls-fastly_skyfire-audio-high-English', 
            '540p': 'hls-fastly_skyfire-1164+hls-fastly_skyfire-audio-high-English',
            '360p': 'hls-fastly_skyfire-664+hls-fastly_skyfire-audio-high-English',
            '240p': 'hls-fastly_skyfire-415+hls-fastly_skyfire-audio-high-English',
            'best': 'best[height<=1080]/best',
            'audio': 'hls-fastly_skyfire-audio-high-English'
        }
        
        format_selector = quality_mapping.get(quality, 'best[height<=720]/best')
        
        cmd = [
            'yt-dlp',
            '-f', format_selector,
            '--output', str(self.download_path / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            '--merge-output-format', 'mp4',
            url
        ]

        try:
            print(f"🎬 Starting Vimeo download...")
            print(f"📊 Quality: {quality}")
            
            # Get video info first
            info = self.get_video_info(url)
            if info:
                print(f"📹 Title: {info['title']}")
                print(f"👤 Uploader: {info['uploader']}")
                print(f"⏱️  Duration: {info['duration']} seconds")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ Vimeo download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("Trying alternative method...")
            self.download_fallback(url)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_fallback(self, url):
        """Fallback method for problematic Vimeo videos"""
        cmd = [
            'yt-dlp',
            '-f', 'best/worst',
            '--output', str(self.download_path / '%(title)s.%(ext)s'),
            '--ignore-errors',
            url
        ]
        
        try:
            result = subprocess.run(cmd, check=True)
            print("✅ Fallback download successful!")
        except Exception as e:
            print(f"❌ Fallback also failed: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vimeo_downloader.py <vimeo_url> [quality]")
        print("Quality options: 1080p, 720p, 540p, 360p, 240p, audio")
        sys.exit(1)
    
    url = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else '720p'
    
    downloader = VimeoDownloader()
    
    print("🎬 Vimeo Video Downloader")
    print("=" * 30)
    
    downloader.download_video(url, quality)


if __name__ == "__main__":
    main() 