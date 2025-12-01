# ✅ Checklist Final para Publicação do Portfólio

Use este checklist antes de publicar o portfólio no GitHub público.

---

## 🔒 Segurança e Privacidade

- [ ] **Arquivos sensíveis removidos**
  - [ ] API keys removidas ou movidas para `.env` (não versionado)
  - [ ] Senhas removidas
  - [ ] CPFs ou dados pessoais anonimizados
  - [ ] Arquivos `*api*.txt` ou `*_key.txt` removidos

- [ ] **`.gitignore` configurado corretamente**
  - [ ] Dados grandes (>10MB) no `.gitignore`
  - [ ] Arquivos `.env` ignorados
  - [ ] Arquivos temporários ignorados (`.ipynb_checkpoints`, `*.aux`, etc.)
  - [ ] Binários ignorados (`chromedriver`, etc.)

- [ ] **Histórico do Git limpo** (se necessário)
  - [ ] Dados sensíveis removidos do histórico (usar `git filter-branch` se necessário)
  - [ ] Commits com dados sensíveis removidos

---

## 📁 Estrutura e Organização

- [ ] **Estrutura de pastas padronizada**
  - [ ] Projetos em destaque na pasta `projects/`
  - [ ] Material de estudo em `_archive/`
  - [ ] Nomes de pastas consistentes (kebab-case)

- [ ] **Nomes de arquivos descritivos**
  - [ ] Sem nomes genéricos (`teste.ipynb`, `final.ipynb`)
  - [ ] Padrão numérico para notebooks (`01-exploracao.ipynb`, `02-modelagem.ipynb`)
  - [ ] Sem caracteres especiais ou espaços

- [ ] **Sem pastas vazias ou temporárias**
  - [ ] Pasta `downloads/` removida ou documentada
  - [ ] Arquivos temporários removidos

---

## 📚 Documentação

- [ ] **README.md principal completo**
  - [ ] Introdução profissional
  - [ ] Projetos em destaque documentados
  - [ ] Tecnologias listadas
  - [ ] Instruções de instalação
  - [ ] Contato atualizado (ou "sob demanda")

- [ ] **README.md em cada projeto principal**
  - [ ] Objetivo do projeto
  - [ ] Resumo dos resultados
  - [ ] Passos para reproduzir
  - [ ] Principais arquivos
  - [ ] Como obter os dados

- [ ] **README.md em cada disciplina**
  - [ ] Lista de projetos
  - [ ] Tecnologias utilizadas
  - [ ] Como executar

- [ ] **data/README.md em projetos com dados**
  - [ ] Como obter os dados
  - [ ] Links para download
  - [ ] Comandos wget/curl (se aplicável)
  - [ ] Descrição do dataset

---

## 💻 Código e Notebooks

- [ ] **Notebooks limpos**
  - [ ] Outputs removidos ou versão `*_clean.ipynb` criada
  - [ ] Seeds definidos para reprodutibilidade (`np.random.seed()`, `random.seed()`)
  - [ ] Caminhos relativos (sem caminhos absolutos locais)
  - [ ] Células de setup claramente separadas

- [ ] **Notebooks documentados**
  - [ ] Células markdown explicando cada etapa
  - [ ] Seção "Resumo" com principais resultados
  - [ ] Referência ao dataset (link ou instruções)

- [ ] **Código Python com qualidade**
  - [ ] Docstrings estilo NumPy em funções
  - [ ] Type hints onde aplicável
  - [ ] Tratamento de erros adequado
  - [ ] Logging em vez de print() (quando aplicável)

- [ ] **Scripts executáveis**
  - [ ] Scripts rodam do início ao fim sem erros
  - [ ] Dependências claramente listadas
  - [ ] Exemplos de uso documentados

---

## 📦 Dependências

- [ ] **requirements.txt atualizado**
  - [ ] Versões específicas de pacotes (usar `==` em vez de `>=`)
  - [ ] Todas as dependências listadas
  - [ ] requirements.txt na raiz e em projetos específicos (quando necessário)

- [ ] **Instruções de instalação claras**
  - [ ] Comandos de instalação documentados
  - [ ] Dependências de sistema documentadas (PostgreSQL, LaTeX, etc.)

---

## 📊 Dados

- [ ] **Datasets grandes no `.gitignore`**
  - [ ] Arquivos >10MB não versionados
  - [ ] `data/raw/` e `data/processed/` no `.gitignore`

- [ ] **Amostras pequenas para testes**
  - [ ] `data/sample/` com amostras pequenas (<1MB)
  - [ ] Amostras suficientes para reproduzir análises básicas

- [ ] **Documentação de dados**
  - [ ] `data/README.md` com instruções para obter dados
  - [ ] Links funcionando
  - [ ] Comandos de download documentados

---

## 🎨 Visualizações

- [ ] **Figuras organizadas**
  - [ ] Figuras salvas em `figures/` (não embutidas nos notebooks)
  - [ ] Figuras principais documentadas
  - [ ] Resolução adequada (300 DPI para publicações)

- [ ] **Screenshots para projetos em destaque**
  - [ ] Screenshot ou plot principal de cada projeto em destaque
  - [ ] Imagens no README principal

---

## 🏆 Projetos em Destaque

- [ ] **3-5 projetos selecionados**
  - [ ] Projetos completos e finalizados
  - [ ] Resultados mensuráveis documentados
  - [ ] README específico para cada projeto

- [ ] **Documentação completa**
  - [ ] Objetivo claro
  - [ ] Metodologia descrita
  - [ ] Resultados apresentados
  - [ ] Tecnologias listadas

---

## 🔄 Versionamento

- [ ] **Commits organizados**
  - [ ] Mensagens descritivas
  - [ ] Commits lógicos (não muitos pequenos, não muito grandes)

- [ ] **Branches organizadas** (se aplicável)
  - [ ] Branch principal (`main` ou `master`)
  - [ ] Branches de feature (se necessário)

---

## 🤖 CI/CD (Opcional)

- [ ] **GitHub Actions configurado** (opcional)
  - [ ] Lint passando
  - [ ] Testes passando (se houver)
  - [ ] Workflow documentado

---

## 📝 Revisão Final

- [ ] **Revisão de ortografia e gramática**
  - [ ] READMEs revisados
  - [ ] Comentários em código revisados
  - [ ] Documentação clara e profissional

- [ ] **Links funcionando**
  - [ ] Todos os links internos funcionam
  - [ ] Links externos verificados

- [ ] **Consistência**
  - [ ] Formatação consistente
  - [ ] Estilo de escrita consistente
  - [ ] Nomenclatura consistente

---

## 🚀 Antes de Publicar

1. ✅ Revisar este checklist completo
2. ✅ Fazer commit final com mensagem descritiva
3. ✅ Criar tag de release (opcional): `git tag -a v1.0.0 -m "Portfolio inicial"`
4. ✅ Push para GitHub: `git push origin main --tags`
5. ✅ Verificar se o repositório está público
6. ✅ Adicionar descrição no GitHub
7. ✅ Adicionar tópicos (tags) no GitHub: `data-science`, `machine-learning`, `python`, `portfolio`

---

**Data da revisão:** _______________  
**Revisado por:** _______________  
**Status:** [ ] Pronto para publicação

---

**Última atualização:** Janeiro 2025

