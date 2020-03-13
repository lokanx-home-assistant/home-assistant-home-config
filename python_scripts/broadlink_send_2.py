service_data = {"host": "192.168.1.93", "packet": "JgAWAB8cOjwgGzs8IBs7HiAbHR4fOjsADQUAAA=="}
hass.services.call("broadlink", "send", service_data, True)