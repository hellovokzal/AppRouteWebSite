from flask import Flask


app = Flask(__name__)

@app.route("/")

def hello():
	return """

 <!DOCTYPE html>
<html>
  <head>
    <title>Трахать</title>
  </head>
  <body>
    <h1>Трахать</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG6i7Cb1Fa6cHYGrdHHQHyyVvclDfQu9wKgwAhJajRW6hmECA&s" alt="Изображение">
    <br><br>
    <button onclick="showSuccessMessage()">Трахать</button>
    <p id="successMessage"></p>

    <script>
      function showSuccessMessage() {
        document.getElementById("successMessage").innerHTML = "Успешно Трахан!";
      }
    </script>
  </body>
</html>
"""
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
