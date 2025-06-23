#!/usr/bin/env python3
"""
Streaming & Emerging Platforms Downloader
Supports: Periscope, Zynn, StreamYard, and other live/streaming platforms
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Optional import - fallback if not available
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class StreamingPlatformsDownloader:
    def __init__(self, download_path="./downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Platform information
        self.platform_info = {
            'periscope': {
                'name': 'Periscope (Twitter Live)',
                'status': 'Discontinued',
                'note': 'Service shut down in 2021'
            },
            'zynn': {
                'name': 'Zynn',
                'status': 'Discontinued', 
                'note': 'App removed from stores'
            },
            'streamyard': {
                'name': 'StreamYard',
                'status': 'Streaming Tool',
                'note': 'Not a content platform'
            }
        }
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def show_platform_status(self):
        """Show status of streaming platforms"""
        print("\n📡 Streaming Platforms Status:")
        print("=" * 45)
        
        platforms = [
            ("📡 Periscope", "Twitter's live streaming", "❌ Discontinued (2021)"),
            ("🎬 Zynn", "Short video app", "❌ Removed from stores"),
            ("🎥 StreamYard", "Live streaming tool", "⚠️ Streaming service only"),
            ("📺 YouNow", "Live streaming platform", "⚠️ Limited support"),
            ("🎮 Trovo", "Gaming live streams", "⚠️ Live content only"),
            ("📱 Live.ly", "Musical.ly successor", "❌ Merged with TikTok"),
            ("🎵 Smule", "Music collaboration", "⚠️ App-based content"),
            ("📹 Bigo Live", "Live streaming", "⚠️ Limited download support")
        ]
        
        for platform, description, status in platforms:
            print(f"{platform:<15} - {description:<25} [{status}]")

    def handle_periscope(self, url):
        """Handle Periscope URLs (discontinued platform)"""
        print("📡 Periscope Analysis:")
        print("=" * 25)
        print("❌ Periscope service was discontinued in March 2021")
        print("💡 Twitter integrated live streaming into main platform")
        print("🔗 Try Twitter live stream URLs instead")
        print("\nAlternatives:")
        print("- Twitter live streams: twitter.com/i/broadcasts/...")
        print("- Twitter Spaces: twitter.com/i/spaces/...")

    def handle_zynn(self, url):
        """Handle Zynn URLs (discontinued platform)"""
        print("🎬 Zynn Analysis:")
        print("=" * 20)
        print("❌ Zynn app was removed from app stores")
        print("💡 Platform faced controversy and shut down")
        print("🔗 Content may have migrated to other platforms")
        print("\nAlternatives:")
        print("- TikTok: tiktok.com")
        print("- Instagram Reels: instagram.com")
        print("- YouTube Shorts: youtube.com")

    def handle_streamyard(self, url):
        """Handle StreamYard (streaming tool, not content platform)"""
        print("🎥 StreamYard Analysis:")
        print("=" * 25)
        print("⚠️ StreamYard is a live streaming production tool")
        print("💡 It's not a content hosting platform")
        print("🔗 Content is streamed to other platforms")
        print("\nTo download StreamYard content:")
        print("- Find the destination platform (YouTube, Facebook, etc.)")
        print("- Use appropriate downloader for that platform")

    def try_live_stream_download(self, url):
        """Attempt to download live stream content"""
        platform_dir = self.download_path / 'live_streams'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '--live-from-start',
            '--output', str(platform_dir / '%(uploader)s/%(title)s_%(timestamp)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"📡 Attempting live stream download...")
            print("⚠️ This may take time for live content")
            result = subprocess.run(cmd, check=True)
            print("✅ Live stream download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Live stream download failed: {e}")
            print("💡 Live streams may not be downloadable")

    def download_archived_stream(self, url, quality='best'):
        """Download archived/recorded streams"""
        platform_dir = self.download_path / 'archived_streams'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--write-thumbnail',
            '--progress',
            url
        ]
        
        try:
            print(f"📼 Starting archived stream download...")
            result = subprocess.run(cmd, check=True)
            print("✅ Archived stream download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def analyze_url(self, url):
        """Analyze URL and determine best action"""
        url_lower = url.lower()
        
        print(f"🔍 Analyzing URL: {url[:50]}...")
        print("=" * 50)
        
        # Check for discontinued platforms
        if any(platform in url_lower for platform in ['periscope', 'pscp.tv']):
            self.handle_periscope(url)
            return
        
        if 'zynn' in url_lower:
            self.handle_zynn(url)
            return
        
        if 'streamyard' in url_lower:
            self.handle_streamyard(url)
            return
        
        # Check for live streaming keywords
        live_keywords = ['live', 'stream', 'broadcast', 'webinar']
        if any(keyword in url_lower for keyword in live_keywords):
            print("📡 Detected potential live content")
            choice = input("Try live stream download? (y/n) [n]: ").strip().lower()
            if choice == 'y':
                self.try_live_stream_download(url)
            else:
                self.download_archived_stream(url)
        else:
            self.download_archived_stream(url)

    def show_alternatives(self):
        """Show alternative platforms for discontinued services"""
        print("\n🔄 Platform Alternatives:")
        print("=" * 30)
        
        alternatives = [
            ("Periscope → Twitter Live", "twitter.com/i/broadcasts/"),
            ("Zynn → TikTok", "tiktok.com"),
            ("Zynn → Instagram Reels", "instagram.com/reels/"),
            ("Live.ly → TikTok", "tiktok.com"),
            ("Vine → TikTok/Instagram", "Short video content"),
            ("Musical.ly → TikTok", "tiktok.com")
        ]
        
        for old_new, url_pattern in alternatives:
            print(f"📱 {old_new:<25} - {url_pattern}")

    def emergency_download(self, url):
        """Emergency download for any platform"""
        cmd = [
            'yt-dlp',
            '--output', str(self.download_path / 'emergency/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--ignore-errors',
            '--no-warnings',
            url
        ]
        
        try:
            print(f"🚨 Emergency download attempt...")
            result = subprocess.run(cmd, check=True)
            print("✅ Emergency download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Emergency download failed: {e}")


def main():
    print("📡 Streaming & Emerging Platforms Downloader")
    print("=" * 50)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Analyze URL: python3 streaming_platforms_downloader.py <url>")
        print("2. Show platform status: python3 streaming_platforms_downloader.py --status")
        print("3. Show alternatives: python3 streaming_platforms_downloader.py --alternatives")
        print("4. Emergency download: python3 streaming_platforms_downloader.py <url> --emergency")
        print("\nNote: Many streaming platforms are discontinued or live-only")
        sys.exit(1)
    
    downloader = StreamingPlatformsDownloader()
    
    if sys.argv[1] == '--status':
        downloader.show_platform_status()
        return
    elif sys.argv[1] == '--alternatives':
        downloader.show_alternatives()
        return
    
    url = sys.argv[1]
    
    if len(sys.argv) > 2 and sys.argv[2] == '--emergency':
        downloader.emergency_download(url)
    else:
        downloader.analyze_url(url)


if __name__ == "__main__":
    main() 