// let vs var variable declaration
function first() {
    var x = 1; // Declare and initialize variable x to 1
    
    {
        var x = 2; // Same variable, just we assigned new value to x!
        console.log(x); // Now x is: 2
    }

    console.log(x); // We print the last value assigned to x and that is: 2
}

function second() {
    let x = 1; // Declare and initialize variable x to 1
    
    {
        let x = 3; // This is a different variable, this is because of the block scope, the above x is not same as this variable x because of the block scope
        console.log(x); // It will print out the value of x declared inside the curly brackets: this is 3
    }

    console.log(x); // Here we have access to the X variable that is declared on top. We don't have access to the X variable defined inside the second block, and that is why the output is 1
}

first()
second();
