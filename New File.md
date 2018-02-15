---


---

<h1 id="a-gentle-introduction-to-neural-nets">A Gentle Introduction To Neural Nets</h1>
<h2 id="python">Python</h2>
<blockquote>
<p><em>“Python is an interpreted, object-oriented, high-level programming<br>
language”</em></p>
</blockquote>
<p>Many of you have probably written in - or heard of - R. Both R and Python are considered high-level programming languages that can be used for analytics.<br>
Although we are taught R here at KU, it is important to be aware of other tools and languages commonly found out in industry.</p>
<p>If you would like to learn more about Python explore the links below:</p>
<p><strong>Learn the History and Common Use of Python</strong></p>
<p>Wikipedia: For history and general knowledge.</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)">https://en.wikipedia.org/wiki/Python_(programming_language)</a></li>
</ul>
<p>Data Science Graduate Programs: A website providing background on all things form Python to Hadoop, Spark and Online Courses.</p>
<ul>
<li><a href="https://www.datasciencegraduateprograms.com/python/">https://www.datasciencegraduateprograms.com/python/</a></li>
</ul>
<p><strong>Beginner Tutorials in Python:</strong></p>
<p>Python Software Foundation: Python’s Official Documentation.</p>
<ul>
<li><a href="https://docs.python.org/2.7/">https://docs.python.org/2.7/</a></li>
</ul>
<p>Python Software Foundation: Beginner’s Guide For <em>Non-Programmers</em>.</p>
<ul>
<li><a href="https://wiki.python.org/moin/BeginnersGuide/NonProgrammers">https://wiki.python.org/moin/BeginnersGuide/NonProgrammers</a></li>
</ul>
<p>Python Software Foundation: Beginner’s Guide For <em>Programmers</em>.</p>
<ul>
<li><a href="https://wiki.python.org/moin/BeginnersGuide/Programmers">https://wiki.python.org/moin/BeginnersGuide/Programmers</a></li>
</ul>
<h2 id="installing-python">Installing Python</h2>
<p>We will be using Python 2.7…<br>
Before we install - let’s check to make sure it is not already installed.</p>
<h3 id="to-check-your-verison-of-python">To Check Your Verison of Python:</h3>
<p>1.) Open Command Prompt Window (Terminal in Mac)</p>
<p>2.) Type the command for you OS from below:</p>
<ul>
<li>Windows:
<blockquote>
<p>python</p>
</blockquote>
</li>
<li>Linux or Mac:
<blockquote>
<p>python -V</p>
</blockquote>
</li>
</ul>
<p><em>If your screen returns Python version 2.7 or above then you are good to go!<br>
If not… Install with the instructions below:</em></p>
<p><strong>Windows:</strong></p>
<h4 id="download-and-install-instructions-for-python-2.7"><em>Download and install Instructions For Python 2.7</em></h4>
<ol>
<li>Go to Python 2.7.10 downloads page --&gt; <a href="https://www.python.org/downloads/release/python-2710/">https://www.python.org/downloads/release/python-2710/</a></li>
<li>Find and download the Windows installer file that matches your system.<br>
<img src="https://lh3.googleusercontent.com/B3_EShhv8L1wzx6NHHPRxaN9YE-mkqwT6UPOTluW15duZxWoyu7S7LvCweunkRPJUIKucdoWKaFf" alt="6522191407708309681"></li>
<li>Open the file to start the installation wizard.</li>
<li>Follow the instructions and make a note of where Python is installed<br>
on your system.</li>
</ol>
<h3 id="add-python-to-path">Add Python to path</h3>
<ol>
<li>In the Windows menu, search for “advanced system settings” and<br>
select <strong>View advanced system settings.</strong></li>
<li>In the window that appears, click <strong>Environment Variables</strong>… near the<br>
bottom right.</li>
<li>In the next window, find and select the user variable named <strong>Path</strong> and<br>
click <strong>Edit</strong>… to change its value. The value for this variable is a<br>
semi-colon-delimited list of file locations.</li>
<li>Scroll to the end of the value, add a semi-colon, and then add the location of <em>python.exe</em>.<br>
<em>(If you do not know where your python.exe is, you can search for it.)</em></li>
<li>Click <strong>OK</strong> to save this change.</li>
<li>If you do not have a user variable named <strong>Path</strong>, click the New… button.</li>
<li>Add a variable named Path and make its value the location of python.exe.</li>
</ol>
<h4 id="finding-python.exe">Finding <em>python.exe</em></h4>
<ol>
<li>If you do not know where Python was installed, search for <em>python.exe</em> in the Windows menu.</li>
<li>Right-click the file name in the results, select <strong>Properties</strong>, and find <strong>Location</strong>.</li>
<li>Copy the location and add it to your path variable.</li>
</ol>
<h4 id="confirm-addition-to-path">Confirm addition to path</h4>
<ol>
<li>Open a new command prompt and re-run the original command:<br>
<code>python</code><br>
to confirm that Python 2.7.10 is installed and added to your path.</li>
</ol>
<p>For Information on How to Add Python to your Path:<br>
<a href="https://docs.python.org/2/faq/windows.html#how-do-i-make-python-scripts-executable">https://docs.python.org/2/faq/windows.html#how-do-i-make-python-scripts-executable</a></p>
<p><strong>Linux or Mac:</strong><br>
If you do not have Python (Which usually all Macs do!)<br>
Go to:<br>
<a href="https://www.python.org/downloads/release/python-2710/">https://www.python.org/downloads/release/python-2710/</a></p>
<hr>
<h5 id="other-install-sources"><em>Other Install Sources:</em></h5>
<p><em>Source I used for Install Instructions can be found here:</em> <a href="https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html">https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html</a></p>
<p><em>Install Guide check out this one from an MIT class:</em><br>
<a href="http://web.mit.edu/6.s189/www/handouts/GettingStarted.html">http://web.mit.edu/6.s189/www/handouts/GettingStarted.html</a></p>
<hr>
<p>For this tutorial we will only be using <strong>1</strong> Python Library : <strong>Numpy!</strong><br>
To install Numpy we can either:</p>
<ol>
<li>
<p>Build from source… Which would suck</p>
<ul>
<li>But I will still provide a reference for those of you brave enough…</li>
<li><a href="https://docs.scipy.org/doc/numpy-1.10.1/user/install.html">https://docs.scipy.org/doc/numpy-1.10.1/user/install.html</a></li>
</ul>
<p><strong>OR</strong></p>
</li>
<li>
<p>Easy Install</p>
<ul>
<li>I will go over how to easy install with the package manager: <strong>pip</strong></li>
</ul>
</li>
</ol>
<h2 id="pip">Pip</h2>
<h3 id="pip-version-check">Pip Version Check</h3>
<ol>
<li>Open Command Line Prompt Window</li>
<li>Check your pip version…
<ul>
<li><strong>Windows Users:</strong>
<ul>
<li>Navigate to the directory (folder) where Python was installed</li>
<li><strong>cd</strong> into the <strong>C:\Python27\Scripts</strong> directory</li>
<li>Enter the command: <code>pip -V</code> OR <code>pip --version</code> OR <code>pip list</code></li>
</ul>
</li>
<li>Linux / Mac Users:
<ul>
<li>Enter the command: <code>pip -V</code></li>
</ul>
</li>
</ul>
</li>
</ol>
<p>If you get a <em>‘…not a recognised command…’</em> error then follow along below:</p>
<h3 id="install-pip">Install Pip</h3>
<ol>
<li>Download the file: <a href="https://bootstrap.pypa.io/get-pip.py">https://bootstrap.pypa.io/get-pip.py</a> to some folder on your computer
<ul>
<li>Alternatively you can follow along with this tutorial: <a href="https://github.com/BurntSushi/nfldb/wiki/Python-&amp;-pip-Windows-installation">https://github.com/BurntSushi/nfldb/wiki/Python-&amp;-pip-Windows-installation</a>
<ul>
<li>Be sure to scroll to the “Pip Install” section to begin…</li>
</ul>
</li>
</ul>
</li>
<li>Open a Command Prompt Window</li>
<li>Go to the folder that contains <code>get-pip.py</code></li>
<li>Type: <code>python get-pip.py</code> to install pip</li>
<li>Open a <em>NEW</em> Command Prompt Window</li>
<li>Type: <code>cd \Python27\Scripts</code><br>
<img src="https://lh3.googleusercontent.com/4BOHwV-TFBJP6uoFiBT_bxeW-hqPx2YJXpwbwprPqHcHcsqHnz4tbxrxFfMW8K0jyWtEIxh7gRy5" alt="enter image description here"></li>
<li><code>pip freeze</code></li>
<li>To test… let’s try using pip to easy install a package…</li>
<li>Open a <strong>NEW</strong> Command Prompt Window<br>
<img src="https://lh3.googleusercontent.com/YeJdRnSSVwPBmqT4eh1IhiaY18PEcwNmLPlMUv-SOQ3blTE3RZthDgwueDOvXlQ4AHHeHrYGDKzm" alt="enter image description here"></li>
<li><code>pip install numpy</code></li>
</ol>
<hr>
<h4 id="so-far-we-have"><em>So far we have:</em></h4>
<ul>
<li>Installed <strong>Python</strong></li>
<li>Installed an awesome package manager - <strong>pip</strong></li>
<li>Installed  the required packaged needed to build our neural net - <strong>Numpy!</strong></li>
</ul>
<hr>
<h2 id="ide">IDE</h2>
<p>Now, we will download a nice Test Editor so we can see the different things going on in our code…</p>
<p>I am suggesting <strong>SublimeText</strong><br>
Download here: <a href="https://www.sublimetext.com/3">https://www.sublimetext.com/3</a></p>
<p>Open Sublime and create a new file<br>
Save the file as: <code>NeuralNet.py</code></p>
<hr>
<h2 id="inspiration">Inspiration:</h2>
<p><strong>Walter Pitts:</strong> (23 April 1923 – 14 May 1969) was a logician who worked in the field of computational neuroscience.</p>
<p><strong>Warren Sturgis McCulloch:</strong>  (November 16, 1898 – September 24, 1969) was an American neurophysiologist and cybernetician, known for his work on the foundation for certain brain theories and his contribution to the cybernetics movement.</p>
<p>In 1943 Pitts and McCulloch published “A Logical Calculus of The Ideas Immanent in Nervous Activity” - a paper that tried to imitate mathematically how a brain produces complex patterns.<br>
Overtime this developed into what we know today as Artificial Neural Networks.</p>
<blockquote>
<p><em>To learn about “A Logical Calculus of The Ideas Immanent in Nervous<br>
Activity”:</em><br>
<a href="http://www.mind.ilstu.edu/curriculum/modOverview.php?modGUI=212">http://www.mind.ilstu.edu/curriculum/modOverview.php?modGUI=212</a></p>
</blockquote>
<blockquote>
<p><em>For more on these guys:</em><br>
<a href="https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch">https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch</a></p>
</blockquote>
<h3 id="defining-loosely-anns">Defining (Loosely) ANNs:</h3>
<p>“An artificial neuron network (ANN) is a computational model based on the structure and functions of biological neural networks”</p>
<blockquote>
<h5 id="biological-view-enter-image-description-here"><em>Biological View:</em> <img src="https://lh3.googleusercontent.com/BrSfA5loUWJybN0x-VsEj4EQrh0gaa89tsemsjiMzX9lnMcWaNzD2P8MINvLk_APxPbf7DhhiZG7" alt="enter image description here"></h5>
<h5 id="technological-view-enter-image-description-here"><em>Technological View:</em> <img src="https://lh3.googleusercontent.com/_siAAfQdqFtNxEgHK5rY3IJZGEICOGutNRlIUkzZZi7jmJP6x45aJohLzr8v9xjSQK_ywm4fJnbF" alt="enter image description here"></h5>
</blockquote>
<p>In Data Science a NN is considered to be:</p>
<ul>
<li>A model for non-linear data</li>
<li>A supervised learning algorithm</li>
</ul>
<p>Neural Nets “learn” about the data you feed it by adjusting <strong>weights</strong> to reduce <strong>error</strong> (we will touch on weights and error later on)</p>
<p><em><strong>With everything - there is a while lot more depth than just what I’m presenting… This is just the tip of the iceberg.</strong></em><br>
This is also just one of many amazing techniques we can leverage to make predictions…<br>
<img src="https://lh3.googleusercontent.com/VJ1dwZ1007qwYnkE7n3s0e-xEufiRGVccoMrPpLfP08S1oxVMKXPRSKce7FPjL7_m5vljzIjtqTu" alt="enter image description here"></p>
<h2 id="a-larger-scale">A Larger Scale</h2>
<p><strong>How Are They Being Used?</strong></p>
<ul>
<li>Self Driving Cars</li>
<li>Beating Humans At Computer Games
<ul>
<li>Go</li>
</ul>
</li>
<li>Chatbots</li>
<li>Advertising</li>
<li>Spam Filters</li>
<li>Recommendation Tools
<ul>
<li>Netflix --&gt; What to watch next?</li>
<li>Amazon --&gt; What other people have bought</li>
</ul>
</li>
<li>To Make Art
<ul>
<li>Like Van Gogh</li>
<li>Making Van Gogh’s:<br>
<img src="https://lh3.googleusercontent.com/x-7JpwHrQho3Pa9k0xOJAXZoJcvVY6CeDShIl9XJEDzDKj51KFiuP-iDLv86W_jhCi72fvovkewH" alt="enter image description here"></li>
</ul>
</li>
<li>Generate Music
<ul>
<li>Google’s Infinite Drum Machine:<br>
<a href="https://experiments.withgoogle.com/ai/drum-machine">https://experiments.withgoogle.com/ai/drum-machine</a></li>
<li>Music Made by DeepMind:<br>
<a href="https://deepmind.com/blog/wavenet-generative-model-raw-audio/">https://deepmind.com/blog/wavenet-generative-model-raw-audio/</a></li>
</ul>
</li>
<li>To Translate Languages</li>
<li>Predict Loan Defaults</li>
<li>Predict House Prices</li>
<li>Sort Mail</li>
<li>Read Texts</li>
<li>Hot Dog or Not Hot Dog?
<ul>
<li>The Infamous Hot Dog/Not Hot Dog App:<br>
<img src="https://lh3.googleusercontent.com/BhVEi4J6xr-CVoDe_gl28uU0v2pnMuqH_nWUXmTtoHLVKc9GaXXOvSDndYiNvBA9-pUMhutSC_rk" alt="enter image description here"></li>
</ul>
</li>
<li>Deep Genomics:
<ul>
<li>To predict gene variation</li>
</ul>
</li>
<li>To Generate Human Faces:		<br>
<img src="https://lh3.googleusercontent.com/0cdXhMdyVBG5F65Zr8NgWNW7AuT5Jv2dCzN3oD7PVHGqCTCkHxJ_Bbk21isMbj7b1Rw0bYJxfWYQ" alt="enter image description here"></li>
</ul>
<p><em>Check some examples out here:</em></p>
<blockquote>
<p><a href="http://www.yaronhadad.com/deep-learning-most-amazing-applications/">http://www.yaronhadad.com/deep-learning-most-amazing-applications/</a><br>
<a href="https://medium.com/merantix/applying-deep-learning-to-real-world-problems-ba2d86ac5837">https://medium.com/merantix/applying-deep-learning-to-real-world-problems-ba2d86ac5837</a></p>
</blockquote>
<h2 id="the-code">The Code:</h2>
<p>We will make a 2 Layer Neural Net. Envision it to look something like:</p>
<p><img src="https://lh3.googleusercontent.com/dBGUgRQw5bgsWZPTJonjuHJIVm2RmE12aBF4uYVMjrK5qmRC2FAzZoRKf-lFR1g4gWB3-qeSl67U" alt="enter image description here"></p>
<hr>
<h3 id="dependencies">Dependencies</h3>
<p>First we need to import Numpy so we can do some math…</p>
<pre><code>import numpy as np
</code></pre>
<hr>
<h3 id="activation-function">Activation Function</h3>
<pre><code># sigmoid function
def activate(x,deriv = False):
   if(deriv == True):
       return x*(1-x)
   return 1/(1+np.exp(-x)) 
</code></pre>
<p>Every neural net must have a function that provides some kind of <strong>nonlinearity</strong>.</p>
<p><em>Why?</em></p>
<p>Because neural nets are algorithms used to find patterns amongst non linear data - unlike linear regression which can find the best equation (best fit line) to some linear relationship.</p>
<p>There are a lot of different types of activation functions. Here, we are using the <strong>Sigmoid function</strong>. Sigmoid - like logistic regression <em>“squashes”</em> an input value into a probability, so the resulting value is something between 0 and 1.</p>
<h4 id="sigmoid-functionsigmoid-function-"><em>Sigmoid Function</em><img src="https://lh3.googleusercontent.com/NDoowAG-giVECrt7ZJE8J17bWiDO43GFAJ66kV892q4NoTydADh3mxwMAg8wOFcV4uRKRR70a_ek" alt="Sigmoid Function "></h4>
<hr>
<h3 id="input-dataset--x-">Input Dataset ( X )</h3>
<ul>
<li>
<p>Our variables, or features that predict the output</p>
<pre><code>_input = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
</code></pre>
</li>
<li>
<p>It’s a Matrix:</p>
</li>
</ul>

<table>
<thead>
<tr>
<th>C1</th>
<th>C2</th>
<th>C3</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table><hr>
<h3 id="output-vector--y-">Output Vector ( Y )</h3>
<pre><code>output = np.array([[0,0,1,1]]).T 
# Where .T means to Transpose
</code></pre>

<table>
<thead>
<tr>
<th>C1</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
</tr>
<tr>
<td>0</td>
</tr>
<tr>
<td>1</td>
</tr>
<tr>
<td>1</td>
</tr>
</tbody>
</table><hr>
<h3 id="set-seed">Set Seed</h3>
<pre><code>np.random.seed(5)
</code></pre>
<hr>
<h3 id="initialize-weights">Initialize Weights</h3>
<pre><code>synapse = 2*np.random.random((3,1)) - 1
</code></pre>
<p><strong>synapse</strong> --&gt; <em>random matrix of weights.</em></p>
<ul>
<li>Our matrix is size (3, 1) to connect our 3 inputs to our 1 output node</li>
<li>The synapse is essentially the ‘controller’ of our weights.</li>
<li>The weight represents the strength of a connection between 2 nodes
<ul>
<li><em>Strength</em> meaning positive, negative or neutral</li>
<li><em>Connection</em> meaning relationship</li>
</ul>
</li>
</ul>
<hr>
<h3 id="the-net">The Net:</h3>
<pre><code># Looping and Layering
for j in range(70000):

    # Layers 
    
    # Forward Propogate:
    layer1 = _input
    layer2 = activate(np.dot(layer1,synapse))

    # Layer 1 Error
    error = output - layer2

    # Now we multiply our error by the 
    # derivative of our activation function
    delta = error * activate(layer2, True)

    # Update weights
    synapse = np.dot(layer2.T, delta)
    

print "Output After Training"
print layer2
</code></pre>
<hr>
<h4 id="lets-discuss-what-just-happened">Let’s discuss what just happened:</h4>
<p><strong>layer1</strong> --&gt;<em>The first layer in our neural net</em></p>
<ul>
<li>This is just a matrix of our input</li>
</ul>
<p><strong>layer2</strong> --&gt; <em>The second layer in our neural net</em></p>
<ul>
<li><strong>np.dot</strong> means we are going to apply some matrix math on some numpy arrays.
<ul>
<li>Remember our input data and synapse are matrices</li>
</ul>
</li>
<li>It says:
<ul>
<li><em>“Multiply layer1 by synapse (our weights), then apply the activation function”</em></li>
</ul>
</li>
</ul>
<p><strong>error</strong> --&gt; <em>We are computing how right we were by subtracting (actual - predictions)</em></p>
<p><strong>delta</strong> --&gt; <em>Our delta calculates the derivative of the sigmoid function on layer 2 then it multiplies the resulting value by our error.</em><br>
Delta is really just reducing our error</p>
<ul>
<li>It’s telling us:
<ul>
<li><em>“For the predictions we feel confident in calling a 0 or a 1, there is a small error rate - so we won’t change those weights. However there are some predictions with about 50% probability - they could be a 0 or a 1. So we will update those weights by a larger number.”</em></li>
</ul>
</li>
</ul>
<p><strong>synapse = np.dot(layer2.T, delta)</strong><br>
The last line in our loop multiplies (Layer 2 * Delta).</p>
<ul>
<li>Keep in mind Delta has some stored values that determine how much or how little our neural net should update the Synapse values.</li>
<li>By performing the operation (Layer 2 * Delta) and setting that equal to Synapse, we handing off Delta’s weight changes to Synapse - the controller of our weights.</li>
</ul>
<hr>
<h2 id="deeper-nets">Deeper Nets</h2>
<h4 id="this-was-a-2-layer-neural-network.">This was a 2 layer Neural Network.</h4>
<p>We just skimmed the basics of neural nets. There’s a whole lot more to dive into! Deep Learning is really just using a multi-layered neural net to solve a problem.</p>
<h4 id="what-does-it-mean-to-be-deep">What does it mean to be deep?</h4>
<p>When we add a <em>Hidden Layer</em> between the <em>Input</em> and <em>Output</em> layer we are creating a “Deep Neural Net”.</p>
<hr>
<h4 id="layers"><em>3 Layers:</em></h4>
<p><img src="https://lh3.googleusercontent.com/A4Zoeo9IyVGp_nXPiQtbjsiZHJScmXvR9M-g0tPpjBHqH6WeFdzyE2Jvi5tpDi5K-BA9v6U0mjZG" alt="enter image description here"></p>
<h4 id="layers-1"><em>3 Layers:</em></h4>
<p><img src="https://lh3.googleusercontent.com/NoepNOJwTZPbx522AbrCS-hysAHmBuTPt9HWLgzkw8S0VtrvN2VjehANU7yrNHSOU6tIIu2UFPok" alt="enter image description here"></p>
<h4 id="layers-2"><em>5 Layers:</em></h4>
<p><img src="https://lh3.googleusercontent.com/bbDT4qRIRY2uuZO6OSiM1wtf4B6M6119XP29yn_rQpbWFvUC6eWLZc9mpJbKrLwwOOQJhxvREPMq" alt="enter image description here"></p>
<h4 id="layers-3"><em>6 Layers:</em></h4>
<p><img src="https://lh3.googleusercontent.com/ZJGYriz_n_cRe9I4f-YAX7yj98JT93xJebpWlnaJVbtFy3PHQxtsj34SQ10x5yOdIqEOLWsZ2xI1" alt="enter image description here"></p>
<h2 id="awesome-onlinefree-learning"><em>Awesome Online/Free Learning:</em></h2>
<blockquote>
<h2 id="courses">Courses</h2>
<p><strong>Full Coursera Course List:</strong><br>
<a href="https://www.coursera.org/courses?languages=en&amp;query=deep+learning">https://www.coursera.org/courses?languages=en&amp;query=deep+learning</a></p>
<h2 id="free-text-books">Free Text Books</h2>
<p><strong>The BEST/Most Highly Referenced Deep Learning Book</strong>       (Used by MIT Students):<br>
<a href="http://www.deeplearningbook.org">http://www.deeplearningbook.org</a></p>
<p>__ Artificial Intelligence Text Book:__<br>
<a href="http://artint.info/html/ArtInt.html#cicontents">http://artint.info/html/ArtInt.html#cicontents</a></p>
<p><strong>Neural Nets and Deep Learning:</strong><br>
<a href="http://neuralnetworksanddeeplearning.com/chap1.html">http://neuralnetworksanddeeplearning.com/chap1.html</a></p>
<h2 id="tutorials-and-blogs">Tutorials and Blogs</h2>
<p><strong>The Ultimate Beginner’s Guide to Deep Learning in Python:</strong><br>
<a href="https://elitedatascience.com/keras-tutorial-deep-learning-in-python">https://elitedatascience.com/keras-tutorial-deep-learning-in-python</a></p>
<p><strong>7 Steps to DP by KDNuggets:</strong><br>
<a href="https://www.kdnuggets.com/2016/01/seven-steps-deep-learning.html">https://www.kdnuggets.com/2016/01/seven-steps-deep-learning.html</a></p>
<p><strong>A Complete Guide on Getting Started with Deep Learning in Python:</strong><br>
<a href="https://www.analyticsvidhya.com/blog/2016/08/deep-learning-path/">https://www.analyticsvidhya.com/blog/2016/08/deep-learning-path/</a></p>
<p><strong>One of My FAVORITE Blogs:</strong><br>
<a href="https://pythonprogramming.net/neural-networks-machine-learning-tutorial/">https://pythonprogramming.net/neural-networks-machine-learning-tutorial/</a></p>
<p><strong>A Tutorial That Builds on This One:</strong><br>
<a href="https://iamtrask.github.io/2015/07/12/basic-python-network/">https://iamtrask.github.io/2015/07/12/basic-python-network/</a></p>
<p><strong>Math for Neural Nets:</strong><br>
<a href="https://juxt.pro/blog/posts/neural-maths.html">https://juxt.pro/blog/posts/neural-maths.html</a></p>
<p><strong>Building a Neural Net:</strong><br>
<a href="https://juxt.pro/blog/posts/neural-maths.html">https://juxt.pro/blog/posts/neural-maths.html</a></p>
</blockquote>
<hr>
<p><em>Cool People in Data Science:</em></p>
<blockquote>
<p><a href="https://www.analyticsvidhya.com/blog/2015/09/ultimate-data-scientists-world-today/">https://www.analyticsvidhya.com/blog/2015/09/ultimate-data-scientists-world-today/</a></p>
</blockquote>

