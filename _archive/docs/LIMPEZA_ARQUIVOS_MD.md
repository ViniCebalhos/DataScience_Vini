# 🧹 Limpeza de Arquivos .md - Recomendações

**Data:** Janeiro 2025  
**Objetivo:** Identificar quais arquivos .md manter, mover ou apagar antes de publicar

---

## ✅ MANTER NA RAIZ (Documentação Pública do Portfólio)

Estes arquivos são úteis para visitantes do portfólio:

1. **README.md** ✅
   - README principal do portfólio
   - **Ação:** MANTER

---

## 📁 MOVER PARA `_archive/docs/` (Documentos Internos de Trabalho)

Estes documentos são úteis para referência, mas não precisam estar na raiz:

1. **ANALISE_CRITICA_COMPLETA.md** 📦
   - Análise interna completa
   - **Ação:** `git mv ANALISE_CRITICA_COMPLETA.md _archive/docs/`

2. **ANALISE_E_REESTRUTURACAO.md** 📦
   - Análise e reestruturação (pode ser duplicado do anterior)
   - **Ação:** `git mv ANALISE_E_REESTRUTURACAO.md _archive/docs/`

3. **COMANDOS_REORGANIZACAO.md** 📦
   - Comandos já executados (útil para referência)
   - **Ação:** `git mv COMANDOS_REORGANIZACAO.md _archive/docs/`

4. **CHECKLIST_FINAL_PUBLICACAO.md** 📦
   - Checklist interno (útil, mas não precisa estar na raiz)
   - **Ação:** `git mv CHECKLIST_FINAL_PUBLICACAO.md _archive/docs/`

5. **RESUMO_EXECUTIVO.md** 📦
   - Resumo executivo interno
   - **Ação:** `git mv RESUMO_EXECUTIVO.md _archive/docs/`

6. **RESUMO_EXECUTIVO_REVISAO.md** 📦
   - Resumo executivo da revisão (pode ser duplicado)
   - **Ação:** `git mv RESUMO_EXECUTIVO_REVISAO.md _archive/docs/`

7. **RESUMO_LIMPEZA_DOCUMENTACAO.md** 📦
   - Resumo interno de limpeza
   - **Ação:** `git mv RESUMO_LIMPEZA_DOCUMENTACAO.md _archive/docs/`

8. **RESUMO_REORGANIZACAO_COMPLETA.md** 📦
   - Resumo interno de reorganização
   - **Ação:** `git mv RESUMO_REORGANIZACAO_COMPLETA.md _archive/docs/`

9. **INDICE_DOCUMENTACAO.md** 📦
   - Índice interno de documentação
   - **Ação:** `git mv INDICE_DOCUMENTACAO.md _archive/docs/`

10. **TEXTOS_LINKEDIN_PORTFOLIO.md** 📦
    - Textos para uso pessoal (LinkedIn, etc.)
    - **Ação:** `git mv TEXTOS_LINKEDIN_PORTFOLIO.md _archive/docs/`

11. **ENTREGAVEIS_REVISAO.md** 📦
    - Lista de entregáveis (resumo interno)
    - **Ação:** `git mv ENTREGAVEIS_REVISAO.md _archive/docs/`

12. **LIMPEZA_ARQUIVOS_MD.md** 📦 (este arquivo)
    - Este documento de limpeza
    - **Ação:** `git mv LIMPEZA_ARQUIVOS_MD.md _archive/docs/` (após executar)

---

## 🗑️ VERIFICAR E POSSIVELMENTE REMOVER (Duplicados)

Estes podem ser duplicados ou consolidados:

1. **ANALISE_E_REESTRUTURACAO.md** vs **ANALISE_CRITICA_COMPLETA.md**
   - Verificar se são duplicados
   - Se sim, manter apenas o mais completo
   - **Ação:** Comparar e remover duplicado

2. **RESUMO_EXECUTIVO.md** vs **RESUMO_EXECUTIVO_REVISAO.md**
   - Verificar se são duplicados
   - Se sim, manter apenas o mais recente
   - **Ação:** Comparar e remover duplicado

---

## 📋 READMEs em Subpastas (MANTER TODOS)

Estes são necessários para documentação dos projetos:

- ✅ Todos os READMEs em `projects/`
- ✅ Todos os READMEs em `banco-dados/`
- ✅ Todos os READMEs em `data-mining/`
- ✅ Todos os READMEs em `machine-learning/`
- ✅ `estatistica/README.md`
- ✅ `_archive/README.md`

**Ação:** MANTER TODOS

---

## 🚀 COMANDOS PARA EXECUTAR

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Mover documentos internos para _archive/docs/
git mv ANALISE_CRITICA_COMPLETA.md _archive/docs/
git mv ANALISE_E_REESTRUTURACAO.md _archive/docs/
git mv COMANDOS_REORGANIZACAO.md _archive/docs/
git mv CHECKLIST_FINAL_PUBLICACAO.md _archive/docs/
git mv RESUMO_EXECUTIVO.md _archive/docs/
git mv RESUMO_EXECUTIVO_REVISAO.md _archive/docs/
git mv RESUMO_LIMPEZA_DOCUMENTACAO.md _archive/docs/
git mv RESUMO_REORGANIZACAO_COMPLETA.md _archive/docs/
git mv INDICE_DOCUMENTACAO.md _archive/docs/
git mv TEXTOS_LINKEDIN_PORTFOLIO.md _archive/docs/
git mv ENTREGAVEIS_REVISAO.md _archive/docs/

# Verificar duplicados antes de remover
# Comparar ANALISE_E_REESTRUTURACAO.md e ANALISE_CRITICA_COMPLETA.md
# Comparar RESUMO_EXECUTIVO.md e RESUMO_EXECUTIVO_REVISAO.md

# Se houver duplicados, remover o menos completo:
# git rm _archive/docs/ANALISE_E_REESTRUTURACAO.md  # se duplicado
# git rm _archive/docs/RESUMO_EXECUTIVO.md  # se duplicado

# Mover este arquivo também (após executar)
git mv LIMPEZA_ARQUIVOS_MD.md _archive/docs/

# Commit
git commit -m "docs(organizacao): mover documentos internos para _archive/docs/

- Mover análises e resumos internos para _archive/docs/
- Manter apenas README.md na raiz para portfólio público
- Documentos de referência disponíveis em _archive/docs/"
```

---

## ✅ RESULTADO ESPERADO

Após executar os comandos, a raiz terá apenas:

```
ciencia_de_dados/
├── README.md                    # ✅ Único .md na raiz (público)
├── requirements.txt
├── .gitignore
└── ... (pastas de projetos)
```

Todos os documentos internos estarão em:
```
_archive/docs/
├── ANALISE_CRITICA_COMPLETA.md
├── COMANDOS_REORGANIZACAO.md
├── CHECKLIST_FINAL_PUBLICACAO.md
├── RESUMO_EXECUTIVO_REVISAO.md
├── TEXTOS_LINKEDIN_PORTFOLIO.md
└── ... (outros documentos internos)
```

---

## 📊 Resumo

- **Manter na raiz:** 1 arquivo (README.md)
- **Mover para _archive/docs/:** 11-12 arquivos
- **Verificar duplicados:** 2 pares de arquivos
- **Total de arquivos .md na raiz após limpeza:** 1

---

**Última atualização:** Janeiro 2025

