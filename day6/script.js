const countToN = (x) => 
{
    var absx = Math.abs(x);
    
    var index = 1
    while (index <= absx)
    {

    console.log(index);
    index = index + 1
    }
}

const multiple = (mult,m,n) => 
{
    var absx = Math.abs(n);
    
    var index = 1
    while (index <= absx)
    {

    mult.push(index * m);
    index = index + 1
    }
}
