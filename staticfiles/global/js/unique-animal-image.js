function setActiveImage(image) {
    const activeImage = document.getElementById('active-image');
    activeImage.src = image.src;

    document.querySelectorAll('.thumbnail').forEach(img => {
        img.classList.remove('active-thumbnail');
    });

    image.classList.add('active-thumbnail');
}