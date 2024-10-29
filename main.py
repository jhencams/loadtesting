from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                max-width: 400px;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            label {
                display: block;
                margin: 10px 0 5px;
                color: #555;
            }
            input[type="text"], select {
                width: 100%;
                padding: 8px;
                margin: 5px 0 15px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Calculator</h1>
            <form action="/calculate" method="post">
                <label for="num1">Number 1:</label>
                <input type="text" id="num1" name="num1" required><br>
                
                <label for="num2">Number 2:</label>
                <input type="text" id="num2" name="num2" required><br>
                
                <label for="operation">Operation:</label>
                <select id="operation" name="operation">
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select><br>
                
                <input type="submit" value="Calculate">
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    num1: float = Form(...),
    num2: float = Form(...),
    operation: str = Form(...)
):
    result = None
    error = None

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            error = "Division by zero"
        else:
            result = num1 / num2
    else:
        error = "Invalid operation"
   
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator Result</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                max-width: 400px;
                text-align: center;
            }}
            h1 {{
                color: #333;
            }}
            label {{
                display: block;
                margin: 10px 0 5px;
                color: #555;
            }}
            input[type="text"], select {{
                width: 100%;
                padding: 8px;
                margin: 5px 0 15px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }}
            input[type="submit"] {{
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }}
            input[type="submit"]:hover {{
                background-color: #45a049;
            }}
            .result {{
                font-size: 18px;
                color: #333;
                margin-top: 15px;
            }}
            .error {{
                font-size: 18px;
                color: red;
                margin-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Calculator</h1>
            <form action="/calculate" method="post">
                <label for="num1">Number 1:</label>
                <input type="text" id="num1" name="num1" required><br>
                
                <label for="num2">Number 2:</label>
                <input type="text" id="num2" name="num2" required><br>
                
                <label for="operation">Operation:</label>
                <select id="operation" name="operation">
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select><br>
                
                <input type="submit" value="Calculate">
            </form>
            
            <div class="result">Result: {result if result is not None else ""}</div>
            <div class="error">{error if error is not None else ""}</div>
        </div>
    </body>
    </html>
    """
