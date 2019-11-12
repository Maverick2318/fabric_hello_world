from fabric import task

@task
def hello(ctx):
    print("hello world")

@task(optional=['name'])
def helloname(ctx, name="world"):
    print("hello %s!" % name)
