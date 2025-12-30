def analyze_log(file_name):
    info_count = 0
    error_count = 0

    try:
        file = open(file_name, "r")

        for line in file:
            if "INFO" in line:
                info_count += 1
            elif "ERROR" in line:
                error_count += 1

        file.close()

        print("Log Analysis Result")
        print("-------------------")
        print("INFO messages :", info_count)
        print("ERROR messages:", error_count)

    except FileNotFoundError:
        print("Log file not found.")

# Run the program
analyze_log("app.log")
