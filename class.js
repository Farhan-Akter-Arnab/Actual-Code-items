class animal {
    constructor (name) {
        this.name = name;
    }
    present () {
        return "The selected animal is a " + this.name;
    }
}
class age extends animal {
    constructor (name, mean_lifespan) {
        super(name);
        this.age = Number(mean_lifespan);
    }
    show() {
        return this.present() + ', having ' + this.age + ' years of life.';
    }
}
let animal1 = new age ("cat", 18);
document.getElementById("detail1").innerHTML = animal1.show();
let animal2 = new age("cow", 20);
document.getElementById("detail2").innerHTML = animal2.show();