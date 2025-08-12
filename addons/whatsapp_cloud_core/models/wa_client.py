import logging, requests
from odoo import models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class WaClient(models.AbstractModel):
    _name = "wa.client"
    _description = "WhatsApp Cloud API Client"

    _api_version = "v20.0"

    def _base_url(self):
        return f"https://graph.facebook.com/{self._api_version}"

    def _headers(self, access_token: str):
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def _request(self, method: str, path: str, *, access_token: str, json=None, params=None, timeout=30):
        url = f"{self._base_url()}{path}"
        try:
            resp = requests.request(method, url, headers=self._headers(access_token),
                                    json=json, params=params, timeout=timeout)
        except requests.RequestException as e:
            _logger.exception("Error de red WhatsApp: %s", e)
            raise UserError(_("Error de red al conectar con WhatsApp Cloud."))
        if not resp.ok:
            try:
                msg = resp.json().get("error", {}).get("message") or resp.text
            except Exception:
                msg = resp.text
            _logger.error("WhatsApp API error %s: %s", resp.status_code, msg)
            raise UserError(_("WhatsApp Cloud API respondió error: %s") % msg)
        return resp.json()

    def send_text(self, *, phone_number_id: str, access_token: str, to_number: str, message: str):
        payload = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {"body": message},
        }
        return self._request("POST", f"/{phone_number_id}/messages",
                             access_token=access_token, json=payload)
