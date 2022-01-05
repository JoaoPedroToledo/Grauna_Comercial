	function clicar(){
		var num1 = document.querySelector(".mp").value;
		var num2 = document.querySelector(".eng").value;
		var num3 = document.querySelector(".mo_insp").value;
		var num4 = document.querySelector(".mo_fab").value;

		var resultado = parseInt(num1) + parseInt(num2) + parseInt(num3) + parseInt(num4);
		document.querySelector(".resultado").innerHTML = resultado;
	}
	
	function clica(){
		var num1 = document.querySelector(".inst_med").value;
		var num2 = document.querySelector(".tools").value;
		var num3 = document.querySelector(".dev").value;

		var resultado = parseInt(num1) + parseInt(num2) + parseInt(num3);
		document.querySelector(".result").innerHTML = resultado;
	}

	function calcular() {
		var n1 = parseInt(document.getElementById('.mp').value, 10);
		var n2 = parseInt(document.getElementById('.eng').value, 10);
		var n3 = parseInt(document.getElementById('.mo_insp').value, 10);
		var n4 = parseInt(document.getElementById('.mo_fab').value, 10);
		document.getElementById('resultado').innerHTML = n1 + n2 + n3 + n4;
	  }