# Descrição do Dataset: Sistema E-Saúde - Perfil de Atendimento Outros Profissionais de Nível Superior

## Objetivo do Dataset

Este dataset contém informações sobre atendimentos realizados por profissionais de nível superior (exceto médicos) nas unidades municipais de saúde de Curitiba, através do Sistema E-Saúde. O objetivo é registrar e monitorar o perfil de atendimentos, procedimentos realizados, características dos pacientes e condições socioeconômicas, visando a gestão e melhoria dos serviços de saúde pública.

## Cobertura dos Dados

- **Período**: Dezembro de 2024 a Julho de 2025 (8 meses de dados)
- **Localização**: Município de Curitiba, Paraná
- **Volume**: Aproximadamente 46.000 registros por mês
- **Fonte**: Sistema E-Saúde da Prefeitura Municipal de Curitiba

## Estrutura das Colunas

### Informações Temporais
- **Data do Atendimento**: Data e hora de realização do atendimento
- **Data de Nascimento**: Data de nascimento do paciente

### Informações Demográficas
- **Sexo**: Sexo do paciente (F/M)
- **Nacionalidade**: Brasileira, Naturalizado, Estrangeiro ou Não informado
- **Município**: Município do paciente
- **Bairro**: Bairro do paciente

### Informações da Unidade de Saúde
- **Código do Tipo de Unidade**: Código identificador do tipo de unidade
- **Tipo de Unidade**: BASICO, SIACE, etc.
- **Código da Unidade**: Código único da unidade de atendimento
- **Descrição da Unidade**: Nome da unidade de saúde

### Informações Profissionais
- **Código do CBO**: Código da Classificação Brasileira de Ocupações
- **Descrição do CBO**: Descrição da ocupação do profissional (ex: Fisioterapeuta, Psicólogo, Nutricionista)
- **Código do Profissional**: Código único do profissional

### Informações do Atendimento
- **Código do Procedimento**: Código do procedimento realizado
- **Descrição do Procedimento**: Descrição detalhada do procedimento
- **Código do CID**: Código do diagnóstico (Classificação Internacional de Doenças)
- **Descrição do CID**: Descrição do diagnóstico
- **Solicitação de Exames**: Indica se houve solicitação de exames (Sim/Não)
- **Encaminhamento para Atendimento Especialista**: Indica se houve encaminhamento (Sim/Não)
- **Área de Atuação**: Área específica de atuação do profissional

### Informações Farmacêuticas
- **Qtde Prescrita Farmácia Curitibana**: Quantidade de medicamentos prescritos
- **Qtde Dispensada Farmácia Curitibana**: Quantidade de medicamentos dispensados
- **Qtde de Medicamento Não Padronizado**: Quantidade de medicamentos não padronizados

### Informações de Internamento
- **Desencadeou Internamento**: Indica se o atendimento desencadeou internamento
- **Data do Internamento**: Data do internamento (se aplicável)
- **Estabelecimento Solicitante**: Estabelecimento que solicitou o internamento
- **Estabelecimento Destino**: Estabelecimento onde ocorreu o internamento
- **CID do Internamento**: Código do diagnóstico do internamento

### Condições Socioeconômicas e Habitacionais
- **Tratamento no Domicílio**: Tipo de tratamento de água no domicílio
- **Abastecimento**: Tipo de abastecimento de água
- **Energia Elétrica**: Indica se há energia elétrica no domicílio
- **Tipo de Habitação**: Tipo de construção da habitação
- **Destino Lixo**: Como o lixo é descartado
- **Fezes/Urina**: Destino das fezes/urina
- **Cômodos**: Quantidade de cômodos no domicílio
- **Em Caso de Doença**: Serviços procurados em caso de doença
- **Grupo Comunitário**: Participação em grupos comunitários
- **Meio de Comunicação**: Meios de comunicação utilizados
- **Meio de Transporte**: Meios de transporte utilizados

### Informações do Usuário
- **cod_usuario**: Código único do usuário
- **origem_usuario**: 1 - Residente no município, 2 - Não residente
- **residente**: 1 - Com cadastro definitivo na UBS, 2 - Sem cadastro definitivo

## Características Especiais

1. **Profissionais Abrangidos**: Inclui fisioterapeutas, psicólogos, nutricionistas, educadores físicos e outros profissionais de nível superior, exceto médicos.

2. **Tipos de Unidades**: 
   - BASICO: Unidades básicas de saúde
   - SIACE: Centros de especialidades médicas

3. **Atenção Primária e Especializada**: O dataset cobre tanto atendimentos na atenção primária quanto na especializada.

4. **Dados Socioeconômicos**: Inclui informações detalhadas sobre condições habitacionais e socioeconômicas dos pacientes.

5. **Rastreabilidade**: Permite acompanhar o fluxo do paciente desde o atendimento inicial até possíveis encaminhamentos e internamentos.

## Potencial de Análise

Este dataset permite análises em diversas áreas:
- Perfil epidemiológico dos atendimentos
- Distribuição geográfica dos serviços
- Análise de eficiência dos diferentes tipos de unidades
- Caracterização socioeconômica dos usuários
- Padrões de encaminhamento e especialização
- Análise temporal dos atendimentos
- Perfil dos profissionais e suas áreas de atuação 