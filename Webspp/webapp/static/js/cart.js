 if(localStorage.getItem('cart') == null){
        var cartstorage = {};
    }
    else{
        cartstorage = JSON.parse(localStorage.getItem('cart'));
    }
    $(".cart-button").click(function(){

        var idstr = this.id.toString();

        if(cartstorage[idstr] != "undefined"){
            cartstorage[idstr] = cartstorage[idstr] + 1;
        }
        else{
            cartstorage[idstr] = 1;

        }
        localStorage.setItem('cartstorage',JSON.stringify(cartstorage));
    });