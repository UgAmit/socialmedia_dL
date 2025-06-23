#!/usr/bin/env python3
"""
Discord Video/Attachment Downloader
Downloads video content and attachments from Discord channels
Note: Requires appropriate permissions and may need authentication
"""

import os
import sys
import subprocess
import json
import requests
from pathlib import Path
from urllib.parse import urlparse


class DiscordDownloader:
    def __init__(self, download_path="./downloads/discord"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)

    def download_attachment(self, url, custom_name=None):
        """Download Discord attachment (video/image/file)"""
        
        try:
            print(f"📎 Starting Discord attachment download...")
            print(f"🔗 URL: {url}")
            
            # Parse Discord CDN URL
            parsed = urlparse(url)
            if 'cdn.discordapp.com' not in parsed.netloc and 'media.discordapp.net' not in parsed.netloc:
                print("❌ Invalid Discord attachment URL")
                return
            
            # Get filename from URL or use custom name
            if custom_name:
                filename = custom_name
            else:
                filename = os.path.basename(parsed.path)
                if not filename:
                    filename = "discord_attachment"
            
            # Create output path
            output_path = self.download_path / filename
            
            # Download with requests
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Save file
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ Downloaded: {filename}")
            print(f"📁 Saved to: {output_path}")
                
        except requests.RequestException as e:
            print(f"❌ Download failed: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def bulk_download_attachments(self, urls_file):
        """Download multiple Discord attachments from a file"""
        
        try:
            with open(urls_file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
            
            print(f"📋 Found {len(urls)} URLs to download")
            
            for i, url in enumerate(urls, 1):
                print(f"\n📎 Downloading {i}/{len(urls)}: {url[:50]}...")
                self.download_attachment(url)
                
            print(f"\n✅ Bulk download completed! Downloaded {len(urls)} files")
                
        except FileNotFoundError:
            print(f"❌ File not found: {urls_file}")
        except Exception as e:
            print(f"❌ Bulk download failed: {e}")

    def show_discord_info(self):
        """Show Discord download information and limitations"""
        print("\n🎮 Discord Download Information:")
        print("=" * 40)
        print("✅ Direct attachments: Downloadable")
        print("✅ Videos/Images posted: Downloadable")
        print("✅ Files uploaded: Downloadable")
        print("🔒 Private channels: Need access")
        print("🔒 Deleted content: Not accessible")
        print("\n💡 How to get Discord URLs:")
        print("1. Right-click on attachment → Copy Link")
        print("2. Open attachment in browser → Copy URL")
        print("\n⚠️  Legal Note:")
        print("   Respect Discord's Terms of Service")
        print("   Only download content you have permission to access")


def main():
    print("🎮 Discord Video/Attachment Downloader")
    print("=" * 40)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("1. Single attachment: python3 discord_downloader.py <discord_url>")
        print("2. Bulk download: python3 discord_downloader.py <urls_file> bulk")
        print("3. Show info: python3 discord_downloader.py --info")
        print("\nExamples:")
        print("python3 discord_downloader.py 'https://cdn.discordapp.com/...'")
        print("python3 discord_downloader.py 'urls.txt' bulk")
        sys.exit(1)
    
    downloader = DiscordDownloader()
    
    if sys.argv[1] == '--info':
        downloader.show_discord_info()
        return
    
    if len(sys.argv) >= 3 and sys.argv[2] == 'bulk':
        # Bulk download from file
        urls_file = sys.argv[1]
        downloader.bulk_download_attachments(urls_file)
    else:
        # Single download
        url = sys.argv[1]
        custom_name = input("Custom filename (optional): ").strip() or None
        downloader.download_attachment(url, custom_name)


if __name__ == "__main__":
    main() 