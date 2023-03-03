// Create a canvas element for the hero image
const heroCanvas = document.createElement('canvas');
heroCanvas.width = 1200;
heroCanvas.height = 800;
const heroCtx = heroCanvas.getContext('2d');

// Draw a gradient background
const heroGradient = heroCtx.createLinearGradient(0, 0, 0, heroCanvas.height);
heroGradient.addColorStop(0, '#f1c40f');
heroGradient.addColorStop(1, '#e67e22');
heroCtx.fillStyle = heroGradient;
heroCtx.fillRect(0, 0, heroCanvas.width, heroCanvas.height);

// Draw the hero text
heroCtx.fillStyle = '#fff';
heroCtx.font = 'bold 72px Arial';
heroCtx.textAlign = 'center';
heroCtx.fillText('OpolCandy', heroCanvas.width / 2, heroCanvas.height / 2);

// Create a canvas element for the about image
const aboutCanvas = document.createElement('canvas');
aboutCanvas.width = 800;
aboutCanvas.height = 600;
const aboutCtx = aboutCanvas.getContext('2d');

// Draw a solid color background
aboutCtx.fillStyle = '#333';
aboutCtx.fillRect(0, 0, aboutCanvas.width, aboutCanvas.height);

// Draw the about text
aboutCtx.fillStyle = '#fff';
aboutCtx.font = 'bold 48px Arial';
aboutCtx.textAlign = 'center';
aboutCtx.fillText('About Us', aboutCanvas.width / 2, 100);
aboutCtx.font = '24px Arial';
aboutCtx.fillText('We are a family-owned candy shop', aboutCanvas.width / 2, 200);
aboutCtx.fillText('that has been in business for over 50 years.', aboutCanvas.width / 2, 250);
aboutCtx.fillText('We take pride in using the finest ingredients', aboutCanvas.width / 2, 300);
aboutCtx.fillText('and creating the most delicious candies.', aboutCanvas.width / 2, 350);

// Export the canvas elements as PNG images
const heroImage = heroCanvas.toDataURL('image/png');
const aboutImage = aboutCanvas.toDataURL('image/png');
