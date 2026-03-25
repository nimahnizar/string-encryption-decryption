import sys
from datetime import datetime

def main():

    # Ensures the log file name is provided as a command-line argument

    if len(sys.argv) != 2:
        print("Usage: python3 logger.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]

    # Opens the log file in append mode so existing logs are preserved
    with open(logfile, "a") as f:
        # Continuously reads log messages from standard input
        for line in sys.stdin:
            line = line.strip()
            
            # QUIT signals the logger to stop and exit
            if line == "QUIT":
                break
                
            # Ignores empty lines
            if line == "":
                continue
                
                
            # Splits the input into an action and a message
            parts = line.split(maxsplit=1)
            action = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            # Generates a timestamp in the required format
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            # Writes the formatted log entry to the file
            f.write(f"{timestamp} [{action}] {message}\n")
            f.flush()

if __name__ == "__main__":
    main()


