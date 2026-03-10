const textarea = document.getElementById("feedback");
const counter = document.getElementById("charCount");

const maxLength = 200;

textarea.addEventListener("input", function(){

let textLength = textarea.value.length;

counter.textContent = textLength;

/* เปลี่ยนสีเมื่อใกล้เต็ม */

if(textLength > 150){
counter.style.color = "orange";
}

if(textLength >= 200){
counter.style.color = "red";
}

});