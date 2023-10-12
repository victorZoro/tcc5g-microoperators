<pre align="center">
    Centro Federal de Educação Tecnológica de Minas Gerais <br>
    Curso Técnico Integrado em Informática
</pre>

# Monetização do 5G em Cenários Locais e Implementação de Microoperadoras

**Equipe:** ANDRADE DA SILVA, A. L; STORCK, C. R. (orientador); SANTOS DA CRUZ, L. V.; MARIANO, V. G. R.

Neste repositório encontram-se todos os arquivos gerados pelos componentes do grupo a fim de realizar o projeto de Trabalho de Conclusão de Curso (TCC) do Curso Técnico Integrado em Informática do Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG).

# Índice

- [Simulação](#simulação)
- [Tabela de Informações](#tabela-de-informações)
- [Diagrama de Classes](#diagrama-de-classes)

# Simulação

Como explicado na seção 2 do relatório final, o software utilizado para a realização da simulação foi o simaldor NS-3 equipado do módulo 5G-LENA.

Nesta seção, é tratada uma explicação das saídas da simulação do arquivo *cttc-nr-traffic-ngmn-mixed.cc*, que pode ser encontrado no repositório do CTTC *"3GPP NR ns-3 module"*, além do diagrama de classes.

## Tabela de Informações

A tabela abaixo lista a maior parte das informações coletadas das simulações feitas pela equipe. Algumas informações, como as saídas da camada PHY e MAC não estão presentes, pois, por motivos explicados na seção 2 do relatório final, essas informações não são relevantes para a pesquisa.

<link rel="stylesheet" href="style.css">


<table align="center">
    <thead>
        <th colspan="5">Dados para cada arquivo</th>
        <tr>
            <th>Dado</th>
            <th>Unidade</th>
            <th colspan="3">Arquivos</th>
        </tr>
    </thead>
    <tbody>
        <tr rowspan="2">
            <td rowspan="2">SINR</td>
            <td rowspan="2">dB</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>-</td>
                <td>-</td>
                <td>
                    <p>DlCtrlSinr</p>
                    <p>DlDataSinr</p>
                    <p>RxPacketTrace</p>
                </td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">pathLoss</td>
            <td rowspan="2">dB</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>-</td>
                <td>-</td>
                <td>
                    <p>UlPathlossTrace</p>
                    <p>DlPathlossTrace</p>
                </td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">time</td>
            <td rowspan="2">seconds</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>*</td>
                <td>*</td>
                <td>*</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">packetSize</td>
            <td rowspan="2">bytes</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>
                    <p>NrDlPdcpRxStats</p>
                    <p>NrDlPdcpTxStats</p>
                    <p>NrUlPdcpRxStats</p>
                    <p>NrUlPdcpTxStats</p>
                </td>
                <td>
                    <p>NrDlRlcRxStats</p>
                    <p>NrDlRlcTxStats</p>
                    <p>NrUlRlcRxStats</p>
                    <p>NrUlRlcTxStats</p>
                </td>
                <td>-</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">delay</td>
            <td rowspan="2">seconds</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>
                    <p>NrDlPdcpStatsE2E</p>
                    <p>NrDlPdcpRxStats</p>
                    <p>NrUlPdcpStatsE2E</p>
                    <p>NrUlPdcpRxStats</p>
                </td>
                <td>
                    <p>NrDlRlcStatsE2E</p>
                    <p>NrDlRxRlcStats</p>
                    <p>NrUlRlcStatsE2E</p>
                    <p>NrUlRlcRxStats</p>
                </td>
                <td>-</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">TxBytes</td>
            <td rowspan="2">bytes</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>
                    <p>NrDlPdcpStatsE2E</p>
                    <p>NrUlPdcpStatsE2E</p>
                </td>
                <td>
                    <p>NrDlRlcStatsE2E</p>
                    <p>NrUlRlcRxStats</p>
                </td>
                <td>-</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">RxBytes</td>
            <td rowspan="2">bytes</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>
                    <p>NrDlPdcpStatsE2E</p>
                    <p>NrUlPdcpStatsE2E</p>
                </td>
                <td>
                    <p>NrDlRlcStatsE2E</p>
                    <p>NrUlRlcStatsE2E</p>
                </td>
                <td>-</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">direction</td>
            <td rowspan="2">UL/DL</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>-</td>
                <td>-</td>
                <td>RxPacketTrace</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">CQI</td>
            <td rowspan="2">?</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>-</td>
                <td>-</td>
                <td>RxPacketTrace</td>
            </tr>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">corrupt</td>
            <td rowspan="2">?</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
            <td class="bold">Others</th>
            <tr>
                <td>-</td>
                <td>-</td>
                <td>RxPacketTrace</td>
            </tr>
        </tr>
    </tbody>
</table>

<div style="display: flex; width: 100%; justify-content: center; gap: 50px;">
    <p class="bold">Legenda:</p>
    <span><strong>-</strong> &nbsp : não possui.</span>
    <span><strong>*</strong> &nbsp : todos possuem.</span>
</div>

<div style="display: flex; width: 100%; justify-content: right; font-size: 18px">
    <a href="#" style="display:flex; align-items: center; margin: 50px 0;">
        <span>☝️ Retornar ao topo.</span>
    </a>
</div>


## Diagrama de Classes

O diagrama de classes abaixo representa a forma com que o programa que faz a leitura dos arquivos e transforma as informações em gráficos foi desenvolvido. O programa será desenvolvido na linguagem de programação Python utilizando as bibliotecas Pandas e Matplotlib, como explicado nas seções 2 e 3 do relatório final.

<div align="center">


```mermaid
---
title: Class diagram for 5G-LENA results.
---

classDiagram

  direction TB

  note for Dataset "linkType stands for uplink ('UL') or downlink ('DL')."

  class Dataset {
    <<abstract>>
    # dataset: DataFrame
    + time: Series
    + linkType: str
    + __init__(self, filename: str)
  }

  class PathLoss {
    + pathLoss: Series
    + __init__(self, filename: str)
  }

  class SINR {
    <<abstract>>
    + SINR: Series
    + __init__(self, filename: str)
  }

  class RxPacketTrace {
    + direction: Series
    + CQI: Series
    + corrupt: Series
    + __init__(self, filename: str)
  }

  class Ctrl {
    + __init__(self)
  }

  class Data {
    + __init__(self)
  }

  class FilePaths {
    <<abstract>>
    - _files: list
    + get_files(self) -> list
  }

  class DataAccess {
    + ctrl: Ctrl
    + data: Data
    + pathLoss: PathLoss
    + rxPacketTrace: RxPacketTrace
    + pdcp: dict
    + rlc: dict
    + __init__(self, files: list)
    + importAllPdcp(self, files: list)
    + importAllRlc(self, files: list)
  }

  class E2EBytes {
    <<abstract>>
    + txBytes: Series
    + rxBytes: Series
    + __init__(self, filename: str)
  }

  class NrLayer {
    <<abstract>>
    + packetSize: Series
    + delay: Series
    + __init__(self, filename: str)
  }

  class PDCP {
    + __init__(self)
  }

  class RLC {
    + __init__(self)
  }

  %% Inheritance
  Dataset <|-- SINR
  Dataset <|-- E2EBytes
  Dataset <|-- PathLoss
  SINR <|-- Ctrl
  SINR <|-- Data
  SINR <|-- RxPacketTrace
  NrLayer <|-- PDCP
  NrLayer <|-- RLC
  E2EBytes <|-- NrLayer

  %% Aggregation
  Ctrl --o DataAccess
  Data --o DataAccess
  RxPacketTrace --o DataAccess
  PathLoss --o DataAccess
  PDCP --o DataAccess
  RLC --o DataAccess

  %% Association
  DataAccess -- FilePaths


```

</div>

<div style="display: flex; width: 100%; justify-content: right; font-size: 18px">
    <a href="#" style="display:flex; align-items: center; margin: 50px 0;">
        <span>☝️ Retornar ao topo.</span>
    </a>
</div>
