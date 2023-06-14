const numbers =  [1,2,3,4,5]
const start = 1
const end = 3

function numbersReverse (array, inicio, final){

    const selection = array.slice(inicio, final + 1).reverse()

    for(let i = inicio; i <= final; i++){
        array[i] = selection[i - inicio]
    }
    return array
}

// console.log(numbersReverse(numbers, start, end));


const palabra = "otto"

function palindrome(text) {
    // escribe aquí tu solución
    const caracteres = text.split("")
    const reverseWord = caracteres.reverse().join("")
    if(text === reverseWord){
      return true
    }else{
      return false
    }
  }

// console.log(palindrome(palabra));  



const string = "()()()()()()"

function balance (array){
    let repeats = ""

    for(let i = 0; i < array.length; i++){
        if(array[0] === '(' && array[i] === array[i + 1] ){
            repeats += array[i]
        }
    }
    if(repeats === ""){
        return true
    }else{
        return false
    }
    
}

console.log(balance(string));


