/**
 * Prospire Next login page — progressive enhancement.
 * Adds a loading state to the native Odoo login submit button.
 * Authentication itself is untouched (native /web/login POST).
 */
(function () {
    "use strict";

    function onReady(fn) {
        if (document.readyState !== "loading") {
            fn();
        } else {
            document.addEventListener("DOMContentLoaded", fn);
        }
    }

    onReady(function () {
        var form = document.querySelector(".prospire-form-container .oe_login_form");
        if (!form) {
            return;
        }
        form.addEventListener("submit", function () {
            var btn = form.querySelector('.oe_login_buttons button[type="submit"].btn-primary');
            if (btn && !btn.disabled) {
                btn.disabled = true;
                btn.textContent = "Signing in…";
            }
        });
    });
})();
