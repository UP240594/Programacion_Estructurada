interface Users{
    id: number ;
    username? : string;
    email : string;
    age : number;
    isActive : boolean;
    permissions : boolean[];
    getAge: () => number;

}

const ana : Users = {
    id : 1 ,
    username : "anita" ,
    email : "anita@gmail.com" ,
    age : 25 ,
    isActive : true , 
    permissions : [true,false] , 
    getAge : () => {
        return 25
    }
}



function printMessage(p : Users) : Users{
    console.log("nombre" , p.username);
    console.log("gmail" , p.email);

    return p[0];
    
}