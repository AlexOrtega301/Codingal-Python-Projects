speed = int(input("Enter download speed MB/s: "))
size = int(input("Enter download size in MB: "))
name = input("Enter download name: ")

# Check if speed and size are positive
if speed <= 0 or size <= 0:
   w = input("Error: Speed and size must be positive numbers.")
else:
    # Calculate the time it will take to download
    time_to_download = size / speed

    print(f"Starting download of {name} with size {size}MB at {speed}MB/S")

    for second in range(int(time_to_download)):
        downloaded = speed * (second + 1)
        remaining = size - downloaded
        print(f"Seconds passed: {second+1}, Downloaded: {downloaded}MB, Remaining: {remaining}MB, Download Name: {name}")
    print("Your Download is Ready with Name", name, "With Size", size, "MB, And Download/Internet Speed", speed,"MB/s")
    f = input("©️Downloads Manager")
