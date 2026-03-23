document.addEventListener('DOMContentLoaded', () => {
  // Header scroll
  const header = document.getElementById('header');
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true   // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});

  // Mobile menu
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('nav');
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    nav.classList.toggle('active');
    // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  nav.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      nav.classList.remove('active');
      // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
    // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = header.offsetHeight;
        window.scrollTo({
          top: target.getBoundingClientRect().top + window.scrollY - offset,
          behavior: 'smooth'
          // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
      }
      // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
    // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});

  // Fade-in on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, i * 80);
        observer.unobserve(entry.target);
      }
      // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  }, { threshold: 0.1   // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});

  document.querySelectorAll('.product-card, .philosophy-card, .quality-list li').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
    observer.observe(el);
    // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  // Scroll progress bar
  const progressBar = document.getElementById('scrollProgress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + '%' : '0%';
    }, { passive: true   // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  }

// Scroll Progress Bar
const scrollProgress = document.getElementById('scrollProgress');
if (scrollProgress) {
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrollTop / docHeight) * 100;
    scrollProgress.style.width = progress + '%';
  }, { passive: true   // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
}

  // Scroll progress bar

  // Scroll progress bar
  const scrollProgress = document.getElementById('scrollProgress');
  if (scrollProgress) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;
      scrollProgress.style.width = progress + '%';
    }, { passive: true   // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  }

  // Scroll progress bar
  const scrollProgress = document.getElementById('scrollProgress');
  if (scrollProgress) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress.style.width = (scrollTop / docHeight * 100) + '%';
    }, { passive: true   // Scroll progress bar
  const progressBar = document.getElementById("scrollProgress");
  if (progressBar) {
    window.addEventListener("scroll", () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      progressBar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + "%" : "0%";
    }, { passive: true });
  }
});
  }

  // Scroll progress bar
  const progressBar = document.getElementById('scrollProgress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    }, { passive: true });
  }

  // Back to top button
  const backBtn = document.getElementById('backToTop');
  if (backBtn) {
    window.addEventListener('scroll', () => {
      backBtn.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });
    backBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
