service_data = {"host": "192.168.1.93", "packet": "JgAYAB8cOj0fGzs8IBs7HiAbHR4fOiAcHQANBQ=="}
hass.services.call("broadlink", "send", service_data, True)