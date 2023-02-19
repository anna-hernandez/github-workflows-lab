import nox

locations = ["src"]


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", "--line-length", "79", *args)


@nox.session(python=["3.8"])
def flake8(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def isort(session):
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)
