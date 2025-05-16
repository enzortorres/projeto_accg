const dropdowns = document.querySelectorAll('.filter-dropdown');

dropdowns.forEach(dropdown => {
    const filterDropdownClick = dropdown.querySelector(".filter-dropdown-click");

    filterDropdownClick.addEventListener("click", () => {
        dropdown.classList.toggle("active");
    });
});
