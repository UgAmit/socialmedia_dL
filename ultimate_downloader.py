#!/usr/bin/env python3
"""
🌟 ULTIMATE SOCIAL MEDIA DOWNLOADER 🌟
Supports 30+ platforms including all requested Asian and emerging platforms
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# Optional import - fallback if not available
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class UltimateDownloader:
    def __init__(self, download_path="./downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
        # All supported platforms
        self.all_platforms = {
            # Main Western Platforms
            'youtube': {'name': '🔴 YouTube', 'status': '✅ Full', 'extractor': 'youtube'},
            'instagram': {'name': '📷 Instagram', 'status': '✅ Full', 'extractor': 'instagram'},
            'twitter': {'name': '🐦 Twitter/X', 'status': '✅ Full', 'extractor': 'twitter'},
            'tiktok': {'name': '🎵 TikTok', 'status': '✅ Full', 'extractor': 'tiktok'},
            'facebook': {'name': '📘 Facebook', 'status': '✅ Full', 'extractor': 'facebook'},
            
            # Video Platforms
            'vimeo': {'name': '🎥 Vimeo', 'status': '✅ Full', 'extractor': 'vimeo'},
            'dailymotion': {'name': '📺 Dailymotion', 'status': '✅ Full', 'extractor': 'dailymotion'},
            'twitch': {'name': '🟣 Twitch', 'status': '✅ Full', 'extractor': 'twitch'},
            'reddit': {'name': '🔴 Reddit', 'status': '✅ Full', 'extractor': 'reddit'},
            
            # Professional Platforms
            'linkedin': {'name': '💼 LinkedIn', 'status': '⚠️ Auth', 'extractor': 'linkedin'},
            'pinterest': {'name': '📌 Pinterest', 'status': '⚠️ Limited', 'extractor': 'pinterest'},
            
            # Alternative Platforms
            'rumble': {'name': '🎯 Rumble', 'status': '✅ Full', 'extractor': 'rumble'},
            'odysee': {'name': '🌊 Odysee', 'status': '✅ Full', 'extractor': 'odysee'},
            'bitchute': {'name': '🎬 BitChute', 'status': '✅ Full', 'extractor': 'bitchute'},
            'peertube': {'name': '🌐 PeerTube', 'status': '✅ Full', 'extractor': 'peertube'},
            
            # Asian Platforms
            'bilibili': {'name': '🇨🇳 Bilibili', 'status': '✅ Good', 'extractor': 'bilibili'},
            'niconico': {'name': '🇯🇵 Niconico', 'status': '✅ Good', 'extractor': 'niconico'},
            'youku': {'name': '🇨🇳 Youku', 'status': '✅ Good', 'extractor': 'youku'},
            'kuaishou': {'name': '🇨🇳 Kuaishou', 'status': '⚠️ Limited', 'extractor': 'kuaishou'},
            'weibo': {'name': '🇨🇳 Weibo', 'status': '⚠️ Limited', 'extractor': 'weibo'},
            'douyin': {'name': '🇨🇳 Douyin', 'status': '⚠️ Limited', 'extractor': 'douyin'},
            
            # Indian Platforms
            'mxtakatak': {'name': '🇮🇳 MX TakaTak', 'status': '⚠️ Limited', 'extractor': 'generic'},
            'moj': {'name': '🇮🇳 Moj', 'status': '⚠️ Limited', 'extractor': 'generic'},
            'chingari': {'name': '🇮🇳 Chingari', 'status': '⚠️ Limited', 'extractor': 'generic'},
            'josh': {'name': '🇮🇳 Josh', 'status': '⚠️ Limited', 'extractor': 'generic'},
            
            # Other Platforms
            'vk': {'name': '🇷🇺 VK Video', 'status': '⚠️ Limited', 'extractor': 'vk'},
            'metacafe': {'name': '🎥 Metacafe', 'status': '⚠️ Limited', 'extractor': 'metacafe'},
            'veoh': {'name': '📹 Veoh', 'status': '⚠️ Limited', 'extractor': 'veoh'},
            'dtube': {'name': '⛓️ DTube', 'status': '⚠️ Limited', 'extractor': 'generic'},
            'younow': {'name': '📡 YouNow', 'status': '⚠️ Live Only', 'extractor': 'younow'},
            'trovo': {'name': '🎮 Trovo', 'status': '⚠️ Live Only', 'extractor': 'trovo'},
            
            # Streaming/Discontinued
            'snapchat': {'name': '👻 Snapchat', 'status': '❌ Very Limited', 'extractor': 'generic'},
            'discord': {'name': '🎮 Discord', 'status': '✅ Direct Links', 'extractor': 'direct'},
            'periscope': {'name': '📡 Periscope', 'status': '❌ Discontinued', 'extractor': 'none'},
            'zynn': {'name': '🎬 Zynn', 'status': '❌ Discontinued', 'extractor': 'none'},
            'tubi': {'name': '📺 Tubi', 'status': '❌ DRM Protected', 'extractor': 'none'},
            'streamyard': {'name': '🎥 StreamYard', 'status': '❌ Tool Only', 'extractor': 'none'}
        }
        
        # Platform detection patterns
        self.platform_patterns = {
            'youtube': ['youtube.com', 'youtu.be'],
            'instagram': ['instagram.com'],
            'twitter': ['twitter.com', 'x.com'],
            'tiktok': ['tiktok.com'],
            'facebook': ['facebook.com', 'fb.com'],
            'vimeo': ['vimeo.com'],
            'dailymotion': ['dailymotion.com'],
            'twitch': ['twitch.tv'],
            'reddit': ['reddit.com'],
            'linkedin': ['linkedin.com'],
            'pinterest': ['pinterest.com'],
            'rumble': ['rumble.com'],
            'odysee': ['odysee.com', 'lbry.tv'],
            'bitchute': ['bitchute.com'],
            'peertube': ['peertube'],
            'bilibili': ['bilibili.com', 'b23.tv'],
            'niconico': ['nicovideo.jp', 'nico.ms'],
            'youku': ['youku.com'],
            'kuaishou': ['kuaishou.com'],
            'weibo': ['weibo.com'],
            'douyin': ['douyin.com'],
            'mxtakatak': ['mxtakatak.com', 'takatak.tv'],
            'moj': ['moj.tv', 'mojapp.in'],
            'chingari': ['chingari.io'],
            'josh': ['josh.in'],
            'vk': ['vk.com', 'vkontakte'],
            'metacafe': ['metacafe.com'],
            'veoh': ['veoh.com'],
            'dtube': ['dtube'],
            'younow': ['younow.com'],
            'trovo': ['trovo.live'],
            'snapchat': ['snapchat.com'],
            'discord': ['cdn.discordapp.com', 'media.discordapp.net'],
            'periscope': ['periscope.tv', 'pscp.tv'],
            'zynn': ['zynn'],
            'tubi': ['tubi.tv'],
            'streamyard': ['streamyard.com']
        }
        
        # Check if yt-dlp is available
        try:
            subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: yt-dlp is not installed")
            print("Please install it with: pipx install yt-dlp")
            sys.exit(1)

    def detect_platform(self, url):
        """Auto-detect platform from URL"""
        url_lower = url.lower()
        
        for platform, patterns in self.platform_patterns.items():
            for pattern in patterns:
                if pattern in url_lower:
                    return platform
        return 'unknown'

    def download_content(self, url, quality='best', format_type='video'):
        """Universal download function"""
        platform = self.detect_platform(url)
        platform_info = self.all_platforms.get(platform, {})
        
        print(f"🔍 Detected Platform: {platform_info.get('name', 'Unknown')}")
        print(f"📊 Support Status: {platform_info.get('status', 'Unknown')}")
        print("-" * 50)
        
        # Handle special cases
        if platform in ['periscope', 'zynn', 'tubi', 'streamyard']:
            self.handle_discontinued_platform(platform, url)
            return
        
        if platform == 'discord':
            self.download_discord_attachment(url)
            return
        
        # Standard download
        platform_dir = self.download_path / platform
        platform_dir.mkdir(exist_ok=True)
        
        # Build command
        cmd = ['yt-dlp']
        
        # Add format selection
        if format_type == 'audio':
            cmd.extend(['--extract-audio', '--audio-format', 'mp3'])
        else:
            cmd.extend(['-f', quality])
        
        # Add geo-bypass for Chinese platforms
        if platform in ['bilibili', 'youku', 'kuaishou', 'weibo', 'douyin']:
            cmd.append('--geo-bypass')
        
        # Add output template
        cmd.extend([
            '--output', str(platform_dir / '%(uploader)s/%(title)s.%(ext)s'),
            '--write-description',
            '--write-info-json',
            '--write-thumbnail',
            '--progress'
        ])
        
        # Add URL
        cmd.append(url)
        
        try:
            print(f"🚀 Starting download from {platform_info.get('name', platform)}...")
            result = subprocess.run(cmd, check=True)
            print("✅ Download successful!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Download failed: {e}")
            
            # Try fallback methods
            if platform in ['mxtakatak', 'moj', 'chingari', 'josh']:
                print("🔄 Trying Indian platform fallback...")
                self.try_indian_platform_fallback(url, platform)
            else:
                print("💡 Try updating yt-dlp or check if URL is accessible")

    def handle_discontinued_platform(self, platform, url):
        """Handle discontinued platforms"""
        messages = {
            'periscope': {
                'emoji': '📡',
                'message': 'Periscope was discontinued in 2021',
                'alternative': 'Try Twitter live streams instead'
            },
            'zynn': {
                'emoji': '🎬', 
                'message': 'Zynn was removed from app stores',
                'alternative': 'Content may be on TikTok or Instagram'
            },
            'tubi': {
                'emoji': '📺',
                'message': 'Tubi has DRM protection',
                'alternative': 'Streaming service content cannot be downloaded'
            },
            'streamyard': {
                'emoji': '🎥',
                'message': 'StreamYard is a streaming tool, not content platform',
                'alternative': 'Find the destination platform (YouTube, Facebook, etc.)'
            }
        }
        
        info = messages.get(platform, {})
        print(f"{info.get('emoji', '⚠️')} {info.get('message', 'Platform not supported')}")
        print(f"💡 {info.get('alternative', 'Try alternative platforms')}")

    def download_discord_attachment(self, url):
        """Special handler for Discord attachments"""
        if not REQUESTS_AVAILABLE:
            print("❌ Discord downloads require 'requests' module")
            print("💡 Install with: pip3 install requests")
            return
            
        try:
            filename = os.path.basename(url.split('?')[0])
            if not filename:
                filename = 'discord_attachment'
            
            platform_dir = self.download_path / 'discord'
            platform_dir.mkdir(exist_ok=True)
            
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            output_path = platform_dir / filename
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ Discord attachment downloaded: {filename}")
        except Exception as e:
            print(f"❌ Discord download failed: {e}")

    def try_indian_platform_fallback(self, url, platform):
        """Fallback for Indian platforms"""
        print(f"🇮🇳 {platform.upper()} may require specialized extraction")
        print("💡 These platforms often have app-specific APIs")
        print("🔄 Attempting generic extraction...")
        
        # Try generic extraction
        cmd = [
            'yt-dlp',
            '--output', str(self.download_path / platform / '%(title)s.%(ext)s'),
            '--ignore-errors',
            '--no-warnings',
            url
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print("✅ Generic extraction successful!")
        except subprocess.CalledProcessError:
            print("❌ Generic extraction failed")
            print(f"💡 {platform.title()} may need manual download or API access")

    def list_all_platforms(self):
        """List all supported platforms"""
        print("\n🌟 ULTIMATE DOWNLOADER - ALL PLATFORMS:")
        print("=" * 60)
        
        categories = {
            'Main Western': ['youtube', 'instagram', 'twitter', 'tiktok', 'facebook'],
            'Video Platforms': ['vimeo', 'dailymotion', 'twitch', 'reddit'],
            'Professional': ['linkedin', 'pinterest'],
            'Alternative': ['rumble', 'odysee', 'bitchute', 'peertube'],
            'Asian Platforms': ['bilibili', 'niconico', 'youku', 'kuaishou', 'weibo', 'douyin'],
            'Indian Platforms': ['mxtakatak', 'moj', 'chingari', 'josh'],
            'Other/Regional': ['vk', 'metacafe', 'veoh', 'dtube'],
            'Streaming/Live': ['younow', 'trovo', 'snapchat', 'discord'],
            'Discontinued': ['periscope', 'zynn', 'tubi', 'streamyard']
        }
        
        for category, platforms in categories.items():
            print(f"\n📂 {category}:")
            for platform in platforms:
                info = self.all_platforms[platform]
                print(f"   {info['name']:<20} [{info['status']}]")

    def show_usage_examples(self):
        """Show comprehensive usage examples"""
        print("\n💡 USAGE EXAMPLES:")
        print("=" * 40)
        
        examples = [
            ("YouTube Video", "python3 ultimate_downloader.py 'https://youtube.com/watch?v=...'"),
            ("Instagram Post", "python3 ultimate_downloader.py 'https://instagram.com/p/...'"),
            ("TikTok Video", "python3 ultimate_downloader.py 'https://tiktok.com/@user/video/...'"),
            ("Bilibili Video", "python3 ultimate_downloader.py 'https://bilibili.com/video/...'"),
            ("Rumble Video", "python3 ultimate_downloader.py 'https://rumble.com/v...'"),
            ("LinkedIn Post", "python3 ultimate_downloader.py 'https://linkedin.com/posts/...'"),
            ("MX TakaTak", "python3 ultimate_downloader.py 'https://mxtakatak.com/...'"),
            ("Audio Only", "python3 ultimate_downloader.py 'URL' --audio"),
            ("HD Quality", "python3 ultimate_downloader.py 'URL' --quality 720p")
        ]
        
        for platform, example in examples:
            print(f"\n{platform}:")
            print(f"  {example}")


def main():
    print("🌟 ULTIMATE SOCIAL MEDIA DOWNLOADER")
    print("Supports 30+ platforms including Asian & emerging platforms")
    print("=" * 60)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Download: python3 ultimate_downloader.py <url>")
        print("2. Audio only: python3 ultimate_downloader.py <url> --audio")
        print("3. Quality: python3 ultimate_downloader.py <url> --quality 720p")
        print("4. List platforms: python3 ultimate_downloader.py --list")
        print("5. Show examples: python3 ultimate_downloader.py --examples")
        print("\n🌏 Supported: YouTube, Instagram, TikTok, Bilibili, MX TakaTak, Moj, and 25+ more!")
        sys.exit(1)
    
    downloader = UltimateDownloader()
    
    if sys.argv[1] == '--list':
        downloader.list_all_platforms()
        return
    elif sys.argv[1] == '--examples':
        downloader.show_usage_examples()
        return
    
    url = sys.argv[1]
    
    # Parse arguments
    quality = 'best'
    format_type = 'video'
    
    if '--audio' in sys.argv:
        format_type = 'audio'
    
    if '--quality' in sys.argv:
        try:
            quality_index = sys.argv.index('--quality')
            quality = sys.argv[quality_index + 1]
        except (IndexError, ValueError):
            quality = 'best'
    
    downloader.download_content(url, quality, format_type)


if __name__ == "__main__":
    main() 