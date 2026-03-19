// Password protection for CogniCit website
// Password: "wenus"

(function() {
    'use strict';

    const PASSWORD = 'wenus';
    const SESSION_STORAGE_KEY = 'cognicit_authorized';

    function checkPassword() {
        return sessionStorage.getItem(SESSION_STORAGE_KEY) === 'true';
    }

    function showModal() {
        const modal = document.getElementById('password-modal');
        if (modal) {
            modal.style.display = 'flex';
        }
    }

    function hideModal() {
        const modal = document.getElementById('password-modal');
        if (modal) {
            modal.style.display = 'none';
        }
    }

    function showError(message) {
        const errorElement = document.getElementById('password-error');
        if (errorElement) {
            errorElement.textContent = message;
            setTimeout(() => {
                errorElement.textContent = '';
            }, 3000);
        }
    }

    function handleSubmit(event) {
        event.preventDefault();

        const passwordInput = document.getElementById('password-input');
        const password = passwordInput.value;

        if (password === PASSWORD) {
            sessionStorage.setItem(SESSION_STORAGE_KEY, 'true');
            hideModal();
            passwordInput.value = '';
        } else {
            showError('Nieprawidłowe hasło. Spróbuj ponownie.');
            passwordInput.value = '';
            passwordInput.focus();
        }
    }

    function init() {
        const form = document.getElementById('password-form');
        const passwordInput = document.getElementById('password-input');

        if (!form || !passwordInput) {
            console.error('Password form elements not found');
            return;
        }

        // Check if already authorized in this session
        if (checkPassword()) {
            hideModal();
            return;
        }

        // Show modal
        showModal();

        // Add event listener
        form.addEventListener('submit', handleSubmit);

        // Allow Enter key to submit
        passwordInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                handleSubmit(e);
            }
        });

        // Focus on input
        passwordInput.focus();
    }

    // Run on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
