import subprocess

subprocess.run(["ls", "-l", ".."])

subprocess.run("exit 1", shell=True, check=True)

subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)

with subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE) as proc:
    print(proc.stdout.read())
