## Step to run GENAI-QUESTIONAIR
- Clone questionair in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to genai-questionair progect (in step 1) from conda prompt and/by follow below commands
    * cd <basepath>/genai-questionair
    * conda create -n questionair python=3.8 -y
    * conda activate questionair
    * pip install -r requirement.txt
    * python setup.py install
- Create a file with name '.env' in genai-questionair folder
- Add below line in .env file
    * OPENAI_API_KEY="Supply your secret token here"
- Run questionair with below command
    * streamlit run chatbot.py --server.port 8080
- Open http://localhost:8080/ on your favorite browser
    * Upload any pdf with content
    * And ask any question related to document e.g. please highlight the key notes from the document?
