var reverse = function(x) {
    const sign = Math.sign(x);
    
    var rest = Math.abs(x);
    
    let reversed=0;
    
    while(rest>0){
         //gettinf reminder
        var rightDigit = rest%10;
        
        rest = Math.floor(rest/10);
        
        reversed *= 10;
        reversed += rightDigit;
        
        if(reversed > (2**31)){
            return 0;
        }
    }
    return reversed*sign;
};
