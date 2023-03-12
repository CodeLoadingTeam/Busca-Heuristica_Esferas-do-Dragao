<h3>Siga os passos abaixo para configurar o seu GIT</h3>

(Recomendação)
Faça o download do GIT Desktop -> <a href="https://desktop.github.com">https://desktop.github.com</a>



(Configuração)
Faça a instalação do terminal GIT Bash -> <a href="https://gitforwindows.org/">https://gitforwindows.org/</a>

Adicione sua chave SSH ao seu GIT para facilitar a execução dos comandos dentro do terminal GIT Bash

- Verifique se em seu computador já existe uma chave SSH -> <a href="https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys">checking-for-existing-ssh-keys</a>

- Gere uma chave SSH e adicione-á ao ssg-agent-> <a href="https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent</a>

- Faça a adição da chave SSH ao seu perfil do GIT Hub -> <a href="https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account">adding-a-new-ssh-key-to-your-github-account</a>



(Comandos do GIT Bash)
--> Para realizar um clone:
$ git clone "coloque aqui o ssh do repositório"

--> Para atualizar a branch local, vá para a master:
$ git checkout origin/master
e 
$ git pull


--> Para criar uma nova branch:
$ git branch "coloque aqui o nome da branch"
e
$ git checkout "nome da sua branch criada"


--> Para fazer um commit, adicione/prepare as alterações:
$ git add .
e salve-as no commit
$ git commit -m "texto do commit"


--> Para salvar na nuvem suas modificações:
$ git push



(Padrões de escrita)
Ao trabalharmos com branches e pull requests, seguiremos a seguinte nomenclatura:

Para Branch
     X/exemplo-de-título

Para Pull Request (PR)
     [FEATURE][TAREFAX] - Exemplo de Título
     [HOTFIX][TAREFAX] - Exemplo de Título


Onde 

Feature: destinado a criações/implementações
Hotfix: destinado a correções
X: Designado ao número da tarefa em questão



