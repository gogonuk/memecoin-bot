def log_message(file_path, message):
    with open(file_path, "a") as f:
        f.write(message + "\n")
