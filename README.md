<h1>How to run (A step by step guide)</h1>
 
<h2>Clone Repo</h2>
On the command line: 
<p>
C:\Users\..\..\projects (master -> origin)
<br>
λ git clone https://github.com/LauraFlaherty/EmergingTechAssignment.git
  </p>

<h2>Create a virtual environment</h2>
Assuming Anaconda is installed, navigate to cloned repo
<p>
C:\Users\..\projects (master -> origin) <br>
λ cd EmergingTechAssignment\
</p>
<h4>Install PIP</h4>
<p> λ conda install pip </p>
<h4>Virtual Environment Creation</h4>
<p>
C:\Users\..\..\projects\EmergingTechAssignment (master -> origin)<br>
λ conda create --name my_project_env
<h4>Activate Virtual Environment</h4>
<p>
C:\Users\..\..\projects\EmergingTechAssignment (master -> origin)<br>
λ conda activate my_project_env
</p>

<h2>Install Requirements.txt </h2>
<p>
C:\Users\..\..\projects\EmergingTechAssignment (master -> origin)<br>
(my_project_env) λ pip install -r requirements.txt
 </p>
 <h2>*NOTE* if requirements installation fails do the following: </h2>
 <p>(my_project_env) λ pip install tensorflow==1.13.1</p>
 <p> (my_project_env) λ pip install Keras==2.3.1</p>

<h2>Navigate to Web folder and run Flask application</h2>
<h4>Go to Web directory </h4>
<p>C:\Users\..\..\projects\EmergingTechAssignment (master -> origin)<br>
(my_project_env) λ cd web
</p>
<h4>Run App</h4>
<p>C:\Users\..\..\projects\EmergingTechAssignment\Web (master -> origin)<br>
(my_project_env) λ python app.py
  </p>
 
 <h2>Open up browser and go to http://localhost:5000/</h2>
 <p>Try out the web app! </p>
 <br>
 <br>
 <h5>When Finished</h5>
<ul>
  <li>In command line hold down Ctrl C to stop app running</li>
  <li>To deactivate virtual environment: conda deactivate</li>
  <li>To delete virtual environment: conda env remove --name my_project_env</li>
</ul>
