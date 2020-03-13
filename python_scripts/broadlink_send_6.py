service_data = {"host": "192.168.1.93", "packet": "JgAWAB8cOj0fGzs8IBs8Hh8bHjsgHDoADQUAAA=="}
hass.services.call("broadlink", "send", service_data, True)