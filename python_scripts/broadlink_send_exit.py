service_data = {"host": "192.168.1.93", "packet": "JgAYAB0dPjkeHTs8HR49HB07IBweHSAbIAANBQ=="}
hass.services.call("broadlink", "send", service_data, True)