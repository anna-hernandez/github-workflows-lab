import nox

locations = ["src", "tests", "noxfile.py"]


@nox.session("python=3.9")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", "--line-length", "79", *args)
