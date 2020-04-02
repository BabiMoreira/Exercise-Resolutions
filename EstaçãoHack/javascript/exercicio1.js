
let user= prompt( "Digite seu Login");
let senha= prompt( "Digite sua Senha");
if( user=="joao" & senha=="aviao123"){
    alert("Seja Bem-Vindo " + user);
}
else{
    alert("Usuário e Senha Incorretos, T{ente Novamente");
}


while(condicao){
    // codigo a ser repetido, enquanto a condição ser verdadeira
}

let contador=0;
while(contador<5){
    console.log(contador);
    // contador=contador + 1; 
    contador++;
} 

//---------- EXEMPLO COM WHILE -----------//
let signos=['aries', 'gemeos', 'virgem']
console.log(signos);
let contador=0;
while( contador<12){
    console.log(signos[contador]);
    contador++;}

//-------- EXEMPLO COM FOR --------//
console.log("EXEMPLO COM FOR");
for(let cont=0; cont<signos.length; cont++){
    console.log(signos[cont]);
}

let idade= Number(prompt("Digite sua Idade"));
while(isNaN(idade)){
    alert( "Digite um número");
    let idade= Number(prompt("Digite sua Idade"));
}

for(let i in signos){
    console.log(signos[i]);
}

for( let signo of signos){
    console.log(signo)
}

let simbolo= prompt("qual material da escada");
let degrau= Number(prompt("Digite quantos degraus"));

let escada=simbolo;
for( let i=1; i <=degrau; i++)
{
    console.log(escada);
    escada+=simbolo;}