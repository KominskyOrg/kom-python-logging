# workflow_scripts/check_versions.py
import re
import requests
import os

def get_current_version():
    with open('setup.py', 'r') as file:
        for line in file:
            match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', line)
            if match:
                return match.group(1)
    raise RuntimeError("Cannot find the version information in setup.py")

def get_latest_pypi_version(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching package information from PyPI: {response.status_code}")
    data = response.json()
    return data['info']['version']

def compare_versions(current_version, latest_version):
    current_parts = list(map(int, current_version.split('.')))
    latest_parts = list(map(int, latest_version.split('.')))

    if current_parts <= latest_parts:
        raise ValueError(f"Current version {current_version} is not greater than the latest PyPI version {latest_version}")

def main():
    package_name = os.getenv('PACKAGE_NAME', 'kom-python-logging')
    current_version = get_current_version()
    latest_pypi_version = get_latest_pypi_version(package_name)
    compare_versions(current_version, latest_pypi_version)
    print(f"Current version {current_version} is greater than the latest PyPI version {latest_pypi_version}")

if __name__ == "__main__":
    main()
