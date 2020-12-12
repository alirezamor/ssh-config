import subprocess
docker_version = subprocess.getoutput("docker -v")
if "Docker version" in docker_version:
    print("docker is installed")
else:
    print("docker is not installed")