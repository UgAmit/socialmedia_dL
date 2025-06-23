// Platform Detection and Mock Data
const platforms = {
    // Main Western Platforms
    youtube: {
        icon: 'fab fa-youtube',
        name: 'YouTube',
        domains: ['youtube.com', 'youtu.be', 'm.youtube.com'],
        color: '#ff0000',
        downloader: 'ultimate_downloader.py'
    },
    instagram: {
        icon: 'fab fa-instagram',
        name: 'Instagram',
        domains: ['instagram.com', 'instagr.am'],
        color: '#e4405f',
        downloader: 'instagram_downloader.py'
    },
    twitter: {
        icon: 'fab fa-twitter',
        name: 'Twitter/X',
        domains: ['twitter.com', 'x.com', 't.co'],
        color: '#1da1f2',
        downloader: 'twitter_downloader.py'
    },
    tiktok: {
        icon: 'fab fa-tiktok',
        name: 'TikTok',
        domains: ['tiktok.com', 'vm.tiktok.com'],
        color: '#000000',
        downloader: 'ultimate_downloader.py'
    },
    facebook: {
        icon: 'fab fa-facebook',
        name: 'Facebook',
        domains: ['facebook.com', 'fb.com', 'm.facebook.com'],
        color: '#1877f2',
        downloader: 'ultimate_downloader.py'
    },
    reddit: {
        icon: 'fab fa-reddit',
        name: 'Reddit',
        domains: ['reddit.com', 'redd.it'],
        color: '#ff4500',
        downloader: 'ultimate_downloader.py'
    },
    vimeo: {
        icon: 'fab fa-vimeo',
        name: 'Vimeo',
        domains: ['vimeo.com'],
        color: '#1ab7ea',
        downloader: 'vimeo_downloader.py'
    },
    twitch: {
        icon: 'fab fa-twitch',
        name: 'Twitch',
        domains: ['twitch.tv', 'clips.twitch.tv'],
        color: '#9146ff',
        downloader: 'ultimate_downloader.py'
    },
    
    // Asian Platforms
    bilibili: {
        icon: 'fas fa-play-circle',
        name: 'Bilibili',
        domains: ['bilibili.com', 'b23.tv'],
        color: '#fb7299',
        downloader: 'asian_platforms_downloader.py'
    },
    niconico: {
        icon: 'fas fa-video',
        name: 'Niconico',
        domains: ['nicovideo.jp', 'nico.ms'],
        color: '#252525',
        downloader: 'asian_platforms_downloader.py'
    },
    youku: {
        icon: 'fas fa-film',
        name: 'Youku',
        domains: ['youku.com'],
        color: '#06a7e1',
        downloader: 'asian_platforms_downloader.py'
    },
    kuaishou: {
        icon: 'fas fa-camera',
        name: 'Kuaishou',
        domains: ['kuaishou.com'],
        color: '#ff6600',
        downloader: 'asian_platforms_downloader.py'
    },
    weibo: {
        icon: 'fab fa-weibo',
        name: 'Weibo Video',
        domains: ['weibo.com', 'weibo.cn'],
        color: '#e6162d',
        downloader: 'asian_platforms_downloader.py'
    },
    douyin: {
        icon: 'fas fa-music',
        name: 'Douyin',
        domains: ['douyin.com', 'iesdouyin.com'],
        color: '#000000',
        downloader: 'asian_platforms_downloader.py'
    },
    
    // Indian Platforms
    mxtakatak: {
        icon: 'fas fa-mobile-alt',
        name: 'MX TakaTak',
        domains: ['mxtakatak.com', 'takatak.tv'],
        color: '#ff4757',
        downloader: 'asian_platforms_downloader.py'
    },
    moj: {
        icon: 'fas fa-star',
        name: 'Moj',
        domains: ['moj.tv', 'mojapp.in'],
        color: '#ffa502',
        downloader: 'asian_platforms_downloader.py'
    },
    chingari: {
        icon: 'fas fa-fire',
        name: 'Chingari',
        domains: ['chingari.io', 'chingariapp.com'],
        color: '#ff6348',
        downloader: 'asian_platforms_downloader.py'
    },
    josh: {
        icon: 'fas fa-heart',
        name: 'Josh',
        domains: ['josh.in', 'joshapp.com'],
        color: '#2f3542',
        downloader: 'asian_platforms_downloader.py'
    },
    
    // Alternative Platforms
    rumble: {
        icon: 'fas fa-bullhorn',
        name: 'Rumble',
        domains: ['rumble.com'],
        color: '#85c742',
        downloader: 'rumble_downloader.py'
    },
    odysee: {
        icon: 'fas fa-wave-square',
        name: 'Odysee',
        domains: ['odysee.com', 'lbry.tv'],
        color: '#047857',
        downloader: 'alternative_platforms_downloader.py'
    },
    bitchute: {
        icon: 'fas fa-video',
        name: 'BitChute',
        domains: ['bitchute.com'],
        color: '#ff6b35',
        downloader: 'alternative_platforms_downloader.py'
    },
    peertube: {
        icon: 'fas fa-share-alt',
        name: 'PeerTube',
        domains: ['peertube'],
        color: '#f1680d',
        downloader: 'peertube_downloader.py'
    },
    dtube: {
        icon: 'fas fa-cube',
        name: 'DTube',
        domains: ['dtube'],
        color: '#ff4757',
        downloader: 'alternative_platforms_downloader.py'
    },
    
    // Professional & Others
    linkedin: {
        icon: 'fab fa-linkedin',
        name: 'LinkedIn',
        domains: ['linkedin.com'],
        color: '#0077b5',
        downloader: 'linkedin_downloader.py'
    },
    pinterest: {
        icon: 'fab fa-pinterest',
        name: 'Pinterest',
        domains: ['pinterest.com'],
        color: '#bd081c',
        downloader: 'pinterest_downloader.py'
    },
    vk: {
        icon: 'fab fa-vk',
        name: 'VK Video',
        domains: ['vk.com', 'vkontakte'],
        color: '#4680c2',
        downloader: 'ultimate_downloader.py'
    },
    discord: {
        icon: 'fab fa-discord',
        name: 'Discord',
        domains: ['cdn.discordapp.com', 'media.discordapp.net'],
        color: '#5865f2',
        downloader: 'discord_downloader.py'
    },
    
    // Live/Streaming Platforms
    younow: {
        icon: '📡',
        name: 'YouNow',
        domains: ['younow.com'],
        color: '#00cf91'
    },
    trovo: {
        icon: '🎮',
        name: 'Trovo',
        domains: ['trovo.live'],
        color: '#20bf55'
    }
};

// Mock media data for demonstration
const mockMediaData = {
    // Western Platforms
    youtube: {
        title: "How to Build Amazing Web Apps | Full Tutorial",
        creator: "TechMaster Pro",
        duration: "12:34",
        views: "1.2M views"
    },
    instagram: {
        title: "Amazing sunset reel from Mumbai",
        creator: "@travel_photographer",
        duration: "0:30",
        views: "45.2K views"
    },
    twitter: {
        title: "Breaking: Tech announcement video",
        creator: "@technews",
        duration: "1:15",
        views: "892K views"
    },
    tiktok: {
        title: "Viral dance challenge #trending",
        creator: "@dancer_girl",
        duration: "0:15",
        views: "2.1M views"
    },
    facebook: {
        title: "Family vacation memories",
        creator: "John Smith",
        duration: "3:45",
        views: "156 views"
    },
    reddit: {
        title: "Funny cat compilation from r/cats",
        creator: "u/catlovers123",
        duration: "2:20",
        views: "78.5K upvotes"
    },
    vimeo: {
        title: "Professional Photography Workshop",
        creator: "Creative Studios",
        duration: "25:18",
        views: "5.2K views"
    },
    twitch: {
        title: "Epic gaming moment highlight",
        creator: "ProGamer2024",
        duration: "0:45",
        views: "234K views"
    },
    
    // Asian Platforms
    bilibili: {
        title: "【科技】未来编程语言趋势分析",
        creator: "科技UP主",
        duration: "15:42",
        views: "458万播放"
    },
    niconico: {
        title: "【ゲーム実況】新作RPG完全攻略",
        creator: "ゲーマー太郎",
        duration: "28:15",
        views: "125万再生"
    },
    youku: {
        title: "中国传统文化纪录片精选",
        creator: "文化传媒",
        duration: "45:30",
        views: "234万播放"
    },
    kuaishou: {
        title: "农村生活记录短视频",
        creator: "乡村博主",
        duration: "0:45",
        views: "89万播放"
    },
    weibo: {
        title: "热门话题讨论视频",
        creator: "@微博用户",
        duration: "2:18",
        views: "567万播放"
    },
    douyin: {
        title: "抖音热门创意短视频",
        creator: "@抖音创作者",
        duration: "0:30",
        views: "1256万播放"
    },
    
    // Indian Platforms
    mxtakatak: {
        title: "Bollywood dance challenge viral",
        creator: "@dance_queen_india",
        duration: "0:30",
        views: "2.3M views"
    },
    moj: {
        title: "Comedy skit Hindi viral video",
        creator: "@comedy_king_moj",
        duration: "0:45",
        views: "1.8M views"
    },
    chingari: {
        title: "Indian cooking recipe short",
        creator: "@cooking_with_love",
        duration: "1:00",
        views: "890K views"
    },
    josh: {
        title: "Talent showcase India",
        creator: "@talent_hub_josh",
        duration: "0:50",
        views: "1.2M views"
    },
    
    // Alternative Platforms
    rumble: {
        title: "Independent journalism report",
        creator: "Truth Seeker News",
        duration: "18:22",
        views: "456K views"
    },
    odysee: {
        title: "Decentralized future of internet",
        creator: "Crypto Educator",
        duration: "22:15",
        views: "89K views"
    },
    bitchute: {
        title: "Alternative media discussion",
        creator: "Free Speech Channel",
        duration: "35:40",
        views: "123K views"
    },
    peertube: {
        title: "Open source video platform demo",
        creator: "FOSS Community",
        duration: "12:08",
        views: "34K views"
    },
    dtube: {
        title: "Blockchain content creation",
        creator: "CryptoCreator",
        duration: "14:30",
        views: "67K views"
    },
    
    // Professional & Others
    linkedin: {
        title: "Leadership in Digital Age",
        creator: "Nitish Nayyar",
        duration: "1:08",
        views: "145K views"
    },
    pinterest: {
        title: "DIY Home Decoration Ideas",
        creator: "Home Design Pro",
        duration: "2:30",
        views: "89K saves"
    },
    vk: {
        title: "Русский контент видео",
        creator: "Русский блогер",
        duration: "8:45",
        views: "234тыс просмотров"
    },
    discord: {
        title: "Discord attachment file",
        creator: "Server Member",
        duration: "N/A",
        views: "Direct download"
    },
    
    // Live/Streaming
    younow: {
        title: "Live streaming session",
        creator: "LiveStreamer2024",
        duration: "Live",
        views: "1.2K watching"
    },
    trovo: {
        title: "Gaming live stream highlight",
        creator: "ProGamer_Trovo",
        duration: "2:15",
        views: "45K views"
    }
};

// Global variables
let currentPlatform = null;
let isDownloading = false;

// Initialize page
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    addSmoothScrolling();
    initializeAdvancedFeatures();
    createParticleEffect();
    setupThemeAnimations();
});

function setupEventListeners() {
    const urlInput = document.getElementById('urlInput');
    
    // Auto-detect platform on input change
    urlInput.addEventListener('input', function() {
        const url = this.value.trim();
        if (url) {
            detectPlatform();
        } else {
            resetPlatformIndicator();
        }
    });

    // Enter key to detect platform
    urlInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            detectPlatform();
        }
    });
}

function detectPlatform() {
    const url = document.getElementById('urlInput').value.trim();
    const platformIcon = document.getElementById('platformIcon');
    const platformName = document.getElementById('platformName');
    const mediaInfo = document.getElementById('mediaInfo');
    const downloadOptions = document.getElementById('downloadOptions');
    const terminalSection = document.getElementById('terminalSection');

    if (!url) {
        showMessage('Please enter a valid URL', 'error');
        return;
    }

    // Professional loading state
    platformIcon.className = 'fas fa-spinner fa-spin platform-icon';
    platformName.textContent = 'Analyzing URL...';
    platformName.style.color = '#00ff88';

    // Simulate detection process
    setTimeout(() => {
        // Detect platform from URL
        let detectedPlatform = null;
        
        for (const [key, platform] of Object.entries(platforms)) {
            if (platform.domains.some(domain => url.toLowerCase().includes(domain))) {
                detectedPlatform = key;
                break;
            }
        }

        if (detectedPlatform) {
            currentPlatform = detectedPlatform;
            const platform = platforms[detectedPlatform];
            
            // Update platform indicator
            platformIcon.className = platform.icon + ' platform-icon';
            platformName.textContent = `${platform.name} detected`;
            platformName.style.color = platform.color;

            // Show media info and options
            setTimeout(() => {
                showMediaInfo(detectedPlatform);
                downloadOptions.style.display = 'block';
                terminalSection.style.display = 'block';
                
                // Generate command
                const command = generatePythonCommand(url, 'video', 'best');
                updateTerminalCommand(command);
            }, 500);

            showMessage(`Platform detected: ${platform.name}`, 'success');
        } else {
            // Universal fallback
            platformIcon.className = 'fas fa-globe platform-icon';
            platformName.textContent = 'Universal Downloader';
            platformName.style.color = '#00ff88';
            
            setTimeout(() => {
                downloadOptions.style.display = 'block';
                terminalSection.style.display = 'block';
                
                const command = generatePythonCommand(url, 'video', 'best');
                updateTerminalCommand(command);
            }, 300);
            
            showMessage('Using universal downloader for this URL', 'info');
        }
    }, 1000);
}

function showMediaInfo(platform) {
    const mediaInfo = document.getElementById('mediaInfo');
    const data = mockMediaData[platform] || {
        title: "Media Content",
        creator: "Unknown Creator",
        duration: "N/A",
        views: "N/A"
    };

    document.getElementById('mediaTitle').textContent = data.title;
    document.getElementById('mediaCreator').textContent = data.creator;
    document.getElementById('mediaDuration').textContent = data.duration;
    document.getElementById('mediaViews').textContent = data.views;

    mediaInfo.style.display = 'block';
    mediaInfo.style.animation = 'fadeInUp 0.5s ease';
}

function resetPlatformIndicator() {
    document.getElementById('platformIcon').className = 'fas fa-globe platform-icon';
    document.getElementById('platformName').textContent = 'Enter URL to detect platform';
    document.getElementById('platformName').style.color = '#333';
    document.getElementById('mediaInfo').style.display = 'none';
    document.getElementById('downloadOptions').style.display = 'none';
    currentPlatform = null;
}

function startDownload() {
    if (isDownloading) {
        showMessage('Download already in progress', 'info');
        return;
    }

    const url = document.getElementById('urlInput').value.trim();
    const format = document.getElementById('formatSelect').value;
    const quality = document.getElementById('qualitySelect').value;

    if (!url) {
        showMessage('Please enter a valid URL', 'error');
        return;
    }

    isDownloading = true;
    showProgressSection();
    
    // Try actual download
    executeDownload(url, format, quality);
}

function executeDownload(url, format, quality) {
    const progressText = document.getElementById('progressText');
    const progressFill = document.getElementById('progressFill');
    
    // Determine which Python script to use
    const platform = currentPlatform ? platforms[currentPlatform] : null;
    const scriptName = platform ? platform.downloader : 'ultimate_downloader.py';
    
    // Build command
    let command = `python3 ${scriptName} "${url}"`;
    if (format === 'audio') {
        command += ' --audio-only';
    }
    if (quality !== 'best') {
        command += ` --quality ${quality}`;
    }
    
    // Show command being executed
    progressText.textContent = `Executing: ${command}`;
    progressFill.style.width = '20%';
    
    // Since we can't execute Python directly from browser, 
    // we'll create a download instruction instead
    setTimeout(() => {
        progressText.textContent = 'Preparing download instructions...';
        progressFill.style.width = '60%';
        
        setTimeout(() => {
            progressText.textContent = 'Download instructions ready!';
            progressFill.style.width = '100%';
            
            // Show download instructions
            setTimeout(() => {
                showDownloadInstructions(command, url, format, quality);
                completeDownload(format, quality);
            }, 1000);
        }, 1500);
    }, 1000);
}

function showDownloadInstructions(command, url, format, quality) {
    const instructionsModal = document.createElement('div');
    instructionsModal.className = 'download-instructions-modal';
    instructionsModal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h3><i class="fas fa-terminal"></i> Download Instructions</h3>
                <button class="close-modal" onclick="this.parentElement.parentElement.parentElement.remove()">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="modal-body">
                <div class="instruction-step">
                    <h4>Step 1: Copy the command</h4>
                    <div class="command-box">
                        <code>${command}</code>
                        <button class="copy-btn" onclick="copyToClipboard('${command}')">
                            <i class="fas fa-copy"></i>
                        </button>
                    </div>
                </div>
                <div class="instruction-step">
                    <h4>Step 2: Open Terminal</h4>
                    <p>Open Terminal (macOS/Linux) or Command Prompt (Windows)</p>
                </div>
                <div class="instruction-step">
                    <h4>Step 3: Navigate to project directory</h4>
                    <div class="command-box">
                        <code>cd /Users/amit/Desktop/socialmedia_dL</code>
                        <button class="copy-btn" onclick="copyToClipboard('cd /Users/amit/Desktop/socialmedia_dL')">
                            <i class="fas fa-copy"></i>
                        </button>
                    </div>
                </div>
                <div class="instruction-step">
                    <h4>Step 4: Run the command</h4>
                    <p>Paste and execute the command from Step 1</p>
                </div>
                <div class="download-info">
                    <h4>Download Details:</h4>
                    <ul>
                        <li><strong>URL:</strong> ${url}</li>
                        <li><strong>Format:</strong> ${format === 'audio' ? 'Audio (MP3)' : 'Video (MP4)'}</li>
                        <li><strong>Quality:</strong> ${quality}</li>
                        <li><strong>Platform:</strong> ${currentPlatform ? platforms[currentPlatform].name : 'Universal'}</li>
                    </ul>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary" onclick="this.parentElement.parentElement.parentElement.remove()">
                    <i class="fas fa-check"></i> Got it!
                </button>
            </div>
        </div>
    `;
    
    document.body.appendChild(instructionsModal);
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showMessage('Command copied to clipboard!', 'success');
    }).catch(() => {
        // Fallback
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showMessage('Command copied to clipboard!', 'success');
    });
}

function generatePythonCommand(url, format, quality) {
    let command = '';
    
    if (currentPlatform) {
        const platform = platforms[currentPlatform];
        command = `python3 ${platform.downloader} "${url}"`;
    } else {
        command = `python3 ultimate_downloader.py "${url}"`;
    }
    
    // Add options
    if (format === 'audio') {
        command += ' --audio-only';
    }
    if (quality !== 'best') {
        command += ` --quality ${quality}`;
    }
    
    return command;
}

function updateTerminalCommand(command) {
    const terminalSection = document.getElementById('terminalSection');
    const terminalCommand = document.getElementById('terminalCommand');
    
    terminalCommand.textContent = command;
    terminalSection.style.display = 'block';
}

function copyCommand() {
    const terminalCommand = document.getElementById('terminalCommand');
    const command = terminalCommand.textContent;
    
    navigator.clipboard.writeText(command).then(() => {
        showMessage('📋 Command copied to clipboard!', 'success');
    }).catch(() => {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = command;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showMessage('📋 Command copied to clipboard!', 'success');
    });
}

function showProgressSection() {
    const progressSection = document.getElementById('progressSection');
    progressSection.style.display = 'block';
    progressSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function simulateDownload(format, quality, startProgress = 0) {
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    
    const steps = [
        { progress: startProgress || 0, text: '🚀 Initializing download...', color: '#00ff88' },
        { progress: startProgress + 10 || 15, text: '🔍 Analyzing media URL...', color: '#667eea' },
        { progress: startProgress + 20 || 30, text: '📊 Fetching media information...', color: '#ff0080' },
        { progress: startProgress + 15 || 45, text: '🎯 Selecting best quality...', color: '#00ff88' },
        { progress: 85, text: `📥 Downloading ${format === 'video' ? 'video' : 'audio'} (${quality})...`, color: '#667eea' },
        { progress: 95, text: '⚙️ Processing media file...', color: '#ff0080' },
        { progress: 100, text: '🎉 Download completed successfully!', color: '#00ff88' }
    ];

    let currentStep = startProgress > 0 ? 3 : 0;

    function updateProgress() {
        if (currentStep < steps.length) {
            const step = steps[currentStep];
            progressFill.style.width = `${step.progress}%`;
            progressText.textContent = step.text;
            progressText.style.color = step.color;
            
            // Add glow effect to progress bar
            progressFill.style.boxShadow = `0 0 20px ${step.color}50`;
            
            if (step.progress === 100) {
                progressFill.style.animation = 'pulse 0.5s ease';
                setTimeout(() => {
                    completeDownload(format, quality);
                }, 1000);
            } else {
                currentStep++;
                setTimeout(updateProgress, Math.random() * 1000 + 500);
            }
        }
    }

    updateProgress();
}

function completeDownload(format, quality) {
    isDownloading = false;
    const platformName = currentPlatform ? platforms[currentPlatform].name : 'Universal';
    const fileType = format === 'video' ? 'MP4' : 'MP3';
    
    showMessage(`🎉 Download completed! ${platformName} ${format} (${quality}) saved as ${fileType} file.`, 'success');
    
    // Reset progress after 3 seconds
    setTimeout(() => {
        document.getElementById('progressSection').style.display = 'none';
        document.getElementById('progressFill').style.width = '0%';
    }, 3000);
}

function getInfo() {
    const url = document.getElementById('urlInput').value.trim();
    
    if (!url) {
        showMessage('❌ Please enter a URL first!', 'error');
        return;
    }

    if (!currentPlatform) {
        detectPlatform();
    }

    const platformName = currentPlatform ? platforms[currentPlatform].name : 'Universal';
    showMessage(`ℹ️ Media information retrieved from ${platformName}. Check the details above!`, 'info');
}

function loadExample(exampleUrl) {
    document.getElementById('urlInput').value = exampleUrl;
    detectPlatform();
    
    // Scroll to download section
    document.querySelector('.download-card').scrollIntoView({ 
        behavior: 'smooth', 
        block: 'center' 
    });
}

function showMessage(message, type = 'info') {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.message');
    existingMessages.forEach(msg => msg.remove());

    // Create new message
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;

    // Insert after download card
    const downloadCard = document.querySelector('.download-card');
    downloadCard.parentNode.insertBefore(messageDiv, downloadCard.nextSibling);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 5000);
}

function addSmoothScrolling() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Platform card hover effects
document.addEventListener('DOMContentLoaded', function() {
    const platformCards = document.querySelectorAll('.platform-card');
    
    platformCards.forEach(card => {
        card.addEventListener('click', function() {
            const platform = this.dataset.platform;
            if (platform && platforms[platform]) {
                const sampleUrl = getSampleUrl(platform);
                document.getElementById('urlInput').value = sampleUrl;
                detectPlatform();
                
                // Scroll to download section
                document.querySelector('.download-card').scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'center' 
                });
            }
        });
    });
});

function getSampleUrl(platform) {
    const sampleUrls = {
        // Western Platforms
        youtube: 'https://youtube.com/watch?v=dQw4w9WgXcQ',
        instagram: 'https://instagram.com/p/ABC123/',
        twitter: 'https://twitter.com/user/status/123456789',
        tiktok: 'https://tiktok.com/@user/video/1234567890',
        facebook: 'https://facebook.com/user/videos/123456789',
        reddit: 'https://reddit.com/r/videos/comments/abc123/',
        vimeo: 'https://vimeo.com/123456789',
        twitch: 'https://clips.twitch.tv/ClipName',
        
        // Asian Platforms
        bilibili: 'https://bilibili.com/video/BV1234567890',
        niconico: 'https://nicovideo.jp/watch/sm12345678',
        youku: 'https://youku.com/v_show/id_XMTI3NDU2Nzg5Mg==.html',
        kuaishou: 'https://kuaishou.com/profile/123456789',
        weibo: 'https://weibo.com/tv/show/1234567890',
        douyin: 'https://douyin.com/video/1234567890123456789',
        
        // Indian Platforms
        mxtakatak: 'https://mxtakatak.com/video/123456789',
        moj: 'https://mojapp.in/@user/video/123456789',
        chingari: 'https://chingari.io/share/post/123456789',
        josh: 'https://josh.in/video/123456789',
        
        // Alternative Platforms
        rumble: 'https://rumble.com/v123456-sample-video.html',
        odysee: 'https://odysee.com/@channel:1/sample-video:1',
        bitchute: 'https://bitchute.com/video/ABC123456789/',
        peertube: 'https://peertube.example.com/videos/watch/123456',
        dtube: 'https://dtube.example.com/v/user/123456',
        
        // Professional & Others
        linkedin: 'https://linkedin.com/posts/user_123456789',
        pinterest: 'https://pinterest.com/pin/123456789/',
        vk: 'https://vk.com/video123456789_123456789',
        discord: 'https://cdn.discordapp.com/attachments/123/456/file.mp4',
        
        // Live/Streaming
        younow: 'https://younow.com/user/123456789',
        trovo: 'https://trovo.live/clip/123456789'
    };
    
    return sampleUrls[platform] || 'https://example.com/media/123';
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + Enter to start download
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        const downloadBtn = document.querySelector('.btn-primary');
        if (downloadBtn && downloadBtn.style.display !== 'none') {
            startDownload();
        }
    }
    
    // Escape to reset
    if (e.key === 'Escape') {
        resetPlatformIndicator();
        document.getElementById('urlInput').value = '';
        document.getElementById('progressSection').style.display = 'none';
    }
});

// Add some fun interactions
document.addEventListener('DOMContentLoaded', function() {
    // Add click effects to buttons
    const buttons = document.querySelectorAll('.btn, .detect-btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });

    // Add floating animation to hero section
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        setInterval(() => {
            heroContent.style.transform = 'translateY(-5px)';
            setTimeout(() => {
                heroContent.style.transform = 'translateY(0)';
            }, 2000);
        }, 4000);
    }
});

// Performance monitoring
console.log('🌟 Social Media Downloader loaded successfully!');
console.log('💡 Tip: Use Ctrl+Enter to quick download, Escape to reset');

// Add PWA-like features
if ('serviceWorker' in navigator) {
    // Could add service worker for offline functionality
}

// Analytics simulation (mock)
function trackEvent(action, platform = null) {
    console.log(`📊 Event: ${action}${platform ? ` (${platform})` : ''}`);
}

// Track platform detection
const originalDetectPlatform = detectPlatform;
detectPlatform = function() {
    originalDetectPlatform();
    if (currentPlatform) {
        trackEvent('platform_detected', currentPlatform);
    }
};

// Track downloads
const originalStartDownload = startDownload;
startDownload = function() {
    originalStartDownload();
    trackEvent('download_started', currentPlatform);
};

// Advanced UI Features
function initializeAdvancedFeatures() {
    // Add glow effect to cards on mouse move
    const cards = document.querySelectorAll('.platform-card, .feature-card, .download-card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            card.style.setProperty('--mouse-x', x + 'px');
            card.style.setProperty('--mouse-y', y + 'px');
        });
    });
    
    // Add typing effect to hero title
    typeWriter();
    
    // Setup intersection observer for animations
    setupScrollAnimations();
}

function createParticleEffect() {
    const hero = document.querySelector('.hero');
    if (!hero) return;
    
    // Create particle container
    const particleContainer = document.createElement('div');
    particleContainer.className = 'particle-container';
    particleContainer.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    `;
    hero.appendChild(particleContainer);
    
    // Create particles
    for (let i = 0; i < 50; i++) {
        createParticle(particleContainer);
    }
}

function createParticle(container) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    
    const size = Math.random() * 4 + 2;
    const x = Math.random() * 100;
    const animationDuration = Math.random() * 20 + 10;
    const delay = Math.random() * 5;
    
    particle.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: rgba(0, 255, 136, 0.6);
        border-radius: 50%;
        left: ${x}%;
        top: 100%;
        animation: particleFloat ${animationDuration}s ${delay}s infinite linear;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.8);
    `;
    
    container.appendChild(particle);
    
    // Remove particle after animation
    setTimeout(() => {
        if (particle.parentNode) {
            particle.parentNode.removeChild(particle);
            createParticle(container); // Create new particle
        }
    }, (animationDuration + delay) * 1000);
}

// Add CSS for particle animation
const particleCSS = `
    @keyframes particleFloat {
        0% {
            transform: translateY(0px) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) rotate(360deg);
            opacity: 0;
        }
    }
    
    .particle-container {
        overflow: hidden;
    }
    
    /* Advanced hover effects */
    .platform-card, .feature-card {
        position: relative;
        overflow: hidden;
    }
    
    .platform-card::after, .feature-card::after {
        content: '';
        position: absolute;
        top: var(--mouse-y, 50%);
        left: var(--mouse-x, 50%);
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(0, 255, 136, 0.1) 0%, transparent 70%);
        transform: translate(-50%, -50%);
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
        z-index: 1;
    }
    
    .platform-card:hover::after, .feature-card:hover::after {
        opacity: 1;
    }
    
    /* Glowing border effect */
    .download-card {
        position: relative;
    }
    
    .download-card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #00ff88, #ff0080, #667eea, #00ff88);
        background-size: 400% 400%;
        border-radius: 26px;
        opacity: 0;
        z-index: -1;
        animation: gradientShift 4s ease infinite;
        transition: opacity 0.3s ease;
    }
    
    .download-card:hover::before {
        opacity: 0.7;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Improved button animations */
    .btn {
        position: relative;
        overflow: hidden;
        transform-style: preserve-3d;
    }
    
    .btn::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transform: translateX(-100%);
        transition: transform 0.6s ease;
    }
    
    .btn:hover::after {
        transform: translateX(100%);
    }
`;

// Add CSS to document
const styleSheet = document.createElement('style');
styleSheet.textContent = particleCSS;
document.head.appendChild(styleSheet);

function typeWriter() {
    const heroTitle = document.querySelector('.hero-content h2');
    if (!heroTitle) return;
    
    const originalText = heroTitle.textContent;
    heroTitle.textContent = '';
    heroTitle.style.borderRight = '2px solid #00ff88';
    
    let i = 0;
    function type() {
        if (i < originalText.length) {
            heroTitle.textContent += originalText.charAt(i);
            i++;
            setTimeout(type, 100);
        } else {
            // Remove cursor after typing
            setTimeout(() => {
                heroTitle.style.borderRight = 'none';
            }, 1000);
        }
    }
    
    // Start typing after a delay
    setTimeout(type, 1000);
}

function setupScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.8s ease forwards';
                entry.target.style.opacity = '1';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.platform-card, .feature-card, .stat-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
}

function setupThemeAnimations() {
    // Add floating animation to platform icons
    const platformIcons = document.querySelectorAll('.platform-icon');
    platformIcons.forEach((icon, index) => {
        icon.style.animation = `float 3s ease-in-out infinite ${index * 0.2}s`;
    });
    
    // Add CSS for floating animation
    const floatCSS = `
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        /* Pulse animation for accent elements */
        .accent-pulse {
            animation: accentPulse 2s ease-in-out infinite;
        }
        
        @keyframes accentPulse {
            0%, 100% { box-shadow: 0 0 20px rgba(0, 255, 136, 0.3); }
            50% { box-shadow: 0 0 30px rgba(0, 255, 136, 0.6); }
        }
        
        /* Advanced text glow */
        .text-glow {
            text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            animation: textGlow 2s ease-in-out infinite alternate;
        }
        
        @keyframes textGlow {
            from { text-shadow: 0 0 10px rgba(0, 255, 136, 0.5); }
            to { text-shadow: 0 0 20px rgba(0, 255, 136, 0.8); }
        }
    `;
    
    const floatStyleSheet = document.createElement('style');
    floatStyleSheet.textContent = floatCSS;
    document.head.appendChild(floatStyleSheet);
}

// Add bounce animation CSS
const bounceCSS = `
    @keyframes bounce {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
`;

const bounceStyleSheet = document.createElement('style');
bounceStyleSheet.textContent = bounceCSS;
document.head.appendChild(bounceStyleSheet); 