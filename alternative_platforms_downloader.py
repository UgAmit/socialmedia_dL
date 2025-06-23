#!/usr/bin/env python3
"""
Alternative Platforms Downloader
Supports: Odysee, BitChute, Metacafe, Veoh, DTube, YouNow, Trovo, etc.
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class AlternativePlatformsDownloader:
    def __init__(self, download_path="./downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def download_odysee(self, url, quality='best'):
        """Download Odysee videos (LBRY blockchain platform)"""
        platform_dir = self.download_path / 'odysee'
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
            print(f"🌊 Starting Odysee download...")
            print(f"🌐 Platform: Odysee (LBRY)")
            result = subprocess.run(cmd, check=True)
            print("✅ Odysee download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def download_bitchute(self, url, quality='best'):
        """Download BitChute videos"""
        platform_dir = self.download_path / 'bitchute'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"🎬 Starting BitChute download...")
            print(f"🌐 Platform: BitChute")
            result = subprocess.run(cmd, check=True)
            print("✅ BitChute download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def download_metacafe(self, url, quality='best'):
        """Download Metacafe videos"""
        platform_dir = self.download_path / 'metacafe'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"🎥 Starting Metacafe download...")
            print(f"🌐 Platform: Metacafe")
            result = subprocess.run(cmd, check=True)
            print("✅ Metacafe download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def download_veoh(self, url, quality='best'):
        """Download Veoh videos"""
        platform_dir = self.download_path / 'veoh'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"📹 Starting Veoh download...")
            print(f"🌐 Platform: Veoh")
            result = subprocess.run(cmd, check=True)
            print("✅ Veoh download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def download_dtube(self, url):
        """Download DTube videos (blockchain platform)"""
        platform_dir = self.download_path / 'dtube'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"⛓️ Starting DTube download...")
            print(f"🌐 Platform: DTube (Decentralized)")
            result = subprocess.run(cmd, check=True)
            print("✅ DTube download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            print("💡 DTube may require IPFS connectivity")

    def download_younow(self, url):
        """Download YouNow streams/videos"""
        platform_dir = self.download_path / 'younow'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"📡 Starting YouNow download...")
            print(f"🌐 Platform: YouNow (Live streaming)")
            result = subprocess.run(cmd, check=True)
            print("✅ YouNow download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            print("💡 YouNow may be for live streams only")

    def download_trovo(self, url):
        """Download Trovo gaming streams"""
        platform_dir = self.download_path / 'trovo'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"🎮 Starting Trovo download...")
            print(f"🌐 Platform: Trovo (Gaming)")
            result = subprocess.run(cmd, check=True)
            print("✅ Trovo download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def download_vk_video(self, url, quality='best'):
        """Download VK (VKontakte) videos"""
        platform_dir = self.download_path / 'vk'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            url
        ]
        
        try:
            print(f"🇷🇺 Starting VK Video download...")
            print(f"🌐 Platform: VKontakte")
            result = subprocess.run(cmd, check=True)
            print("✅ VK Video download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            print("💡 VK may require authentication")

    def download_tubi(self, url):
        """Download Tubi content (if available)"""
        platform_dir = self.download_path / 'tubi'
        platform_dir.mkdir(exist_ok=True)
        
        print(f"📺 Tubi download attempt...")
        print("⚠️ Tubi is a streaming service with DRM protection")
        print("💡 Most content cannot be downloaded due to licensing")

    def auto_detect_and_download(self, url, quality='best'):
        """Auto-detect platform and download"""
        url_lower = url.lower()
        
        if 'odysee.com' in url_lower or 'lbry.tv' in url_lower:
            self.download_odysee(url, quality)
        elif 'bitchute.com' in url_lower:
            self.download_bitchute(url, quality)
        elif 'metacafe.com' in url_lower:
            self.download_metacafe(url, quality)
        elif 'veoh.com' in url_lower:
            self.download_veoh(url, quality)
        elif 'dtube' in url_lower:
            self.download_dtube(url)
        elif 'younow.com' in url_lower:
            self.download_younow(url)
        elif 'trovo.live' in url_lower:
            self.download_trovo(url)
        elif 'vk.com' in url_lower or 'vkontakte' in url_lower:
            self.download_vk_video(url, quality)
        elif 'tubi.tv' in url_lower:
            self.download_tubi(url)
        else:
            print("🔍 Platform not recognized, trying generic download...")
            self.generic_download(url, quality)

    def generic_download(self, url, quality='best'):
        """Generic download for unknown platforms"""
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(self.download_path / 'unknown/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            '--ignore-errors',
            url
        ]
        
        try:
            print(f"🌐 Generic download attempt...")
            result = subprocess.run(cmd, check=True)
            print("✅ Generic download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")

    def list_platforms(self):
        """List all supported alternative platforms"""
        print("\n🌐 Alternative Platforms Support:")
        print("=" * 40)
        
        platforms = [
            ("🌊 Odysee", "Decentralized video platform", "✅ Good"),
            ("🎬 BitChute", "Alternative video platform", "✅ Good"),
            ("🎥 Metacafe", "Classic video platform", "⚠️ Limited"),
            ("📹 Veoh", "Video sharing platform", "⚠️ Limited"),
            ("⛓️ DTube", "Blockchain video platform", "⚠️ Limited"),
            ("📡 YouNow", "Live streaming platform", "⚠️ Limited"),
            ("🎮 Trovo", "Gaming streaming platform", "⚠️ Limited"),
            ("🇷🇺 VK Video", "Russian social platform", "⚠️ Limited"),
            ("📺 Tubi", "Streaming service", "❌ DRM Protected"),
            ("🌐 StreamYard", "Live streaming tool", "❌ Not supported")
        ]
        
        for platform, description, status in platforms:
            print(f"{platform:<15} - {description:<30} [{status}]")


def main():
    print("🌐 Alternative Platforms Downloader")
    print("=" * 40)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Download: python3 alternative_platforms_downloader.py <url>")
        print("2. List platforms: python3 alternative_platforms_downloader.py --list")
        print("\nSupported Platforms:")
        print("🌊 Odysee, 🎬 BitChute, 🎥 Metacafe, 📹 Veoh")
        print("⛓️ DTube, 📡 YouNow, 🎮 Trovo, 🇷🇺 VK Video")
        sys.exit(1)
    
    downloader = AlternativePlatformsDownloader()
    
    if sys.argv[1] == '--list':
        downloader.list_platforms()
        return
    
    url = sys.argv[1]
    quality = input("Quality (best/720p/480p/360p) [best]: ").strip() or 'best'
    
    downloader.auto_detect_and_download(url, quality)


if __name__ == "__main__":
    main() 