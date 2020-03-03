# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:28:00 2020

@author: buzz buzz
"""

!DOCTYPE html>
<html>
	<body>
{% extends "dropdown.html" %}
{% block content %}
		<div class="login">
            <h1>USER LOGIN</h1>
            <form action="{{ url_for('userlogin') }}" method="POST">
    			<input type="text" name="username" placeholder="Username" id="username" required>
				<input type="password" name="password" placeholder="Password" id="password" required>
				<div class="msg">{{ msg }}</div>
                <button onclick="redirect()">Login</button>				
			</form>
            <script>
            var redirect = function() {
                 setTimeout(function(){ alert("Login successfull"); 
                     window.location.href = "http://localhost:5000/logout/";
                     }, 5);
                 };
        </script>
 
            
	     </div>
{% endblock %}
	</body>


</html>