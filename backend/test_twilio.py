"""Simple tester that sends WhatsApp messages using the project's AlertService.

Usage:
 - Ensure backend/.env contains correct `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`.
 - For Twilio Sandbox: each recipient must opt-in by messaging the sandbox join code.
"""
try:
    from .alerts import AlertService
except Exception:
    from alerts import AlertService

service = AlertService()

# Recipients in international format (E.164) WITHOUT the 'whatsapp:' prefix
recipients = [
    "923109661075",   # 03109661075
]

for number in recipients:
    try:
        res = service.send_whatsapp_message(number, """🚨 AIR QUALITY ALERT – SMOGNET 🚨
                                                    Unhealthy pollutant levels detected.

                                                    ➤ Avoid outdoor exposure.
                                                    ➤ Wear an N95 mask if you must go out.
                                                    ➤ Keep windows closed. Use air purifiers if available.

                                                    Stay safe. SmogNet Intelligence""")
        print(f"Sent to {res['to']} | SID: {res['sid']} | status: {res['status']}")
    except Exception as e:
        print(f"Failed to send to +{number}: {e}")
