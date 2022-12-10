// fruit=prompt("what is your favorite food")
//  console.log(fruit);

// food =20 ;
// tippercentage = 0.2;
// timamount = food * tippercentage;
// console.log(timamount)
// //user input
//  function abtest(a,b) {

//     if (a < 0 || b < 0 ){

//         return undefined;
//     }
//  return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b),  2));
// } 

// console.log(abtest(2,2));


// set in java script
// var myset= new Set();
// myset.add(1)
// myset.add(2)
// myset.add(3)
// myset.add(4)
// console.log(myset)

// let arr= [3,4,4,5,5,5,6,9,8,7]

// var myset2  =new Set(arr)
// console.log(myset2)

// let myArr=Array.from(myset2)
// console.log(myArr)
 
// for (let item of myArr)
// console.log(item)

// const groceries=["banana","apple","orange","stawberry"];

// groceries.push("mango");
// groceries.push("pawpaw");
// console.log(groceries[0])
// console.log(groceries.slice(0,5));
// console.log(groceries.length)

// calculatefoodtotal =(food ,tip) => {
// tipPercentage =tip/100;
// tipAmount =food * tipPercentage;
// total=food+tipAmount ;
// return total
// }

// console.log(calculatefoodtotal(100,20))


// let person ={
//     name:"leonardo",
// shirt:"white"

// }
// console.log(person.name)
// console.log(person.shirt)

// console.log(person["name"])
// person["phone"] ="08025306563"

// console.log(person)

// const groceries=["banana","apple","orange","stawberry","banana","apple","orange","stawberry","banana","apple","orange","stawberry","banana","apple","orange","stawberry","banana","apple","orange","stawberry"];

// // for (let x =0 ; x < groceries.length; x++){
// //     console.log(x,groceries[x])
// //}
// for(const print of groceries){
// console.log(print)
// }
// let result = 0;

// const howmanyletters = () => {
// const phrase = "hey,can  you go to grocery store with me ?"

// for ( const letter in phrase){
// console.log(Number(letter) + 1)
// result=Number(index) + 1
// }
// }
// howmanyletters()

// const sumArray=(numbers) => {
// let result= 0;
// for(const number of numbers){
//     console.log(number)
// result = result+ number ;
// }
// return {result}
// }
// const nums = [1,2,3];

// console.log(sumArray(nums))

// const max = () => {

// }
// create a funtion of random fruit
// const randomfruit = () => {
//     const randomitems=Math.floor(Math.random()*fruits.length);
//     console.log(fruits[randomitems])
//     console.log("very good")
// }
// //global variable of fruit
// let fruits =["banana","orange","apple","mango"]
// //console.log it 
// randomfruit()


// class me {
//     constructor(name,job,hobby){
//         this.name=name;
//         this.job=job;
//         this.hobby=hobby;

//     }
// }
// var x=new me("aycode","programmer","coding,gym")
// console.log(x);


// class user {
// constructor(name,user,online ){
//     this.name=name;
//     this.user=user;
//     this.online=online;
// }
// }
// var user1=new user("Ayo","good",true);

// console.log(user1);

// funtion me(name,job,hobby)
// {
//     this.name=name;
//     this.job=job;
//     this.hobby=hobby;
// }
// me.prototype.getname= funtion(){
//     return this.name;
// }
// me.prototype.getjob =function () {
//     return this.job;
// }
// var me1 =new me("azeez","babalola","Ayomide");
// var me2= new me("akande","good","GainNode");
// document.write(me1);


// function one()
// {
// console.log("hello");
// }
// function two(){
//     console.log("Ayo,"+"Welcome to programming world");
// };

// one();
// setTimeout(two,2000);

//promise in javascript


// var prom = new Promise(function(resolve,reject){

 
// var drive= true;
// if(drive)
// {
//     resolve("Yes");
// }
// else{
//     reject("No");
// }
// });




// prom.then(function(resolve){
//     console.log(resolve + " the user knows how to drive")
// }).catch(function(reject){
//     console.log(reject + " the user does not know how to drive")
// })




// var me=(a,b) => a*b;

// let x =me(5,5);
// console.log(x)




//global modifiers i & g !\
//g modifier help to print 2 or more times
// i modifier help too print overide case insensitive

//var regex = /hello/
 //var strings= "hello ayo,welcome to javascript world,proceed to become the next greatest programmar of all time"

//var output= regex.exec(strings);
//console.log(output);


//regrex test funtion method for true or false statement!
//test help to show if  true or false statement
 
//var output=regex.test(strings);
//console.log(output);

//match method 

// var output = strings.match(regex);
// console.log(output);

//replace  method

//var output = strings.replace(regex,"bablol");
 //console.log(output.toLocaleUpperCase());

 

// metacharacters in javascript = ^ * . $ ?


// let regex= /ayo$/
// let strings= "hello ayo,welcome to javascript world,thank ayo"
 
// let output=regex.test(strings);
// console.log(output);



// let op=regex.exec(strings);
// console.log(op);



//  var me = {
//  name :"babalola",
// profession : "programmer",
// hobby :"being good "
//  }

//  console.log(me.hobby);
// var cool = 3 ;
// switch(cool)
// {
//     case 1:
//         console.log("high");
//         break;
//     case 2:
//     console.log("mid");
//         break;
//     case 3:
//     console.log("low");
//         break;
//         default:
//             console.log("not valid");


// }

//switch statement to check names 

// const names ="ayomide"
// switch(names){
// case "joke":
//     answer:console.log("hello ,it joke")
//     break;
//     case "babalola":
//     answer:console.log(" hello,it babalola")
//     break;
//     case "ayomide":console.log("hello,it ayomide")
//         break;
//         default:console.log("not found")


// }


//conditional statement  to check names

// const check =(name) => {  
//     return name === "ayomide" ? "hey,it ayomide"  : name === "babalola" ? "hey ,it babalola":  "not found";
// }

// console.log(check("babalola"))

//if  else statement that check names 

// var CHECK= "ayomide"

// if (CHECK === "ayomide"){
//     console.log("hey it ayomide")
// }else if ( CHECK === "babalola"){
// console.log("hey,it babalola")
// }else{
// console.log("not found")
// }
 

// var func =new Function("x","y", "console.log( x*y);" )

// func(10,20)




//object oriented programming 

// class user {
//     constructor(company){
//         this.company=company;
    
//     }
//     greet() {
//         console.log("Hi,i study " + this.language)
//     }
// }

//  class developer extends user {
//     constructor(company,language){
//         super(company)
//         this.language=language;

//     }

//  }
//  var dev = new developer("Aycode","js")
//  console.log(dev)




//object oriented programming  


// class user {
// greet(){
// console.log("hi ,it Aycode")
// }
// }

// class ting extends user{
//     greet(){
//   console.log("hi, it ayotech")
//     }
// }

// var one=new user()
// var two=new ting()

// one.greet()
// two.greet()



// class user{
// constructor(name,age){
//     this.name=name;
//     this.age=age;
// }
// }

// class developer extends user{
//     constructor(name,age,language){
//         super(name,age)
//         this.language =language
//     }
// }

// var printdeveloper =new developer('Aycode',23,"javascript")


// console.log(printdeveloper)

//void in javascript

// function getValue(){
//     var a,b,c;
//     a = void (  b = 6, c = 7 );
//     console.log('a = ' + a + ' b = ' + b +' c = ' + c );
//    }
//     getValue()


// function showValue()
// {
//  var dayOfMonth = 50;
//  if (dayOfMonth < 1 || dayOfMonth > 31)
//  {
//  dayOfMonth = Number.NaN
//  console.log("Day of Month must be between 1 and 31.")
//  }
//  console.log("Value of dayOfMonth : " + dayOfMonth );
// }

// showValue()


//concat-this blind together two strings to become a sentence

// var str1 = new String( "This is string one" );
// var str2 = new String( " This is string two" );
// var str3 = str1.concat( str2 );
// console.log("Concatenated String :" + str3);

//const myArr=["hi","get","new","done","bad"]

//  const showthis =() => {
 
//  for(let x in myArr){
//     console.log(x)
// }
//  }


// myArr.forEach(showthis)

//console.log(myArr.join())

//Date in javascript

//Date() -  this is used to get actual date of the system

//console.log(Date())

//getting  date in js 


//const date1=new Date("january 21, 2022 06:46:30")

//console.log(date1.getDate())

//console.log(date1.getDay())

//console.log(date1.getFullYear())

//console.log(date1.getMonth())

//console.log(date1.getHours())

//console.log(date1.getMilliseconds())

//console.log(date1.getMinutes())

//console.log(date1.getSeconds())

//console.log(date1.getTime())

//console.log(date1.getTimezoneOffset())

//setting date in js

//const date2=new Date("january 21, 2022 06:46:12")

//date2.setMonth(2)
//date2.setSeconds(40)
//date2.setTime(500000)
//date2.setDate(11)
//date2.setUTCDate(20)
//date2.setFullYear(1999)

//console.log(date2)

//formatting date in js

//const date3=new Date(1993, 6, 28, 14, 39, 7);

 //console.log(date3.toDateString())
//console.log(date3.toLocaleDateString())
//console.log(date3.toUTCString())
//console.log(date3.toSource())

