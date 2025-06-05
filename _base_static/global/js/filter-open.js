const filterButton = document.querySelector(".filter-button");
const close_filter = document.querySelector(".close-filter");
const overlay_filter = document.getElementById("overlay");
const filter = document.querySelector(".filter");
let isOpen = false;

function openFilter() {
    filter.style.right = "0px";
    overlay_filter.style.display = 'flex';
    isOpen = true;
}

function closeFilter() {
    filter.style.right = "-400px";
    overlay_filter.style.display = 'none';
    isOpen = false;
}

filterButton.addEventListener("click", () => {
    if (isOpen) {
        closeFilter();
    } else {
        openFilter();
    }
})

overlay_filter.addEventListener("click", () => {
    closeFilter();
})

close_filter.addEventListener("click", () => {
    closeFilter();
})