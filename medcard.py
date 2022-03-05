from main import app, db
from main.models import Animal, Procedure


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Animal": Animal, "Procedure": Procedure}


if __name__ == "__main__":
    app.run()
