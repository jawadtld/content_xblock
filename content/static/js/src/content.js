/* Javascript for ContentXBlock. */
function ContentXBlock(runtime, element) {

	var modal1 = document.getElementById('myModal1');
	var modal2 = document.getElementById('myModal2');
	var modal3 = document.getElementById('myModal3');
	var modal4 = document.getElementById('myModal4');

	// Get the button that opens the modal
	var btn1 = document.getElementById("myBtn1");
	var btn2 = document.getElementById("myBtn2");
	var btn3 = document.getElementById("myBtn3");
	var btn4 = document.getElementById("myBtn4");

	// Get the <span> element that closes the modal
	var span1 = document.getElementsByClassName("close")[0];
	var span2 = document.getElementsByClassName("close")[1];
	var span3 = document.getElementsByClassName("close")[2];
	var span4 = document.getElementsByClassName("close")[3];

    $(function ($) {
        /* Here's where you'd do things on page load. */
		// When the user clicks on the button, open the modal
		btn1.onclick = function() {
		    modal1.style.display = "block";
		    document.getElementById('iframe1').src = "{self.sim_url}";
		}

		btn2.onclick = function() {
		    modal2.style.display = "block";
		    document.getElementById('iframe2').src = "{self.anim_url}";
		}

		btn3.onclick = function() {
		    modal3.style.display = "block";
		    document.getElementById('iframe3').src = "{self.vid_url}";
		}

		btn4.onclick = function() {
		    modal4.style.display = "block";
		    document.getElementById('iframe4').src = "{self.game_url}";
		}

		// When the user clicks on <span> (x), close the modal
		span1.onclick = function() {
		    modal1.style.display = "none";
		    document.getElementById('iframe1').src = "";
		}

		span2.onclick = function() {
		    modal2.style.display = "none";
		    document.getElementById('iframe2').src = "";
		}

		span3.onclick = function() {
		    modal3.style.display = "none";
		    document.getElementById('iframe3').src = "";
		}

		span4.onclick = function() {
		    modal4.style.display = "none";
		    document.getElementById('iframe4').src = "";
		}

		// When the user clicks anywhere outside of the modal, close it
		window.onclick = function(event) {
		    if (event.target == modal1) {
		        modal1.style.display = "none";
		        document.getElementById('iframe1').src = "";
		    }
		    if (event.target == modal2) {
		        modal2.style.display = "none";
		        document.getElementById('iframe2').src = "";
		    }
		    if (event.target == modal3) {
		        modal3.style.display = "none";
		        document.getElementById('iframe3').src = "";
		    }
		    if (event.target == modal4) {
		        modal4.style.display = "none";
		        document.getElementById('iframe4').src = "";
		    }

		}
    });
}

