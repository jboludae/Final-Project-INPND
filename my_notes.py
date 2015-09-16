notes_list = [['Stage 0', 'The World Wide Web',
'''
<p>The WWW is a collection of HTML documents. HTML can contain anything:
images, videos, music, hyperlinks, etc. HTML glues everything together.</p>
<p>The WWW was created in the early 90s and now contains more than 30 billion
pages.</p>
<p>This nice <a href="http://www.udacity.com/course/viewer#!/c-nd000/l-3873828673/e-48230539/m-48742046">video</a> explains this very well.</p>
'''],
['Stage 0', 'Major Concepts of the web',
'''
<p>When you visit a website, your computer browser sends an HTTP request to a
server. A server is a computer that is optimized to host files while it sits
in a closet. The server finds the HTML document and returns it to your
computer. Your computer browser is able to interpret the HTML code and
translate it to what you see on your computer.</p>
'''],
['Stage 0', 'HTML',
'''
<p>HTML stands for Hypertext Markup Language. The <b>text</b> is the content
you see, while the <b>markup</b> defines how the text will look like. HTML
can contain reference to other documents as well as links to other pages</p>
'''],
['Stage 0', 'HTML markup',
'''
<p>HTML markup defines how the text will look like. It contains:</p>
	<ul>
		<li>An opening tag</li>
		<li>The content</li>
		<li>A closing tab</li>
	</ul>
	<p>Some useful tags include the <b>bold</b> (b) tag and the <em>emphasis tag</em> (em)</p>
'''],
['Stage 0', 'HTML attributes',
'''
<p>Tags can have multiple attributes. Attributes have names and values. An example is the "anchor" tag. The anchor tag is useful to introducevlinks to other pages. <a href="http://www.reddit.com">This</a> hyperlink directs you to www.reddit.com.
</p>
<p>If you want to embed images in your website, you can use the image tag:<br>
<img src="http://lh4.googleusercontent.com/-dnJmXnBZ67A/AAAAAAAAAAI/AAAAAAAACFs/YoghUeotS5A/photo.jpg" alt="Image not available"></p>
<p>You have to take into account that the image tag is a <b>void</b> tag. That
means that it has no content.
</p>
<p>Then we have to distinguish between inline tags and block tags. For example, there
are two ways we can break a line in HTML. One is using the <b>br</b> tag, which is
an <em>inline tag</em>. This tag breaks the line and that's it.
</p>
<p>The other way is by using a <b>p</b> tag. This tag make an <em>invisible box</em>
that surrounds the content.
</p>
<p>We can also use <b>unordered lists</b> and <b>ordered lists</b></p>
<p>This is an unordered list:</p>
	<ul>
		<li>Croissant</li>
		<li>Coffee</li>
	</ul>
<p>This is an ordered list:</p>
	<ol>
		<li>Croissant</li>
		<li>Coffee</li>
		<li>Cake</li>
	</ol>
'''],
['Stage 0', 'Some useful resources to learn to code',
'''
<p><b><a href="http://codepen.io">Codepen</a></b></p>
<p><b><a href="www.scratchpad.io">ScratchPad</a></b></p>
<p><b><a href="http://jsfiddle.net">JSFiddle</a></b></p>
'''],
['Stage 1', 'Html and CSS as languages',
'''
<ul>
	<li>Html and CSS are languages with a specific grammar and syntax</li>
	<li>Basic words in HTML are the "tags"</li>
	<li>Html elements can be either <em>inline</em> or <em>block</em>:
		<ol>
			<li>A block element has an invisible box around it</li>
			<li><b>Span</b> and <b>Div</b> are inline and block elements respectively
		</ol>
	</li>
</ul>
'''],
['Stage 1', 'HTML controls the structure of a website',
'''
<ul>
	<li>Basic words in HTML are the "tags"</li>
	<li>The browser converts the tags to a tree-like-structure thanks to the <b>DOM</b>
	(Document Object Model)</li>
</ul>
'''],
['Stage 1', 'CSS controls the style of a document',
'''
<ul>
	<li>The HTML provides the info about what style to use via the <em>class</em>
	attribute</li>
	<li>CSS sets the size of the text, fonts, colors, etc.</li>
</ul>
'''],
['Stage 1', "Don't repeat yourself!",'''
<p>When coding, it is extremely important to avoid repetition for at least three reasons:</p>
<ol>
	<li><strong>Efficiency:</strong> obviously, the less you have to repeat your code by copying and pasting, or worse, by typing, the more efficient you are.</li>
	<li><strong>Avoiding mistakes:</strong> the same idea mentioned in point 1 applies here. The less you type, the less mistakes you make. Additionally, if you make a mistake and you have lots of duplicated code, it will take you a long time to fix that.</li>
	<li><strong>Avoiding inconsistencies:</strong> when you have assigned the design of each of the elements of the website manually, you will be more prone to inconsistencies. If you, however, use classes in CSS to automatically style the similar elements in your website at once, the result will be much more consistent.</li>
</ol>
<p>CSS means Cascading Style Sheets and it is a powerful language to give styles to documents avoiding repetition.</p>
<p><b>Cascading</b> is the key word here. This means that CSS rules follow a hierarchy: from more general to more specific.</p>
<p><b>Inheritance</b> is another highly important concept. It is a powerfull CSS feature by which properties are applied not only to specific elements, but also to its descendants</p>
'''],
['Stage 1', 'Styling up your HTML',
'''
<p>In CSS you select elements by using <b>selectors</b>. There are many types of selectors, from more generic to more specific. The following types are some examples:</p>
<ul>
	<li><b>*</b>, the star symbol will target every element on the page</li>
	<li><b>Type</b> selectors correspond to an HTML type, such as a <em>heading (h1)</em>, a <em>body</em>, a <em>bold</em> highlight, etc.</li>
	<li><b>ID</b> selectors are assigned to elements that are <em>unique</em> in the page</li>
	<li><b>CLASS</b> selectors are very similar to ID selectors. The difference is that while <b>ID</b> elements are unique, we can assign the same <b>CLASS</b> to as many elements as we want</li>
</ul>
<p>For each of the selectors you can have many <b>declarations</b>, which match <b>properties</b> with <b>values</b>. Some interesting properties are:</p>
<ul>
	<li>text-align: center, left or right</li>
	<li>color: in RGB, hexadecimal, etc.</li>
	<li>font-family: this is the font</li>
	<li>background-color: in RGB, hexadecimal, etc.</li>
	<li>border-radius: this is the box corner radius</li>
	<li>font-style: italic, oblique, normal</li>
	<li>font-weight: bold, light, etc. You can also assign a numeric weig
'''],
['Stage 1', 'The Box Model',
'''
<p>Understanding the boxes is crucial for HTML programming. Each box has 4 distinct zones:</p>
<ul>
	<li>The content</li>
	<li>The padding</li>
	<li>The border</li>
	<li>The margin</li>
</ul>
<p>Furthermore, you can specify the size of the box in several ways. First, you can set a fixed size in pixels, which do not lead to a good user experience. Second, you can set it in %, so it will change depending on the size of the browser window. And last, you can set a maximumum width, so the box will not exceed certain dimensions.</p>
<p>Finally, you can use the "border-box" property to simplify sizing of boxes. The syntax is the following: <b> box-sizing: content-box|border-box|initial|inherit;</b>. Each of the values for box-sizing means the following:</p>
<ul>
	<li>content-box: the specified size of the box will match the content</li>
	<li>border-box: the specified size of the box will match content plus padding plus border</li>
	<li>initial: set this property to its default value</li>
	<li>inherit: will inherit this property from its parent</li>
</ul>
<p>By default, each element will be displayed on top of each other following a "papyrus" structure</p>
<p>If you want elements displayed next to each other, you have to use <b>display:flex</b>.
'''],
['Stage 1', 'Code, test, refine',
'''
<p>The process to write a webpage is very systematic:</p>
<ol>
	<li>You look at natural boxes in the design</li>
	<li>You look for repeated styles</li>
	<li>You write the html code</li>
	<li>You apply styles</li>
	<li>You fix and fine-tune things</li>
</ol>
'''],
['Stage 2', 'Computers',
'''
<p>With a toaster, you can perform a very specific task with: toasting bread. You may even be able to introduce little variations like <em>toasting time</em>, but if you want to perform a very different task, you need to introduce major changes in the hardware.</p>
<p>Computers, however, can use <b>computer programs</b> to perform many different tasks without modifying the hardware.</p>
'''],
['Stage 2', 'Programs',
'''
<p>Computer programs are nothing else than a very precise sequence of steps. In this Nanodegree, when we run a program we have written in Python, a Python interpreter <em>translates</em> the instructions to a language the computer hardware can understand, and the computer executes them step by step.</p>
'''],
['Stage 2', 'Programming Languages',
'''
<p>Why do we even need programming languages to build programs when we can use english, spanish or any natural language? There are many reasons, but here we have two important ones:</p>
<ul>
	<li><b>Ambiguity</b>: natural languages are ambiguous. The same thing can be interpreted in many different ways. Programming languages give unambiguous instructions.</li>
	<li><b>Verbosity</b>: natural languages are verbose. To write precise instructions you would need to write quite a lot. Programming languages allow us to be <b>concise</b></li>
</ul>
'''],
['Stage 2', 'Grammar',
'''
<p>Programming languages follow very precise <b>grammatical rules</b>. In natural languages there is also an underlying grammar, however, in many occasions, you can make yourself understood using grammatically incorrect expressions.</p>
<p>You can express grammar rules very concisely using the <b>Backus-Naur</b> notation:</p>
<div class="code">
	<p>Sentence -> Subject Verb Object</p>
	<p>Subject -> Noun</p>
	<p>Object -> Noun</p>
	<p>Noun -> I</p>
	<p>Verb -> eat</p>
	<p>Noun -> cookies</p>
</div>
'''],
['Stage 2', 'Python expressions',
'''
<p>Python expressions can be very interesting cause they can be defined <b>recursively</b>:</p>
<div class="code">
	<p>Expression -> Expression Operator Expression</p>
	<p>Expression -> Number</p>
	<p>Expression -> (Expression)</p>
	<p>Number -> 1,2,3...</p>
	<p>Operator -> +, *, -...</p>
</div>
<p><b>Recursive</b> means that you have <em>Expression</em> in both sides of the definition. That allows us, with the very concise and limited set of rules we set above, to construct really long and complex numeric expressions.</p>
'''],
['Stage 2', 'Variables',
'''
<p>Variables are used in Python to store values. That way you can use them in your algorithms in order to keep track of them. When thinking about variables, we have to keep several things in mind.</p>
<p><b>Values are assigned to variables with the "=" sign</b>: the equal sign has a different meaning than in algebra. It doesn't mean "equal" but "assignment".
<p><b>Variables can vary</b>: you can modify the value of the variable with another assignment statement.</p>
'''],
['Stage 2', 'Strings',
'''
<p>A string, in Python, is a sequence of characters. A string can be defined using either " " or ' '. The requirement is that whatever quote sign you use to open the string, you must use to close it.</p>
<p>You can assign strings to variables just like you assign numbers.</p>
<p>Some interesting operations with strings</p>
<ul>
	<li>Concatenation: using the "+" sign.</li>
	<li>Indexing: <span class="code">&lt;string&gt;[number]</span> will return the element sitting on the "numberth" position of the string</li>
	<li>Subsequencing: you can extract a fragment of a string using the <span class="code">&lt;string&gt;[number1:number2]</span> structure</li>
</ul>
'''],
['Stage 2', 'Finding strings within strings',
'''
<p>Using <span class="code">&lt;SearchString&gt;.find(&lt;TargetString&gt;,number)</span>, we can return the position in which the first <b>Search String</b> appears after the position indicated by <b>number</b>.</p>
<p>This function can be used jointly with variables and control structures to perform interesting tasks such as:</p>
<ul>
	<li>Finding words</li>
	<li>Getting rid of characters</li>
	<li>Subsituting a word for another.</li>
	<li>Extract a list of words from a text</li>
</ul>
'''],
['Stage 2', 'Functions',
'''
<p>A function takes one or several inputs, process a sequence of steps to them and returns one or several outputs.</p>
<p>To define a function in Python you use the following syntax:</p>
<p><span class="code">def &lt;funtion name&gt; &lt;input1, input2,...&gt;</span></p>
<p><span class="code">&lt;block&gt;</span></p>
<p>To use a function you just call the function with the inputs you want and you will automatically get the outputs.</p>
<p>Functions help avoiding repetition because they can perform virtually any task you can imagine without having to write every single step every time.</p>
<p>For function to be useful they need to contain a <b>return</b> statement. Without that the function does not return anything, so it does nothing</p>
'''],
['Stage 2', 'Making comparisons',
'''
<p>You can compare numbers using a <span class="code">&lt;number1&gt;&lt;operand&gt;&lt;number2&gt;</span> structure</p>
<p>Operands can be:</p>
<ul>
	<li>Greater than: <span class="code">&gt;</span> </li>
	<li>Less than: <span class="code">&lt;</span> </li>
	<li>Equal to: <span class="code">==</span> </li>
	<li>Different than: <span class="code">!=</span> </li>
</ul>
<p>The output of a comparison can be either <b>True</b> or <b>False</b>, that is, a boolean value.</p>
'''],
['Stage 2', 'If statements',
'''
<p>If statements are a basic block to code in Python. It allows to take decisions on whether to perform a set of instructions or not depending on the conditions you define. If statements follow the following structure:</p>
<p><span class="code">if &lt;Test Expression&gt;:</span><br><span class="code">&lt;Block&gt;</span></p>
'''],
['Stage 2', 'While and For statements',
'''
<p>While and for statement allow to do repetitive tasks using very little code. This is the structure they follow:</p>
<p><span class="code">while &lt;TestExpression&gt;:</span><br><span class="code">&lt;Block&gt;</span></p>
<p><span class="code">for &lt;name&gt; in &lt;list&gt;:</span><br><span class="code">&lt;Block&gt;</span></p>
<p>For statements are used to loop through list elements. While statements can be used to loop in a very diverse way.</p>
'''],
['Stage 2', 'Debugging',
'''
<p>Just a collection of tips to find mistakes in your code.</p>
'''],
['Stage 2', 'Introduction to Lists',
'''
<p>While a string is a sequence of characters, a list can include any element we want: characters, numbers, strings, or even lists.</p>
<p>Lists follow the format <span class="code">&lt;list&gt; &#8594; [&lt;Expression&gt;,&lt;Expresssion&gt;,...]</span></p>
<p>Subsequencing is very similar to subsequencing in strings. For example:<br><span class="code">p=['y','a','b','b,'a']</span><br><span class="code">p[0]&#8594;'y'</span><br><span class="code">p[2:4]&#8594;['b','b']</span></p>
'''],
['Stage 2', 'Mutation and Aliasing',
'''
<p>Lists support <b>mutation</b>, string dont't. That means that we can change the values of any elements in a list, after we created them. For example:<br><span class="code">p=['H','e','l','l','o']</span><br><span class="code">p[0]='!'</span> this changes the value of the last character of the list to '!'.</p>
<p><b>Aliasing</b> is an interesting concept in Python. <em>James Bond</em> and <em>007</em>, both refer to the same person. Whatever happens to <em>James Bond</em> happens to <em>007</em> and the opposite. Unless, of course, we reassign the alias <em>007</em> to a different agent.</p>
<p>This happens also to variables in Python:</p>
<p><span class="code">p=['j','a','m','e','s']</span><br><span class="code">p=q</span><br></p>
<p>If we mutate <b>p</b> we mutate <b>q</b> and the opposite. However, if we assign <b>q</b> to a different value, <b>p</b> stays unchanged.</p>
'''],
['Stage 2', 'Some interesting operations with lists',
'''
<p><span class="code">&lt;list&gt;.append(&lt;element&gt;)</span> will add &lt;element&gt; at the end of the list and will <b>mutate</b> the list.</p>
<p><span class="code">&lt;list&gt;+&lt;list&gt;</span> works very similar to concatenation in strings. However, it will not mutate the list.</p>
<p><span class="code">length(&lt;list&gt;)</span> will return the length of the list. Note that this command will work with anything: lists, strings, etc.</p>
<p><span class="code">&lt;list&gt;.index(&lt;value&gt;)</span> returns the index of the list in which &lt;value&gt; is found. If the element does not exist in the list, it will return an error.</p>
<p><span class="code">&lt;value&gt; in &lt;list&gt;</span> if &lt;value&gt; is in list it will return TRUE, otherwise, it will return FALSE.</p>
'''],
['Stage 2', 'Loops in lists',
'''
<p><span class="code">for &lt;name&gt; in &lt;list&gt;:</span><br><span class="code">&lt;Block&gt;</span></p>
<p>This structure loops through all elements contained in &lt;list&gt; and executes &lt;Block&gt; in every loop.</p>
'''],
['Stage 2', 'Solving problems',
'''
<p>For solving problems, it is important to follow a "step by step" strategy:</p>
<p>
<ol start="0">
	<li>Don't panic</li>
	<li>Understand what are the inputs</li>
	<li>Understand what are the output</li>
	<li>Work out some examples to understand the relationship between input and output better</li>
	<li>Develop a simple, mechanical solution</li>
	<li>Do not optimize prematurely</li>
	<li>Develop solution incrementally and test as you go</li>
	<li>Programm defensively! Introduce <span class="code">assert &lt;test&gt;</span> statements where required.
</ol>
'''],
['Stage 3', 'Abstraction',
'''
<p>In python there are many predefined libraries and functions and you can save a lot of time by using them instead of having to write every function from scratch.</p>
<p>The really nice thing about them is that, in order to use those functions, you only need to know what are the inputs they need and what are the outputs they produce. <b>You do not need to know what happens behind the scenes!</b> That allows you to focus on what we want the program to do and is called <b>abstraction</b>.</p>
'''],
['Stage 3', 'Limitations of functions',
'''
<p>If you want to creat a movie website using functions you can use two approaches:</p>
<ul>
	<li>Build a function and call it with the info you want to show as arguments.</li>
	<li>Build <em>function templates</em>for each movie. Each template includes both a function and the information you want to show, that way you can call the functions with no arguments</li>
</ul>
<p>The first option is obviously not functional and second is not smart. The reason is that every time you want to change the template, you have to change all of them.</p>
<p>We need a way to make a template with no need to have multiple files. <b>Classes</b> allow us to do that. This <a href="https://www.udacity.com/course/viewer#!/c-nd000/l-4182338913/m-1015728621">video</a> explains all this very well.</p>
'''],
['Stage 3', 'Some useful functions and libraries',
'''
<p> Some useful libraries are the following:</p>
<ul>
	<li><a href='https://docs.python.org/2/library/os.html'>OS library</a> provides access to many operating system related functions</li>
	<li><a href='https://docs.python.org/2/library/time.html'>TIME library</a> contains some time related functions</li>
	<li><a href='https://docs.python.org/2/library/webbrowser.html'>WEBBROWSER library</a> allows to display websites</li>
</ul>
'''],
['Stage 4', 'Networks',
'''
<p>A <b>network</b> is a group of entities that can communicate even though they are not directly connected. It requires at least three entities that are not directly connected.</p>
<p>To make a network, we need:</p>
<ul>
	<li>A way to encode and interpret messages. In internet this works through <em>"bit and electrons"</em>.</li>
	<li>A way to route messages. In Internet, routers are in charge of doingvthis.</li>
	<li>We need rules for deciding who gets to use the resources: in case there are two messages at the same time -> priority should be decided. In internet there are no real rules for this, each router decides. You get what is called "Best effort service". There is no guarantee that your message will arrive where you want.</li>
</ul>
<p>A nice <a href="https://www.udacity.com/course/viewer#!/c-nd000/l-4212668559/e-48011978/m-48692661Video networks:">video</a> about networks.</p>
'''],
['Stage 4', 'Latency',
'''
<p> Latency is the time it takes for message to get from source to destination -> the time from you start writing a message to when you start to receive it</p>
<p>Here is a nice <a href='https://www.udacity.com/course/viewer#!/c-nd000/l-4212668559/e-48737168/m-48729193'>video</a> about latency.</p>
'''],
['Stage 4', 'Bandwidth',
'''
<p>Bandwidth is amount of information that can be transmitted per unit time. It can be measured in bits per second. Mbps: megabits per second.</p>
<p>Here you have a <a href='https://www.udacity.com/course/viewer#!/c-nd000/l-4212668559/m-48739102'>video</a> that explains the concept</p>

'''],
['Stage 4', 'Bit',
'''
<p>A bit is an answer to a yes/no question. It is codified using 0's and 1's</p>
'''],
['Stage 4', 'Protocol',
'''
<p>The protocol is the set of rules that dictate how two entities can communicate with each other. The protocol used in internet is called HTTP (hypertext transfer protocol).</p>
<p>There are two main messages in this protocol: <b>GET</b> and <b>POST</b>.</p>
<p>The sintax is: <span class="code">&ltGET&gt &ltobject&gt</span>. When the server receives a <b>GET</b> message, it will run some code to find the object and send a response</p>
<p>Client: web Browser<br>Server: udacity.com</p>
<p>This nice <a href = 'https://www.udacity.com/course/viewer#!/c-nd000/l-4212668559/m-48676978'>video</a> includes an explanation about internet protocols.</p>
'''],
['Stage 4', 'HTML documents',
'''
<p>HTML documents have the following structure:</p>
<p><b>&lt!DOCTYPE HTML&gt</b> - html5<br>
<b>&lthtml&gt</b> - this surround entire document<br>
	<b>&lthead&gt</b> - metadata, javascript, css - that would be included in the head<br>
		<b>&lttitle&gt &lt/title&gt</b> - this is the title of the page, appears on top of browser window<br>
	<b>&lt/head&gt</b><br>
	<b>&ltbody&gt</b> - this is the content of the page<br>
	<b>&lt/body&gt</b><br>
<b>&lt/html&gt</b>
'''],
['Stage 4', 'URL',
'''
<p><b>URL</b> means <em>Uniform Resource Locator</em></p>
<p> Take as an example the following URL: <em>http://www.example.com/foo/logo.png?p=1&q=2#fragment</em></p>
<ul>
	<li><b>http</b>: this indicates the http protocol</li>
	<li><b>www.example.com</b>: this indicates the name of the server we want to address. It translates to an IP direction that indicates where the server is located physically</li>
	<li><b>/foo/logo.png?p=1&q=2</b>: this indicates the <b>relative</b> path to the host (in this case www.example.com). If we want to indicate the full path, we would have to use http://www.example.com/foo/logo.png?p=1&q=2. Not that the fragment is not included in the path.</li>
	<li><b>?p=1&q=2</b> are the query parameters. The syntax is <span class='code'>name = value</span>. The <b>&</b> symbol is used to introduce several queries.</li>
	<li><b>#fragment</b> is the fragment. It comes to the end of the URL and is separated from the rest by a <b>#</b> sign. It is used to point at specific sections of your website and it exist purely on your browser. It does not a
'''],
['Stage 4', 'The HTTP',
'''
<p>The syntax of an HTTP message is as follows: GET /foo HTTP/1.1</p>
<ul>
	<li><b>GET</b> is the method and it is used to retrieve data from a server. The other method is <b>POST</b> and it is used to send data to a server.</li>
	<li><b>/foo</b> is the path. Fragments are not included in the path, but query parameters are</li>
	<li><b>HTTP/1.1</b> that is the version HTTP/1.1, which is the language of most servers.</li>
</ul>
<p>Besides this, you can have <b>HEADERS</b>, which define the operating parameters of an http transaction. For example:</p>
<p>GET /foo?p=1 HTTP/1.1<br>
<b>Name: value</b> is the syntax of headers.<br>
Host: www.example.com - the host part of the URL, required in http 1.1, not in 1.0. Web servers may have multiple websites hosted, they need to know which one you are requesting.<br>
User-Agent: chrome - this is your browser, the server has to know what kind of machine is making the request.</p>
<p>This <a href='https://www.udacity.com/course/viewer#!/c-nd000/l-4169998949/m-48439389'>video</a> contains an explanation about headers.</p>
'''],
['Stage 4', 'Server responses',
'''
<p>The purpose of servers: respond to HTTP requests. Two classification of responses:<p>
<ul>
	<li>Static: pre-written files like images</li>
	<li>Dynamic: requests where response is built on the fly by web applications. Today, most of the content is dynamic.</li>
</ul>
<p>A server response has the following structure: HTTP/1.1 200 OK</p>
<p>The number is the status code:<br>
<ul>
	<li>200 - OK</li>
	<li>302 - Found - but somewhere else</li>
	<li>404 - Not found - there is an error on the browser side</li>
	<li>500 - Server error: server broke trying to find request</li>
</ul>
<p>This <a href='https://www.udacity.com/course/viewer#!/c-nd000/l-4169998949/m-48724355'>video</a> contains an explanation about headers.</p>
<p>Some headers are required in the response, but the WWW has evolves over time so this is variable</p>
<ul>
	<li><b>Date: Tue Mar 2012 04:44:44 GMT</b></li>
	<li><b>Server: Apache /2.2.3.</b> - do not include this, free info for hackers.</li>
	<li><b>Content-Type: text/html;</b> - content type that needs to be displayed by browser.</li>
	<li><b>Content-Lenght:  1539 </b>- not strictly required, not very useful.</li>
</ul>
'''],
['Stage 4', 'Forms',
'''
<p>There is a way to send data from browser to server... In html there is an attribute called <b>&ltform&gt</b></p>
<p>Here you have some examples to use <b>form</b>:</p>
<ul>
	<li>Sending a search query to Google:
		<div class='code'>
			<p><b>&ltform action="http://www.google.com/search"&gt</b>: the &ltaction&gt attribute specifies where the data is directed to.<br>
				<b>&ltinput type="text" name = "q"&gt</b> this sets up a box that can accept <b>text</b> and will set the query parameter <b>q</b> to what you input in the box.<br>
				<b>&ltinput type = "submit"&gt</b> this sets up a <b>submit</b> button.<br>
			<b>&lt/form&gt</b></p>
		</div>
	</li>
	<li>Sending a search query to Google:
		<div class='code'>
			<p><b>&ltform action="http://www.google.com/search"&gt</b>: the &ltaction&gt attribute specifies where the data is directed to.<br>
				<b>&ltinput type="text" name = "q"&gt</b> this sets up a box that can accept <b>text</b> and will set the query parameter <b>q</b> to what you input in the box.<br>
				<b>&ltinput type = "submit"&gt</b> this sets up a <b>submit</b> button.<br>
			<b>&lt/form&gt</b></p>
		</div>
	</li>
	<li>Setting up three radio buttons that set the value of "q" to 1,2 or 3:
		<div class='code'>
			<p><b>&ltform&gt</b><br>
			<b>&ltlabel&gt</b> This set up labels so names of radio buttons will appear next to them<br>
			<b>One</b><br>
			<b>&ltinput name='q' type='radio' value=1&gt</b> Note that type='radio'. It could also be that type='checkbox', so you would have checkboxes instead of radio buttons. Note also that value=1, this will set query parameter "q" to 1 if this radio button is selected.<br>
			<b>&lt/label&gt</b><br>
			<b>&ltlabel&gt</b><br>
			<b>Two</b><br>
			<b>&ltinput name='q' type='radio' value=2&gt</b><br>
			<b>&lt/label&gt</b><br>
			<b>Three</b><br>
			<b>&ltinput name='q' type='radio' value=3&gt</b><br>
			<b>input type="submit"&gt</b><br>
			<b>&lt/form&gt</b><br></p>
		</div>
			<p>Note that in this form the name of the three radio buttons is "q". This groups them so only one of them can be selected simultaneously.</p>
	</li>
	<li>Setting up a dropdown list:
		<div class='code'>
			<b><p>&ltform&gt</b><br>
			<b>&ltselect name='q'&gt</b><br>
			<b>&ltoption&gtOne&lt/option&gt</b><br>
			<b>&ltoption&gtTwo&lt/option&gt</b><br>
			<b>&ltoption&gtThree&lt/option&gt</b><br>
			<b>&lt/select&gt</b><br>
			<b>&ltbr&gt</b><br>
			<b>&ltinput type='submit'&gt</b><br>
			<b>&lt/form&gt</b><br>
		</div>
	</li>
</ul>
'''],
['Stage 4', 'Modulus operator and Dictionaries',
'''
<p>In python, the modulud operator it is indicated by the &#37 sign:</p>
<p>Syntax is as follows: <span class='code'>&ltnumber&gt &#37 &ltnumber&gt -&gt &ltremainder&gt</span></p>
<p>A dictionary is used to map or associate things you want to retrieve to keys. Main advantages over lists are:</p>
<ul>
	<li>You can look up by "key", so you do not have to remember index numbers.</li>
	<li>As dictionaries operate using hash tables, lookup time does not significantly goes up with the number of keys</li>
</ul>
<p>Dictionaries are built using "key:value" pairs, where a "key" can be any inmutable value and "value" can take any value. Here you have a comparison of strings, lists and tables:</p>
<table>
	<tr>
		<th></th>
		<th>Strings</th>
		<th>Lists</th>
		<th>Dictionaries</th>
	</tr>
	<tr>
					<td>Example</td>
					<td>"String"</td>
					<td>['a',3,'dog']</td>
					<td>{'UK':'London,'Spain':'Madrid'}</td>
				</tr>
	<tr>
					<td>Type of data</td>
					<td>Sequence of characters</td>
					<td>Any elements</td>
					<td>key:value pairs</td>
				</tr>
				<tr>
					<td>Mutability</td>
					<td>Not mutable</td>
					<td>Mutable</td>
					<td>Mutable</td>
				</tr>
				<tr>
					<td>Indexing</td>
					<td>string[i] returns the ith value of the string</td>
					<td>list[i] returns the ith value of the string</td>
					<td>dictionary['key'] returns the value associated with 'key'</td>
				</tr>
</table>
<p>Dictionaries can contain other dictionaries. Some useful operations with dictionaries:</p>
<ul>
	<li><b>dictonary['new_key']='new_value'</b> will set new_key equal to new_value</li>
	<li><b>dictonary.items()</b> converts the dictionary into a list</li>
	<li><b>del dictionary['key']</b> can be used to delete 'key' from 'dictionary'</li>
	<li><b>dictionary.keys()</b> returns a list of all keys used in 'dictionary'</li>
</ul>
'''],
['Stage 4', 'Differences between GET and POST requests',
'''
<p>GET requests are mainly used to retrieve data from servers, while POST requests are used to get data from servers. These are the main differences between GET and POST:</p>
<ul><b>GET requests are a simple way for fetching documents:</b>
	<li>Parameters go to URL</li>
	<li>Are used for fetching documents</li>
	<li>Maximum URL length is approximately 2000 words</li>
	<li>OK to cache, in fact, these requests are cached most of times</li>
	<li>These requests should not update the server</li>
</ul>
<ul><b>POST requests are used to update data in servers:</b>
	<li>Parameters go to the body of the request message</li>
	<li>Are used for updating data</li>
	<li>No maximum length</li>
	<li>Not OK to cache as you are probably udating data on a server</li>
</ul>
'''],
['Stage 4','Validation',
'''
<p>Validating user input is essential. Not only for the user experience but for security.</p>
<p>Two major strategies to approach validation are the following:</p>
<ul>
	<li>Use white lists: check if user inputs are among a list of valid inputs. This approach is very safe, but as it limit inputs, it may affect usability.</li>
	<li>Using black lists: check if user inputs are <b>not</b> included in a blacklist of bad inputs. This approach provides better usability but it is less safe, as you may forget to include some bad inputs in your blacklist</li>
</ul>
<p>It is good practice to escape any html characters that can be introduced in your forms. Either by using cgi.escape() or autoescape = True (if you are using Jinja2).</p>
<p>Users that enter bad input may not have malicious intentions, so make sure to provide a good user experience:</p>
<ul>
	<li>Prompt your users if the input entered is not valid</li>
	<li>Redirect them so they can fill out the form again</li>
	<li>Pre-fill any valid input they have entered, so they do not have to start all over again</li>
</ul>
'''],
['Stage 4',"Don't repeat yourself! And use html templates...",
'''
<p>When coding, it is extremely important to avoid repetition for at least three reasons:</p>
<ol>
	<li><strong>Efficiency:</strong> obviously, the less you have to repeat your code by copying and pasting, or worse, by typing, the more efficient you are.</li>
	<li><strong>Avoiding mistakes:</strong> the same idea mentioned in point 1 applies here. The less you type, the less mistakes you make. Additionally, if you make a mistake and you have lots of duplicated code, it will take you a long time to fix that.</li>
	<li><strong>Avoiding inconsistencies:</strong> when you have assigned the design of each of the elements of the website manually, you will be more prone to inconsistencies. If you, however, use classes in CSS to automatically style the similar elements in your website at once, the result will be much more consistent.</li>
</ol>
<p>Using HTML templates have many benefits: separate html and python codes, more readable code, more security (if you use autoescape features) and easier to modify html.</p>
<p>But... it also helps you avoid repetition in at least two ways:</p>
<ul>
	<li>Template inheritance allows you to replicate the header and footer of a website accross as many different html docs as you want without having to write it again and again.</li>
	<li>By passing in form inputs as variable values to jinja templates you can automatically generate html code</li>
	<li>You use "for" loops in you templating language of choice in order to loop through iterables</li>
</ul>
'''],
['Stage 5',"Intro to HTML and CSS",
'''
<p>In CSS, if you use <span class="code">display: flex;</span> in a "parent" container, all its "child" elements will be displayed in one line of code.</p>
<p>In general, when you are working on a design, you have to follow a CODE, TEST, REFINE process:</p>
<ul>
	<li>Look for "boxes" or different areas</li>
	<li>Look for repeated style and semantic elements</li>
	<li>Write html</li>
	<li>Apply styles</li>
	<li>Fix small things</li>
</ul>
<p><b>CSS frameworks</b> are pre-prepared software frameworks that are meant to allow for easier, more standards-compliant web design using CSS. Mos of these frameworks contain at least a grid model.</p>
<p><b>Responsiveness</b> is the ability of websites to adapt to the size of different devices</p>
<p>If you design a website using Bootstrap, it already includes some responsive features which provide a good place to start. If you need more customization, you can use media queries:</p>
<div class="code">
media only screen (max-width: 300px){<br>
	p{<br>
	background-color: blue;<br>
	}<br>
}
</div>
<p>The media query above, sets a blue background color whenever the screen width is smaller than 300px.</p>
<p><b>Bootstrap</b> provides a nice grid system. Elements should all be in a .container class. Then, the page can have multiple .row classes that will span the whole width. These rows will contain differnt .col classes. Depending on the specific class, it will span through a fraction of the total width. Example: .col-md-9 will span through 9/12 of the total width.</p>
<p>The <a href="http://getbootstrap.com/">Bootstrap</a> website is a very good resource for web development. There you can find very complete documentation and numerous examples of the different bootstrap features. Of special interest are the following sections within the CSS and Javascript tabs:</p>
<ul>
	<li>The <b>Grid</b> section provides and explanation of what elements you can use to design the layout of your website.</li>
	<li>The <b>Typography</b> section contains some useful text features to control capitalization, text alignment, highlights and more</li>
	<li>The <b>Images</b> section explains how to use bootstrap to add responsiveness to your image and change shapes.</li>
	<li>The <b>Modal</b> section within the Javascript tab, explains how to introduce <em>modals</em> to your website. Modals can be used to display additional information within the page you are navigationg. Depending on the options you set, a new box will appear and the rest of the content will be shaded.</li>
</ul>
'''],
['Stage 5',"Responsive Design Fundamentals",
'''
<p>The mobile internet market is booming. In fact, it already is the first device used for internet. It is then essential to ensure a good user experience in mobile devices.</p>
<p>The way to think about responsive design is "mobile first". Instead of designing a full-blow website made for a desktop screen. Start small, design it for a small device. Then, make changes to adapt to bigger screens. That way:</p>
<ul>
	<li>You optimize your content by keeping it to the essentials.</li>
	<li>>You optimize your code. Working this way, you do not include superfluous features.</li>
	<li>You improve performance. This is a consecuence of the last two points.</li>
</ul>
<p>The Chrome development tools include simulators for smaller devices. Using simulators you can simulate your website on different devices and different browsers. This is not fully accurate, but is inexpensive and convenient.</p>
<p>The <b>viewport</b> defines the area of the screen that the browser renders content to. Some important concepts to keep in mind are the following:</p>
<ul>
	<li>DIP (Device Independent Pixels): these try to match the real size of the screens. Similar screen sizes should have similar DIPs</li>
	<li>Physical pixel: is the real number of pixels of the device.</li>
	<li>Pixel Ratio: this is the ratio between the hardware pixels and the DIP. Note that pixels are measured in one dimension, normally accross the width of the device.</li>
</ul>
<p>It is essential to set up the viewport in the head section of your html:</p>
<div class="code">
&lt name=&quotviewport&quot content=&quotwidth=device-width, initial-scale=1&quot&gt
</div>
<p>This sets the content width to the device width and assigns a ratio between DIPs and CSS pixels of 1.</p>
<p>For images, videos, etc. it is recommended to add a "catch-all" that limits the width of the elements to 100%. Using relative widths instead of absolute widths improves responsiveness.</p>
<div class="code">
img, embed, object, video{
	max-width:100%;
}
</div>
<p>For good experience with touchscreens, buttons should be 48px x 48px and have at least 40px between them.</p>
<p><b>Media queries</b> allow you to apply different styles depending on the width. By adding <em>breakpoints</em> you can keep a good experience accross devices. When adding breakpoints, do not think about devices, think about how the content is displayed!</p>
<p>To add media queries you have two reasonable options (there are more, but they compromise performance):</p>
<ul>
	<li>Use the media query to link a different css file for each width</li>
	<li>Embbed the media query in the html document</li>
</ul>
<p>A good <b>grid</b> model is essential for good user experience. Use the following code in a "container" element, and elements will be displayed in a row:</p>
<div class="code">
display: flex;
flex-wrap: wrap;
</div>
<p>The flex-wrap option allows elements to jump from one row to another when they do not fit in a single line.</p>
<p>The <b>order</b> attribute allows you to change the order in which the elements are displayed</p>
<p>There are mainly four types of responsive pattern:</p>
<ul>
	<li>Column drop: columns are simply stacked as the screen shrinks.</li>
	<li>Mostly fluid: similar to column drop</li>
	<li>Layout shifter: layout is changed more dramatically as screen width changes. Order is altered using the "order" attribute</li>
	<li>Off-canvas: may require a little bit of JS. Not frequently used content is put off-screen and only showed when user hits a "hamgurguer button"(for example)</li>
</ul>
<p>These patterns can be used in combination, you do not have to stick with a specific pattern.</p>
<p>Aside from layout, many other things can be optimized, including tables, images, and typography.</p>
<p>Major breakpoints, include major changes to layout. For an excellent experience, you will need <b>minor breakpoints</b> that adjust font sizes, that hide content, etc. In general, 65 characters per line is ideal for the web (research outputs on ideal length range from 40 to 90 characters). Shorter lines are awkward, and longer lines may be painful for readers. A size of 16 px and 1.2 em is the minimum required.</p>
<p>The <a href="https://developers.google.com/web/fundamentals/media/index?hl=en">Google Web Fundamentals</a> website is a very good source to learn about responsive design. A good section is the <strong>images</strong> section. There you find tips for responsive images like the following:</p>
<ul>
	<li>Use relative sizes for images: <span div="code">max-width:100%;</span> is your friend</li>
	<li><span div="code">srcset</span> allows the browser to choose the best image size, depending on the device on which it's shown</li>
	<li>Use expandable product images: users want to know what they are buying</li>
</ul>
<p>In addition, this website contains many, many tips to ensure good user experience: how to place "calls to action", navigation tips, form entry, etc. etc.</p>
''']
]












