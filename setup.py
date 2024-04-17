from setuptools import find_packages,setup

setup(
    name='genai-questionair',
    version='0.0.1',
    author='Satyaprakash Nayak',
    author_email='n.satyaprakash@yahoo.com',
    install_requires=["openai","tiktoken","langchain","langchain-community","streamlit","faiss-cpu","python-dotenv","PyPDF2"],
    packages=find_packages()
)