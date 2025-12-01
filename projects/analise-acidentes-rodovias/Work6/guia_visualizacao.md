# Guia de Visualização Padronizada - Artigo SBC

## 🎨 Tema Visual Unificado

Todos os gráficos foram criados com um **tema visual padronizado** para garantir consistência e profissionalismo:

### 🎯 Paleta de Cores
- **Cor Principal**: `#2E86AB` (Azul profissional)
- **Cor de Destaque**: `#A23B72` (Rosa para elementos importantes)
- **Cor Secundária**: `#F18F01` (Laranja para linhas de referência)
- **Cor de Fundo**: `#F8F9FA` (Cinza claro)

### 📊 Características dos Gráficos

#### **Gráfico 1: Acidentes por Mês**
- **Tipo**: Gráfico de barras verticais
- **Cor base**: Azul principal (#2E86AB)
- **Destaques**: Rosa (#A23B72) para Jul, Out, Dez
- **Elementos**: Linha de média em laranja, valores formatados com separadores de milhares
- **Estilo**: Bordas brancas, transparência 0.8

#### **Gráfico 2: Causas de Acidentes**
- **Tipo**: Gráfico de barras horizontais
- **Cor base**: Azul principal (#2E86AB)
- **Destaques**: Rosa (#A23B72) para as 3 principais causas
- **Elementos**: Valores formatados com separadores de milhares
- **Estilo**: Bordas brancas, transparência 0.8

#### **Gráfico 3: Acidentes por Hora**
- **Tipo**: Gráfico de linha com marcadores
- **Cor da linha**: Azul principal (#2E86AB)
- **Marcadores**: Rosa (#A23B72) com bordas brancas
- **Destaque**: Área sombreada rosa para período de pico (17h-19h)
- **Elementos**: Anotações com caixas de texto para valores de pico

### 🔧 Configurações Técnicas

#### **Estilo Global**
- **Fonte**: DejaVu Sans (compatível com português)
- **Tema**: seaborn-v0_8-whitegrid
- **Resolução**: 300 DPI (alta qualidade)
- **Formato**: PNG com fundo branco

#### **Elementos Visuais**
- **Títulos**: Fonte bold, cor escura (#2C3E50)
- **Eixos**: Linhas cinza claro, rótulos em negrito
- **Grid**: Transparência 0.3, cor cinza claro
- **Legendas**: Fundo semi-transparente, posicionamento otimizado

#### **Formatação de Números**
- **Separadores de milhares**: Vírgulas (ex: 6,587)
- **Decimais**: Apropriados para cada contexto
- **Posicionamento**: Otimizado para legibilidade

### 📐 Dimensões Padronizadas

- **Gráfico de Barras (Mês)**: 12x6 polegadas
- **Gráfico de Barras (Causas)**: 12x8 polegadas  
- **Gráfico de Linha (Hora)**: 14x6 polegadas

### 🎯 Benefícios do Tema Padronizado

1. **Consistência Visual**: Todos os gráficos seguem o mesmo padrão
2. **Profissionalismo**: Cores e estilos adequados para publicação acadêmica
3. **Legibilidade**: Contraste e formatação otimizados
4. **Acessibilidade**: Cores que funcionam bem em impressão e tela
5. **Branding**: Identidade visual coesa para o artigo

### 📝 Como Usar

Os gráficos estão prontos para inclusão no artigo SBC. Cada um possui:
- **Alta resolução** (300 DPI) para impressão
- **Fundo branco** para compatibilidade com documentos
- **Formatação consistente** de títulos e rótulos
- **Destaques visuais** para elementos importantes

### 🔄 Reproduzibilidade

Para gerar novos gráficos com o mesmo tema, execute:
```bash
python anexos.py
```

O script automaticamente aplicará todas as configurações de estilo padronizadas.








