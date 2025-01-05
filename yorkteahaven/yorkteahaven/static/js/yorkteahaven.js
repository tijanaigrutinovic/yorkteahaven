const hamburger = document.getElementById('hamburger');
const modal = document.getElementById('modal');
const closeModal = document.getElementById('close');
const navLinks = document.querySelectorAll('.modal-nav-list a');

hamburger.addEventListener('click', () => {
    modal.style.display = 'block'; 
});

closeModal.addEventListener('click', () => {
    modal.style.display = 'none'; 
});

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        modal.style.display = 'none';
    });
});


//brew tips
window.addEventListener('scroll', function() {
    const tips = document.querySelectorAll('.brew-tip');
    
    tips.forEach(tip => {
      const tipPosition = tip.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
  
      if (tipPosition < windowHeight - 100) {
        tip.classList.add('active');
      }
    });
  });
  
  document.querySelectorAll('.learn-more').forEach(button => {
    button.addEventListener('click', function() {
      const parentDiv = this.closest('.brew-tip');
      const fullDescription = parentDiv.querySelector('.full-description');
      
      if (fullDescription.style.display === 'block' || fullDescription.style.display === '') {
        fullDescription.style.display = 'block';
      }
    });
  });