class Homem {
    nome
    peso
    idade

    setIdade(novaIdade){
        this.idade=novaIdade;
        if (this.idade >= 20) {
            console.log(`VC É VELHO`);
        } else {
            console.log(`VOCE É JOVEM`);
        }
        
    }
    getIdade(){
        return this.idade
    }

 setNome2(novoNome){
    this.nome=novoNome
}
    getNome2(){
        return this.nome
    }

    setNome(novoNome){
    this.nome=novoNome
}
    getNome(){
        return this.nome
    }
    
    setPeso(novoPeso){
        this.peso=novoPeso
    }
    getPeso(){
        return this.peso
    }

    //comportamento
    engordar(quilos){
        this.peso+=quilos
    }
    fzrNiver(){
        this.idade++
        console.log(`PARABENS ${this.nome} pelo seus ${this.idade} anos!! Feliz aniversário`)
        
    }
}
var p1 = new Homem 
p1.setNome('Emanuel')
p1.setNome2('Mariana')
p1.setPeso(0)
p1.setIdade(21)
p1.engordar(5)
p1.fzrNiver()

console.log(`Olá, eu sou o ${p1.getNome2()}!`)
console.log(`Emanuel, vc engordou ${p1.getPeso()} kg`)
