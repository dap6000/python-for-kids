chapter7Facts = [
    'I sometimes think of functions as a sort of robot that eats parameters and leaves behind something new. The parentheses are like a mouth. And the parameters are what the robot needs to do its job.',
    'I also sometimes think about functions like placing an order in a resturaunt. The waiter takes the order, maybe asking some questions along the way. This is like the parameters of the function. Then the order goes back to the kitch where the work happens. This is like the function body. Eventually my order arrives. This is like a return value.',
    'In both the robot and resturaunt metaphor for functions, you don\'t have to know the details of what goes on to get the work done. The inside of the robot and the inside of the kitchen can be a total mystery and you can still get what you want.',
    'Of course you have to worry about the details of a function body when you are writing it. But once it is written you can re-use it as long as you know the parameters and the return value. You could forget evrything about how you wrote the function and still use it in other code.',
    'This ability to use a function without worrying about its internal details is sometimes called the "black box" and is especially relevant when using libraries written by someone else.',
    'The black box view of functions helps to explain variable scope. The values passed in as parameters continue to exist in the scope outside the function, even though they may be referenced by a new name inside the body of the function due to named parameters. But any values created inside the function body (rather than passed in as parameters) only exist to get some work done inside the function body. They effectively do not exist outside of the function body.',
    'The number of parameters a function has is called its arity. There are also special words for describing functions that take zero parameters (nullary), a single parameter (unary), two parameters (binary), etc.',
    'Using the int() function to change user input from a string to an integer can be confusing. This is an example of what computer scientists call types.',
    'Types deal with the nature of the data a computer is storing in memory. Ultimately it is all ones and zeros. And if the computer knows it is dealing with an integer then it can optimize memory use in some special ways.',
    'Types also matter when performing operations. Adding two integers is straight forward but what about adding two string? Or adding a string and an integer? Computers like to have a very clear interpretation of the things we ask them to do via code. If the system expects an integer but sees a string (or expects a string but sees an integer instead) it doesn\'t understand how to proceed and gives you a type error.',
]