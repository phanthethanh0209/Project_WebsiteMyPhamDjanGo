var canvas = document.getElementById('linecanvas');
var ctx = canvas.getContext('2d');

// Đường thứ nhất
ctx.beginPath();
var gradient = ctx.createLinearGradient(0, 0, 42, 0);
gradient.addColorStop("0", "magenta");
gradient.addColorStop("0.5", "blue");
gradient.addColorStop("1.0", "pink");
ctx.lineWidth = 2;
//Ngang 1 
ctx.moveTo(25, 25);
ctx.lineTo(75, 25);
ctx.stroke();
//
ctx.moveTo(87, 75);
ctx.lineTo(12, 75);
ctx.stroke();


// Đường thứ 2
ctx.beginPath();
ctx.strokeStyle = ''; //Đặt màu đường
ctx.lineWidth = 2; //Độ rộng

ctx.moveTo(25, 25);
ctx.lineTo(0, 37);
ctx.stroke();

ctx.moveTo(25, 75);
ctx.lineTo(0, 37);
ctx.stroke();

ctx.moveTo(100, 37);
ctx.lineTo(75, 25);
ctx.stroke();

ctx.moveTo(100, 37);
ctx.lineTo(75, 75);
ctx.stroke();

//Duong len 
ctx.moveTo(50, 75);
ctx.lineTo(50, 42);
ctx.stroke();

ctx.moveTo(87, 75);
ctx.lineTo(50, 42);
ctx.stroke();

ctx.moveTo(12, 75);
ctx.lineTo(50, 42);
ctx.stroke();
//Tam Giac trên 
ctx.moveTo(25, 50);
ctx.lineTo(75, 50);
ctx.stroke();

ctx.moveTo(25, 50);
ctx.lineTo(50, 0);
ctx.stroke();

ctx.moveTo(75, 50);
ctx.lineTo(50, 0);
ctx.stroke();

//Gạch ngang 
ctx.moveTo(150, 57);
ctx.lineTo(0, 57);
ctx.stroke()
//Cây đứng F
ctx.moveTo(57, 62);
ctx.lineTo(57, 75);
ctx.stroke();
//Cây ngang dưới F
ctx.moveTo(67, 69);
ctx.lineTo(56, 69);
ctx.stroke();
//Cây ngang trên F
ctx.moveTo(68, 63);
ctx.lineTo(56, 63);
ctx.stroke();
//Chu T
ctx.moveTo(37, 62);
ctx.lineTo(37, 75);
ctx.stroke();
ctx.moveTo(42, 62);
ctx.lineTo(32, 62);
ctx.stroke();
ctx.font = '13px serif';
ctx.fillStyle = 'Magenta';
ctx.fillText('The Face Shop', 10 , 88);