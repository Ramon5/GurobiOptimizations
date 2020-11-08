## Pesquisa Operacional

### Resolução de problemas

### Requisitos:

1 - SO: Unix Like \
2 - Python3 ou superior \
3 - pip \
4 - virtualenv ou virtualenvwrapper \
5 - gurobi: https://www.gurobi.com/downloads/gurobi-software/

### Instruções de utilização

Com o gurobi devidamente instalado e configurado, clone o projeto: \
`git clone git@github.com:Ramon5/GurobiOptimizations.git`
ou
`git clone https://github.com/Ramon5/GurobiOptimizations.git`

navegue até a pasta do projeto:

$ virtualenv -p python3 env

o comando acima criará o ambiente virtual dentro do projeto.

### Execução

No terminal:

$ make run
<br><br>
### Problemas que serão solucionados
<br>
1. Um sapateiro faz 6 sapatos por hora, se fizer somente sapatos, e 5 cintos por hora, se fizer
somente cintos. Ele gasta 2 unidades de couro para fabricar 1 unidade de sapato e 1 unidade
couro para fabricar uma unidade de cinto. Sabendo-se que o total disponível de couro é de 6
unidades e que o lucro unitário por sapato é de 5 unidades monetárias e o do cinto é de 2
unidades monetárias, pede-se: o modelo do sistema de produção do sapateiro, se o objetivo é
maximizar seu lucro por hora.
<br><br>
2. Certa empresa fabrica 2 produtos P1 e P2. O lucro por unidade de P1 é de 100 u.m. e o lucro
unitário de P2 é de 150 u.m. A empresa necessita de 2 horas para fabricar uma unidade de P1
e 3 horas para fabricar uma unidade de P2. O tempo mensal disponível para essas atividades é
de 120 horas. As demandas esperadas para os 2 produtos levaram a empresa a decidir que os
montantes produzidos de P1 e P2 não devem ultrapassar 40 unidades de P1 e 30 unidades de
P2 por mês. Construa o modelo do sistema de produção mensal com o objetivo de maximizar o
lucro da empresa.
<br><br>
3. Uma rede de televisão local tem o seguinte problema: foi descoberto que o programa “A"
com 20 minutos de música e 1 minuto de propaganda chama a atenção de 30.000
telespectadores, enquanto o programa "B", com 10 minutos de música e 1 minuto de
propaganda chama a atenção de 10.000 telespectadores. No decorrer de uma semana, o
patrocinador insiste no uso de no mínimo, 5 minutos para sua propaganda e que não há verba
para mais de 80 minutos de música. Quantas vezes por semana cada programa deve ser levado
ao ar para obter o número máximo de telespectadores? Construa o modelo do sistema.
<br><br>
4. Um empresa fabrica 2 modelos de cintos de couro. O modelo M1, de melhor qualidade,
requer o dobro do tempo de fabricação em relação ao modelo M2. Se todos os cintos fossem
do modelo M2, a empresa poderia produzir 1.000 unidades por dia. A disponibilidade de couro
permite fabricar 800 cintos de ambos os modelos por dia. Os cintos empregam fivelas
diferentes, cuja disponibilidade diária é de 400 para M1 e 700 para M2. Os lucros unitários são

de $ 4,00 para M1 e $ 3,00 para M2. Qual o programa ótimo de produção que maximiza o
lucro total diário da empresa? Construa o modelo do sistema descrito.
<br><br>
5. Uma empresa, após um processo de racionalização de produção, ficou com disponibilidade
de 3 recursos produtivos, R1, R2 e R3. Um estudo sobre o uso desses recursos indicou a
possibilidade de se fabricar 2 produtos P1 e P2. Levantando os custos e consultando o
departamento de vendas sobre o preço de colocação no mercado, verificou-se que P1 daria
um lucro de $ 120,00 por unidade e P2, $ 150,00 por unidade. O departamento de produção
forneceu a seguinte tabela de uso de recursos.

| Produtos                            	| Recursos R1 por UN. 	| Recursos R2 por UN. 	| Recursos R3 por UN. 	|
|-------------------------------------	|---------------------	|---------------------	|---------------------	|
| P1<br>P2                               	| 2<br>4                 	| 3<br>2                 	| 5<br>3                 	|
| Disponibilidade de recursos por mês 	| 100                 	| 90                  	| 120                 	|
<br>
Que produção mensal de P1 e P2 traz o maior lucro para a empresa? Construa o modelo do
sistema.





