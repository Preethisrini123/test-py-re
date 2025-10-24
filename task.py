import json
config = {
    "app_name": "MyApp",
    "version": "1.0",
    "debug": True
}
with open("config.json", "w") as file:
    json.dump(config, file, indent=4)
with open("config.json", "r") as file:
    data = json.load(file)
print("Old Config:", data)
data["debug"] = False
with open("config.json", "w") as file:
    json.dump(data, file, indent=4)
print("New Config:", data)
print("Config updated successfully!")
