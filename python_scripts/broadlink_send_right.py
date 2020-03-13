service_data = {"host": "192.168.1.93", "packet": "JgAWAB4dOzweHTs8HR49HB08PTkeHSAADQUAAA=="}
hass.services.call("broadlink", "send", service_data, True)