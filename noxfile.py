import nox

locations = ["src"]


@nox.session(python=["3.9"])
def black(session):
    args = locations
    session.install("black")
    session.run("black", "--line-length", "79", *args)
