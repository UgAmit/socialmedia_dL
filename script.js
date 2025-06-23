// Platform Detection and Mock Data
const platforms = {
    youtube: {
        icon: '🎬',
        name: 'YouTube',
        domains: ['youtube.com', 'youtu.be', 'm.youtube.com'],
        color: '#ff0000'
    },
    instagram: {
        icon: '📱',
        name: 'Instagram',
        domains: ['instagram.com', 'instagr.am'],
        color: '#e4405f'
    },
    twitter: {
        icon: '🐦',
        name: 'Twitter/X',
        domains: ['twitter.com', 'x.com', 't.co'],
        color: '#1da1f2'
    },
    tiktok: {
        icon: '🎵',
        name: 'TikTok',
        domains: ['tiktok.com', 'vm.tiktok.com'],
        color: '#000000'
    },
    facebook: {
        icon: '📘',
        name: 'Facebook',
        domains: ['facebook.com', 'fb.com', 'm.facebook.com'],
        color: '#1877f2'
    },
    reddit: {
        icon: '🤖',
        name: 'Reddit',
        domains: ['reddit.com', 'redd.it'],
        color: '#ff4500'
    },
    vimeo: {
        icon: '🎥',
        name: 'Vimeo',
        domains: ['vimeo.com'],
        color: '#1ab7ea'
    },
    twitch: {
        icon: '🎮',
        name: 'Twitch',
        domains: ['twitch.tv', 'clips.twitch.tv'],
        color: '#9146ff'
    }
};

// Mock media data for demonstration
const mockMediaData = {
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
    }
};

// Global variables
let currentPlatform = null;
let isDownloading = false;

// Initialize page
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    addSmoothScrolling();
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

    if (!url) {
        showMessage('Please enter a valid URL', 'error');
        return;
    }

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
        platformIcon.textContent = platform.icon;
        platformName.textContent = `${platform.name} detected!`;
        platformName.style.color = platform.color;

        // Show media info after a delay (simulating API call)
        setTimeout(() => {
            showMediaInfo(detectedPlatform);
            downloadOptions.style.display = 'block';
        }, 800);

        showMessage(`✅ ${platform.name} URL detected successfully!`, 'success');
    } else {
        showMessage('⚠️ Platform not recognized. Trying universal downloader...', 'info');
        // Fallback to universal
        platformIcon.textContent = '🌐';
        platformName.textContent = 'Universal Downloader';
        platformName.style.color = '#4a56e2';
        
        setTimeout(() => {
            downloadOptions.style.display = 'block';
        }, 500);
    }
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
    document.getElementById('platformIcon').textContent = '🌐';
    document.getElementById('platformName').textContent = 'Enter URL to detect platform';
    document.getElementById('platformName').style.color = '#333';
    document.getElementById('mediaInfo').style.display = 'none';
    document.getElementById('downloadOptions').style.display = 'none';
    currentPlatform = null;
}

function startDownload() {
    if (isDownloading) {
        showMessage('⏳ Download already in progress!', 'info');
        return;
    }

    const url = document.getElementById('urlInput').value.trim();
    const format = document.getElementById('formatSelect').value;
    const quality = document.getElementById('qualitySelect').value;

    if (!url) {
        showMessage('❌ Please enter a URL first!', 'error');
        return;
    }

    isDownloading = true;
    showProgressSection();
    
    // Simulate download process
    simulateDownload(format, quality);
}

function showProgressSection() {
    const progressSection = document.getElementById('progressSection');
    progressSection.style.display = 'block';
    progressSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function simulateDownload(format, quality) {
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    
    const steps = [
        { progress: 0, text: 'Initializing download...' },
        { progress: 15, text: 'Analyzing media URL...' },
        { progress: 30, text: 'Fetching media information...' },
        { progress: 45, text: 'Selecting best quality...' },
        { progress: 60, text: `Downloading ${format === 'video' ? 'video' : 'audio'} (${quality})...` },
        { progress: 80, text: 'Processing media file...' },
        { progress: 95, text: 'Finalizing download...' },
        { progress: 100, text: 'Download completed! 🎉' }
    ];

    let currentStep = 0;

    function updateProgress() {
        if (currentStep < steps.length) {
            const step = steps[currentStep];
            progressFill.style.width = `${step.progress}%`;
            progressText.textContent = step.text;
            
            if (step.progress === 100) {
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
        youtube: 'https://youtube.com/watch?v=dQw4w9WgXcQ',
        instagram: 'https://instagram.com/p/ABC123/',
        twitter: 'https://twitter.com/user/status/123456789',
        tiktok: 'https://tiktok.com/@user/video/1234567890',
        facebook: 'https://facebook.com/user/videos/123456789',
        reddit: 'https://reddit.com/r/videos/comments/abc123/',
        vimeo: 'https://vimeo.com/123456789',
        twitch: 'https://clips.twitch.tv/ClipName'
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