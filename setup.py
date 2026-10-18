from pathlib import Path

from setuptools import find_packages, setup


def get_requirements(file_path: Path) -> list[str]:
    with file_path.open(encoding="utf-8") as file_obj:
        return [
            requirement
            for line in file_obj
            if (requirement := line.strip()) and not requirement.startswith("-e")
        ]


setup(
    name="MLProject",
    version="0.1.0",
    author="Manoj Prajapati",
    author_email="manojoffice525@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(Path(__file__).parent / "requirements.txt"),
)