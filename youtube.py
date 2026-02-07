let totalSeconds = 0;
document.querySelectorAll('#overlays span.ytd-thumbnail-overlay-time-status-renderer').forEach(el => {
    let parts = el.innerText.trim().split(':').map(Number);
    if (parts.length === 3) {
        // hh:mm:ss
        totalSeconds += parts[0]*3600 + parts[1]*60 + parts[2];
    } else if (parts.length === 2) {
        // mm:ss
        totalSeconds += parts[0]*60 + parts[1];
    }
});

let hours = Math.floor(totalSeconds / 3600);
let minutes = Math.floor((totalSeconds % 3600) / 60);
let seconds = totalSeconds % 60;

console.log(`Total playlist length: ${hours}h ${minutes}m ${seconds}s`);
