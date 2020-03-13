service_data = {"host": "192.168.1.93", "packet": "JgAYAB8cOjwgGzs8Hxw7HiAbHTwgGyAbHQANBQ=="}
hass.services.call("broadlink", "send", service_data, True)