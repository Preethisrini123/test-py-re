from datetime import datetime

username = "balaji"
action = "login, logout, viewed dashboard"
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

with open("activity_log.txt", "a") as file:
    file.write(f"{current_time} - {username} - {action}\n") 

print("Log updated successfully") 
