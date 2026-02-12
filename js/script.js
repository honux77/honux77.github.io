/* ============================================
   HONUX PROFILE - Retro Interactions
   ============================================ */

(function () {
  'use strict';

  /* --- Theme Toggle --- */
  var themeToggle = document.getElementById('themeToggle');
  var toggleIcon = document.getElementById('toggleIcon');
  var html = document.documentElement;

  function getStoredTheme() {
    return localStorage.getItem('honux-theme') || 'dark';
  }

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('honux-theme', theme);
    toggleIcon.textContent = theme === 'dark' ? '\u2600' : '\u263E';
  }

  setTheme(getStoredTheme());

  themeToggle.addEventListener('click', function () {
    var current = html.getAttribute('data-theme');
    setTheme(current === 'dark' ? 'light' : 'dark');
  });

  /* --- Typewriter Effect --- */
  var typewriterEl = document.getElementById('typewriter');
  var config = window.SITE_CONFIG || {};
  var text = config.typewriterText || 'Software Developer & Bootcamp Organizer';
  var charIndex = 0;

  function typeChar() {
    if (charIndex < text.length) {
      typewriterEl.textContent += text.charAt(charIndex);
      charIndex++;
      setTimeout(typeChar, 60 + Math.random() * 40);
    }
  }

  setTimeout(typeChar, 600);

  /* --- Scroll Reveal Sections --- */
  var sections = document.querySelectorAll('.section');

  function revealSections() {
    var windowHeight = window.innerHeight;
    for (var i = 0; i < sections.length; i++) {
      var rect = sections[i].getBoundingClientRect();
      if (rect.top < windowHeight * 0.85) {
        sections[i].classList.add('visible');
      }
    }
  }

  revealSections();
  window.addEventListener('scroll', revealSections, { passive: true });

  /* --- Sticky Nav on Scroll --- */
  var nav = document.getElementById('nav');
  var heroBottom = 200;

  function handleNav() {
    if (window.scrollY > heroBottom) {
      nav.classList.add('visible');
    } else {
      nav.classList.remove('visible');
    }
  }

  window.addEventListener('scroll', handleNav, { passive: true });

  /* --- Star Field (Dark Mode Only) --- */
  var canvas = document.getElementById('starfield');
  var ctx = canvas.getContext('2d');
  var stars = [];
  var starCount = 80;
  var animFrameId = null;

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function createStars() {
    stars = [];
    for (var i = 0; i < starCount; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 2 + 0.5,
        speed: Math.random() * 0.3 + 0.05,
        opacity: Math.random() * 0.8 + 0.2,
        twinkleSpeed: Math.random() * 0.02 + 0.005
      });
    }
  }

  function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (var i = 0; i < stars.length; i++) {
      var star = stars[i];
      star.opacity += star.twinkleSpeed;
      if (star.opacity >= 1 || star.opacity <= 0.1) {
        star.twinkleSpeed = -star.twinkleSpeed;
      }

      star.y -= star.speed;
      if (star.y < -2) {
        star.y = canvas.height + 2;
        star.x = Math.random() * canvas.width;
      }

      ctx.beginPath();
      ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(200, 210, 255, ' + star.opacity + ')';
      ctx.fill();
    }

    animFrameId = requestAnimationFrame(drawStars);
  }

  resizeCanvas();
  createStars();
  drawStars();

  window.addEventListener('resize', function () {
    resizeCanvas();
    createStars();
  });

  /* --- Konami Code Easter Egg --- */
  var konamiCode = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'b', 'a'
  ];
  var konamiIndex = 0;

  document.addEventListener('keydown', function (e) {
    if (e.key === konamiCode[konamiIndex]) {
      konamiIndex++;
      if (konamiIndex === konamiCode.length) {
        activateKonamiMode();
        konamiIndex = 0;
      }
    } else {
      konamiIndex = 0;
    }
  });

  function activateKonamiMode() {
    document.body.style.animation = 'none';
    void document.body.offsetHeight;
    document.body.style.animation = 'rainbow-bg 2s ease';

    var style = document.createElement('style');
    style.textContent = '@keyframes rainbow-bg { ' +
      '0% { filter: hue-rotate(0deg); } ' +
      '50% { filter: hue-rotate(180deg); } ' +
      '100% { filter: hue-rotate(360deg); } }';
    document.head.appendChild(style);

    setTimeout(function () {
      document.body.style.animation = '';
      document.head.removeChild(style);
    }, 2000);
  }
})();
