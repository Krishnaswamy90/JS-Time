const startButton=document.getElementById('startButton');
const messageArea=document.getElementById('message-area');

startButton.addEventListener('click',function(){
  const fullname=prompt('Enter full name');
  const age=prompt("Enter your age");
  const country=prompt('Enter your country');
  const favoriteLanguage=prompt("Enter your favourite programming Language");

if (!fullname || !age || !country || !favoriteLanguage) {
    messageArea.innerHTML = `
      <p>Please complete all registration questions to receive your welcome message.</p>
    `;
    return;
}

const studentInfo = `===== Student Information =====
Name: ${fullname}
Age: ${age}
Country: ${country}
Favorite Language: ${favoriteLanguage}
===============================`;

messageArea.innerHTML=`
<p><strong>Welcome,${fullname}!</strong></p>
<p>We are excited to have a ${age}-year-old student from ${country}. </p>
 <p>Your favorite programming language is ${favoriteLanguage}.</p>
    <p>We hope you enjoy your learning journey!</p>
    <div class="student-info">${studentInfo}</div>`;

  console.log(studentInfo);
});






