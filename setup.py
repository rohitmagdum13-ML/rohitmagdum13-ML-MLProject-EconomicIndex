from setuptools import setup, find_packages

# Define a variable to identify specific marker text that might appear in the requirements file
HYPEN_E_DOT = '-e.'

# Function to retrieve requirements from a file and process them
def get_requirements(filepath):
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()  # Read each line in the file as a list

        # Clean up newline characters from each line
        requirements = [each.replace("/n", "") for each in requirements]

        # Remove any occurrences of '-e .' from the requirements list if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements  # Return the list of requirements


# Use the setup() function from setuptools to define the package details and installation requirements
setup(
    name="MLProject-Economic_Index",         # The name of the project/package
    version="0.0.1",                         # Initial version number
    author="Rohit",                          # Author's name
    author_email="rohitmagdum1306@gmail.com",  # Author's email address
    description="A short description of your project",  # Brief description of the project
    # long_description=long_description,      # (Optional) Full project description, often from README
    # long_description_content_type="text/markdown",  # (Optional) Specify markdown format for the long description
    # url="https://github.com/yourusername/yourproject",  # (Optional) Link to project repository or homepage
    packages=find_packages(),                # Automatically discover and include all packages in the directory
    install_requires=get_requirements('requirements.txt')  # List of external dependencies needed by the project
)
