// function using Traditional Function  or normal function

// function fun1(){
//     console.log("Hello");
// }

// fun1()

// function using Function Expression 

// var f1 = function(){
//     console.log("Hello");
// }
// f1()

// function using arrow function

// var f1 = ()=>{
//     console.log("Hello arrow")
// }

// f1()

// modify arrow function

// var f1 = ()=>console.log("Hello arrow function modify")
// f1()


// modify arrow function in term of return

// var f2 = num=>num*num;
// console.log(f2(5))


// using height order function


// function higherOrderFunction(callback) {
//     console.log("Inside higher-order function");
//     // Execute the callback function
//     callback();
//   }
 
//   // Callback function
//   let callbackFunction = function() {
//     console.log("Inside callback function");
//   }
 


//   // Passing the callback function to the higher-order function
//   higherOrderFunction(callbackFunction);
 
	      
//   // OR calling the highOrderFunction by supplying the callbackFunction directly


//   higherOrderFunction(function(){
//     console.log("inside the callback function");
//   });


//   // OR calling the highOrderFunction by supplying the callbackFunction as arrow function


//   higherOrderFunction(() => {
//     console.log("inside the callback function");
//   });

// Hight order function using traditional or normal 

// function f1(){
//     console.log("Inside f1 using");
// }

// function f2(){
//     console.log("Inside f2 using");
//     f1()
// }
// f2()


// Hight order function using expresion

// var a1 = function(){
//     console.log("Inside a1");
// }

// var b1 = function(){
//     console.log("Inside b1");
//     a1()
// }

// b1()

// Hight order function using arrow function

// var a1 = ()=>console.log("Inside a1");
// var b1 = () => {
//     console.log("Inside b1");
//     a1()
// }
// b1()





// var a1 = num=> num*num;


// // console.log(result)

//  var b1 = num1=>{
//     var result = a1(5)
//     console.log(result * num1);
// };

// b1(4)



// var sum_of_two_num = (num1,num2)=>num1+num2

// console.log(sum_of_two_num(5,10))

// Student Activity: Write an arrow function that accepts a number if the number is positive then return true and if the number is negative then it returns false.


// var f1 = function(num){
//     if(num%2 === 0){
//         return true;
//     }
//     else{
//         return false;
//     }
// }
// console.log(f1(5))

// var f1 = num=>num > 0;

// console.log(f1(5))


// var a1 = num=>num%2==0

// console.log(a1(7))




// hight order function

// var add = (num1, num2)=>console.log("sum of two numbers: ",num1+num2);

// var sub = (num1, num2)=>console.log("sub of two numbers: ",num1-num2);

// var mul = (num1, num2)=> console.log("mul of two numbers: ",num1*num2);
 
// var div = (num1, num2)=>{
//     if (num2 != 0){
//         return num1/num2;
//     }
//     else{
//         console.log("num2 not equal to 0")
//     }
// }

// var calculate = ()=>{
//     console.log("Using calculator!!!!");
//     return add(5,10)
//     // return sub(10,5)
//     // return mul(5, 2)
//     // return div(10,2)
// }


// result =  calculate()

// console.log(result)








var add = (num1, num2)=>{
    console.log("sum of two numbers: ",num1+num2);
    sub(num1, num2)
}

var sub = (num1, num2)=>{
    console.log("sub of two numbers: ",num1-num2);
    mul(num1, num2)
}
var mul = (num1, num2)=> {
    console.log("mul of two numbers: ",num1*num2);
    div(num1,num2)
}
 
var div = (num1, num2)=>{
    if (num2 != 0){
        console.log("div of two numbers: ",num1/num2);
    }
    else{
        console.log("num2 not equal to 0")
    }
}

var calculate = ()=>{
    console.log("Using calculator!!!!");
    // add(10,5)
}


// console.log(calculate())
// calculate(add(10,4))
// calculate(sub(20,5))
calculate(mul(2,5))



