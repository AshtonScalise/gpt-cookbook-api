from app import create_app  # Adjusted this line

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
