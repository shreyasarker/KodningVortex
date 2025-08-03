const images = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg'
];

let current = 0;

const sliderImg = document.getElementById('slider-img');

function showSlide(index) {
    sliderImg.src = images[index];
}

function nextSlide() {
    current = (current + 1) % images.length;
    showSlide(current);
}

function prevSlide() {
    current = (current - 1 + images.length) % images.length;
    showSlide(current);
}

// Auto-play every 4 seconds
setInterval(nextSlide, 4000);
