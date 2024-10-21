
# Guia de Uso do GitHub com VSCode e Streamlit

Este guia descreve os passos necessários para criar, subir, atualizar e publicar projetos no GitHub usando o VSCode, além de como voltar uma versão e publicar um app no Streamlit.

## 1. Entrar no GitHub

Para acessar sua conta do GitHub:
- Acesse o site: [GitHub.com](https://github.com/)
- Clique em **Sign In** no canto superior direito.
- Insira seu **usuário** ou **e-mail** e **senha**.
- Se você ainda não tem uma conta, clique em **Sign up** e siga os passos para criar uma nova conta.

## 2. Criar um novo repositório no GitHub

1. Faça login no GitHub e vá até a sua página inicial.
2. Clique no botão verde **New** (Novo) à esquerda ou no botão **+** no canto superior direito e selecione **New repository**.
3. Defina um nome para o repositório no campo **Repository name**.
4. Escolha se o repositório será **público** ou **privado**.
5. (Opcional) Marque a opção **Initialize this repository with a README** para começar com um arquivo README.
6. Clique em **Create repository** para criar o repositório.

## 3. Subir um repositório do VSCode para o GitHub

1. No VSCode, abra o terminal integrado (`Ctrl + '`).
2. Navegue até o diretório do seu projeto, caso ainda não esteja nele:
   ```bash
   cd caminho/para/seu/projeto
   ```
3. Inicialize o repositório local do Git, se ainda não foi feito:
   ```bash
   git init
   ```
4. Adicione os arquivos ao repositório:
   ```bash
   git add .
   ```
5. Faça o primeiro commit:
   ```bash
   git commit -m "Primeiro commit"
   ```
6. Conecte seu repositório local ao GitHub. Use a URL do repositório que você criou no GitHub:
   ```bash
   git remote add origin https://github.com/seu-usuario/nome-repositorio.git
   ```
7. Faça o envio (push) do repositório para o GitHub:
   ```bash
   git push -u origin main
   ```

## 4. Atualizar um repositório do VSCode no GitHub

1. Adicione os novos arquivos ou mudanças ao repositório:
   ```bash
   git add .
   ```
2. Faça o commit com uma mensagem que descreva as alterações:
   ```bash
   git commit -m "Descrição das alterações"
   ```
3. Envie as alterações para o GitHub:
   ```bash
   git push origin main
   ```

## 5. Publicar um projeto do GitHub no Streamlit

1. Crie um arquivo **`requirements.txt`** na raiz do projeto, listando todas as bibliotecas usadas no projeto, por exemplo:
   ```plaintext
   streamlit
   pandas
   numpy
   ```
2. No site do [Streamlit](https://share.streamlit.io/), faça login.
3. Clique em **New App** para iniciar o processo de deploy.
4. No campo **Repository**, insira a URL do seu repositório GitHub, por exemplo:
   ```plaintext
   https://github.com/seu-usuario/nome-repositorio
   ```
5. No campo **Branch**, selecione **main**.
6. No campo **Main file path**, insira o caminho do arquivo Python principal que roda o Streamlit, por exemplo:
   ```plaintext
   src/app.py
   ```
7. Clique em **Deploy** para publicar seu app.

## 6. Voltar para uma versão anterior no GitHub usando o VSCode

1. Verifique o histórico de commits com:
   ```bash
   git log
   ```
   Isso mostrará a lista de commits, incluindo os códigos de hash dos commits (identificadores únicos).
   
2. Para voltar para um commit anterior temporariamente, use o comando:
   ```bash
   git checkout <hash-do-commit>
   ```
   Isso permite que você explore o código como ele estava naquele commit.

3. Para voltar permanentemente para um commit anterior, faça um reset:
   ```bash
   git reset --hard <hash-do-commit>
   ```
   **Atenção:** Isso sobrescreverá as mudanças feitas após esse commit. Use com cuidado.

4. Se você já tiver feito um `reset` e precisar atualizar o repositório remoto, faça o push forçado:
   ```bash
   git push --force
   ```

---

Esse é o guia básico para trabalhar com GitHub, VSCode e Streamlit. Certifique-se de seguir as melhores práticas para versionamento de código e uso do Git.



git atualizado para main
git atualizado formatacao