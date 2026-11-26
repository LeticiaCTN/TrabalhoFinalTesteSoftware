# TrabalhoFinalTesteSoftware

# Tema e Objetivo
Durante o semestre você escreveu testes que rodavam na sua máquina. Neste desafio final, o objetivo é dar o
próximo passo: fazer os testes rodarem automaticamente no GitHub a cada envio de código. Isso se chama
integração contínua (CI). Você vai criar um repositório novo com uma função simples e seus testes, configurar
um CI, introduzir um erro de propósito em uma branch separada e comprovar que o CI detecta sozinho que
um teste quebrou, barrando a alteração na Pull Request.
Objetivo: configurar um fluxo de CI com GitHub Actions do zero e demonstrar, na prática, o CI identificando
um teste que falhou. É a aplicação direta dos conceitos de regressão e teste antecipado vistos em aula

# O que Fazer?
1. Crie um repositório novo e público no GitHub, só para este desafio.
2. Escreva uma função simples e nova, à sua escolha (por exemplo: somar dois números, verificar se um
número é par, calcular a média de uma lista ou converter uma temperatura), em Jest (JavaScript) ou pytest
(Python).
3. Escreva pelo menos dois testes para essa função e confirme que passam localmente.
4. Suba o projeto para o repositório, com os testes funcionando.
5. Pesquise e configure um CI com GitHub Actions que instale as dependências e rode os testes
automaticamente a cada push e a cada Pull Request. Faça o primeiro CI passar (check verde).
6. Crie uma branch separada e, nela, introduza um erro de propósito na função (algo que faça um dos testes
falhar).
7. Suba a branch e abra uma Pull Request. O CI deve rodar sozinho e acusar que um teste quebrou (check
vermelho na PR).
8. Deixe tudo registrado no repositório: os commits e a Pull Request com o CI vermelho

