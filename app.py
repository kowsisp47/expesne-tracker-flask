from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage (list)
products = []

@app.route("/")
def home():
    return render_template("grocery.html", items=products)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    price = request.form["price"]

    products.append({"name": name, "price": price})
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(products):
        products.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)