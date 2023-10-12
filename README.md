<pre align="center">
    Centro Federal de Educação Tecnológica de Minas Gerais <br>
    Curso Técnico Integrado em Informática
</pre>

# Monetização do 5G em Cenários Locais e Implementação de Microoperadoras

**Equipe:** ANDRADE DA SILVA, A. L; STORCK, C. R. (orientador); SANTOS DA CRUZ, L. V.; MARIANO, V. G. R.


Neste repositório encontram-se todos os arquivos gerados pelos componentes do grupo a fim de realizar o projeto de Trabalho de Conclusão de Curso (TCC) do Curso Técnico Integrado em Informática do Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG).

# Simulação

Como explicado na seção 2 do relatório final, o software utilizado para a realização da simulação foi o simaldor NS-3 equipado do módulo 5G-LENA.

Nesta seção, é tratada uma explicação das saídas da simulação do arquivo *cttc-nr-traffic-ngmn-mixed.cc*, que pode ser encontrado no repositório do CTTC *"3GPP NR ns-3 module"*.

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
            <td rowspan="2">SINR</td>
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
                    <p>NrUlRlcRxStats</p>
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

<div align="center">
    <h4>Legenda:</h4>
    <span><strong>-</strong> : não possui.</span>
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <span><strong>*</strong> : todos possuem.</span>
</div>
