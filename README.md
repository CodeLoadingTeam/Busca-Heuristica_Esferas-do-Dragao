<h2>Siga os passos abaixo para configurar o seu GIT</h2>

<h4>(Recomendação)</h4>
Faça o download do GIT Desktop -> <a href="https://desktop.github.com">https://desktop.github.com</a>



<br><h4>(Configuração)</h4>
Faça a instalação do terminal GIT Bash -> <a href="https://gitforwindows.org/">https://gitforwindows.org/</a><br><br>

Adicione sua chave SSH ao seu GIT para facilitar a execução dos comandos dentro do terminal GIT Bash<br>

- Verifique se em seu computador já existe uma chave SSH -> <a href="https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys">checking-for-existing-ssh-keys</a><br>

- Gere uma chave SSH e adicione-á ao ssg-agent-> <a href="https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent</a><br>

- Faça a adição da chave SSH ao seu perfil do GIT Hub -> <a href="https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account">adding-a-new-ssh-key-to-your-github-account</a><br>



<br><h4>(Comandos do GIT Bash)</h4>
--> Para realizar um clone: <br>
$ git clone "coloque aqui o ssh do repositório" <br><br>

--> Para atualizar a branch local, vá para a master: <br>
$ git checkout origin/master <br>
e <br>
$ git pull <br><br>


--> Para criar uma nova branch: <br>
$ git branch "coloque aqui o nome da branch" <br>
e <br>
$ git checkout "nome da sua branch criada" <br><br>


--> Para fazer um commit, adicione/prepare as alterações: <br>
$ git add . <br>
e salve-as no commit <br>
$ git commit -m "texto do commit" <br><br>


--> Para salvar na nuvem suas modificações: <br>
$ git push <br><br>



<br><h4>(Padrões de escrita)</h4>
Ao trabalharmos com branches e pull requests, seguiremos a seguinte nomenclatura:<br><br>

Para Branch <br>
     X/exemplo-de-título <br><br>

Para Pull Request (PR) <br>
     [FEATURE][TAREFAX] - Exemplo de Título<br>
     [HOTFIX][TAREFAX] - Exemplo de Título<br><br>


Onde <br>
Feature: destinado a criações/implementações<br>
Hotfix: destinado a correções<br>
X: Designado ao número da tarefa em questão<br><br>
