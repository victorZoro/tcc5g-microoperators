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
        <th colspan="4">Dados para cada arquivo</th>
        <tr>
            <th>Dado</th>
            <th>Unidade</th>
            <th colspan="2">Arquivos</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>SINR</td>
            <td>dB</td>
            <td colspan="2">
                <p>DlCtrlSinr</p>
                <p>DlDataSinr</p>
                <p>RxPacketTrace</p>
            </td>
        </tr>
        <tr>
            <td>pathLoss</td>
            <td>dB</td>
            <td colspan="2">
                <p>UlPathlossTrace</p>
                <p>DlPathlossTrace</p>
            </td>
        </tr>
        <tr>
            <td>time</td>
            <td>seconds</td>
            <td colspan="2">
                <p class="bold">*</p>
            </td>
        </tr>
        <tr rowspan="2">
            <td rowspan="2">packetSize</td>
            <td rowspan="2">bytes</td>
            <td class="bold">PDCP</th>
            <td class="bold">RLC</th>
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
            </tr>
        </tr>
    </tbody>
</table>

<!-- <table align="center">
    <tr>
        <th colspan="3">Dados para cada arquivo</th>
    </tr>
    <tr class="header">
        <td>Dado</td>
        <td>Unidade</td>
        <td>Arquivos</td>
    </tr>
    <tr>
        <td>SINR</td>
        <td>dB</td>
        <td>DlCtrlSinr; DlDataSinr; RxPacketTrace</td>
    </tr>
    <tr>
        <td>pathloss</td>
        <td>dB</td>
        <td>UlPathlossTrace; DlPathlossTrace</td>
    </tr>
    <tr>
        <td>time</td>
        <td>seconds</td>
        <td>*</td>
    </tr>
        <tr>
        <td>packetSize</td>
        <td>bytes</td>
        <td>NrDlPdcpRxStats; NrDlPdcpTxStats; NrUlPdcpRxStats; NrUlPdcpTxStats;</td>
    </tr>
</table> -->
