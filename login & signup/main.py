from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

@app.post("/signup")
async def signup(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    # Perform validation (you can add more validation as needed)
    if not (username and email and password):
        raise HTTPException(status_code=400, detail="Please fill in all fields")

    # Perform signup logic (replace with your actual signup logic)
    # For simplicity, we'll just print the data here
    print(f"Signup successful! Username: {username}, Email: {email}, Password: {password}")

    # You can return a response or data here if needed
    return {"message": "Signup successful"}
