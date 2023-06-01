import pexpect
# Spawn a new process with 'sudo passwd'
child = pexpect.spawn('sudo passwd')

# Expect the first password prompt and provide the new password
child.expect('Enter new UNIX password:')
child.sendline('new_password')

# Expect the second password prompt for confirmation and provide the same password again
child.expect('Retype new UNIX password:')
child.sendline('new_password')

# Wait for the command to finish executing
child.wait()

# Print the output of the command
print(child.before.decode())
