class Pessoa { //Especificar todos os obejtos pessoas (Abstração)

    //ATRIBUTOS
    nome
    idade
    altura 
    peso
    sexo
    braço

//set e get 
//SET COLOCA, GET PEGA
//SET DADOS DOS ATRIBUTOS
    setNome(novoNome){
        this.nome=novoNome
    }
    getNome(){
        return this.nome
    }

    setIdade(novaIdade){
        this.idade= novaIdade
    }

    getIdade(){
        return this.idade
    }

    setPeso(novoPeso){
    this.peso=novoPeso
    }

    setSexo(novoSexo){
        if(novoSexo=='feminino'|| novoSexo=='masculino')
            this.sexo=novoSexo
        else{
            this.sexo='não identificado'
        }
    }

//COMPORTAMENTOS - FUNÇÕES
    falar(){//ação
        console.log(`OLÁ!!!!!!!!!! eu sou a ${this.nome} e tenho ${this.idade} anos`)
    }

    fazerAniversário(){
        this.idade++ //++1
        console.log(`${this.nome}: PARABENS, FELIZ ANIVERSÁRIO ${this.nome}!!!! Voçê agora tem ${this.idade} anos!!!`)
    }


    engordar(quilos){ //ação, com parametros
        this.peso=this.peso+quilos
        console.log(`${this.nome}, VOCE AGORA PESA ${this.peso}kg`)
    }

    emagrecer(quilos){
        this.peso= this.peso-quilos
        console.log(`${this.nome} vc emagreceu ein, está com ${this.peso} kg`)

}

    crescer(aumentou){
        this.braço+=aumentou
        console.log(`${this.nome}, seu braço aumentou ${this.braço}cm`)
    }

    socar(){
        console.log(`${this.nome}: VOU SOCAR VOCE`)
    }

    falar2(){
        console.log(`Olá, sou do sexo ${this.sexo}`)
    }
}

// Criar objetos do tipo Pessoa
 
//nossa variável
let p1 = new Pessoa
p1.setNome('emanuel')
p1.setIdade(21)
p1.setPeso(85)
p1.setSexo('gay')
p1.fazerAniversário(5)
p1.engordar(5)

p1.falar2();

console.log(`Olá eu sou o ${p1.getNome()}, e tenho ${p1.getIdade()} anos de idade`)