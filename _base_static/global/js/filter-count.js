const filters = document.querySelectorAll(".filter-checkbox")
const filterCount = document.querySelector('.filter-count')
const clean_filters = document.querySelector('.reset')

function updateFilterCount() {
    const selectedFilters = document.querySelectorAll('.filter-checkbox:checked');

    if (selectedFilters.length > 0) {
        filterCount.style.display = 'flex';
    } else {
        filterCount.style.display = 'none';
    }
    
    filterCount.textContent = selectedFilters.length;
}

filters.forEach(filter => {
    filter.addEventListener("change", () => {
        updateFilterCount();
    });
});

clean_filters.addEventListener('click', () => {
    filters.forEach(filter => {
        filter.checked = false;
    })
    updateFilterCount();
});

updateFilterCount();