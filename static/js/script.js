function showMore(groupId, button) {
    const extraItems = document.querySelectorAll('.extra-' + groupId);
  
    extraItems.forEach(element => {
      element.classList.remove('d-none');
    });
  
    button.remove();
  }

  // Refresh chores when child changes
  document.addEventListener("DOMContentLoaded", function () {
    const childSelect = document.querySelector("#id_child");
    const filterForm = document.querySelector("#childFilterForm");

    if (childSelect && filterForm) {
      childSelect.addEventListener("change", function () {
        filterForm.submit();  // ✅ reload page with correct chores for chosen child
      });
    }
  });

  