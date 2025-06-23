#!/usr/bin/env python3
"""
PeerTube Video Downloader
Downloads videos from PeerTube instances using yt-dlp
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from urllib.parse import urlparse


class PeerTubeDownloader:
    def __init__(self, download_path="./downloads/peertube"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def detect_peertube_instance(self, url):
        """Detect PeerTube instance from URL"""
        domain = urlparse(url).netloc
        return domain

    def get_video_info(self, url):
        """Get PeerTube video information"""
        try:
            cmd = ['yt-dlp', '--dump-json', '--no-warnings', url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            info_line = result.stdout.strip().split('\n')[0]
            info = json.loads(info_line)
            
            return {
                'title': info.get('title', 'PeerTube Video'),
                'description': info.get('description', ''),
                'uploader': info.get('uploader', 'Unknown'),
                'channel': info.get('channel', 'Unknown'),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown'),
                'thumbnail': info.get('thumbnail', ''),
                'instance': self.detect_peertube_instance(url)
            }
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None

    def download_video(self, url, quality='best', format_type='video'):
        """Download PeerTube video"""
        
        instance = self.detect_peertube_instance(url)
        instance_dir = self.download_path / instance
        instance_dir.mkdir(exist_ok=True)
        
        cmd = ['yt-dlp']
        
        if format_type == 'audio':
            cmd.extend([
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '192K'
            ])
        else:
            # Quality mapping for PeerTube
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
            '--output', str(instance_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--write-thumbnail',
            '--progress',
            url
        ])

        try:
            print(f"🌐 Starting PeerTube download...")
            print(f"🏠 Instance: {instance}")
            print(f"🎯 Format: {format_type}")
            if format_type == 'video':
                print(f"📊 Quality: {quality}")
            
            # Get video info first
            info = self.get_video_info(url)
            if info:
                print(f"📹 Title: {info['title']}")
                print(f"👤 Uploader: {info['uploader']}")
                print(f"📺 Channel: {info['channel']}")
                print(f"⏱️  Duration: {info['duration']} seconds")
                print(f"👀 Views: {info['view_count']:,}")
                print("-" * 50)
            
            # Run download
            result = subprocess.run(cmd, check=True)
            print("✅ PeerTube download successful!")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed with exit code {e.returncode}")
            print("💡 Some PeerTube content may be private or instance-restricted")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def download_channel(self, url, max_downloads=50):
        """Download videos from PeerTube channel"""
        instance = self.detect_peertube_instance(url)
        instance_dir = self.download_path / instance
        
        cmd = [
            'yt-dlp',
            '--playlist-end', str(max_downloads),
            '--output', str(instance_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--progress',
            url
        ]
        
        try:
            print(f"📺 Downloading PeerTube channel...")
            print(f"🏠 Instance: {instance}")
            print(f"🔢 Max downloads: {max_downloads}")
            result = subprocess.run(cmd, check=True)
            print("✅ Channel download completed!")
        except Exception as e:
            print(f"❌ Channel download failed: {e}")

    def download_instance_trending(self, instance_url, max_downloads=20):
        """Download trending videos from PeerTube instance"""
        trending_url = f"{instance_url.rstrip('/')}/api/v1/videos?sort=-trending"
        
        try:
            print(f"🔥 Downloading trending videos from: {instance_url}")
            print(f"🔢 Max downloads: {max_downloads}")
            print("💡 Note: This feature may require API access")
            print("   Try using specific video/channel URLs instead")
        except Exception as e:
            print(f"❌ Trending download failed: {e}")

    def list_popular_instances(self):
        """List popular PeerTube instances"""
        print("\n🌐 Popular PeerTube Instances:")
        print("=" * 40)
        
        instances = [
            ("framapiaf.org", "French general instance"),
            ("peertube.tv", "General PeerTube instance"),
            ("tube.nuagelibre.fr", "French tech-focused"),
            ("video.ploud.fr", "French general instance"),
            ("peertube.social", "English general instance"),
            ("tube.jeena.net", "Personal instance"),
            ("peertube.linuxrocks.online", "Linux community"),
            ("video.blender.org", "Blender Foundation")
        ]
        
        for domain, description in instances:
            print(f"🏠 {domain:<25} - {description}")
        
        print("\n💡 Usage Examples:")
        print("python3 peertube_downloader.py 'https://framapiaf.org/videos/watch/...'")
        print("python3 peertube_downloader.py 'https://peertube.tv/c/channel-name/videos' channel")


def main():
    print("🌐 PeerTube Video Downloader")
    print("=" * 35)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Single video: python3 peertube_downloader.py <peertube_url>")
        print("2. Channel: python3 peertube_downloader.py <channel_url> channel")
        print("3. List instances: python3 peertube_downloader.py --list-instances")
        print("\nExamples:")
        print("python3 peertube_downloader.py 'https://framapiaf.org/videos/watch/...'")
        print("python3 peertube_downloader.py 'https://peertube.tv/c/channel/' channel")
        sys.exit(1)
    
    downloader = PeerTubeDownloader()
    
    if sys.argv[1] == '--list-instances':
        downloader.list_popular_instances()
        return
    
    if len(sys.argv) >= 3 and sys.argv[2] == 'channel':
        # Channel download
        channel_url = sys.argv[1]
        max_downloads = int(input("Max downloads [50]: ") or 50)
        downloader.download_channel(channel_url, max_downloads)
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