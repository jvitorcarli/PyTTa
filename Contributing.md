Contributing
============
If you want to contribute to this project and make it better, your help is very welcome.

## How to make a clean pull request

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `development` with the name `dev-NAME_RELATED_TO_CHANGE`.
- Implement/fix your feature, comment on your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the `development` branch!
- If further changes are requested, just push them to your branch. PR will be updated automatically.
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit when applied, does to the code – not what you did to the code.

Adapted from [MarcDiethelm](https://github.com/MarcDiethelm/contributing)

## Installing PyTTa locally for development

PyTTa currently uses [Poetry](https://python-poetry.org/), a pip alternative, to manage its regular and development dependencies. You can get it at: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

After getting Poetry and cloning your forked repository to your machine install the regular and development dependencies, as follows:

```bash
$ poetry install
```

Have fun developing!
