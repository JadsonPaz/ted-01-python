# TED 01 — Processamento e Análise de Dados de Chamados com Coleções em Python

**Disciplina:** Algoritmos e Programação Avançada  
**Data de Entrega:** 31/08/2026  

---

## 👥 Integrantes da Dupla
* **Jadson Paz Sales** — RA: `26.1.13308`
* **Victor Gabriel** — RA: `26.1.13209`

---

## 📌 Cenário Recebido
**Cenário:** Sistema de Atendimento e Suporte ao Cliente (*Helpdesk*)

O conjunto de dados contém registros brutos de chamados de suporte técnico, dúvidas, financeiro, cadastros e entregas de clientes. Cada registro traz informações referentes ao protocolo, nome do cliente, categoria da solicitação, atendente responsável, prioridade, status e o tempo de atendimento em minutos (`tempo_min`).

---

## 💡 Descrição Resumida da Solução
A solução foi desenvolvida inteiramente com recursos e coleções nativas do Python, sem o auxílio de bibliotecas externas (como Pandas). O programa carrega os dados brutos de um arquivo CSV, higieniza os registros eliminando duplicatas por protocolo e executa três análises estratégicas para tomada de decisão no atendimento ao cliente.

---

## 🛠️ Estruturas de Dados Utilizadas

1. **Tuplas (`tuple`):** Utilizadas para modelar a estrutura fixa e imutável de cada chamado lido do arquivo `(protocolo, cliente, categoria, atendente, prioridade, status, tempo_min)`.
2. **Listas (`list`):** Utilizadas para armazenar a coleção de todos os chamados processados e os tempos de atendimento por funcionário.
3. **Conjuntos (`set`):** Utilizados para:
   - Controlar e remover chamados duplicados com base no número de protocolo;
   - Realizar operações matemáticas de teoria dos conjuntos (**interseção `&`**, **diferença `-`** e **união `|`**) no cruzamento de clientes entre diferentes categorias.
4. **Dicionários (`dict`):** Utilizados para mapear e agrupar contagens de categorias e o desempenho individual (volume e tempo médio) de cada atendente.
5. **Estruturas Aninhadas:** Combinação de lista de tuplas (`list[tuple]`) e dicionários contendo tuplas e listas como valores (`dict[str, tuple]`).

---

## ⚡ Recursos Avançados do Python

* **List Comprehension:**
  - Extração da lista de categorias a partir dos registros de chamados;
  - Filtragem e seleção de clientes associados a uma determinada categoria.
* **Dict Comprehension:**
  - Mapeamento e contagem de ocorrências para cada categoria única;
  - Cálculo consolidado do volume e tempo médio de atendimento agrupado por atendente.

---

## 📊 Principais Análises Realizadas

1. **Volume por Categoria de Chamado:** Identificação das categorias mais demandadas pelos clientes (ex: Reclamação, Cadastro, Técnico) para direcionar o treinamento da equipe.
2. **Desempenho dos Atendentes:** Avaliação da quantidade de chamados resolvidos/atendidos por cada funcionário e o seu tempo médio de atendimento em minutos.
3. **Análise de Sobreposição de Clientes (Operações de Conjunto):** Identificação de clientes que acionaram o suporte em múltiplas áreas (ex: *Técnico* e *Financeiro*) através da interseção, diferença e união de conjuntos.

---

## 🚀 Instruções para Executar o Programa

### Pré-requisitos
* Python 3.10 ou superior instalado.

### Passos de Execução
1. Clone este repositório para o seu ambiente local:
   ```bash
   git clone [https://github.com/JadsonPaz/ted-01-python.git](https://github.com/JadsonPaz/ted-01-python.git)
