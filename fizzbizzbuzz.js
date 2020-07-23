function fizzbuzz(val){

    if(typeof val !== "number") {
	console.log("Must be a number!");
	return;
}

   for(let i = 1; i <= val ; i++){
    if(i % 3 === 0 && i % 5 === 0){
     console.log("FizzBuzz");
    }else if (i % 3 === 0){
     console.log("Fizz");
    }else if (i % 5 === 0){
     console.log("Buzz");
    }else{
     console.log(i);
    }
  }
}

fizzbuzz(7)