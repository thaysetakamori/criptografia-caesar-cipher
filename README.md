## Objetivo
Implementar uma função que realize a criptografia de uma string usando a Cifra de César, que é um tipo de criptografia por substituição. Isso significa que cada letra do texto é substituída por outra, que aparece um certo número de posições (chamado de deslocamento) à frente no alfabeto.
- O parâmetro str representa a string a ser criptografada.
- O parâmetro num representa o número de posições que cada letra será deslocada no alfabeto.<br><br>

**Regras adicionais:**  
- Qualquer coisa que não seja uma letra (como espaços, números ou pontuação) não deve ser alterada.
- Se a string for "Caesar Cipher" e o número for 2, o resultado esperado seria "Ecguct Ekrjgt".<br><br>

## Como resolver o desafio
**Entender o funcionamento da Cifra de César:**
- Cada letra no texto é deslocada um número fixo de posições no alfabeto.
- Exemplo: com deslocamento de 2, 'A' vira 'C', 'B' vira 'D', e assim por diante.
- Ao chegar ao final do alfabeto (como de 'Z' para 'A'), ele deve "circular" para o início.<br><br>

**Distinguir maiúsculas e minúsculas:**
- As letras maiúsculas e minúsculas têm posições diferentes na tabela ASCII (onde cada caractere tem um código numérico associado), então é preciso tratar isso separadamente.