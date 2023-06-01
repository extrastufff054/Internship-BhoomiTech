import subprocess
import getpass

# Define the command you want to execute
command = "your_command_here"

# Prompt the user for the root password
root_password = getpass.getpass("Enter the root password: ")

# Use the 'sudo' command to execute the command with root privileges
sudo_command = f"echo '{root_password}' | sudo -S {command}"

# Execute the command using subprocess
process = subprocess.Popen(sudo_command, shell=True)
process.wait()
