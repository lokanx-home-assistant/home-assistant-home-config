service_data = {"host": "192.168.1.93", "packet": "JgAYAB8cPTofHDo9IBsdHj0cHR4eHSAbHgANBQ=="}
hass.services.call("broadlink", "send", service_data, True)