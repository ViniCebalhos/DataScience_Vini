# ✅ Checklist Final para Publicação do Portfólio

**Autor:** Vinícius de Souza Cebalhos  
**Data:** Janeiro 2025  
**Objetivo:** Checklist completo antes de publicar o portfólio no GitHub

---

## 🔒 1. Segurança e Privacidade

### Dados Sensíveis
- [ ] Arquivos sensíveis removidos (API keys, senhas, CPFs)
- [ ] `.gitignore` configurado corretamente
- [ ] Dados pessoais anonimizados (se houver)
- [ ] Arquivos `.env` não versionados
- [ ] Histórico do Git limpo (se necessário, usar `git filter-branch`)

### Verificação de Segurança
- [ ] Executado: `grep -r "api_key\|API_KEY\|secret\|SECRET" --include="*.txt" --include="*.py" .`
- [ ] Executado: `find . -name ".env" -o -name "*.env"`
- [ ] Nenhum arquivo com dados sensíveis encontrado

---

## 📁 2. Estrutura e Organização

### Estrutura de Pastas
- [ ] Estrutura de pastas padronizada
- [ ] Nomes de arquivos descritivos e consistentes
- [ ] Projetos em destaque na pasta `projects/`
- [ ] Material de estudo em `_archive/`
- [ ] Sem pastas vazias ou temporárias
- [ ] Subpastas desnecessárias removidas (Work6/, Work8/, Work3/, challenge/)

### Nomenclatura
- [ ] Sem nomes genéricos (teste.ipynb, final.ipynb)
- [ ] Nomes descritivos e padronizados
- [ ] Sem duplicatas (teste.ipynb, Teste2.ipynb, final.ipynb, final2.ipynb)

---

## 📝 3. Documentação

### READMEs
- [ ] README.md principal completo e atualizado
- [ ] README.md em cada projeto em `projects/`
- [ ] README.md em cada disciplina (data-mining/, machine-learning/, banco-dados/, estatistica/)
- [ ] README.md em `_archive/` explicando o conteúdo
- [ ] `data/README.md` explicando como obter dados (quando aplicável)

### Documentação de Projetos
- [ ] Cada projeto tem descrição clara
- [ ] Objetivos documentados
- [ ] Principais resultados documentados
- [ ] Como executar documentado
- [ ] Arquivos importantes listados
- [ ] Exemplos de uso documentados

### Contato
- [ ] Contato atualizado no README principal
- [ ] LinkedIn atualizado (ou "sob demanda")
- [ ] Email atualizado (ou "sob demanda")
- [ ] GitHub atualizado (ou "sob demanda")

---

## 💻 4. Código e Notebooks

### Notebooks
- [ ] Notebooks limpos (outputs removidos) ou versões `*_clean.ipynb`
- [ ] Seeds definidos para reprodutibilidade (`np.random.seed(42)`)
- [ ] Caminhos relativos (sem caminhos absolutos locais)
- [ ] Células de setup claramente separadas
- [ ] Seção "Resumo" com principais resultados
- [ ] Referência ao dataset (link ou instruções)
- [ ] Documentação em células markdown
- [ ] Execução completa: notebook roda do início ao fim sem erros
- [ ] Notebooks duplicados removidos ou consolidados

### Código Python
- [ ] Docstrings em funções Python (estilo NumPy)
- [ ] Type hints onde aplicável
- [ ] Funções pequenas e com responsabilidade única
- [ ] Tratamento de erros (try/except onde necessário)
- [ ] Logging em vez de print() (quando apropriado)
- [ ] Scripts executáveis do início ao fim

### Estrutura de Código
- [ ] Estrutura `src/` quando aplicável
- [ ] `__init__.py` em módulos Python
- [ ] Código organizado em módulos lógicos

---

## 📦 5. Dependências

### Requirements
- [ ] `requirements.txt` na raiz atualizado
- [ ] `requirements.txt` em cada projeto (quando necessário)
- [ ] Versões específicas de pacotes (usar `==` em vez de `>=`)
- [ ] Instruções de instalação claras no README

### Verificação
- [ ] Executado: `pip install -r requirements.txt` (sem erros)
- [ ] Dependências testadas em ambiente limpo

---

## 📊 6. Dados

### Datasets Grandes
- [ ] Datasets grandes (>10MB) no `.gitignore`
- [ ] `data/raw/` adicionado ao `.gitignore`
- [ ] `data/processed/` adicionado ao `.gitignore`
- [ ] `data/sample/` com amostras pequenas para testes (quando aplicável)

### Documentação de Dados
- [ ] `data/README.md` com links/instruções para obter dados
- [ ] Instruções claras de como baixar datasets
- [ ] Comandos wget/curl documentados (quando aplicável)
- [ ] Sem dados sensíveis versionados

### Verificação
- [ ] Executado: `find . -type f -size +10M` (verificar se há arquivos grandes)
- [ ] Arquivos grandes identificados e movidos para `.gitignore`

---

## 🎨 7. Visualizações

### Figuras
- [ ] Figuras salvas em `figures/` (não embutidas nos notebooks)
- [ ] Figuras principais documentadas
- [ ] Screenshots/plots para projetos em destaque
- [ ] Figuras com qualidade adequada (300 DPI quando necessário)

### Organização
- [ ] Pasta `figures/` criada nos projetos principais
- [ ] `figures/README.md` com descrição das figuras (opcional)

---

## 🏆 8. Projetos em Destaque

### Seleção
- [ ] 3-5 projetos selecionados e documentados
- [ ] Projetos em `projects/` organizados
- [ ] README específico para cada projeto em destaque
- [ ] Resultados mensuráveis documentados
- [ ] Links funcionando

### Documentação de Destaques
- [ ] Descrição clara de cada projeto
- [ ] Tecnologias utilizadas listadas
- [ ] Resultados principais destacados
- [ ] Impacto/motivação explicados
- [ ] Links para visualizações/artigos (quando aplicável)

---

## 🔄 9. Versionamento

### Commits
- [ ] Commits com mensagens descritivas
- [ ] Padrão de commits seguido (conventional commits)
- [ ] Histórico limpo e organizado

### Branches
- [ ] Branches organizadas (se aplicável)
- [ ] Branch principal (main/master) atualizada

### Tags (Opcional)
- [ ] Tags para releases (opcional)
- [ ] Versionamento semântico (opcional)

---

## 🤖 10. CI/CD (Opcional)

### GitHub Actions
- [ ] GitHub Actions configurado (`.github/workflows/ci.yml`)
- [ ] Lint passando (flake8, black)
- [ ] Testes passando (se houver)
- [ ] Workflow testado localmente

### Templates
- [ ] Template de Pull Request criado (`.github/pull_request_template.md`)
- [ ] Template de Issue criado (opcional)

---

## 📋 11. Checklist Específico por Projeto

Para cada projeto em `projects/`:

### Estrutura
- [ ] README.md completo
- [ ] requirements.txt (se necessário)
- [ ] .gitignore (se necessário)
- [ ] Estrutura de pastas padronizada (data/, notebooks/, src/, figures/)

### Notebooks
- [ ] Notebooks renomeados (01-*, 02-*, etc.)
- [ ] Notebooks limpos (outputs removidos)
- [ ] Seeds definidos
- [ ] Caminhos relativos
- [ ] Seção Resumo

### Código
- [ ] Docstrings em funções
- [ ] Scripts executáveis
- [ ] Tratamento de erros

### Dados
- [ ] data/README.md explicando como obter dados
- [ ] data/sample/ com amostras pequenas (quando aplicável)
- [ ] Dados grandes no .gitignore

---

## 🧪 12. Testes Finais

### Execução
- [ ] Todos os notebooks principais executados sem erros
- [ ] Scripts Python principais executados sem erros
- [ ] Dependências instaladas corretamente
- [ ] Exemplos de uso testados

### Verificação
- [ ] Links no README funcionando
- [ ] Imagens carregando corretamente
- [ ] Estrutura de pastas correta
- [ ] Sem erros de sintaxe

---

## 📊 13. Métricas e Resultados

### Documentação de Resultados
- [ ] Métricas principais documentadas
- [ ] Resultados quantitativos destacados
- [ ] Visualizações principais incluídas
- [ ] Comparações com baselines (quando aplicável)

---

## 🎯 14. Apresentação

### README Principal
- [ ] Introdução clara e profissional
- [ ] Projetos em destaque bem apresentados
- [ ] Tecnologias listadas
- [ ] Competências destacadas
- [ ] Instruções de uso claras

### Formatação
- [ ] Markdown bem formatado
- [ ] Badges atualizados
- [ ] Emojis usados com moderação
- [ ] Links funcionando

---

## ✅ 15. Verificação Final

### Antes de Publicar
- [ ] Todos os itens acima verificados
- [ ] Revisão final do README principal
- [ ] Revisão final dos READMEs dos projetos em destaque
- [ ] Teste de clonagem do repositório em ambiente limpo
- [ ] Verificação de que tudo funciona após clonar

### Comandos de Verificação Final
```bash
# Clonar em pasta temporária para testar
cd /tmp
git clone /home/vinicius/Projects/11111/ciencia_de_dados teste-portfolio
cd teste-portfolio

# Verificar estrutura
tree -L 2

# Verificar se requirements.txt funciona
pip install -r requirements.txt

# Verificar se há erros óbvios
find . -name "*.py" -exec python -m py_compile {} \;
```

---

## 📝 16. Próximos Passos Após Publicação

### Após Publicar no GitHub
- [ ] Adicionar descrição no repositório GitHub
- [ ] Adicionar tópicos (topics) no GitHub
- [ ] Adicionar link no LinkedIn
- [ ] Compartilhar em redes sociais (opcional)
- [ ] Atualizar currículo com link do portfólio

---

**Status:** ⬜ Não iniciado | 🟡 Em progresso | ✅ Completo

**Última atualização:** Janeiro 2025
