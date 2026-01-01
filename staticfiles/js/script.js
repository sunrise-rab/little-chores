function showMore(groupId, button) {
    const extraItems = document.querySelectorAll('.extra-' + groupId);
  
    extraItems.forEach(element => {
      element.classList.remove('d-none');
    });
  
    button.remove();
  }
  