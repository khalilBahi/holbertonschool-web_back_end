export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const clonedCar = new this.constructor();
    for (const key of Object.getOwnPropertySymbols(this)) {
      clonedCar[key] = this[key];
    }
    return clonedCar;
  }
}
