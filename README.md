# Boston-House-Price-Prediction

## Create New Repository

- Clone the repository into our machine.

## Software and Tools Requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://heroku.com)
4. [Git CLI](https://git-scm.com/downloads)

## Create New Environment

```bash
conda create -p venv python==3.9 -y
```

## Activate New Environment

```bash
conda activate env_name
conda init shell
conda info --envs
```

## Create a requirements.txt file

Attach the lirabried we require in this file.

```txt
Flask
sklearn
pandas
numpy
matplotlib
```

Install the libraries using below command,


```bash
pip install -r requirements.txt
```

## Setting up git


```bash
git config --global user.name
git config --global user.email
```

- Create a *.gitignore* file and add the files not required to be pushed to remote repository.

```bash
git add --all
git commit -am "Add All"
git pull && git push
```




