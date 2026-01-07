from flask import Flask, request, render_template

app = Flask(__name__)

#page route
@app.route("/home", methods=["GET", "POST"])
def index():
    #initialize result variable 
    result = None
    #if user send post,
    if request.method == "POST":
        #get temperature field from HTML input
        temp = request.form.get("temperature")
        #get the option (C or F)
        scale = request.form.get("scale")
        try:
            temp = float(temp)
            if scale == "C": #Celsius
                result = f"{temp}°C = {(temp * 9/5) + 32:.2f}°F"
            else:            #Fahrenheit
                result = f"{temp}°F = {(temp - 32) * 5/9:.2f}°C"
        #if input isnt a number
        except ValueError:
            result = "Please enter a valid number"
    #function of the Flask library
    #put the variable result in the html file
    return render_template("index.html", result=result)

if __name__ == "__main__":
    #with host="0.0.0.0":  the application will be accessible from any computer
    #port=5000: http://localhost:5000
    app.run(host="0.0.0.0", port=5000)
