import nox

locations = ["src"]


@nox.session(python=["3.9"])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", "--line-length", "79", *args)


@nox.session(python=["3.9"])
def flake8(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)


@nox.session(python=["3.9"])
def isort(session):
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)
