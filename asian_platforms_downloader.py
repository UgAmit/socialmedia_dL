#!/usr/bin/env python3
"""
Asian & Emerging Platforms Downloader
Supports: MX TakaTak, Moj, Chingari, Josh, Bilibili, Kuaishou, Weibo, Douyin, etc.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from urllib.parse import urlparse

# Optional import - fallback if not available
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class AsianPlatformsDownloader:
    def __init__(self, download_path="./downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # Platform detection patterns
        self.platform_patterns = {
            'takatak': ['mxtakatak.com', 'takatak.tv'],
            'moj': ['moj.tv', 'mojapp.in'],
            'chingari': ['chingari.io', 'chingariapp.com'],
            'josh': ['josh.in', 'joshapp.com'],
            'bilibili': ['bilibili.com', 'b23.tv'],
            'kuaishou': ['kuaishou.com', 'ks.com'],
            'weibo': ['weibo.com', 'weibo.cn'],
            'douyin': ['douyin.com', 'iesdouyin.com'],
            'niconico': ['nicovideo.jp', 'nico.ms'],
            'youku': ['youku.com', 'youku.cn']
        }
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def detect_platform(self, url):
        """Detect which platform the URL belongs to"""
        url_lower = url.lower()
        
        for platform, patterns in self.platform_patterns.items():
            for pattern in patterns:
                if pattern in url_lower:
                    return platform
        return 'unknown'

    def download_bilibili(self, url, quality='best'):
        """Download Bilibili videos (Chinese YouTube)"""
        platform_dir = self.download_path / 'bilibili'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--write-thumbnail',
            '--progress',
            '--geo-bypass',
            url
        ]
        
        try:
            print(f"📺 Starting Bilibili download...")
            print(f"🌏 Platform: Bilibili (哔哩哔哩)")
            result = subprocess.run(cmd, check=True)
            print("✅ Bilibili download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            print("💡 Try using VPN or proxy for geo-restricted content")

    def download_niconico(self, url, quality='best'):
        """Download Niconico videos (Japanese platform)"""
        platform_dir = self.download_path / 'niconico'
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
            print(f"🎌 Starting Niconico download...")
            print(f"🌏 Platform: Niconico (ニコニコ動画)")
            result = subprocess.run(cmd, check=True)
            print("✅ Niconico download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            print("💡 Niconico may require account authentication")

    def download_youku(self, url, quality='best'):
        """Download Youku videos (Chinese platform)"""
        platform_dir = self.download_path / 'youku'
        platform_dir.mkdir(exist_ok=True)
        
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--geo-bypass',
            '--progress',
            url
        ]
        
        try:
            print(f"🇨🇳 Starting Youku download...")
            print(f"🌏 Platform: Youku (优酷)")
            result = subprocess.run(cmd, check=True)
            print("✅ Youku download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            print("💡 Youku content may be geo-restricted")

    def download_indian_platform(self, url, platform_name):
        """Download from Indian short video platforms"""
        platform_dir = self.download_path / platform_name.lower()
        platform_dir.mkdir(exist_ok=True)
        
        # Try with yt-dlp first
        cmd = [
            'yt-dlp',
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            '--ignore-errors',
            url
        ]
        
        try:
            print(f"🇮🇳 Starting {platform_name} download...")
            result = subprocess.run(cmd, check=True)
            print(f"✅ {platform_name} download successful!")
        except subprocess.CalledProcessError:
            # Fallback to direct download if yt-dlp fails
            print(f"⚠️ yt-dlp failed for {platform_name}, trying direct download...")
            self.try_direct_download(url, platform_dir, platform_name)

    def try_direct_download(self, url, platform_dir, platform_name):
        """Try direct download for platforms not fully supported by yt-dlp"""
        try:
            print(f"🔄 Attempting direct download for {platform_name}...")
            
            if REQUESTS_AVAILABLE:
                # Basic video URL extraction (simplified)
                response = requests.get(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                })
                # This is a simplified approach - real implementation would need
                # platform-specific API analysis
                print(f"⚠️ {platform_name} requires specialized extraction")
                print(f"💡 Platform may need manual analysis or API access")
            else:
                print(f"⚠️ {platform_name} requires specialized extraction")
                print(f"💡 Install 'requests' module for enhanced functionality: pip3 install requests")
                print(f"💡 Platform may need manual analysis or API access")
            
        except Exception as e:
            print(f"❌ Direct download failed: {e}")

    def download_with_platform_detection(self, url, quality='best'):
        """Auto-detect platform and download accordingly"""
        platform = self.detect_platform(url)
        
        print(f"🔍 Detected platform: {platform}")
        
        if platform == 'bilibili':
            self.download_bilibili(url, quality)
        elif platform == 'niconico':
            self.download_niconico(url, quality)
        elif platform == 'youku':
            self.download_youku(url, quality)
        elif platform in ['takatak', 'moj', 'chingari', 'josh']:
            self.download_indian_platform(url, platform.title())
        else:
            # Generic download attempt
            self.generic_download(url, quality)

    def generic_download(self, url, quality='best'):
        """Generic download for any platform"""
        cmd = [
            'yt-dlp',
            '-f', quality,
            '--output', str(self.download_path / 'generic/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--progress',
            '--ignore-errors',
            url
        ]
        
        try:
            print(f"🌐 Starting generic download...")
            result = subprocess.run(cmd, check=True)
            print("✅ Generic download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Generic download failed: {e}")
            print("💡 Platform may not be supported by yt-dlp")

    def list_supported_platforms(self):
        """List all supported platforms"""
        print("\n🌏 Asian & Emerging Platforms Support:")
        print("=" * 50)
        
        platforms = [
            ("🇮🇳 MX TakaTak", "Indian short videos", "Limited"),
            ("🇮🇳 Moj", "Indian short videos", "Limited"),
            ("🇮🇳 Chingari", "Indian short videos", "Limited"),
            ("🇮🇳 Josh", "Indian short videos", "Limited"),
            ("🇨🇳 Bilibili", "Chinese video platform", "Good"),
            ("🇨🇳 Kuaishou", "Chinese short videos", "Limited"),
            ("🇨🇳 Weibo Video", "Chinese social media", "Limited"),
            ("🇨🇳 Douyin", "Chinese TikTok", "Limited"),
            ("🇯🇵 Niconico", "Japanese video platform", "Good"),
            ("🇷🇺 VK Video", "Russian social media", "Limited"),
            ("🌐 Odysee", "Decentralized platform", "Good"),
            ("🌐 BitChute", "Video platform", "Good"),
            ("🌐 Metacafe", "Video platform", "Limited"),
            ("🌐 Veoh", "Video platform", "Limited"),
            ("🇨🇳 Youku", "Chinese video platform", "Good")
        ]
        
        for platform, description, support in platforms:
            status_emoji = "✅" if support == "Good" else "⚠️" if support == "Limited" else "❌"
            print(f"{status_emoji} {platform:<20} - {description:<25} [{support}]")

    def show_usage_examples(self):
        """Show usage examples for different platforms"""
        print("\n💡 Usage Examples:")
        print("=" * 30)
        
        examples = [
            ("Bilibili", "python3 asian_platforms_downloader.py 'https://bilibili.com/video/...'"),
            ("Niconico", "python3 asian_platforms_downloader.py 'https://nicovideo.jp/watch/...'"),
            ("MX TakaTak", "python3 asian_platforms_downloader.py 'https://mxtakatak.com/...'"),
            ("Youku", "python3 asian_platforms_downloader.py 'https://youku.com/v_show/...'"),
            ("Auto-detect", "python3 asian_platforms_downloader.py 'ANY_URL'")
        ]
        
        for platform, example in examples:
            print(f"\n{platform}:")
            print(f"  {example}")


def main():
    print("🌏 Asian & Emerging Platforms Downloader")
    print("=" * 45)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Download: python3 asian_platforms_downloader.py <url>")
        print("2. List platforms: python3 asian_platforms_downloader.py --list")
        print("3. Show examples: python3 asian_platforms_downloader.py --examples")
        print("\nSupported Platforms:")
        print("🇮🇳 Indian: MX TakaTak, Moj, Chingari, Josh")
        print("🇨🇳 Chinese: Bilibili, Kuaishou, Weibo, Douyin, Youku")
        print("🇯🇵 Japanese: Niconico")
        print("🌐 Others: Odysee, BitChute, Metacafe, Veoh")
        sys.exit(1)
    
    downloader = AsianPlatformsDownloader()
    
    if sys.argv[1] == '--list':
        downloader.list_supported_platforms()
        return
    elif sys.argv[1] == '--examples':
        downloader.show_usage_examples()
        return
    
    url = sys.argv[1]
    quality = input("Quality (best/720p/480p/360p) [best]: ").strip() or 'best'
    
    downloader.download_with_platform_detection(url, quality)


if __name__ == "__main__":
    main() 