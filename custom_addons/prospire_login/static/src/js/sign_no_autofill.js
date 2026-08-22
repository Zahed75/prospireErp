/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { SignablePDFIframe } from "@sign/components/sign_request/signable_PDF_iframe";

/**
 * Prospire Next: never one-click auto-fill a signature box.
 *
 * Stock Odoo fills a signature box with the signer's saved signature on a
 * single click, without opening the dialog. Combined with a template whose
 * fields share one role, that silently stamps the current signer's
 * signature into boxes meant for someone else.
 *
 * This patch always opens the signature dialog so every fill is a
 * deliberate action by the signer responsible for that box.
 */
patch(SignablePDFIframe.prototype, {
    handleSignatureDialogClick(signatureItem, signItemType) {
        if (signatureItem.dataset.signature) {
            // Box already filled: keep stock behavior (allows re-sign/reset).
            return super.handleSignatureDialogClick(signatureItem, signItemType);
        }
        this.refreshSignItems();
        this.openSignatureDialog(signatureItem, signItemType);
    },
});
