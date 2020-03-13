service_data = {"host": "192.168.1.93", "packet": "JgAUACEaOzwgGzo8IBs8HiA4PDs6AA0FAAAAAA=="}
hass.services.call("broadlink", "send", service_data, True)