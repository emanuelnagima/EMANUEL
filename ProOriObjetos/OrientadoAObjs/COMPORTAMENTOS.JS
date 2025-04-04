class Pessoa { //Especificar todos os obejtos pessoas (Abstração)

    //ATRIBUTOS
    nome
    idade
    altura 
    peso
    sexo
    braço

//set e get

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
        console.log(`${this.nome}, VOCE AGORA PESA ${this.peso}`)
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


}

// Criar objetos do tipo Pessoa
 
//nossa variável
var p1 = new Pessoa()
p1.nome = 'Emanuel'
p1.idade = 21
p1.altura = 1.74
p1.sexo = 'Masculino'
p1.peso = 85.5
p1.braço = 5
p1.crescer(5);
// console.log(`o nome é ${p1.nome} e tem ${p1.idade} anos`)

p1.engordar(5)//parametros;

//--------------------------------------------------------------

var p2 = new Pessoa()
p2.nome = 'Mariana'
p2.idade = 16
p2.altura = 1.68
p2.sexo = 'Feminino'
p2.peso = 65
// console.log(`o nome é ${p2.nome} e tem ${p2.idade} anos`)
p2.falar();
p2.emagrecer(10);
p2.socar();
p2.fazerAniversário();