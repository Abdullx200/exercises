# Write your code here
def generate_git_script(id):
    return f'if [ ! -d {id}]; then \n    git clone https://github.com/id/project {id}\nels\n    (cd {id}; git pull)\nfi'